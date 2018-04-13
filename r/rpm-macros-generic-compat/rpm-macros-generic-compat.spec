%define module generic-compat
Name: rpm-macros-%module
Summary: Generic non-ALTLinux compatibility set of macro
Version: 0.03
Release: alt1
License: GPL
Group: System/Base
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
install -D -m644 %module -p %buildroot%_rpmmacrosdir/%module-base
#for ext in cmake kde4 kf5 qt4 perl systemd; do
#    install -D -m644 macros.$ext -p %buildroot%_rpmmacrosdir/%module-$ext
#done

%files
%_rpmmacrosdir/*

%changelog
* Fri Apr 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added %%sunsparc

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- updated architectures

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build for ALT Linux Sisyphus
