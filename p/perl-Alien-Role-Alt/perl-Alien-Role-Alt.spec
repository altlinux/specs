%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Alien/Base.pm) perl(Class/Method/Modifiers.pm) perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(Role/Tiny.pm) perl(Storable.pm) perl(Test/Alien.pm) perl(Test2/V0.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_name Alien-Role-Alt
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt1
Summary: Alien::Base role that supports alternates
Group: Development/Perl
License: perl
URL: https://metacpan.org/pod/Alien::Role::Alt

Source0: http://www.cpan.org/authors/id/P/PL/PLICEASE/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Some packages come with multiple libraries, and multiple `.pc' files to
use with them.  This the Role::Tiny manpage role can be used with the Alien::Base manpage
to access different configurations.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE author.yml
%perl_vendor_privlib/A*

%changelog
* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Mon Apr 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- to Sisyphus as perl-Math-GMP dependency

* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new version

