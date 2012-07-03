%define testname rpm-recursive-symlink

Name: repocop-unittest-%testname
Version: 0.07
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop test for recurrent symlinks.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop > 0.43
Requires: sqlite3

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
repocop-sqlite -function symlink_canonpath.pl "$REPOCOP_TEST_TMPDIR/tmp.db" <<EOSQL
attach database '$REPOCOP_TEST_DBDIR/rpm.db' as rpm;
CREATE TEMPORARY TABLE rpm_symlinks (pkgid TEXT, symlink TEXT, symvalue TEXT);
INSERT INTO rpm_symlinks select pkgid, filename, symlink_canonpath(FILENAME,FILELINKTO) FROM rpm_files WHERE filemode & 61440 = 40960;
.mode tabs
.output $REPOCOP_TEST_TMPDIR/msg
select pkgid, symlink from rpm_symlinks where symlink = symvalue;
DROP TABLE rpm_symlinks;
EOSQL
perl -ne 'chomp;@a=split /\t/;system("repocop-test-fail", "-k", $a[0], "broken sybolic link $a[1] points to itself.")' $REPOCOP_TEST_TMPDIR/msg
rm "$REPOCOP_TEST_TMPDIR/"*
EOF

%install
install -D -m 755 %testname.posttest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/posttest
install -D -m 644 symlink_canonpath.pl $RPM_BUILD_ROOT%_datadir/repocop/sqlite-functions/symlink_canonpath.pl

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname
%_datadir/repocop/sqlite-functions/*

%changelog
* Tue Mar 23 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added external function for repocop-sqlite

* Thu Feb 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added symlink value in canonical paths.
- First build for Sisyphus.
