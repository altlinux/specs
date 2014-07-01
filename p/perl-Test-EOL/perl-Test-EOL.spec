# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-EOL
Version:	1.5
Release:	alt2_5
Summary:	Check the correct line endings in your project
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Test-EOL/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Test-EOL-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/NoTabs.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
This module scans your project/distribution for any perl files (scripts,
modules, etc.) with Windows line endings. It can also check for trailing
whitespace.

%prep
%setup -q -n Test-EOL-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test RELEASE_TESTING=1

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/Test/

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_2
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_1
- moved to Sisyphus (Tapper dep)

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_6
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- fc import

