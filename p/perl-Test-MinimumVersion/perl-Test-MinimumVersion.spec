# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-MinimumVersion
Version:	0.101080
Release:	alt2_9
Summary:	Check whether your code requires a newer perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Test-MinimumVersion/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Test-MinimumVersion-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	perl(base.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Find/Rule.pm)
BuildRequires:	perl(File/Find/Rule/Perl.pm)
BuildRequires:	perl(Perl/MinimumVersion.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Tester.pm)
BuildRequires:	perl(YAML/Tiny.pm)
BuildRequires:	perl(version.pm)

# For improved tests
BuildRequires:	perl(Test/Pod.pm)
Source44: import.info

%description
Check whether your code requires a newer perl than you think.

%prep
%setup -q -n Test-MinimumVersion-%{version}
find -type f -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test RELEASE_TESTING=1

%files
%doc Changes LICENSE
%{perl_vendor_privlib}/Test

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt2_9
- moved to Sisyphus

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt1_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt1_8
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt1_6
- fc import

