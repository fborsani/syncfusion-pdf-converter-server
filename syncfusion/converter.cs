using System;
using System.IO;
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;
using Syncfusion.DocIORenderer;
using Syncfusion.Pdf;

namespace WordToPDFConverter
{
    class Program
    {
        static void Main(string[] args)
        {
            FileStream docStream = new FileStream(args[0], FileMode.Open, FileAccess.Read);
            WordDocument wordDocument = new WordDocument(docStream, Syncfusion.DocIO.FormatType.Automatic);
            docStream.Dispose();
            DocIORenderer render = new DocIORenderer();
            PdfDocument pdfDocument = render.ConvertToPDF(wordDocument);
            render.Dispose();
            wordDocument.Dispose();
            FileStream outputStream = new FileStream(args[1], FileMode.OpenOrCreate, FileAccess.ReadWrite);
            pdfDocument.Save(outputStream);
            pdfDocument.Close();
            outputStream.Dispose();
        }
    }
}