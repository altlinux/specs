%define _unpackaged_files_terminate_build 1
%define module_name Alien-Libxml2
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Alien/Base.pm) perl(Alien/Build.pm) perl(Alien/Build/MM.pm) perl(Alien/Build/Plugin/Build/SearchDep.pm) perl(Alien/Build/Plugin/Prefer/BadVersion.pm) perl(Config.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/Alien.pm) perl(Test2/V0.pm) perl(base.pm) pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.12
Release: alt1
Summary: Install the C libxml2 library on your system
Group: Development/Perl
License: perl
URL: https://metacpan.org/pod/Alien::Libxml2

Source0: http://www.cpan.org/authors/id/P/PL/PLICEASE/%{module_name}-%{version}.tar.gz
#BuildArch: noarch

%description
This module provides libxml2 for other modules to use.  There was an
already existing the Alien::LibXML manpage, but it uses the older
the Alien::Build::ModuleBuild manpage and has not bee actively maintained for a
while.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README author.yml
%perl_vendor_archlib/A*
%perl_vendor_autolib/*

%changelog
* Wed Dec 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Thu Oct 31 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Wed May 29 2019 Alexey Shabalin <shaba@altlinux.org> 0.09-alt2
- build to Sisyphus

* Fri May 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- updated by package builder

* Thu Mar 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- updated by package builder

* Wed Mar 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Mon Mar 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt1.1
- rebuild with perl 5.28.1

* Wed Dec 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

