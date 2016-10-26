# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(File/Basename.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(Getopt/Long.pm)
# END SourceDeps(oneline)
%define module RPM-Source-Convert

Name: perl-%module
Version: 0.620
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl-RPM-Source-Editor perl-RPM-Source-Dependency-Analyzer perl(RPM/Vercmp.pm) perl-DistroMap
Requires: perl-RPM-Source-Editor > 0.856

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
* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.620-alt1
- moved SourceAnalyzer after prehooks

* Mon Oct 24 2016 Igor Vlasenko <viy@altlinux.ru> 0.619-alt1
- development release

* Sun Oct 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.618-alt1
- bumped suse version to 1320 thnx to Ruslan Hihin 

* Tue Oct 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.617-alt1
- bugfix release

* Thu Oct 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.616-alt1
- bugfix release

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.615-alt2
- indirect RPM deps

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.615-alt1
- use RPM::Vercmp

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.614-alt1
- better SuSE support

* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.613-alt1
- stable release

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.612-alt1
- stable release (mageia)

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.611-alt1
- stable release (mageia)

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.610-alt1
- mageia support fixes

* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.609-alt1
- stable release

* Fri Apr 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.608-alt1
- stable release

* Sun Apr 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.607-alt1
- development release

* Sun Feb 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.606-alt1
- stable release

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.605-alt1
- development release

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.604-alt1
- development release

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.603-alt1
- stable release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.602-alt1
- bugfix release

* Fri Jan 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.601-alt1
- development release

* Sat Dec 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.600-alt1
- bugfix release
