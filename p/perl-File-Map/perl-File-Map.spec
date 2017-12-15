Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-File-Map
Version:        0.65
Release:        alt1.1
Summary:        Memory mapping made simple and safe
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/File-Map/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/File-Map-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel >= 0:5.008
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(PerlIO/Layers.pm)
BuildRequires:  perl(Sub/Exporter/Progressive.pm)
BuildRequires:  perl(subs.pm)
BuildRequires:  perl(XSLoader.pm)
# Tests
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IO/Socket/INET.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(open.pm)
# Pod::Coverage::TrustPod 1.08 not used
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
BuildRequires:  perl(Test/Warnings.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(utf8.pm)


Source44: import.info

%description
File::Map maps files or anonymous memory into perl variables.


%prep
%setup -q -n File-Map-%{version}
chmod -x examples/fastsearch.pl


%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc LICENSE
%doc Changes examples README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/File*


%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1.1
- rebuild with new perl 5.26.1

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_4
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_3.1
- rebuild with new perl 5.24.1

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_2
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_1.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_1
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1.1_1
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt2_2
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt2_1
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1_1
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.60-alt2_1
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1_2
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1_1
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1_2
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1_1
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1_1
- update to new release by fcimport

* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.31-alt3_7
- rebuild with new perl

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2_7
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_7
- fc import

