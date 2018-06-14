%def_disable snapshot
# LO required
%def_disable check

Name: unoconv
Version: 0.8.2
Release: alt1

Summary: Tool to convert between any document format supported by LibreOffice
Group: File tools
License: GPLv2
Url: http://dag.wieers.com/home-made/%name/

%if_disabled snapshot
Source: http://dag.wieers.com/home-made/%name/%name-%version.tar.gz
%else
#VCS: https://github.com/dagwieers/unoconv
Source: %name-%version.tar
%endif

# fc
Patch: 0001-python3-added-compatibility.patch
Patch1: 0001-update-FSF-address.patch
Patch2: 0001-make-LaTeX-export-usable-with-writer2latex-ext.patch
Patch3: 0001-libreoffice-or-OO.o-has-never-had-wps-export.patch
Patch4: 0002-remove-export-formats-dropped-by-LibreOffice.patch
# alt
Patch100: ALT-LOpath.patch

BuildArch: noarch

# libreoffice with pyuno (.../program/libpyuno.so)
Requires: LibreOffice

BuildRequires: asciidoc
%{?_enable_check:BuildRequires: LibreOffice}

%description
Universal Office Converter (unoconv) is a command line tool to convert any
document format that LibreOffice can import to any document format that
LibreOffice can export. It makes use of the LibreOffice's UNO bindings for
non-interactive conversion of documents.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%patch100 -p1

# pix python path
sed -i 's/\(python=\).*$/\1%__python3/' tests/Makefile

%build
%make -C doc

%install
%makeinstall_std

%check
%make -C tests

%files
%_bindir/%name
%_man1dir/%name.1*
%doc AUTHORS ChangeLog README.* doc/*.html tests/

%changelog
* Wed Jun 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2
- dropped obsolete 0001-Updated-ChangeLog.patch
- %%check section (disabled by default)

* Tue Jul 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- 0.7
- updated fc patchset

* Tue Jul 29 2014 Fr. Br. George <george@altlinux.ru> 0.6-alt2
- Apply FC patches for Python3/LO4 compatibility
- Adapt to ALT LO4 location

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for Sisyphus

