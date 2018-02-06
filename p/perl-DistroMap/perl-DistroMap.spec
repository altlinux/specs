%define module DistroMap

Name: perl-%module
Version: 0.39
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl interface for DistroMap database
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/DistroMap/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Pod/Usage.pm) perl(Pod/Text.pm) perl-Source-Shared-CLI

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
%_bindir/distrodb*
%_man1dir/distro*

%changelog
* Tue Feb 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- support for python-module-DistroDbMaker-generated distrodb

* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- rosa support

* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt2
- bugfix release

* Thu Sep 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- added distromap-db-query-extra-unimap

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- added distromap-db-query-binary-name

* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- new version

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- new CLI in DistroMap::Repository

* Fri Jan 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- bugfix release

* Fri Jan 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- script bugfixes

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- use shared CLI

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- back multimap fixes

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- python3 support

* Tue Nov 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2
- bugfix release

* Fri Oct 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- development release

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- stable release

* Mon Jul 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- stable release

* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- support for static distrodb tables

* Mon May 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- added calls to raw distromap

* Fri Mar 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- stable release

* Wed Nov 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2
- added texlive-python exception

* Wed Apr 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- API cleanup

* Fri Apr 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt2
- bugfix release

* Fri Apr 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- cpan support

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3
- NMU: added missing Pod dependencies

* Tue Oct 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2
- bugfix release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- basic pld support

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt4
- updated distrodb-*

* Sat Jun 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3
- higher priority for the stem map

* Fri May 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2
- pre-support for autoimports/t7

* Wed May 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- renamed distromap-update-* utils to distrodb-update-*

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- disabled generic stem filter by default (thanks to aris@)

* Mon Jan 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- noepoch flag support

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- bugfix release

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- support for versioned distrodb

* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- added flags/binary/exclude

* Tue Nov 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- mageia support

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- development release

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
