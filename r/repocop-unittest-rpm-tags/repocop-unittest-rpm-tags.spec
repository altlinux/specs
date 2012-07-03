Name: repocop-unittest-rpm-tags
Version: 0.02
Release: alt3
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: test for tag values in rpm packages.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop > 0.19
Requires: perl-RPM-Source-Editor >= 0.40
Requires: repocop-collector-rpm-ext >= 0.05

Source: %name-%version.tar

%description
integration test for repocop test platform.

%prep
%setup -q

%build

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

# stub for 2-in-1 test rpm-obsolete-live-package
mkdir -p %buildroot%_datadir/repocop/pkgtests/rpm-package-is-obsoleted/
touch %buildroot%_datadir/repocop/pkgtests/rpm-package-is-obsoleted/posttest
chmod 755 %buildroot%_datadir/repocop/pkgtests/rpm-package-is-obsoleted/posttest

#mkdir -p %buildroot%_datadir/repocop/fixscripts/
#install -m 644 *.pl %buildroot%_datadir/repocop/fixscripts/

%files
%_datadir/repocop/pkgtests/*
#%_datadir/repocop/fixscripts/*

%changelog
* Thu Sep 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt3
- fixed misprint 

* Sun Nov 08 2009 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- fixed Url:

* Fri Nov 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixed misprint (thanks to REAL@)

* Wed Oct 28 2009 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- added Url:

* Tue Oct 27 2009 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
