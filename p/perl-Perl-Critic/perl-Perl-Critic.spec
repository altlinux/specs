%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(List/SomeUtils.pm) perl(PPIx/Utils/Traversal.pm)
# END SourceDeps(oneline)
%define m_distro Perl-Critic
Name: perl-Perl-Critic
Version: 1.150
Release: alt1

Summary: Critique Perl source code for best-practices.  

License: Perl (Artistic and GPL)
Group: Development/Perl
Url: %CPAN %m_distro

BuildArch: noarch
# https://github.com/Perl-Critic/Perl-Critic.git
Source0: http://www.cpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-%{version}.tar.gz

BuildRequires: perl-B-Keywords perl-Config-Tiny perl-Exception-Class perl-File-HomeDir perl-File-Which perl-HTML-Parser perl(PPIx/QuoteLike.pm)
BuildRequires: perl-Module-Build perl-PPI perl-Perl-Tidy perl-Pod-Spell perl-Readonly perl-Regexp-Parser perl-String-Format
BuildRequires: perl-version perl-podlators perl-Module-Pluggable perl-autodie perl-Email-Address perl-PPIx-Utilities perl-PPIx-Regexp perl-Test-Deep perl(List/MoreUtils.pm) perl(IO/String.pm) perl(Pod/PlainText.pm)
Requires: perl(Module/Pluggable.pm)

%description
Perl::Critic is an extensible framework for creating and applying
coding standards to Perl source code. Essentially, it is a static
source code analysis engine. Perl::Critic is distributed with a number
of Perl::Critic::Policy modules that attempt to enforce various coding
guidelines.

%package -n perlcritic
Summary: Perl source code analysis utility
Requires: perl-Perl-Critic
Buildarch: noarch
Group: Text tools

%description -n perlcritic
perlcritic is a Perl::Critic based command line utility for Perl source
code analysis.

%prep
%setup -q -n Perl-Critic-%{version}
[ %version = 1.132 ] && rm t/05_utils.t

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc TODO.pod CONTRIBUTING.md README.md Changes README examples
%perl_vendor_privlib/Perl/Critic*
%perl_vendor_privlib/Test/Perl/Critic/Policy.pm
%doc examples extras Changes README.*
%exclude %perl_vendor_archlib

%files -n perlcritic
%_bindir/*
%_man1dir/*
%exclude %perl_vendor_archlib

%changelog
* Mon Mar 06 2023 Igor Vlasenko <viy@altlinux.org> 1.150-alt1
- automated CPAN update

* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1.148-alt1
- automated CPAN update

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.146-alt1
- automated CPAN update

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 1.140-alt3
- fixed build

* Mon Mar 28 2022 Igor Vlasenko <viy@altlinux.org> 1.140-alt2
- fixed build

* Wed Mar 31 2021 Igor Vlasenko <viy@altlinux.org> 1.140-alt1
- automated CPAN update

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.138-alt2
- fixed build

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.138-alt1
- automated CPAN update

* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 1.136-alt1
- automated CPAN update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.134-alt1
- automated CPAN update

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.132-alt2
- fixed build

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.132-alt1
- automated CPAN update

* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.130-alt1
- Updated to upstream version 1.130.

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.126-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.125-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.123-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.122-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.121-alt1
- automated CPAN update

* Sat Oct 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.120-alt1
- automated CPAN update

* Fri Sep 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.119-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.118-alt1
- automated CPAN update

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.117-alt1
- new version

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.116-alt2
- manually added Requires: perl(Module/Pluggable.pm) -
  do required for Critic plugins to work

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.116-alt1
- New version 1.116
- Spec cleanup

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.082-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.082-alt1.1
- NMU fixing directory ownership violation

* Tue May 20 2008 Michael Bochkaryov <misha@altlinux.ru> 1.082-alt1
- first build for ALT Linux Sisyphus

