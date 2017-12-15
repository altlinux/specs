%define module Source-Repository-Mass

Name: perl-%module
Version: 0.406
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Source-Editor perl(RPM/Header.pm) perl(RPM/Vercmp.pm) perl-String-ShellQuote perl-RPM-Source-Convert perl-Source-Package perl-RPM-Source-BundleImport perl-Source-Repository perl-Source-Shared-Resource perl(Source/Shared/Utils/GlobList.pm)
Requires: perl-RPM-Source-Editor > 0.912
Conflicts: perl-Source-Repository < 0.391

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
#doc README
%_bindir/*mass
%perl_vendor_privlib/Source*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.406-alt1
- added rosamass

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.405-alt1
- added jppmass

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.404-alt1
- bugfix release

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.403-alt1
- support for web mirrors

* Mon Oct 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.402-alt1
- development release

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.401-alt1
- bugfix release

* Thu Oct 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.400-alt1
- development release

* Wed Oct 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.399-alt1
- development release

* Tue Oct 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.398-alt1
- development release

* Sat Sep 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.397-alt1
- development release

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.396-alt1
- stable release

* Sun Apr 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.395-alt1
- development release

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.394-alt1
- stable release

* Thu Feb 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.393-alt1
- development release

* Sun Jan 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.392-alt1
- bugfix release

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.391-alt1
- use new CLI

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.390-alt1
- refactoring; use Source::Shared::*

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.387-alt1
- python3 fixes in Matcher

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.386-alt1
- development release

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.385-alt1
- chenges in new Convert and new TransformContainer

* Sat Jan 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.384-alt1
- new BundleImport

* Wed Jan 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.383-alt1
- new TransformContainer

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.382-alt1
- split Mass

* Wed Dec 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.381-alt1
- added tarball version trimmers

* Wed Dec 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.380-alt1
- added pypi shared subroutines

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.379-alt1
- stable release
