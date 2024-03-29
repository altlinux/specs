Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Enable debugging with Devel::MAT
%bcond_with perl_Syntax_Keyword_Dynamically_enables_Devel_MAT
# Perform optional tests
%bcond_with perl_Syntax_Keyword_Dynamically_enables_optional_test

Name:           perl-Syntax-Keyword-Dynamically
Version:        0.13
Release:        alt1_1
Summary:        Dynamically change the value of a variable
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Keyword-Dynamically
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Dynamically-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
%if %{with perl_Syntax_Keyword_Dynamically_enables_Devel_MAT}
BuildRequires:  perl(Devel/MAT/Dumper/Helper.pm)
%endif
BuildRequires:  perl(ExtUtils/CBuilder.pm)
%define Future_AsyncAwait_minver 0.60
BuildRequires:  perl(Future/AsyncAwait/ExtensionBuilder.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XS/Parse/Keyword/Builder.pm)
# Run-time:
BuildRequires:  perl
BuildRequires:  perl(Carp.pm)
# lib/Syntax/Keyword/Dynamically.xs includes XSParseKeyword.h generated by
# XS::Parse::Keyword::Builder which loads XS::Parse::Keyword of version
# specified by boot_xs_parse_keyword() argument in Dynamically.xs
BuildRequires:  perl(XS/Parse/Keyword.pm)
BuildRequires:  perl(XSLoader.pm)
# Tests:
BuildRequires:  perl(Test2/V0.pm)
%if %{with perl_Syntax_Keyword_Dynamically_enables_optional_test} && !%{defined perl_bootstrap}
# A cycle: perl-Future-AsyncAwait a.. perl-Syntax-Keyword-Dynamically
# Optional tests:
BuildRequires:  perl(Future.pm)
# Higher version from boot_future_asyncawait()
BuildRequires:  perl(Future/AsyncAwait.pm)
%define Object_Pad_minver 0.800
BuildRequires:  perl(Object/Pad.pm)
BuildRequires:  perl(Sentinel.pm)
BuildRequires:  perl(Test/Pod.pm)
%endif
# From boot_future_asyncawait() argument in lib/Syntax/Keyword/Dynamically.xs
Requires:       perl(Future/AsyncAwait.pm) >= %{Future_AsyncAwait_minver}
%if %{defined perl_Future_AsyncAwait_ABI}
# Future::AsyncAwait maintains multiple ABIs whose compatibility is checked at
# run-time.
Requires:       %{perl_Future_AsyncAwait_ABI}
%endif
# lib/Syntax/Keyword/Dynamically.xs includes XSParseKeyword.h generated by
# XS::Parse::Keyword::Builder which loads XS::Parse::Keyword of version
# specified by boot_xs_parse_keyword() argument in Dynamically.xs
Requires:       perl(XS/Parse/Keyword.pm) >= 0.130
%if %{defined perl_XS_Parse_Keyword_ABI}
# XS::Parse::Keyword maintains multiple ABIs whose compatibility is checked at
# run-time by S_boot_xs_parse_keyword() compiled into this package.
# The ABI is defined in XSPARSEKEYWORD_ABI_VERSION of XSParseKeyword.h
Requires:       %{perl_XS_Parse_Keyword_ABI}
%endif
Source44: import.info

%description
This Perl module provides a syntax plugin that implements a single keyword,
dynamically, which alters the behavior of a scalar assignment operation.
Syntactically and semantically it is similar to the built-in Perl keyword
local, but is implemented somewhat differently to give two key advantages over
regular local: You can dynamically assign to left-value functions and
accessors, and you can dynamically assign to regular lexical variables.

%package tests
Group: Development/Perl
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with perl_Syntax_Keyword_Dynamically_enables_optional_test} && !%{defined perl_bootstrap}
# A cycle: perl-Future-AsyncAwait a.. perl-Syntax-Keyword-Dynamically
Requires:       perl(Future.pm)
Requires:       perl(Future/AsyncAwait.pm) >= 0.310
Requires:       perl(Object/Pad.pm) >= %{Object_Pad_minver}
Requires:       perl(Sentinel.pm)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Syntax-Keyword-Dynamically-%{version}
%if !%{with perl_Syntax_Keyword_Dynamically_enables_optional_test} || %{defined perl_bootstrap}
for F in t/80await+dynamically.t t/80dynamically+Object-Pad.t \
    t/80dynamically+Sentinel.t t/81async-method+dynamically.t t/99pod.t
do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
%endif
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
# %{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Syntax_Keyword_Dynamically_enables_optional_test} && !%{defined perl_bootstrap}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%doc --no-dereference LICENSE
%doc Changes README
%dir %{perl_vendor_archlib}/auto/Syntax
%dir %{perl_vendor_archlib}/auto/Syntax/Keyword
%{perl_vendor_archlib}/auto/Syntax/Keyword/Dynamically
%dir %{perl_vendor_archlib}/Syntax
%dir %{perl_vendor_archlib}/Syntax/Keyword
%{perl_vendor_archlib}/Syntax/Keyword/Dynamically.pm

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon Oct 23 2023 Igor Vlasenko <viy@altlinux.org> 0.13-alt1_1
- updated import, removed circular deps

* Mon Sep 25 2023 Igor Vlasenko <viy@altlinux.org> 0.13-alt1
- automated CPAN update

* Mon Mar 06 2023 Igor Vlasenko <viy@altlinux.org> 0.12-alt1
- automated CPAN update

* Sun Dec 25 2022 Igor Vlasenko <viy@altlinux.org> 0.11-alt1
- automated CPAN update

* Fri Dec 02 2022 Igor Vlasenko <viy@altlinux.org> 0.10-alt2_5
- to Sisyphus as perl-Sub-HandlesVia dep

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 0.10-alt1_5
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 0.10-alt1_4
- update to new release by fcimport

* Fri May 06 2022 Igor Vlasenko <viy@altlinux.org> 0.10-alt1_2
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.09-alt1_3
- update to new release by fcimport

* Wed Nov 24 2021 Igor Vlasenko <viy@altlinux.org> 0.09-alt1_2
- use import

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.08-alt2
- rebuild with perl 5.34.0

* Tue May 04 2021 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- updated by package builder

* Fri Feb 05 2021 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- updated by package builder

* Tue Nov 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Wed Oct 07 2020 Cronbuild Service <cronbuild@altlinux.org> 0.05-alt2
- rebuild to get rid of unmets

* Wed Jul 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Thu Feb 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated by package builder

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.01-alt1.1
- rebuild with perl 5.28.1

* Sun Aug 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

