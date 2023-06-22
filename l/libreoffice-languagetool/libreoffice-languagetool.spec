%define ext_dir  %{_libdir}/LibreOffice/share/extensions/
%define ext_name languagetool

Name:       libreoffice-languagetool
Version:    6.1.1
Release:    alt1

Summary:    LibreOffice/OpenOffice.org extension for proofreading
License:    LGPL-2.1
Group:      Office
URL:        http://www.languagetool.org

# XXX actually, .oxt
Source0:    LanguageTool-%version.zip

BuildRequires(pre): rpm-build-python3
BuildRequires: unzip
AutoReq: yes, noperl

%description
LanguageTool is an Open Source proofreading software for English,
French, German, Polish, Romanian, and more than 20 other languages.
It finds many errors that a simple spell checker cannot detect like
mixing up there/their and it detects some grammar problems.

This package is packed as a LibreOffice/OpenOffice.org extension.

%prep

%build

%install
install -d -m0755 %buildroot%ext_dir/%ext_name
unzip %SOURCE0 -d %buildroot%ext_dir/%ext_name

%files
%ext_dir/%ext_name

%changelog
* Thu Jun 22 2023 Fr. Br. George <george@altlinux.org> 6.1.1-alt1
- Version update

* Wed May 05 2021 Andrey Cherepanov <cas@altlinux.org> 5.1-alt2
- FTBFS: Use rpm-build-python3 for autreq and autoprov.

* Sat Sep 26 2020 Fr. Br. George <george@altlinux.ru> 5.1-alt1
- New version 5.1

* Tue Apr 02 2013 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- New version 2.1

* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- Initial build in Sisyphus (ALT #22138)
