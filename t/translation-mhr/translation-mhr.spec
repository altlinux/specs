Name: translation-mhr
Version: 231022
Release: alt1

Summary: Translation files for meadow dialect of the Mari language
License: GPLv2+
Group: Text tools

BuildArch: noarch
Source: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/locale/mhr/LC_MESSAGES
msgfmt po/mate-calc.po -o %buildroot%_datadir/locale/mhr/LC_MESSAGES/mate-calc.mo

%files
%_datadir/locale/mhr/LC_MESSAGES/*

%changelog
* Tue Oct 31 2023 Kirill Izmestev <felixz@altlinux.org> 231022-alt1
- Initial build for Sisyphus
