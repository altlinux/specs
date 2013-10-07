%define module RPM-Source-BundleImport

Name: perl-%module
Version: 0.010
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Source-Editor perl-Source-Package
Requires: perl-RPM-Source-Editor > 0.810

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
