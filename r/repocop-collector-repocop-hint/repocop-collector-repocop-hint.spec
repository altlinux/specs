%define testname repocop-hint

Name: repocop-collector-%testname
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop collector for debian watch files.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop > 0.61
Requires: sqlite3


%description
%summary

%prep

%build
# repocop-test-hint:binary:python-module-ztfy.jqueryui:altlinux-python-test-is-packaged
cat > %testname.filepattern <<'EOF'
^repocop-test-hint:
EOF

cat > %testname.test <<'EOF'
#!/bin/sh
files_exist()
{
    [ -e "$1" ]
}
rm -f $REPOCOP_TEST_STATEDIR/$REPOCOP_PKG_KEY
if files_exist $REPOCOP_PKG_ROOT/repocop-test-hint:*; then
   mkdir -p $REPOCOP_TEST_STATEDIR/$REPOCOP_PKG_KEY
   cp $REPOCOP_PKG_ROOT/repocop-test-hint:* $REPOCOP_TEST_STATEDIR/$REPOCOP_PKG_KEY/
fi
EOF

%install
install -D -m 755 %testname.test $RPM_BUILD_ROOT%_datadir/repocop/srccollectors/%testname/test
install -D -m 644 %testname.filepattern $RPM_BUILD_ROOT%_datadir/repocop/srccollectors/%testname/filepattern
ln -s ../../common/purge-keydir $RPM_BUILD_ROOT%_datadir/repocop/srccollectors/%testname/purge

%files
#doc README ChangeLog
%_datadir/repocop/srccollectors/%testname

%changelog
* Sun Feb 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
