%define testname systemd-but-no-native-init

Name: repocop-unittest-%testname
Version: 0.02
Release: alt1
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: repocop > 0.55
Url: http://repocop.altlinux.org

Summary: %testname integration tests for repocop test platform.
Group: Development/Other
License: GPLv2+

%description
The test warns packages that have support for
systemd but not for Sys-V init


%prep

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_DBDIR/rpm.db" <<EOSQL
.mode tabs
.output $REPOCOP_TEST_TMPDIR/msg-pre
select a.pkgid,a.filename from rpm_files as a where (a.filename glob '/lib/systemd/system/*' or a.filename glob '/usr/lib/systemd/system/*') and a.pkgid not in (select c.pkgid from rpm_files as c where c.filename glob '/etc/rc.d/init.d/*');
EOSQL
sed -i -e '/^service-/d;/^systemd-/d' $REPOCOP_TEST_TMPDIR/msg-pre
cat $REPOCOP_TEST_TMPDIR/msg-pre | while read -r pkgid service; do
    servicename=${service##/usr}
    servicename=${servicename##/lib/systemd/system/}
    case $pkgid in
    	 vsftpd-*|daemontools-* ) : nothing
	 ;;
	 *)
	 servicepath=$REPOCOP_STATEDIR/systemd/$pkgid/system/$servicename
	 if ! [ -e $servicepath ] || ! (grep -q '^Type=dbus' $servicepath || grep -q '^Alias=display-manager.service' $servicename); then
	     echo $pkgid >> $REPOCOP_TEST_TMPDIR/msg
	 fi
	 ;;
    esac
done

for i in `cat $REPOCOP_TEST_TMPDIR/msg`; do repocop-test-info -k $i "The package have native systemd file(s) but no  SysV init scripts."; done
rm $REPOCOP_TEST_TMPDIR/*
EOF

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

#mkdir -p %buildroot%_datadir/repocop/fixscripts/
#install -p -m 755 *.pl %buildroot%_datadir/repocop/fixscripts/

%files
%_datadir/repocop/pkgtests/%testname/
#%_datadir/repocop/fixscripts/*.pl

%changelog
* Thu Feb 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- ignore Type=dbus services
- Alias=display-manager.service

* Wed Feb 04 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- fixed misprints

* Tue Feb 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial version
