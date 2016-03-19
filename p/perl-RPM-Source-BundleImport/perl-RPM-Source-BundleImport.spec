%define module RPM-Source-BundleImport

Name: perl-%module
Version: 0.027
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Source-Editor perl-Source-Package perl(Pod/PlainText.pm)
Requires: perl-Source-Package > 0.04
Requires: perl-RPM-Source-Editor > 0.854

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/RPM*

%changelog
* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1
- development release

* Wed Feb 24 2016 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- bugfix release

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- development release

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- development release

* Sat Jan 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- development release

* Sun Feb 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- development release

* Thu Oct 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- development release

* Tue May 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- development release

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- development release

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- bugfix release

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- development release

* Tue Apr 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- bugfix release

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- development release

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- development release

* Fri Oct 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- bugfix release

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- development release

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- development release

* Sun Oct 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- development release

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- development release

* Thu Sep 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- development release

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- development release

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- development release

* Wed Aug 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- development release

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- development release

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- development release

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- development release

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial release
