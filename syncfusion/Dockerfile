FROM mcr.microsoft.com/dotnet/runtime:3.1-bionic AS base
RUN apt-get update -y && apt-get install fontconfig python3 -y
COPY postServer.py /opt/postServer.py
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:3.1-bionic AS build
WORKDIR /src
COPY ["WordToPDFConverter.csproj", "."]
RUN dotnet restore "./WordToPDFConverter.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "WordToPDFConverter.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "WordToPDFConverter.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["python3", "/opt/postServer.py"]