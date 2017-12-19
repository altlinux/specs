Name: repocop-unittest-systemd
Version: 0.06
Release: alt1
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>
Url: http://repocop.altlinux.org

Summary: systemd integration tests for repocop test platform.
Group: Development/Other
License: GPLv2+

Source: %name-%version.tar

# for pixmap-in-deprecated-location
# Requires: pcregrep
Requires: repocop-collector-systemd
Requires: repocop > 0.59

%description
The test check systemd related files.

%prep
%setup

%build

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

install -D -m 755 systemd.dir-verify.pl %buildroot%_bindir/systemd.dir-verify.pl
rm systemd.dir-verify.pl

for i in *.pl; do
    install -pD -m 644 $i %buildroot%_datadir/repocop/fixscripts/$i
done

%files
%_bindir/*
%_datadir/repocop/pkgtests/*
%_datadir/repocop/fixscripts/*

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- fixed build with new perl 5.26

* Tue Apr 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- bugfix release

* Mon Apr 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- bugfix release

* Mon Apr 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- bugfix release

* Sun Apr 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added *-files-in-etc tests and patch generators

* Mon Jul 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first release for Sysiphus
