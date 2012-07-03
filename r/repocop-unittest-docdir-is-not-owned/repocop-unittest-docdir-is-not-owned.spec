%define testname docdir-is-not-owned

Name: repocop-unittest-%testname
Version: 0.07
Release: alt1
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: repocop > 0.55
Url: http://repocop.altlinux.org

Summary: %testname integration tests for repocop test platform.
Group: Development/Other
License: GPLv2+

%description
The test warns packages that place files into 
/usr/share/doc/%%name-%%version directory but do not own it.

%prep

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_DBDIR/rpm.db" <<EOSQL
.mode tabs
.output $REPOCOP_TEST_TMPDIR/msg
select distinct a.pkgid from rpm_files as a left join rpm as b on a.pkgid=b.pkgid where a.filename glob '/usr/share/doc/'||b.name||'-'||b.version||'/*' and a.pkgid not in (select c.pkgid from rpm_files as c left join rpm as d on c.pkgid=d.pkgid where c.filename glob '/usr/share/doc/'||d.name||'-'||d.version);
EOSQL
for i in `cat $REPOCOP_TEST_TMPDIR/msg`; do repocop-test-warn -k $i "package places files into /usr/share/doc/%%name-%%version directory but does not own it."; done
rm $REPOCOP_TEST_TMPDIR/*
EOF

cat > %testname.pl <<'EOF'
#!/usr/bin/perl -w
push @SPECHOOKS, sub {
    my ($spec, undef, $pkgname) = @_;
    my $section=$spec->get_section("files","-n $pkgname");
    unless ($section) {
	print STDERR "Oops! %%files -n $pkgname not found!\n";
	return;
    }
    $section->push_body(q"# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%%dir %%_docdir/".$pkgname.q"-%%version 
");
## %%doc is not required (%%_docdir/).
##%%doc %%dir 
};
1;
EOF

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

mkdir -p %buildroot%_datadir/repocop/fixscripts/
install -p -m 755 *.pl %buildroot%_datadir/repocop/fixscripts/

%files
%_datadir/repocop/pkgtests/%testname/
%_datadir/repocop/fixscripts/*.pl

%changelog
* Wed Nov 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- adapted for new fixscript syntax

* Fri Dec 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- added url.

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- posttests migration

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- fixscript: removed explicit %%doc (no need for that - @ldv)

* Wed Dec 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- fixscript: just %%doc %%dir is enough.

* Tue Dec 09 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added fixscript

* Mon Dec 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixed test

* Sun Dec 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial version
