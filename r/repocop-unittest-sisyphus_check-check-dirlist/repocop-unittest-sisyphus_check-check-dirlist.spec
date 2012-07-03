%define testname sisyphus_check-check-dirlist
Name: repocop-unittest-%testname
Version: 0.6
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname intergration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop
Requires: repocop-collector-rpmbuild-files-req-list

%description
%testname intergration test for repocop test platform.
The test checks packages for that own prohibited directories.

%prep

%build
cat > sisyphus_check-check-dirlist.posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_DBDIR/rpmbuild-files-req-list.db" <<EOSQL
attach database '$REPOCOP_TEST_DBDIR/rpm.db' as rpm;
.mode tabs
-- select distinct rpm_files.pkgid, FILEREQDIR, FILEREQNAME from rpm_files LEFT JOIN rpm ON rpm_files.pkgid = rpm.pkgid, RPMBUILDFILESREQLIST where filename=FILEREQDIR and FILEREQNAME <> NAME;
CREATE TEMPORARY TABLE DIR_INTERSECTION (pkgid TEXT, REQDIR TEXT, REQNAME TEXT);
INSERT INTO DIR_INTERSECTION select distinct rpm_files.pkgid, FILEREQDIR, FILEREQNAME from rpm_files, RPMBUILDFILESREQLIST where filename=FILEREQDIR;
CREATE INDEX IF NOT EXISTS dir_intersection_IDX_NAME ON dir_intersection(pkgid);
.output $REPOCOP_TEST_TMPDIR/msg
select distinct DIR_INTERSECTION.pkgid, REQDIR, REQNAME from DIR_INTERSECTION LEFT JOIN rpm ON DIR_INTERSECTION.pkgid = rpm.pkgid where REQNAME <> NAME;
DROP TABLE DIR_INTERSECTION;
EOSQL
perl -ne 'chomp;@a=split /\t/;system(qq{repocop-test-warn -k $a[0] "sisyphus_check --check-dirlist failed: package contains a directory $a[1] that exclusively belongs to package $a[2]"})' $REPOCOP_TEST_TMPDIR/msg
rm $REPOCOP_TEST_TMPDIR/*
EOF


%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 %testname.posttest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/posttest

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Wed Oct 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- added temporary table to speed up test

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- posttests migration

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.0.8.3-alt1
- added url

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
