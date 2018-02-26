%define testname library-pkgnames

Name: repocop-unittest-%testname
Version: 0.09
Release: alt1
BuildArch: noarch
Requires: repocop >= 0.19

Summary: %testname intergration tests for repocop test platform.
Group: Development/Other
License: GPLv2+
Packager: Igor Yu. Vlasenko <viy@altlinux.org>
Url: http://repocop.altlinux.org 

%description
The test warns packages that contain shared libraries, but are not named
appropriately.

%prep

%build

cat > %testname.posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_TMPDIR/tmp.db" <<EOSQL
attach database '$REPOCOP_TEST_DBDIR/rpm.db' as rpm;
.mode tabs
.output $REPOCOP_TEST_TMPDIR/info
-- select distinct a.pkgid from rpm_provides as a LEFT JOIN rpm as c ON a.pkgid=c.pkgid LEFT JOIN rpm as e ON c.sourceid=e.pkgid, rpm_requires as b LEFT JOIN rpm as d ON b.pkgid=d.pkgid LEFT JOIN rpm as f ON f.pkgid=d.sourceid where a.pkgid!=b.pkgid AND providename glob 'lib*.so*' AND a.pkgid NOT glob 'lib*' AND a.pkgid NOT glob 'glib*' AND c.name NOT glob '*lib' AND providename = requirename AND e.name!=f.name;
select distinct a.pkgid from rpm_provides as a LEFT JOIN rpm as c ON a.pkgid=c.pkgid LEFT JOIN srcrpm as e ON c.sourceid=e.pkgid, rpm_requires as b LEFT JOIN rpm as d ON b.pkgid=d.pkgid LEFT JOIN srcrpm as f ON f.pkgid=d.sourceid where a.pkgid!=b.pkgid AND providename glob 'lib*.so*' AND a.pkgid NOT glob 'lib*' AND a.pkgid NOT glob 'glib*' AND c.name NOT glob '*lib' AND providename = requirename AND e.name!=f.name;
EOSQL
for i in `cat $REPOCOP_TEST_TMPDIR/info`; do repocop-test-info -k $i "package contains public library which is used in external packages: name should be lib* according to http://altlinux.org/Drafts/SharedLibs"; done
rm $REPOCOP_TEST_TMPDIR/*
EOF

cat > %testname-static.posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_TMPDIR/tmp.db" <<EOSQL
attach database '$REPOCOP_TEST_DBDIR/rpm.db' as rpm;
CREATE TEMPORARY TABLE static_list (alibpkgid TEXT, alib TEXT, soliblikepatt TEXT, alibname TEXT);
INSERT INTO static_list select a.pkgid, filename, substr(a.filename,1,length(a.filename)-2)||'.so*', NAME from rpm_files as a, rpm as b where a.filename glob '*.a' and not a.pkgid glob '*-devel-static-*' and not a.filename glob '/lib/*/*' and not a.filename glob '/usr/lib/*/*' and not a.filename glob '/usr/lib64/*/*' AND a.pkgid=b.pkgid;

CREATE TEMPORARY TABLE dynamic_list (solibpkgid TEXT, solib TEXT, solibname TEXT);
INSERT INTO dynamic_list select a.pkgid, filename, name from rpm_files as a, rpm as b where filename glob '*.so*' AND a.pkgid=b.pkgid;
.mode tabs
.output $REPOCOP_TEST_TMPDIR/warn
-- to view both libraries
-- select alibpkgid,alib,solibpkgid from dynamic_list as a, static_list as b where solib GLOB soliblikepatt AND not solibname IN (SELECT CONFLICTNAME from rpm_conflicts as c WHERE c.pkgid = alibpkgid) AND not alibname IN (SELECT CONFLICTNAME from rpm_conflicts as d WHERE d.pkgid = solibpkgid);
select distinct alibpkgid from dynamic_list as a, static_list as b where solib GLOB soliblikepatt AND not solibname IN (SELECT CONFLICTNAME from rpm_conflicts as c WHERE c.pkgid = alibpkgid) AND not alibname IN (SELECT CONFLICTNAME from rpm_conflicts as d WHERE d.pkgid = solibpkgid);
DROP TABLE static_list;
DROP TABLE dynamic_list;
EOSQL
for i in `cat $REPOCOP_TEST_TMPDIR/warn`; do repocop-test-warn -k $i "package contains static library which has the same name as a shared library in the repository, but neither package name ends with -devel-static according to http://altlinux.org/Drafts/SharedLibs nor the package explicitly conflicts with the package with .so library"; done
rm $REPOCOP_TEST_TMPDIR/*
EOF


%install
install -pD -m 755 %testname.posttest %buildroot%_datadir/repocop/pkgtests/%testname/posttest
install -pD -m 755 %testname-static.posttest %buildroot%_datadir/repocop/pkgtests/%testname-static/posttest

%files
%_datadir/repocop/pkgtests/%testname/
%_datadir/repocop/pkgtests/%testname-static/

%changelog
* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- posttests migration

* Sat Aug 01 2009 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- fixed bug in substr

* Thu May 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- added url

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- repocop 0.10 adaptation

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- library-pkgnames:
  fixed sensitivity to duplicate srpms (thanks to ldv@)

* Mon Sep 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- refs to wiki.altlinux.org (#16724)

* Tue May 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- fixed duplicate messages

* Sat Apr 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added test for static libs

* Wed Apr 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- adapted to repocop 0.07

* Fri Mar 14 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.01-alt1
- initial version
