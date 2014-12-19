Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(Test/Kit.pm) perl(YAML/Tiny.pm) perl(base.pm) perl-devel perl-podlators perl(Data/Perl/Role/String.pm)
# END SourceDeps(oneline)
Name:           perl-Pod-Readme
Version:        1.1.2
Release:        alt1_1
Summary:        Intelligently generate a README file from POD
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Pod-Readme/
Source0:        http://www.cpan.org/authors/id/R/RR/RRWO/Pod-Readme-v%{version}.tar.gz
Patch0:         Pod-Readme-v1.0.2-no-author-deps.patch
BuildArch:      noarch
# Module Build
BuildRequires:  perl
BuildRequires:  perl(inc/Module/Install.pm)
# Module Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Class/Method/Modifiers.pm)
BuildRequires:  perl(CPAN/Changes.pm)
BuildRequires:  perl(CPAN/Meta.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(feature.pm)
BuildRequires:  perl(File/Slurp.pm)
BuildRequires:  perl(Hash/Util.pm)
BuildRequires:  perl(IO.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Module/CoreList.pm)
BuildRequires:  perl(Module/Load.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(Moo/Role.pm)
BuildRequires:  perl(MooX/HandlesVia.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(Path/Tiny.pm)
BuildRequires:  perl(Role/Tiny.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Try/Tiny.pm)
BuildRequires:  perl(Type/Tiny.pm)
BuildRequires:  perl(Types/Standard.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(warnings.pm)
# Script Runtime
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(Getopt/Long/Descriptive.pm)
BuildRequires:  perl(IO/Handle.pm)
# Test Suite
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Compare.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
# Runtime
Requires:       perl(Role/Tiny.pm)
Source44: import.info

%description
This module filters POD to generate a README file, by using POD commands to
specify which parts are included or excluded from the README file.

%prep
%setup -q -n Pod-Readme-v%{version}

# Unbundle inc::Module::Install; we'll use the system version instead
rm -rf inc/
perl -ni -e 'print unless /^inc\//;' MANIFEST

# Avoid the need for Module::Install::AuthorRequires and
# all of upstream's toolchain modules as a result of the unbundling
%patch0

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README.pod
%{_bindir}/pod2readme
%{perl_vendor_privlib}/Pod/
%{_mandir}/man1/pod2readme.1*

%changelog
* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_1
- new release

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.110-alt3_10
- update to new release by fcimport

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt3_9
- Sisyphus build; switch to fc import

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_8
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.110-alt1_4
- fc import

