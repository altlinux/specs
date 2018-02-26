%define testname init-lsb

Name: repocop-unittest-%testname
Version: 0.06
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname integration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop > 0.40
Requires: repocop-collector-init-script

%description
%testname integration test for repocop test platform.
The test warns packages that do not have lsb compliant init scripts.

%prep

%build
cat > posttest <<'EOF'
#!/bin/sh
for repocop_pkg_key in `ls $REPOCOP_STATEDIR/init-script`; do
    keydir="$REPOCOP_STATEDIR/init-script/$repocop_pkg_key"
    STATUS=ok
    MESSAGE=
    for i in "$keydir"/*; do
        filename=${i##$keydir}
	if [ -x $i ]; then
	    HAS_INIT=`grep '# chkconfig:' $i`
	    HAS_LSB_INIT=`grep '### BEGIN INIT INFO' $i`
            if [ -z "$HAS_LSB_INIT" ]; then
                if [ -n "$HAS_INIT" ]; then
                    STATUS=warn
                    MESSAGE="$MESSAGE%_initdir/$filename: lsb init header missing. "
                else
		    STATUS=warn
                    MESSAGE="$MESSAGE%_initdir/$filename: strange executable: neither lsb header nor chkconfig header aren't found. "
                fi
            fi
        fi
    done
    repocop-test-$STATUS -k $repocop_pkg_key "$MESSAGE See http://www.altlinux.org/Services_Policy for details."
done
EOF

cat > description <<'EOF'
The files the test is worrying about are non lsb compliant init scripts.
In order to implement parallel system boot we need to add an lsb init header
to every init script.
See http://www.altlinux.org/Services_Policy for details.
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 755 posttest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 644 description $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- rewritten as posttest

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- raised importance to warning

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- added url

* Sat Mar 29 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- now use repocop-test-info

* Thu Feb 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- silent skip

* Mon Feb 25 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- First build for Sisyphus.
