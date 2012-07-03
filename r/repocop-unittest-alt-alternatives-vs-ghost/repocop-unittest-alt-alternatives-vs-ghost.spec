%define testname alt-alternatives-vs-ghost

Name: repocop-unittest-%testname
Version: 0.02
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop test for alternatives/ghosts intersections.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop >= 0.07
Requires: repocop-collector-altlinux-alternatives > 0.01
Requires: sqlite3


%description
Repocop intergration test for alternatives/filesystem ghost intersections.
ALT Linux specific.

%prep

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
#--select rpm_files.pkgid, group_concat(FILENAME), group_concat(altlinux_alternatives.pkgid) from altlinux_alternatives, rpm_files WHERE ALTALTERNATIVE=FILENAME GROUP BY rpm_files.pkgid;
sqlite3 "$REPOCOP_TEST_DBDIR/altlinux-alternatives.db" <<EOSQL
attach database '$REPOCOP_TEST_DBDIR/rpm.db' as rpm;
.mode tabs
.output $REPOCOP_TEST_TMPDIR/msg
-- note: 64 is RPMFILE_GHOST (1 << 6)
select rpm_files.pkgid, FILENAME, altlinux_alternatives.pkgid from altlinux_alternatives, rpm_files WHERE ALTALTERNATIVE=FILENAME and FILEFLAG & 64 > 0;
EOSQL
perl -ne 'chomp;@a=split /\t/;system("repocop-test-info -k $a[0] Since alternatives 0.4 the practice to own alternative symlinks as ghost files is deprecated. the ghost file $a[1] is an alternative in package $a[2]. Consider removing the ghost file $a[1].")' $REPOCOP_TEST_TMPDIR/msg
rm $REPOCOP_TEST_TMPDIR/*
EOF

%install

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 %testname.posttest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/posttest

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- posttests migration

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
