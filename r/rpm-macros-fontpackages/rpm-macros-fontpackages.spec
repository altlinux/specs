%define module fontpackages
Name: rpm-macros-%module
Summary: Fedora compatible set of font macros
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
install -D -m644 macros.%module -p %buildroot%_rpmmacrosdir/%module

%files
%_rpmmacrosdir/*

%changelog
* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- bugfix release

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added _fontstem macro

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build for ALT Linux Sisyphus
