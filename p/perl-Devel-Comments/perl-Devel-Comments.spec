Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Devel-Comments
Version:        1.1.4
Release:        alt2_22
Summary:        Debug with executable smart comments to logs
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Devel-Comments
Source0:        https://cpan.metacpan.org/authors/id/X/XI/XIONG/developer-tools/Devel-Comments-v%{version}.tar.gz
BuildArch:      noarch
# Compile-time:
BuildRequires:  rpm-build-perl
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
Requires:       perl(Filter/Simple.pm) >= 0.800
Requires:       perl(Test/More.pm) >= 0.940
Requires:       perl(Text/Balanced.pm) >= 2

# Remove under-specifed dependencies

Source44: import.info
%filter_from_requires /^perl(Filter.Simple\|Text.Balanced\\)\\s*$/d

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
/usr/bin/perl Build.PL installdirs=vendor
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
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_22
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_18
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_16
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_14
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt2_13
- update to new release by fcimport

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

