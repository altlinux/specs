%define ext_dir  %{_libdir}/libreoffice/share/extensions/
%define ext_name languagetool

Name:       libreoffice-languagetool
Version:    2.0
Release:    alt1

Summary:    LibreOffice/OpenOffice.org extension for proofreading
License:    LGPL
Group:      Office
URL:        http://www.languagetool.org

Packager:   Andrey Cherepanov <cas@altlinux.org>

Source0:    LanguageTool-%version.zip

BuildRequires: unzip

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
* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- Initial build in Sisyphus (ALT #22138)
