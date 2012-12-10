# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(File/Spec/Functions.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-File-Pid
Version:        1.01
Release:        alt3_10
Summary:        Pid File Manipulation
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/File-Pid/
Source0:        http://www.cpan.org/authors/id/C/CW/CWEST/File-Pid-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Class/Accessor/Fast.pm) >= 0.19
Source44: import.info

%description
This software manages a pid file for you. It will create a pid file,
query the process within to discover if it's still running, and remove
the pid file.

%prep
%setup -q -n File-Pid-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_10
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_10
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_8
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_8
- fc import

