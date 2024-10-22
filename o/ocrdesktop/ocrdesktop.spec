%define _unpackaged_files_terminate_build 1
%def_without check

Name:    ocrdesktop
Version: 3.0
Release: alt1

Summary: Accessiblity tool for use the current window with OCR technique 
License: GPL
Group:   Accessibility
URL:     https://github.com/chrys87/ocrdesktop
Source: %name-%version.tar
Requires: tesseract-langpack-en
Requires: tesseract-langpack-ru

BuildRequires(pre): rpm-build-python3
BuildArch: noarch

%description
OCRdesktop is a useful accessibility tool to grab content from the screen as text via OCR technology.

It takes an image of the current window or workspace, prepares it for better results and uses tesseract to recognize text on it. The result is presented in a caret enabled text area, in a detailed list with coordinates and confidence or in the clipboard. It also can emulate clicks on the text.

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/doc/%name
mkdir -p %buildroot%_man1dir/

install -m 755 ./%name %buildroot%_bindir/%name
install -m 644 ./TODO %buildroot%_datadir/doc/%name
install -m 644 ./ChangeLog %buildroot%_datadir/doc/%name
install -m 644 ./docu/* %buildroot%_datadir/doc/%name
install -m 644 ./README.md %buildroot%_datadir/doc/%name
install -m 644 ./%name.1.gz %buildroot%_man1dir/

%files
%_bindir/%name
%_man1dir/*
%dir %_datadir/doc/%name
 %_datadir/doc/%name/*

%changelog
* Mon Oct 14 2024 Artem Semenov <savoptik@altlinux.org> 3.0-alt1
- Initial build for Sisyphus (ALT bug: 50788)
