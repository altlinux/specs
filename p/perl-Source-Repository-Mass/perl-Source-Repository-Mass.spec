%define module Source-Repository-Mass

Name: perl-%module
Version: 0.392
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Source-Editor perl(RPM/Header.pm) perl(RPM/Vercmp.pm) perl-String-ShellQuote perl-RPM-Source-Convert perl-Source-Package perl-RPM-Source-BundleImport perl-Source-Repository perl-Source-Shared-Resource
Requires: perl-RPM-Source-Editor > 0.898
Conflicts: perl-RPM-Source-Convert < 0.48
Conflicts: perl-Source-Repository < 0.382

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
