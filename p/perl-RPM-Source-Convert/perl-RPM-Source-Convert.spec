# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(File/Basename.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(Getopt/Long.pm) perl(Source/Repository/Mass.pm) perl(Source/Repository/Mass/Transform/Embedded.pm) perl(Source/Repository/Mass/Transform/PassThrough.pm) perl(Source/Repository/Matcher.pm) perl(Source/Repository/Matcher/DistroMap.pm)
# END SourceDeps(oneline)
%define module RPM-Source-Convert

Name: perl-%module
Version: 0.46
Release: alt6
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Source-Editor perl-RPM perl-DistroMap
Requires: perl-RPM-Source-Editor > 0.782

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
%_bindir/fcmass
%perl_vendor_privlib/RPM*

%changelog
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
