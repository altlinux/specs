%define collectorname specfile

Name: repocop-collector-%collectorname
Version: 0.04
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop specfile collector.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.15

Source: %name-%version.tar

%description
Repocop specfile collector.

%prep
%setup -q

%build
cat > %collectorname.test <<'EOF'
#!/bin/sh
`dirname $0`/changelog_filter "$REPOCOP_PKG_SPECFILE" > "$REPOCOP_TEST_STATEDIR/$REPOCOP_PKG_KEY.spec"
EOF

cat > %collectorname.purge <<'EOF'
#!/bin/sh
case $1 in
--given) 
	while read key;do rm -f "$REPOCOP_TEST_STATEDIR/$key.spec"; done 
	;;
--except) 
	mkdir "$REPOCOP_TEST_STATEDIR/except";
	while read key; do
	      [ -e "$REPOCOP_TEST_STATEDIR/$key.spec" ] && \
	      mv -f "$REPOCOP_TEST_STATEDIR/$key.spec" "$REPOCOP_TEST_STATEDIR/except/"; 
	done 
	pushd "$REPOCOP_TEST_STATEDIR/" >/dev/null
	      #	rm -f *.spec # for extra long filelist
	      ls | grep '.spec' | xargs rm -f
	popd >/dev/null
	pushd "$REPOCOP_TEST_STATEDIR/except/" >/dev/null
	      #	mv -f *.spec .. # for extra long filelist
	      ls | grep '.spec' | xargs -I '{}' mv -f '{}' ..
	popd >/dev/null
	rm -rf "$REPOCOP_TEST_STATEDIR/except/"
	;;
*) 
	echo "error: incorrect option"; exit 9
   	;;
esac
EOF

%install

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/srccollectors/%collectorname/
%__install -m 755 %collectorname.test $RPM_BUILD_ROOT%_datadir/repocop/srccollectors/%collectorname/test
%__install -m 755 %collectorname.purge $RPM_BUILD_ROOT%_datadir/repocop/srccollectors/%collectorname/purge
%__install -m 755 changelog_filter $RPM_BUILD_ROOT%_datadir/repocop/srccollectors/%collectorname/changelog_filter

%files
#doc README ChangeLog
%_datadir/repocop/srccollectors/%collectorname

%changelog
* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- use interface of repocop >= 0.15

* Fri Feb 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- fixes in purge script

* Fri Feb 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- changelogs are no more collected; just spec bodies.

* Mon Feb 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
