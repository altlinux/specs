Name: unoconv
Version: 0.6
Release: alt2

Summary: Tool to convert between any document format supported by LibreOffice
Group: File tools
License: GPLv2
Url: http://dag.wieers.com/home-made/%name/

Source: http://dag.wieers.com/home-made/%name/%name-%version.tar.gz
# fc
Patch1: 0001-Fix-a-broken-export-option-and-add-V-as-alternative-.patch
Patch2: 0001-make-LaTeX-export-usable-with-writer2latex-ext.patch
Patch3: 0001-python3-added-compatibility.2.patch
Patch4: 0001-python3-added-compatibility.3.patch
Patch5: 0001-Resolves-fdo-70309-can-t-write-bytes-direct-to-stdou.patch
Patch6: 0001-update-FSF-address.patch
Patch7: 0002-remove-export-formats-dropped-by-LibreOffice.patch

# alt
Patch100: ALT-LOpath.patch

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
%patch1 -p1
%patch2 -p1
#patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%patch100 -p1

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1*
%doc AUTHORS ChangeLog README.asciidoc WISHLIST doc/*.txt tests/

%changelog
* Tue Jul 29 2014 Fr. Br. George <george@altlinux.ru> 0.6-alt2
- Apply FC patches for Python3/LO4 compatibility
- Adapt to ALT LO4 location

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for Sisyphus

