Name: pdftohtml
Version: 0.40a
Release: alt1.qa1

Summary: %name is a utility which converts PDF files into HTML and XML formats.
License: GNU GPL
Group: System/Libraries

Url: http://pdftohtml.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/pdftohtml/%name-%version.tar.gz
Patch0: pdftohtml-build.patch
Packager: Eugene Ostapets <eostapets@altlinux.ru>

# Automatically added by buildreq on Mon Nov 27 2006
BuildRequires: gcc-c++

%description
%name is a utility which converts PDF files into HTML and XML formats.
Use %name -dev jpeg -c -enc KOI8-R file.pdf to convert russian documents.

%prep
%setup -q
%patch0 -p1

%build
%make

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.40a-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Nov 27 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.40a-alt1
- first build

