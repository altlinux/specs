%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(ExtUtils/Command.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators perl(Moo.pm) perl(MooX/Types/MooseLike/Base.pm)
# END SourceDeps(oneline)
BuildRequires: perl(Moose.pm)
Name:           perl-Config-GitLike
Version:        1.12
Release:        alt1
Summary:        Git-compatible config file parsing
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Config-GitLike/
Source:        http://www.cpan.org/authors/id/A/AL/ALEXMV/Config-GitLike-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Any/Moose.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
This module handles interaction with configuration files of the style used
by the version control system Git. It can both parse and modify these
files, as well as create entirely new ones.

%prep
%setup -q -n Config-GitLike-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_4
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_1
- fc import

