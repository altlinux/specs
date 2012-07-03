%define testname checkbashisms

Name: repocop-unittest-%testname
Version: 0.05
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname integration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop
Requires: checkbashisms > 2.11

%description
%testname integration test for repocop test platform.
The test checks sh scripts for bashisms.

%prep

%build
cat > filepattern <<'EOF'
^/bin/
^/sbin/
^/usr/bin/
^/usr/sbin/
^/etc/rc.d/init.d/
^/usr/share/repocop/
EOF

cat > test <<'EOF'
#!/bin/bash
echo ok > $REPOCOP_TEST_TMPDIR/status
rm -f $REPOCOP_TEST_TMPDIR/message
FAIL_STATUS=experimental
shabangbinshpath=`dirname $0`
shabangbinsh=${shabangbinshpath}/shabangbinsh
findpath=
for fdir in bin sbin usr/bin usr/sbin etc/rc.d/init.d usr/share/repocop; do
[ -d "$REPOCOP_PKG_ROOT/$fdir" ] && findpath="$findpath $REPOCOP_PKG_ROOT/$fdir"
done
[ -z "$findpath" ] && exec repocop-test-ok
find $findpath -type f -print  | \
while read file; do
    if [ -e "$file" ] && cmp -n 9 $shabangbinsh "$file" > /dev/null && \
    [[ `file "$file"` == *'Bourne shell script text executable'* ]]; then
        TODO_MSG=`checkbashisms "$file" 2>&1`
        if [ $? -eq 1 ]; then
	    [ -e $REPOCOP_TEST_TMPDIR/message ] || echo -n "checkbashisms utility found possible bashisms in:" > $REPOCOP_TEST_TMPDIR/message
	    echo $FAIL_STATUS > $REPOCOP_TEST_TMPDIR/status
	    echo -n " ${file##$REPOCOP_PKG_ROOT}" >> $REPOCOP_TEST_TMPDIR/message
	fi
    fi
done
[ -e $REPOCOP_TEST_TMPDIR/message ] && \
exec repocop-test-`cat $REPOCOP_TEST_TMPDIR/status` `cat $REPOCOP_TEST_TMPDIR/message` || \
exec repocop-test-`cat $REPOCOP_TEST_TMPDIR/status`
EOF

# line #!/bin/sh is given to cmp as $shabangbinsh
cat > shabangbinsh <<'EOF'
#!/bin/sh 
EOF

cat > description <<'EOF'
At present time /bin/sh is the link to bash but that may change in the future.
The test checks sh scripts for bashisms.
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 755 test $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 644 description $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 644 filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 644 shabangbinsh $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Mon Aug 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- new checkbashisms version

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new checkbashisms version
- reduced importance to experimental

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- fixed extra verbosity

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- bugfix release.

* Wed Aug 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build.
