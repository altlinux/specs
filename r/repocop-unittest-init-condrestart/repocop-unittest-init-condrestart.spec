%define testname init-condrestart

Name: repocop-unittest-%testname
Version: 0.04
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: lsb-init integration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop

%description
init-condrestart integration test for repocop test platform.
The test warns packages that do not have condrestart and condstop
goals in their init scripts. It is because alt-specific scripts
/usr/sbin/post_service (used in %%post_service macro)
and /usr/sbin/preun_service (used in %%preun_service macro)
depends on condrestart and condstop respectively.

%prep

%build
cat > test <<'EOF'
#!/bin/sh
files_exist()
{
    [ -e "$1" ]
}
if files_exist $REPOCOP_PKG_ROOT/etc/init.d/*; then
	STATUS=warn
	MESSAGE="warning: found files in /etc/init.d/; better to use %%_initdir=%_initdir"
else
	STATUS=ok
	MESSAGE=
	files_exist $REPOCOP_PKG_ROOT%_initdir/* || exec repocop-test-skip
fi

for i in $REPOCOP_PKG_ROOT%_initdir/* $REPOCOP_PKG_ROOT/etc/init.d/*; do
    filename=${i##$REPOCOP_PKG_ROOT}
    if [ -x $i ]; then
        HAS_CONDRESTART=`grep 'condrestart' $i`
        if [ -z "$HAS_CONDRESTART" ]; then
	    if rpmquery --scripts -p $REPOCOP_PKG | grep post_service >/dev/null; then
	        STATUS=fail
            	MESSAGE="$MESSAGE$filename: missing condrestart target. ERROR: alt-specific script %%_sbindir/post_service (used in your %%post_service macro) depends on condrestart. Please, fix."
	    else
	    	[ "$STATUS" != "fail" ] && STATUS=warn
		MESSAGE="$MESSAGE$filename: missing condrestart target. Note: alt-specific script %%_sbindir/post_service (used in %%post_service macro) depends on condrestart. It is wise to add condrestart anyway."
	    fi
        fi
        HAS_CONDSTOP=`grep 'condstop' $i`
        if [ -z "$HAS_CONDSTOP" ]; then
	    if rpmquery --scripts -p $REPOCOP_PKG | grep preun_service >/dev/null; then
	        STATUS=fail
            	MESSAGE="$MESSAGE$filename: missing condstop target. ERROR: alt-specific script %%_sbindir/preun_service (used in your %%preun_service macro) depends on condstop. Please, fix."
	    else
	    	[ "$STATUS" != "fail" ] && STATUS=warn
		MESSAGE="$MESSAGE$filename: missing condstop target. Note: alt-specific script %%_sbindir/preun_service (used in %%preun_service macro) depends on condstop. It is wise to add condstop anyway."
	    fi
        fi
    fi
done
repocop-test-$STATUS $MESSAGE
EOF

cat > description <<'EOF'
The test warns packages that do not have condrestart and condstop
goals in their init scripts. It is because alt-specific scripts
/usr/sbin/post_service (used in %%post_service macro)
and /usr/sbin/preun_service (used in %%preun_service macro)
depends on condrestart and condstop respectively.
TODO: write page on wiki.
EOF

cat > filepattern <<'EOF'
^/etc/rc.d/init.d/
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 755 test $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 644 description $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 644 filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added filepattern

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- added url

* Sat Mar 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added check for /etc/init.d/ used instead of %%_initdir

* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added check on condstop target

* Sat Mar 01 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
