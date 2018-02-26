%define testname bin-permissions

Name: repocop-unittest-%testname
Version: 0.04
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop test for non-executable files in /usr/bin.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop >= 0.19
Requires: repocop-collector-rpm
Requires: sqlite3

%description
Repocop intergration test for non-executable files in /usr/bin.

%prep

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_DBDIR/rpm.db" <<EOSQL
.mode tabs
.output $REPOCOP_TEST_TMPDIR/info
select pkgid,filename from rpm_files where FILEMODE & 73=0 and (filename like '/usr/bin/%%' OR filename like '/usr/sbin/%%' OR filename like '/bin/%%' OR filename like '/sbin/%%') and filename not like '%%-functions' and pkgid not glob 'libshell-*';
EOSQL
perl -ne 'chomp;@a=split /\t/;system("repocop-test-info -k $a[0] not executable file $a[1]")' $REPOCOP_TEST_TMPDIR/info
rm $REPOCOP_TEST_TMPDIR/*
EOF

%install

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 %testname.posttest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/posttest

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- posttests migration

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- added url

* Wed Dec 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added exception for libshell.

* Sun Apr 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added sbin check

* Sat Apr 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
