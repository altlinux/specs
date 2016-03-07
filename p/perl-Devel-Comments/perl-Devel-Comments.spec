# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Devel-Comments
Version:        1.1.4
Release:        alt2_12
Summary:        Debug with executable smart comments to logs
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Devel-Comments/
Source0:        http://www.cpan.org/authors/id/X/XI/XIONG/developer-tools/Devel-Comments-v%{version}.tar.gz
BuildArch:      noarch
# Compile-time:
BuildRequires:  perl(Module/Build.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Filter/Simple.pm)
BuildRequires:  perl(IO/Capture/Tie_STDx.pm)
BuildRequires:  perl(IO/Capture/Stdout.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(version.pm)
# Tests only:
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Try/Tiny.pm)
BuildRequires:  perl(IO/Capture/Stderr/Extended.pm)
BuildRequires:  perl(IO/Capture/Stdout/Extended.pm)
Requires:       perl(Filter/Simple.pm) >= 0.8
Requires:       perl(Test/More.pm) >= 0.94
Requires:       perl(Text/Balanced.pm) >= 2

# Remove under-specifed dependencies

Source44: import.info
%filter_from_requires /^perl\\(Filter.Simple|Text.Balanced.pm\\)\\s*$/d

%description
Devel::Comments is a source filter for your Perl code, intended to be used
only during development. Specially-formatted 'smart' comments are replaced by
executable code to dump variables to screen or to file, display loop progress
bars, or enforce conditions. These smart comments can all be disabled at once
by commenting out the "use Devel::Comments" line, whereupon they return to
being simple, dumb comments. Your debugging code can remain in place,
guaranteed harmless, ready for the next development cycle.

%prep
%setup -q -n Devel-Comments-v%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_11
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_8
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_7
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_6
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_4
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_2
- fc import

