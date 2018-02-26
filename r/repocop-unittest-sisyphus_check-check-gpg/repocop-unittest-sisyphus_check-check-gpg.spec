%define testname sisyphus_check-check-gpg
%define sisyphus_check_ver 0.8.7
%define sisyphus_check_rel alt1
Name: repocop-unittest-%testname
Version: 0.5.%sisyphus_check_ver
# we should bump release at every sisyphus_check release
Requires: sisyphus_check >= %sisyphus_check_ver-%sisyphus_check_rel
Release: %sisyphus_check_rel
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname intergration test for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop

%description
%testname intergration test for repocop test platform.
The test checks packages using sisyphus_check utility for the 
following sisyphus_check tests: gpg, buildhost, buildtime.

Note that this test is only for the very old packages in Sisyphus 
that are kept there from the ancient times before the hasher 
was even invented. Newer packages that have passed through 
the hasher should always pass those tests.

The test is not recommended for general use.

%prep

%build
cat > sisyphus_check-check-gpg.test <<'EOF'
#!/bin/bash
if sisyphus_check --verbose --files --no-check=ALL \
--check-gpg --check-buildhost --check-buildtime \
$REPOCOP_PKG > $REPOCOP_TEST_TMPDIR/msg 2>&1; then
    exec repocop-test-ok
else
    exec repocop-test-warn "package need a rebuild: it is too old, so that sisyphus_check complains: " `cat $REPOCOP_TEST_TMPDIR/msg`;
fi
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 %testname.test $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/test
cat > $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/options <<EOF
need_unpack=0
EOF

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.5.0.8.7-alt1
- added url

* Thu Feb 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.0.8.7-alt1
- added need_unpack=0 option

* Thu Nov 27 2008 Igor Vlasenko <viy@altlinux.ru> 0.4.0.8.6-alt1
- fixed #17944 (thanks to ildar@)

* Thu Nov 20 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.0.8.6-alt1
- fixed dependency on sisyphus_check (thanks to ildar@)

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.0.8.3-alt1
- check-gpg test moved to separate package

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
