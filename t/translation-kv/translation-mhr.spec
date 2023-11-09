Name: translation-kv
Version: 231109
Release: alt1

Summary: Translation files for Komi language
License: GPLv2+
Group: Text tools

BuildArch: noarch
Source: %name-%version.tar
Requires: glibc-locales-kv_RU-utf8

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/locale/kv/LC_MESSAGES
msgfmt po/mate-calc.po -o %buildroot%_datadir/locale/kv/LC_MESSAGES/mate-calc.mo

%files
%_datadir/locale/kv/LC_MESSAGES/*

%changelog
* Thu Nov 09 2023 Kirill Izmestev <felixz@altlinux.org> 231109-alt1
- Initial build for Sisyphus
