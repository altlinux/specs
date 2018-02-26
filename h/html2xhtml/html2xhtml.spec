Name: html2xhtml
Version: 1.1.2.2
Release: alt1

Summary: Converts HTML files into XHTML
License: GPLv2
Group: Text tools
Url: http://www.it.uc3m.es/jaf/html2xhtml/
Source: http://www.it.uc3m.es/jaf/html2xhtml/downloads/%name-%version.tar.gz

Packager: Paul Wolneykien <manowar@altlinux.ru>

%description
html2xhtml converts HTML files into XHTML. It can fix many common errors
in HTML files (e.g. missing end tags, elements with incorrect content
model, non-standard elements or attributes, etc.) It can also handle
invalid or non well-formed XHTML input, and clean it to produce a well-
formed and valid XHTML output. The output document type can be selected
among several XHTML DTDs (1.0, 1.1, Basic, etc.)

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS README TODO

%changelog
* Sun Oct 16 2010 Paul Wolneykien <manowar@altlinux.ru> 1.1.2.2-alt1
- Initial release for ALT Linux.

