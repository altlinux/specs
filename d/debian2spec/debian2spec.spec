%define module RPM-Specfile-Multispec

Name: debian2spec
Version: 1.07
Release: alt3
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: converter of debian source directory to RPM specfile format
Group: Development/Other
License: GPL or Artistic
Url: http://search.cpan.org/dist/RPM-Specfile-Multispec

Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl-RPM-Specfile

%description -n debian2spec
debian2spec utility creates a initial RPM spec file for the source RPM package
using debian control directory of source Debian package.

%package -n perl-%module
Summary: RPM::Specfile::Multispec - Perl extension for creating RPM Specfiles
Group: Development/Perl

%description -n perl-%module
This is a debian2spec utility used to create initial spec files 
from the debian control directory using RPM-Specfile-Multispec ---
 module for creation of RPM spec files with multiple subpackages.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%_bindir/*

%files -n perl-%module
%perl_vendor_privlib/R*
#perl_vendor_man3dir/*

%changelog
* Sun Nov 21 2010 Igor Vlasenko <viy@altlinux.ru> 1.07-alt3
- rebuild w/new perl

* Wed Sep 03 2008 Igor Vlasenko <viy@altlinux.ru> 1.07-alt2
- removed perl dir ownership

* Mon Apr 28 2008 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- added License: detection

* Sun Jan 21 2007 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- removed duplication in subpackages

* Sun Jan 21 2007 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- added pickup of docs, watch, prein

* Sat Dec 23 2006 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- ver. 1.03 was lost :(
- resurrected: more groups, macros, etc
- still lost: aggresive altlinux macro substitution in rules

* Wed Dec 20 2006 Grigory Batalov <bga@altlinux.ru> 1.03-alt0.M24.1
- Backport to Master 2.4.

* Thu Nov 30 2006 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- aggresive altlinux macro substitution in rules
- more groups, macros, etc

* Sat Oct 28 2006 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- new version - added pickup of doc-base
- picked up .rpmmacros

* Tue Jul 18 2006 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- new version - added pickup of man pages

* Thu Jul 06 2006 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- First build for Sisyphus.
