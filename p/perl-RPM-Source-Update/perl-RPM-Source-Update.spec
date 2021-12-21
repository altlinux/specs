%define module RPM-Source-Update
%define _unpackaged_files_terminate_build 1

Name: perl-%module
Version: 0.004
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: RPM-Source-Editor extension for updating packages
Group: Development/Perl
License: GPLv2+ or Artistic-2.0
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
Url: http://git.altlinux.org/people/viy/packages/%{module}.git

BuildRequires: perl-devel perl(Pod/PlainText.pm) perl-RPM-Source-BundleImport perl-Gear-Remotes girar-nmu
Requires: perl-RPM-Source-BundleImport > 0.070
Requires: perl-RPM-Source-Editor > 0.9229

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/RPM*
%_bindir/*
%_man1dir/*

%changelog
* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 0.004-alt1
- new version

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- new version

* Thu Feb 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new version

* Tue Feb 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
