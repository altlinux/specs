%define _unpackaged_files_terminate_build 1
%define soname 1

Name: pdfio
Version: 1.6.3
Release: alt1

Summary: Simple C library for reading and writing PDF files
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/michaelrsweet/pdfio
VCS: https://github.com/michaelrsweet/pdfio

Source: %name-%version.tar

BuildRequires: zlib-devel

%description
PDFio is a simple C library for reading and writing PDF files. The
primary goals of PDFio are:

- Read and write any version of PDF file
- Provide access to pages, objects, and streams within a PDF file
- Support reading and writing of encrypted PDF files
- Extract or embed useful metadata (author, creator, page information, etc.)
- Provide access to objects used for each page

PDFio is not concerned with rendering or viewing a PDF file, although
a PDF RIP or viewer could be written using it.

%package -n libpdfio%soname
Summary: %summary
Group: System/Libraries

%description -n libpdfio%soname
PDFio is a simple C library for reading and writing PDF files. The
primary goals of PDFio are:

- Read and write any version of PDF file
- Provide access to pages, objects, and streams within a PDF file
- Support reading and writing of encrypted PDF files
- Extract or embed useful metadata (author, creator, page information, etc.)
- Provide access to objects used for each page

PDFio is not concerned with rendering or viewing a PDF file, although
a PDF RIP or viewer could be written using it.

%package devel
Summary: Development files for pdfio
Group: System/Libraries

%description devel
The pdfio-devel package contains libraries and header files for
developing applications that use pdfio.

%package doc
Summary: Documentation and examples for pdfio
Group: System/Libraries

%description doc
The pdfio-doc package contains documentation and examples for the
pdfio library, including:

- HTML documentation
- Example programs demonstrating PDF manipulation
- Sample fonts and resources for examples

PDFio is a simple C library for reading and writing PDF files.

%prep
%setup

%build
%configure \
  --enable-shared \
  --disable-static \
  #
%make

%install
%make install

%files -n libpdfio%soname
%_libdir/libpdfio.so.%soname

%files devel
%_includedir/pdfio-content.h
%_includedir/pdfio.h
%_libdir/pkgconfig/pdfio.pc
%_libdir/libpdfio.so
%_man3dir/pdfio.3.xz

%files doc
%doc %_defaultdocdir/pdfio/LICENSE
%doc %_defaultdocdir/pdfio/NOTICE
%doc %_defaultdocdir/pdfio/pdfio.html
%doc %_defaultdocdir/pdfio/pdfio-512.png
%_defaultdocdir/pdfio/examples/

%changelog
* Tue May 05 2026 Anton Farygin <rider@altlinux.org> 1.6.3-alt1
- 1.6.2 -> 1.6.3

* Wed Apr 29 2026 Anton Farygin <rider@altlinux.org> 1.6.2-alt1
- 1.6.0 -> 1.6.2

* Mon Dec 22 2025 Constantin Sunzow <protvin@altlinux.org> 1.6.0-alt1
- Initial build.
