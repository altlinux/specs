%define testname watch

Name: repocop-collector-%testname
Version: 0.03
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

cat > %testname.filepattern <<'EOF'
\.watch$
EOF

cat > %testname.test <<'EOF'
#!/bin/sh
files_exist()
{
    [ -e "$1" ]
}
rm -f $REPOCOP_TEST_STATEDIR/$REPOCOP_PKG_NAME.watch
if files_exist $REPOCOP_PKG_ROOT/*.watch; then
   mkdir -p $REPOCOP_TEST_STATEDIR/$REPOCOP_PKG_KEY
   cp $REPOCOP_PKG_ROOT/*.watch $REPOCOP_TEST_STATEDIR/$REPOCOP_PKG_KEY/$REPOCOP_PKG_NAME.watch
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
* Thu Jul 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added purge script

* Thu Jul 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- proper dependency on repocop version

* Thu Jul 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
