# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Cache/FileCache.pm) perl(Catalyst.pm) perl(Catalyst/Plugin/Session/Store.pm) perl(Catalyst/Plugin/Session/Test/Store.pm) perl(Catalyst/Utils.pm) perl(Config.pm) perl(Path/Class.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Catalyst-Plugin-Session-Store-File
Version:        0.18
Release:        alt2_10
Summary:        File storage backend for session data
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-File/
Source0:        http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Catalyst-Plugin-Session-Store-File-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Cache/Cache.pm)
BuildRequires:  perl(Catalyst/Plugin/Session.pm)
BuildRequires:  perl(Catalyst/Runtime.pm)
BuildRequires:  perl(Class/Data/Inheritable.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(MRO/Compat.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Requires:       perl(Cache/Cache.pm) >= 1.02
Requires:       perl(Catalyst/Plugin/Session.pm)
Requires:       perl(Catalyst/Runtime.pm) >= 5.700.0
Requires:       perl(Class/Data/Inheritable.pm) >= 0.04
Source44: import.info

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess
cache. It is based on Cache::FileCache.

%prep
%setup -q -n Catalyst-Plugin-Session-Store-File-%{version}

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_10
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_10
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_8
- fc import

