%define testname rpm-ext

Name: repocop-collector-%testname
Version: 0.06
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop postcollector for extended rpm database.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop > 0.40
Requires: sqlite3


%description
Repocop postcollector creates rpm-ext database
with the following tables:
* explicit package conflicts table.

%prep

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
#--select rpm_files.pkgid, group_concat(FILENAME), group_concat(altlinux_alternatives.pkgid) from altlinux_alternatives, rpm_files WHERE ALTALTERNATIVE=FILENAME GROUP BY rpm_files.pkgid;
rm -f "$REPOCOP_TEST_DBDIR/rpm-ext.db"
repocop-sqlite "$REPOCOP_TEST_DBDIR/rpm-ext.db" <<EOSQL
attach database '$REPOCOP_TEST_DBDIR/rpm.db' as rpm;
CREATE TABLE EXPLICIT_CONFLICT (CONFLICTER TEXT, CONFLICTEE TEXT);
-- note: asymmetric;
insert INTO EXPLICIT_CONFLICT select distinct a.pkgid, b.pkgid FROM rpm_conflicts as a, rpm_provides as b WHERE a.pkgid<>b.pkgid AND b.providename = a.conflictname;
CREATE INDEX EXPLICIT_CONFLICT_IDX_NAME ON EXPLICIT_CONFLICT(CONFLICTER);
-- 
CREATE TABLE EXPLICIT_OBSOLETE (OBSOLETER TEXT, OBSOLETEE TEXT);
-- note: asymmetric; 
-- TODO: index left join is possible if RPM will have an index on NAME
-- simple version: 
-- insert INTO EXPLICIT_OBSOLETE select distinct a.pkgid, b.pkgid FROM rpm_obsoletes as a, rpm as b WHERE a.pkgid<>b.pkgid AND b.name = a.obsoletename AND (obsoleteversion IS NULL OR obsoleteversion;
INSERT INTO EXPLICIT_OBSOLETE select distinct a.pkgid, b.pkgid FROM rpm_obsoletes as a, rpm as b WHERE a.pkgid<>b.pkgid AND b.name = a.obsoletename AND (obsoleteversion='' OR obsoleteversion IS NULL OR rpm_compare_op_evr_e_v_r(obsoleteFLAG,obsoleteversion,epoch,version,release)>0);
CREATE INDEX EXPLICIT_OBSOLETE_IDX_NAME ON EXPLICIT_OBSOLETE(OBSOLETER);
EOSQL
#rm "$REPOCOP_TEST_TMPDIR/"*
EOF

%install
install -D -m 755 %testname.posttest $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%testname/posttest

%files
#doc README ChangeLog
%_datadir/repocop/pkgcollectors/%testname

%changelog
* Thu Feb 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- spec cleanup

* Tue Nov 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3
- fixed Url:

* Wed Oct 28 2009 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- added Url:

* Tue Oct 27 2009 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added version check to obsoletes table

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- posttests migration

* Thu Jan 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- SQL bugfixes

* Thu Jan 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added EXPLICIT_OBSOLETE table

* Tue Dec 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
