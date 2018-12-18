%define _unpackaged_files_terminate_build 1
%define m_distro Astro-SunTime
Name: perl-%m_distro
Version: 0.06
Release: alt2
Summary: Astro::SunTime provides a function interface to calculate sun rise/set times.
Group: Development/Perl
License: Artistic/GPL
Url: http://search.cpan.org/dist/Astro-SunTime/
Source0: http://www.cpan.org/authors/id/R/RO/ROBF/Astro-SunTime-%{version}.tar.gz
BuildRequires: perl-Time-modules perl-devel perl(Module/Build.pm)
BuildArch: noarch

%description
Astro::SunTime provides a function interface to calculate sun rise/set times.

%prep
%setup -q -n Astro-SunTime-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE README.md
%perl_vendor_privlib/Astro/*
%doc Changes MANIFEST README

%changelog
* Tue Dec 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- set as noarch package

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.01-alt1.1
- redundant buildreq dropped

* Thu Jan 13 2011 Alex Negulescu <alecs@altlinux.org> 0.01-alt1
- initial build

