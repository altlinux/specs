%define module Source-Repository

Name: perl-%module
Version: 0.07
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Source-Editor perl-RPM perl-DistroMap perl-String-ShellQuote perl-RPM-Source-Convert
Requires: perl-RPM-Source-Editor > 0.773
# for ALTLinux Backport; TODO: use separate module?
Requires: perl-RPM-Source-Convert > 0.40

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
* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- more strategies

* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt4
- added verbosity

* Tue Apr 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3
- bugfix release

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- support for rawhide nested folders

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- bugfix release

* Sat Dec 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3
- maintainance release

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- bugfix

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- new version

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3
- bugfix

* Wed Dec 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- bugfix

* Wed Dec 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new version

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- bugfixes

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- more options

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
