%define testname alt-alternatives-vs-filesystem

Name: repocop-unittest-%testname
Version: 0.06
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop test for alternatives/filesystem intersections.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop >= 0.07
Requires: repocop-collector-altlinux-alternatives > 0.01
Requires: sqlite3


%description
Repocop intergration test for alternatives/filesystem intersections.
ALT Linux specific.

%prep

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
#--select rpm_files.pkgid, group_concat(FILENAME), group_concat(altlinux_alternatives.pkgid) from altlinux_alternatives, rpm_files WHERE ALTALTERNATIVE=FILENAME GROUP BY rpm_files.pkgid;
sqlite3 "$REPOCOP_TEST_DBDIR/altlinux-alternatives.db" <<EOSQL
attach database '$REPOCOP_TEST_DBDIR/rpm.db' as rpm;
.mode tabs
.output $REPOCOP_TEST_TMPDIR/warn
-- note: 580 is RPMFILE_DONOTUSE (1 << 2) + RPMFILE_GHOST (1 << 6) + RPMFILE_EXCLUDE (1 << 9)
select rpm_files.pkgid, FILENAME, altlinux_alternatives.pkgid from altlinux_alternatives LEFT JOIN rpm as c ON altlinux_alternatives.pkgid = c.pkgid, rpm_files LEFT JOIN rpm as d ON altlinux_alternatives.pkgid = d.pkgid WHERE ALTALTERNATIVE=FILENAME and FILEFLAG & 580 = 0 AND c.name <> d.NAME;
EOSQL
perl -ne 'chomp;@a=split /\t/;system("repocop-test-warn -k $a[0] file $a[1] is alternative in package: $a[2]")' $REPOCOP_TEST_TMPDIR/warn
rm $REPOCOP_TEST_TMPDIR/warn
EOF

%install

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 %testname.posttest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/posttest

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- posttests migration

* Sun Aug 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- fix for #21272

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- skipping ghosts (thanks to mithraen@)

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- added url

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new collector

* Thu Mar 27 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- test cleanup

* Tue Mar 25 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
