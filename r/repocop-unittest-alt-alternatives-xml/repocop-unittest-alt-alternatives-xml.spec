%define testname alt-alternatives-xml

Name: repocop-unittest-%testname
Version: 0.07
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop test for alternatives in old xml format.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop >= 0.59
Requires: repocop-collector-altlinux-alternatives > 0.01
Requires: sqlite3


%description
Repocop integration test for alternatives in old xml format.
ALT Linux specific.

%prep

%build
cat > %testname.distrotest <<'EOF'
#!/bin/sh
#--select rpm_files.pkgid, group_concat(FILENAME), group_concat(altlinux_alternatives.pkgid) from altlinux_alternatives, rpm_files WHERE ALTALTERNATIVE=FILENAME GROUP BY rpm_files.pkgid;
sqlite3 "$REPOCOP_DISTROTEST_DBDIR/altlinux-alternatives.db" <<EOSQL
.mode tabs
.output $REPOCOP_TEST_TMPDIR/msg
select distinct pkgid from altlinux_alternatives where altisxml>0;
EOSQL
perl -ne 'chomp;system("repocop-test-fail -k $_ xml format of alternatives is obsolete. Its support will be removed soon")' $REPOCOP_TEST_TMPDIR/msg
rm $REPOCOP_TEST_TMPDIR/*
EOF

%install

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 %testname.distrotest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/distrotest

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Mon Jul 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- moved to distrotests

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- posttests migration

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- added url

* Sun Nov 23 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- bugfix

* Fri Nov 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- severity is risen to 'fail' due to devel@ deprecation announcement

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new collector 

* Thu Mar 27 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- test cleanup

* Tue Mar 25 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
