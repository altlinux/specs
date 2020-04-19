%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
#BuildRequires: perl(Test/CleanNamespaces.pm) perl(Test/EOL.pm) perl(Test/Kit.pm) perl(Test/Kwalitee.pm) perl(Test/MinimumVersion.pm) perl(Test/NoTabs.pm) perl(Test/Perl/Critic.pm) perl(Test/Pod.pm)
BuildRequires: perl-podlators perl(Data/Perl/Role/String.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Pod-Readme
Version:        1.2.3
Release:        alt1_5
Summary:        Intelligently generate a README file from POD
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Readme
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Readme-v%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  sed
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
BuildRequires:  perl(Pod/Simple.pm)
BuildRequires:  perl(Role/Tiny.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Try/Tiny.pm)
BuildRequires:  perl(Type/Tiny.pm)
BuildRequires:  perl(Types/Standard.pm)
BuildRequires:  perl(warnings.pm)
# Script Runtime
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(Getopt/Long/Descriptive.pm)
BuildRequires:  perl(IO/Handle.pm)
# Test Suite
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Compare.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Module/Metadata.pm)
BuildRequires:  perl(Pod/Simple/Text.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Test/Exception.pm)
# Pod::Readme::Test::Kit not actually used
#BuildRequires: perl(Test::Kit)
BuildRequires:  perl(Test/More.pm)
# Runtime
Requires:       perl(Role/Tiny.pm)
Source44: import.info

%description
This module filters POD to generate a README file, by using POD commands to
specify which parts are included or excluded from the README file.

%prep
%setup -q -n Pod-Readme-v%{version}

# Fix script interpreter
sed -i -e 's|#!/usr/bin/env perl|#!/usr/bin/perl|' bin/pod2readme

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} -c %{buildroot}

# Remove spurious Pod::README files, which are the same as Pod::Readme
rm -vf %{buildroot}%{_mandir}/man3/Pod::README.3*

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes README.pod
%{_bindir}/pod2readme
%{perl_vendor_privlib}/Pod/
%{_mandir}/man1/pod2readme.1*

%changelog
* Sun Apr 19 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_5
- dropped perl-Module-Install frpm BR:

* Sun Dec 30 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1
- automated CPAN update

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

