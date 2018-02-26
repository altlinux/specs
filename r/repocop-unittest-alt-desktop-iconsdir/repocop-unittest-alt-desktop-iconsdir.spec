%define testname iconsdir

Name: repocop-unittest-alt-desktop-%testname
Version: 0.12
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: ALT desktop integration tests for repocop test platform.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
 
Requires: repocop >= 0.40

%description
Repocop integration tests for ALT Linux specific Icons Packaging Policy.
see http://www.altlinux.org/IconPaths.

%prep

%build
cat > test <<'EOF'
#!/bin/sh
files_exist()
{
    [ -e "$1" ]
}
if ! files_exist $REPOCOP_PKG_ROOT%_menudir/*  && \
   ! files_exist $REPOCOP_PKG_ROOT%_desktopdir/* ; then
    exec repocop-test-skip
fi
if files_exist $REPOCOP_PKG_ROOT%_liconsdir/* ; then
    exec repocop-test-ok
fi
if files_exist $REPOCOP_PKG_ROOT%_datadir/pixmaps/*; then
    exec repocop-test-experimental "Please, move pixmaps from /usr/share/pixmaps to %%_liconsdir, %%_niconsdir, %%_miconsdir according to their size. See http://www.altlinux.org/IconPathsPolicy."
fi
exec repocop-test-skip
EOF

cat > filepattern <<'EOF'
^/usr/share/pixmaps/
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 755 test $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
install -m 644 filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added filepattern

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- reduced complains. Intermediate test until pixmap collector will be written.

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- dropped info in case of sole _liconsdir

* Sun Jan 18 2009 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- reduced level to info.

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- refer to altlinux.org

* Fri Mar 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- pkgtests/iconsdir split off to avoid frequent cache rebuilds.
- fixed warning in iconsdir: should require %%_liconsdir, not %%_niconsdir

* Tue Mar 11 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added update_wms test

* Mon Mar 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- fixed bug in update_menus test

* Mon Mar 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added ShowOnlyIn check

* Thu Feb 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated messages

* Mon Feb 25 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- First build for Sisyphus.
