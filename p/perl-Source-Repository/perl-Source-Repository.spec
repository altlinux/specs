%define module Source-Repository

Name: perl-%module
Version: 0.384
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Source-Editor perl(RPM/Header.pm) perl(RPM/Vercmp.pm) perl-String-ShellQuote perl-Source-Package perl(JSON/XS.pm)
Conflicts: perl-RPM-Source-Convert < 0.48

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
%perl_vendor_privlib/Source*

%changelog
* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.384-alt1
- PyPI metadata download support

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.383-alt1
- stable release

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.382-alt1
- split Mass away

* Wed Dec 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.381-alt1
- added tarball version trimmers

* Wed Dec 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.380-alt1
- added pypi shared subroutines

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.379-alt1
- stable release

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.378-alt1
- stable release

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.377-alt1
- new version

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.376-alt1
- bugfix release

* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.375-alt1
- fast girar-copymass

* Tue Oct 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.374-alt1
- added girar-copymass

* Thu Oct 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.373-alt1
- mirror finder for bundle import

* Mon Oct 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.372-alt1
- added susemass

* Wed Oct 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.371-alt1
- local mirror finder
