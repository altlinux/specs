
Name: debian2spec
Version: 1.090
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: converter of debian source directory to RPM specfile format
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Url: git://git.altlinux.org/people/viy/%name

Source: %name-%version.tar

BuildRequires: perl-devel perl-podlators perl-RPM-Specfile-Multispec perl(Pod/Usage.pm)

%description -n debian2spec
debian2spec utility creates a initial RPM spec file for the source RPM package
using debian control directory of source Debian package.

%prep
%setup -q

%build
pod2man debian-patches-series2spec-in > debian-patches-series2spec-in.1

%install
mkdir -p %buildroot%_bindir/ %buildroot%_man1dir/
install -m 755 debian-patches-series2spec-in debian2spec %buildroot%_bindir/
install -m 644 debian-patches-series2spec-in.1 %buildroot%_man1dir/

%files
%doc Changes
%_bindir/*
%_man1dir/*

%changelog
* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 1.090-alt1
- new version
- moved RPM-Specfile-Multispec to separate distribution

* Fri Sep 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- new version

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
