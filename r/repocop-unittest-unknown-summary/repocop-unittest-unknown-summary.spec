%define testname unknown-summary

Name: repocop-unittest-%testname
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop test for non-informative summary.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.73
Requires: repocop-collector-description
Requires: sqlite3

%description
Repocop integration test for non-informative summary.

%prep

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_DBDIR/description.db" <<EOSQL
.mode tabs
.output $REPOCOP_TEST_TMPDIR/msg
select pkgid,summary from SRCRPM_SUMMARY_DESCRIPTION where summary='unknown';
EOSQL
perl -ne 'chomp;@a=split /\t/;system("repocop-test-fail -k $a[0]: bad summary: $a[1]")' $REPOCOP_TEST_TMPDIR/msg
rm $REPOCOP_TEST_TMPDIR/*
EOF

%install

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/srctests/%testname/
%__install -m 755 %testname.posttest $RPM_BUILD_ROOT%_datadir/repocop/srctests/%testname/posttest

%files
#doc README ChangeLog
%_datadir/repocop/srctests/%testname

%changelog
* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
