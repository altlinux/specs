# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(File/Basename.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(Getopt/Long.pm)
# END SourceDeps(oneline)
%define module RPM-Source-Convert

Name: perl-%module
Version: 0.603
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl-RPM-Source-Editor perl-RPM-Source-Dependency-Analyzer perl-RPM perl-DistroMap
Requires: perl-RPM-Source-Editor > 0.851

# for srpmbackport 
Requires: distromap-altlinux-sisyphus-altlinux-branch
Conflicts: perl-RPM-Source-Editor < 0.73

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
%_bindir/srpmbackport
%_bindir/srpmconvert-*
%perl_vendor_privlib/RPM*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.603-alt1
- stable release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.602-alt1
- bugfix release

* Fri Jan 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.601-alt1
- development release

* Sat Dec 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.600-alt1
- bugfix release

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt4
- stable release

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt3
- stable release

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt2
- bugfix release

* Sun Nov 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- stable release

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.58-alt4
- stable release

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.58-alt3
- stable release

* Thu Nov 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.58-alt2
- stable release

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- bugfix release

* Sat Jul 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- stable release

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- bugfix release

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- development release

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.54-alt5
- bugfix release
- bumped fc version to 21

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt4
- bumped fc version to 20

* Tue Oct 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt3
- bugfix release

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt2
- c7 support in srpmbackport

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- development release

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.53-alt2
- bugfix release

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- support for the new API

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt7
- initial PLD support

* Sat Aug 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt6
- stable release

* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt5
- bugfix release

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt4
- better mageya perl support

* Thu Jul 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt3
- A70 support

* Sat May 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt2
- bugfix release

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- bugfix release

* Sat Apr 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.51-alt5
- bugfix release

* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.51-alt4
- bugfix release

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.51-alt3
- bugfix release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.51-alt2
- bugfix release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- new version

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt5
- stable release

* Fri Feb 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt4
- development release

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt3
- development release

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2
- development release

* Sun Jan 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- development release

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- development release

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- development release

* Wed Oct 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- stable release

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt10
- development release

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt9
- improvements in fc support

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt8
- improved fc support

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt7
- improved fc support

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt6
- development release

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt5
- improved fc support

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt4
- improvements in perl fc import

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt3
- improved perl fc import

* Tue May 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt2
- improved fc support

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- new version

* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- new version

* Sat Dec 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- new version

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- new version

* Tue Dec 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- new version

* Fri Dec 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- support for new Analyzer

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.39-alt4
- maintainance release

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.39-alt3
- removed Mass.pm (obsoleted by Source-Repository)
