%define _unpackaged_files_terminate_build 1

Name:    ocrdesktop
Version: 4.0
Release: alt4

Summary: Accessibility tool for use the current window with OCR technique
License: GPL
Group:   Accessibility
URL:     https://github.com/chrys87/ocrdesktop
Source: %name-%version.tar
Requires: tesseract-langpack-en
Requires: tesseract-langpack-ru
Requires: libwnck3-gir
Requires: python3-module-pyatspi

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3

BuildArch: noarch

%description
OCRdesktop is a useful accessibility tool to grab content from the screen as text via
OCR technology.

It takes an image of the current window or workspace, prepares it for better results
and uses tesseract to recognize text on it. The result is presented in a caret
enabled text area, in a detailed list with coordinates and confidence or in the
clipboard. It also can emulate clicks on the text.

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir/

install -m 755 ./%name %buildroot%_bindir/%name
install -m 644 ./%name.1.gz %buildroot%_man1dir/%name.1.gz

%files
%doc README.md docu/user.txt ChangeLog TODO
%_bindir/%name
%_man1dir/%name.1.xz

%changelog
* Fri Jul 04 2025 Artem Semenov <savoptik@altlinux.org> 4.0-alt4
- Reverted fix for working through xwailand
- Cleaned-up the spec

* Tue Jun 24 2025 Artem Semenov <savoptik@altlinux.org> 4.0-alt3
- Fixed work in wayland (Closes: 54263)

* Tue May 20 2025 Artem Semenov <savoptik@altlinux.org> 4.0-alt2
- Added req to pyatspi (Closes: 54263)

* Tue Apr 22 2025 Artem Semenov <savoptik@altlinux.org> 4.0-alt1
- Updated to new version 4.0

* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 3.0-alt3
- Cleaned-up the spec

* Thu Oct 24 2024 Artem Semenov <savoptik@altlinux.org> 3.0-alt2
- Added req to libwnck3-gir (ALT bug: 51815)

* Mon Oct 14 2024 Artem Semenov <savoptik@altlinux.org> 3.0-alt1
- Initial build for Sisyphus (ALT bug: 50788)
