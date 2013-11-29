# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(ExtUtils/Command.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-CPAN-Changes
Summary:	Read and write Changes files
Version:	0.26
Release:	alt1_1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/CPAN-Changes/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BR/BRICAS/CPAN-Changes-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(Pod/Usage.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
BuildRequires:	perl(Text/Wrap.pm)
BuildRequires:	perl(version.pm)
Source44: import.info

%description
It is standard practice to include a Changes file in your distribution. The
purpose of the Changes file is to help a user figure out what has changed
since the last release.

People have devised many ways to write the Changes file. A preliminary
specification has been created (CPAN::Changes::Spec) to encourage module
authors to write clear and concise Changes.

This module will help users programmatically read and write Changes files
that conform to the specification.

%prep
%setup -q -n CPAN-Changes-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"

%files
%doc Changes README
%{_bindir}/tidy_changelog
%{perl_vendor_privlib}/CPAN/
%{perl_vendor_privlib}/Test/
%{_mandir}/man1/tidy_changelog.1*

%changelog
* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_1
- update to new release by fcimport

* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_1
- Sisyphus build

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_1
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_1
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_5
- update to new release by fcimport

* Thu Nov 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_3
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_1
- fc import

