%define testname sisyphus_check
%define sisyphus_check_ver 0.8.14
%define sisyphus_check_rel alt1
Name: repocop-unittest-%testname
Version: 0.6.3
Requires: sisyphus_check >= %sisyphus_check_ver
#Requires: sisyphus_check = %sisyphus_check_ver-%sisyphus_check_rel
Release: %sisyphus_check_rel
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname intergration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop

%description
%testname intergration test for repocop test platform.
The test checks packages using sisyphus_check utility.

%prep

%build
cat > sisyphus_check.test <<'EOF'
#!/bin/bash
# gpg,buildhost,buildtime are in separate test %name-check-gpg
# check-group is too rpm-sensitive; also, GROUPS are monotonic.
if sisyphus_check --verbose --files \
   --no-check-gpg --no-check-buildhost --no-check-buildtime --no-check-dirlist \
   --no-check-group \
   $REPOCOP_PKG > $REPOCOP_TEST_TMPDIR/msg 2>&1; then
    exec repocop-test-ok
else
    exec repocop-test-fail "sisyphus_check failed: " `cat $REPOCOP_TEST_TMPDIR/msg`;
fi
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 %testname.test $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/test
cat > $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/options <<EOF
need_unpack=0
EOF
touch $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/build.timestamp

%triggerin -- sisyphus_check
# if test itself is installed/updated, just keep build timestamp
[ $2 = 1 ] && exit 0 ||:
# at every sisyphus_check change we should bump timestamp
# to discard cached results of old sisyphus_check
touch %_datadir/repocop/pkgtests/%testname/test

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Sat Oct 10 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1
- use sisyphus_check >= 0.8.14-alt1

* Sat Aug 01 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1
- use sisyphus_check >= 0.8.13-alt1

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- added url

* Sat Feb 14 2009 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- keeps build timestamp to be able to use repocop cache

* Thu Feb 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- use triggerin on sisyphus_check to to discard cached results 
  on sisyphus_check update instead of strict dependency.

* Thu Feb 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.0.8.7-alt1
- hack around girar (not to burden sisyphus-check)

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0.4.0.8.6-alt1
- disabled check-group as its warnings are always due to outdated rpm.

* Thu Oct 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.0.8.6-alt1
- use sisyphus_check = 0.8.6-alt1

* Sun Sep 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.0.8.5-alt1
- use sisyphus_check = 0.8.5-alt1

* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.0.8.4-alt1
- use sisyphus_check = 0.8.4-alt1

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.0.8.3-alt1
- check-gpg,check-dirlist tests moved to separate packages

* Wed Aug 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.0.8.2-alt1
- added check-gpg test

* Tue Aug 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.2.0.8.2-alt1
- sisyphus_check-check-dirlist implemented using collector
- set fail level
- future support for sisyphus_check-check-gpg

* Sat Aug 09 2008 Igor Vlasenko <viy@altlinux.ru> 0.1.0.8.2-alt1
- use sisyphus_check = 0.8.2-alt1
- set info level

* Fri Aug 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- use sisyphus_check = 0.8.1-alt1
- First build for Sisyphus.
