%define module DistroMap

Name: perl-%module
Version: 0.13
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl interface for DistroMap database
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/DistroMap/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Pod/Usage.pm)

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
%perl_vendor_privlib/D*
%_bindir/distromap*

%changelog
* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- basic support for flags

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt7
- bugfixes in distromap-filter-translate-source-names

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt6
- updated autoimports location - again

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt5
- updated autoimports location

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt4
- support for autoimports

* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3
- added python modules filter;

* Wed May 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2
- improvements in binary mapping

* Mon Jan 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- SuSE support

* Thu Jan 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt3
- fixes in filters

* Wed Jan 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- added drop-uncomparable option

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- new version

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- added doc subpackage translation

* Fri Dec 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- new version

* Thu Dec 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- more verbose

* Thu Dec 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- moved repodb to distrodb

* Mon Dec 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added generic translate method

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- lazy load of repo db

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- new version

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Fri Dec 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- added subscripts for distromap update

* Tue Nov 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- new version

* Fri Nov 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new version

* Sat Oct 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new version

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- bugfix release

* Thu Jun 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
