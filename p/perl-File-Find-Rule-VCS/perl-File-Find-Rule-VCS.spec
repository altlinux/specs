# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl(inc/Module/Install/DSL.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-File-Find-Rule-VCS
Version:        1.08
Release:        alt3_9
Summary:        Exclude files/directories for Version Control Systems
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/File-Find-Rule-VCS/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/File-Find-Rule-VCS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Find/Rule.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Text/Glob.pm)
Source44: import.info

%description
Many tools need to be equally useful both on ordinary files, and on code
that has been checked out from revision control systems.

%prep
%setup -q -n File-Find-Rule-VCS-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt3_9
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2_8
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_4
- fc import

