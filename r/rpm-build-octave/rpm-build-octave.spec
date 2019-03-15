%define module octave
Name: rpm-build-%module
Summary: %module packaging macros
Version: 0.1.1
Release: alt1
License: GPL
Group: Development/Other
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
install -D -m644 %module -p %buildroot%_rpmmacrosdir/%module

%files
%_rpmmacrosdir/*

%changelog
* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- fix in %%octave_build

* Thu Mar 14 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus
