%define _unpackaged_files_terminate_build 1
%define module_name Alien-GMP
# BEGIN SourceDeps(oneline):
BuildRequires: libgmp-devel perl(Alien/Base.pm) perl(Alien/Build.pm) perl(Alien/Build/MM.pm) perl(Alien/Role/Alt.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/MakeMaker.pm) perl(Pod/Wordlist.pm) perl(Role/Tiny/With.pm) perl(Test/Alien.pm) perl(Test/Spelling.pm) perl(Test2/V0.pm) perl(parent.pm) perl(Devel/CheckLib.pm) perl(Class/Method/Modifiers.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.10
Release: alt1
Summary: Build and install the GNU Multiple Precision library.
Group: Development/Perl
License: lgpl
URL: https://metacpan.org/release/Alien-GMP

Source0: http://www.cpan.org/authors/id/P/PL/PLICEASE/%{module_name}-%{version}.tar.gz

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_archlib/A*
%perl_vendor_autolib/A*
%perl_vendor_autolib/share/dist/A*

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Mon Apr 09 2018 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2
- to Sisyphus as perl-Math-GMP dependency

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- regenerated from template by package builder

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- regenerated from template by package builder

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.0.6-alt2
- rebuild to get rid of unmets

* Thu Apr 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1
- initial import by package builder

