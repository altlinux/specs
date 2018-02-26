Name: iat
Version: 0.1.7
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Iso9660 Analyzer Tool
License: GPLv2+
Group: File tools

Url: http://iat.berlios.de/
Source: http://download.berlios.de/iat/iat-%version.tar.bz2

%description
iat (Iso9660 Analyzer Tool) is a tool for detecting the structure of many
types of CD-ROM image file formats, such as BIN, MDF, PDI, CDI, NRG, and B5I,
and converting them into ISO-9660.

%prep
%setup

%build
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_bindir/*
%_man1dir/*
%exclude %_includedir/*

%changelog
* Thu Sep 03 2009 Victor Forsyuk <force@altlinux.org> 0.1.7-alt1
- 0.1.7

* Fri Sep 28 2007 Victor Forsyuk <force@altlinux.org> 0.1.3-alt1
- Initial build.
