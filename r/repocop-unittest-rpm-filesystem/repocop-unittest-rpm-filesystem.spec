Name: repocop-unittest-rpm-filesystem
Version: 0.12
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: test for filesystem conflicts in rpm packages.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop > 0.59
Requires: perl-RPM-Source-Editor >= 0.70
Requires: repocop-collector-rpm-ext >= 0.07

Source: %name-%version.tar

%description
integration test for repocop test platform.

%prep
%setup -q

%build

%install
for i in *.distrotest; do
    testname=`echo $i | sed -e s,.distrotest\$,,`
    install -pD -m 755 $testname.distrotest %buildroot%_datadir/repocop/pkgtests/$testname/distrotest
done

#mkdir -p %buildroot%_datadir/repocop/fixscripts/
#install -m 644 *.pl %buildroot%_datadir/repocop/fixscripts/

%files
%_datadir/repocop/pkgtests/*
#%_datadir/repocop/fixscripts/*

%changelog
* Mon Jul 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- introduced distrotests

* Thu Jan 14 2010 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- increased level of all filesystem conflict tests.

* Fri Dec 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- added url 

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- posttests migration

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- excluded ghost files ftom checking.
  (thanks to @mithraen for report)

* Thu Jan 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added check for Obsoletes according to policy

* Fri Dec 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fixed bug: conflicts was not detected properly
  (thanks to @mithraen for report)

* Tue Dec 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- use repocop-collector-rpm-ext; stabilized against dups 

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- now checks not for conflict to name, but to providename.
  (thanks to mithraen@ for pointing out the problem)

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- bugfix in conflict-symlink-file (thanks to mithraen@)

* Wed Dec 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- removed duplicated messages

* Wed Dec 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixed message (thanks to mithraen@)

* Wed Dec 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
