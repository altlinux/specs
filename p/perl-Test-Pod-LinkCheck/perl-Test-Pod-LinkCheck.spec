# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(CPAN/Common/Index/MetaDB.pm) perl(ExtUtils/MakeMaker.pm) perl(HTTP/Tiny.pm) perl(LWP/UserAgent.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-Pod-LinkCheck
Version:        0.008
Release:        alt1_1
Summary:        Tests POD for invalid links
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-Pod-LinkCheck/
Source0:        http://www.cpan.org/authors/id/A/AP/APOCAL/Test-Pod-LinkCheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
# ExtUtils::MakeMaker not used
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(App/PodLinkCheck/ParseLinks.pm)
BuildRequires:  perl(App/PodLinkCheck/ParseSections.pm)
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Util/TypeConstraints.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Pod/Find.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/Pod.pm)
# Tests:
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Tester.pm)
# Optional tests:
%if %{undefined perl_bootstrap}
# Break build-time cycle with perl-Test-Apocalypse
#BuildRequires:  perl(Test/Apocalypse.pm)
%endif
Requires:       perl(App/PodLinkCheck/ParseSections.pm)
Requires:       perl(Capture/Tiny.pm)
Requires:       perl(Config.pm)
Requires:       perl(File/Spec.pm)
Requires:       perl(Pod/Find.pm)
Source44: import.info

%description
This module looks for any links in your POD and verifies that they point to
a valid resource. It uses the Pod::Simple parser to analyze the pod files
and look at their links. In a nutshell, it looks for L<Foo> links and makes
sure that Foo exists. It also recognizes section links, L</SYNOPSIS> for
example. Also, manual pages are resolved and checked.

%prep
%setup -q -n Test-Pod-LinkCheck-%{version}

%build
perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor
./Build

%install
./Build install "--destdir=$RPM_BUILD_ROOT" --create_packlist=0
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc AUTHOR_PLEDGE Changes CommitLog examples LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_1
- new release

* Sat Jun 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt2_8
- converted for ALT Linux by srpmconvert tools

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt2_6
- build for Sisyphus

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_6
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_5
- update to new release by fcimport

* Mon Feb 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_4
- initial fc import

