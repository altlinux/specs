Name: unoconv
Version: 0.6
Release: alt1

Summary: Tool to convert between any document format supported by LibreOffice
Group: File tools
License: GPLv2
Url: http://dag.wieers.com/home-made/%name/

Source: http://dag.wieers.com/home-made/%name/%name-%version.tar.gz
# fc
Patch: 0001-update-FSF-address.patch

BuildArch: noarch

# libreoffice with pyuno (.../program/libpyuno.so)
Requires: libreoffice

%description
Universal Office Converter (unoconv) is a command line tool to convert any
document format that LibreOffice can import to any document format that
LibreOffice can export. It makes use of the LibreOffice's UNO bindings for
non-interactive conversion of documents.

%prep
%setup
%patch -p1

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1*
%doc AUTHORS ChangeLog README.asciidoc WISHLIST doc/*.txt tests/

%changelog
* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for Sisyphus

