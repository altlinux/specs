%define testname buildreq-xorg

Name: repocop-unittest-buildreq
Version: 0.05
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname integration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop >= 0.19

%description
%testname integration test for repocop test platform.
The test checks BuildRequires: tags against a list of not
recommended requirements and issues appropriate warnings.

%prep

%build
cat > posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_TMPDIR/tmp.db" <<EOSQL
attach database '$REPOCOP_TEST_DBDIR/rpm.db' as rpm;
.mode tabs
.output $REPOCOP_TEST_TMPDIR/warn
 select pkgid, buildrequirename from rpm_buildrequires where buildrequirename='XFree86-devel' OR buildrequirename='XFree86-libs' OR buildrequirename='xorg-x11-devel' OR buildrequirename='xorg-x11-libs' OR buildrequirename='xorg-devel' OR buildrequirename='xorg-libs' OR buildrequirename='libmesa-devel';
EOSQL
cat > $REPOCOP_TEST_TMPDIR/repocop.pl <<'EOPERL'
my %%pkg; while (<>) {
   chomp;
   my ($id,$req)=split(/\t/);
   if ($pkg{$id}) {$pkg{$id}.=' '.$req} else {$pkg{$id}=$req};
}
while (my ($id, $reqstr)=each (%%pkg)) {
      system('repocop-test-warn', '-k',$id, "Please, refresh your BuildRequires: using buildreq. The following obsolete dependencies blow up the build: ".$reqstr);
}
EOPERL
cat $REPOCOP_TEST_TMPDIR/warn | perl $REPOCOP_TEST_TMPDIR/repocop.pl
rm $REPOCOP_TEST_TMPDIR/*
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/srctests/%testname/
%__install -m 755 posttest $RPM_BUILD_ROOT%_datadir/repocop/srctests/%testname/

%files
#doc README ChangeLog
%_datadir/repocop/srctests/%testname

%changelog
* Mon Aug 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated forbidden buildreq list

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- posttests migration

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- added url

* Tue May 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added check for xorg-x11-libs

* Fri Mar 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- test renamed to buildreq-xorg to avoid misunderstanding.

* Thu Mar 20 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
