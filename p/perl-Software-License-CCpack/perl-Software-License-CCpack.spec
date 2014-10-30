%define module_version 1.11
%define module_name Software-License-CCpack
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Software/License.pm) perl(Test/CheckDeps.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.11
Release: alt2
Summary: Software::License pack for Creative Commons' licenses
Group: Development/Perl
License: lgpl
URL: https://github.com/SineSwiper/Software-License-CCpack

Source0: http://cpan.org.ua/authors/id/B/BB/BBYRD/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.html README CHANGES
%perl_vendor_privlib/S*

%changelog
* Thu Oct 30 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2
- moved to Sisyphus as dependency

* Wed Oct 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- regenerated from template by package builder

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- initial import by package builder

