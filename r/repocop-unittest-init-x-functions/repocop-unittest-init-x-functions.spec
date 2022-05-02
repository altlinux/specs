%define testname init-x-functions

Name: repocop-unittest-%testname
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname integration tests for repocop test platform
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Url: http://repocop.altlinux.org 
Requires: repocop repocop-collector-init-script

%description
%testname integration test for repocop test platform.
The test finds init scripts with incorrect test
[ -x /etc/rc.d/init.d/functions ].

%prep

%build
cat > posttest <<'EOF'
#!/bin/sh
pushd "$REPOCOP_STATEDIR/init-script" >/dev/null
for i in `grep -P -rl -- '-x /etc/rc.d/init.d/functions' *` ; do
    key=`dirname $i`
    file=`basename $i`
    repocop-test-warn -k $key "Invalid due to mode 644 test -x /etc/rc.d/init.d/functions in /etc/rc.d/init.d/$file. Use test -r or -e."
done
popd >/dev/null
EOF

cat > description <<'EOF'
The test finds init scripts with incorrect (due to 644 mode) test
[ -x /etc/rc.d/init.d/functions ].
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 755 posttest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 644 description $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Mon May 02 2022 Igor Vlasenko <viy@altlinux.org> 0.03-alt1
- new version

* Thu Oct 14 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- bugfix release

* Thu Oct 14 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
