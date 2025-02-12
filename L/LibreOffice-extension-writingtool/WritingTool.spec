%define ext_dir  %_libdir/LibreOffice/share/extensions/
%define ext_name WritingTool

Name: LibreOffice-extension-writingtool
Version: 1.1.1
Release: alt1

Summary: LibreOffice extension for proofreading
License: LGPL-2.1
Group: Office
Url: https://writingtool.org

Source0: %ext_name-%version.oxt

BuildRequires(pre): rpm-build-python3
BuildRequires: unzip
AutoReq: yes, noperl
Provides: libreoffice-languagetool = 6.1.100
Obsoletes: libreoffice-languagetool < 6.1.100

%description
WritingTool extends LibreOffice's text editing functionality with
a writing assistant. It is designed for creating and editing extensive
texts (e.g., for literature, science, and business).

This package is packed as a LibreOffice/OpenOffice.org extension.

%prep
%build
%install
install -d -m0755 %buildroot%ext_dir/%ext_name
unzip %SOURCE0 -d %buildroot%ext_dir/%ext_name

%files
%ext_dir/%ext_name

%changelog
* Wed Feb 12 2025 Fr. Br. George <george@altlinux.org> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Wed Feb 12 2025 Fr. Br. George <george@altlinux.org> 1.1-alt1
- Initial build for ALT

