%define _name abiword
%define ver_major 3.0
%define abi_ver 3.0

Name: %_name-docs
Version: %ver_major.1
Release: alt1

Summary: Documentation for AbiWord word processor
Group: Office
License: GPL
Url: http://www.abisource.com/

Source: http://www.abisource.com/downloads/abiword/%version/source/%name-%version.tar.gz

BuildArch: noarch

Obsoletes: %name-%abi_ver
Provides: %name-%abi_ver = %version-%release

BuildRequires: abiword-devel

%description
AbiWord is a cross-platform, Open Source Word Processor developed
by the people at AbiSource, Inc. and by developers from around the world.
(http://www.abisource.com)
It is a lean and fast full-featured word processor. It works on Microsoft
Windows and most Unix Systems. Features include:

   * Basic character formatting (bold, underline, italics, etc.)
   * Paragraph alignment
   * Spell-check
   * Import of Word97 and RTF documents
   * Export to RTF, Text, HTML, and LaTeX formats
   * Document Templates
   * Interactive rulers and tabs
   * Styles
   * Unlimited undo/redo
   * Multiple column control
   * Widow/orphan control
   * Find/Replace
   * Images
   and much more...

This package provides user documentation for AbiWord.

%prep
%setup

%build
%configure

%make_build

%install
%makeinstall_std

%files
%_datadir/%_name-%abi_ver/help/

%changelog
* Sat Jan 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- renamed to abiword-docs

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Nov 29 2012 Yuri N. Sedunov <aris@altlinux.org> 2.9.4-alt1
- first build for Sisyphus

