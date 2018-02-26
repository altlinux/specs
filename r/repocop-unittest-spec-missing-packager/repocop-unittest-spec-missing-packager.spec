%define testname spec-missing-packager

Name: repocop-unittest-%testname
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname intergration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop

%description
%testname intergration test for repocop test platform.
The test checks spec files to have Packager: tag.

%prep

%build
cat > test <<'EOF'
#!/bin/sh
if grep '^Packager:' $REPOCOP_PKG_SPECFILE >/dev/null; then 
    exec repocop-test-ok
else 
    exec repocop-test-experimental "spec file: missing Packager: tag. Gear unfriendly :("
fi
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/srctests/%testname/
%__install -m 755 test $RPM_BUILD_ROOT%_datadir/repocop/srctests/%testname/

%files
#doc README ChangeLog
%_datadir/repocop/srctests/%testname

%changelog
* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added url

* Tue May 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- message level is set to experimental

* Mon Apr 14 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
