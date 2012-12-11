# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(FindBin.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-NoTabs
Version:	1.3
Release:	alt2_4
Summary:	Check the presence of tabs in your project
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Test-NoTabs/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Test-NoTabs-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(inc/Module/Install.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
This module scans your project/distribution for any perl files (scripts,
modules, etc.) for the presence of tabs.

%prep
%setup -q -n Test-NoTabs-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir --skip INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Test/

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_4
- moved to Sisyphus (Tapper dep)

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- fc import

