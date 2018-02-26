%define __find		/bin/find
%define __xargs		/bin/xargs

Name: pgadmin3
Version: 1.14.2
Release: alt1

Summary: Powerful administration and development platform for PostgreSQL.
License: BSD
Group: Databases
Packager: PostgreSQL Maintainers Team <pgsql@packages.altlinux.org>

Url: http://www.pgadmin.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: %name-docs-en_US

BuildRequires: gcc-c++ libssl-devel libxslt-devel postgresql-devel
BuildRequires: libwxGTK-contrib-ogl-devel libwxGTK-contrib-stc-devel libwxGTK-devel
BuildRequires: findutils ImageMagick-tools

%description
pgAdmin III is a powerful administration and development platform for
the PostgreSQL database, free for any use.
The application runs under GNU/Linux, FreeBSD and Windows 2000/XP.
pgAdmin III is designed to answer the needs of all users, from writing
simple SQL queries to developing complex databases.
The graphical nterface supports all PostgreSQL features and makes
administration easy. The application also includes a query builder,
an SQL editor, a server-side code editor and much more.

%package docs-en_US
Summary: US english docs for %name
Group: Databases
BuildArch: noarch

%description docs-en_US
US english docs for %name.

%package docs-all
Summary: All docs for %name
Group: Databases
BuildArch: noarch

%description docs-all
All docs for %name.

%prep
%setup -q

%build
/bin/sh bootstrap
%configure CPPFLAGS="-I./include"

%make_build

%install
%make_install DESTDIR=%buildroot install

rm -rf %buildroot%_datadir/%name/docs/*
# make symlink for en_US docs.
ln -s %_defaultdocdir/%name-docs-en_US-%version/en_US %buildroot%_datadir/%name/docs/
#make symlink for all docs.
ln -s %_defaultdocdir/%name-docs-all-%version/de_DE %buildroot%_datadir/%name/docs/
ln -s %_defaultdocdir/%name-docs-all-%version/es_ES %buildroot%_datadir/%name/docs/
ln -s %_defaultdocdir/%name-docs-all-%version/fr_FR %buildroot%_datadir/%name/docs/
ln -s %_defaultdocdir/%name-docs-all-%version/sl_SI %buildroot%_datadir/%name/docs/

mkdir -p %buildroot%_datadir/applications
cat >| %buildroot%_datadir/applications/%name.desktop << 'EOF'
[Desktop Entry]
Name=pgadmin3
Name[en_CA]=%name
Name[en_GB]=%name
Name[ru]=%name
Comment=administration and development platform for the PostgreSQL.
Comment[en_CA]=administration and development platform for the PostgreSQL.
Comment[en_GB]=administration and development platform for the PostgreSQL.
Comment[ru]=Администрирование и разработка для PostgreSQL.
Exec=%name
Terminal=false
Type=Application
Icon=%name
Categories=Development;Database;
StartupNotify=true
EOF

mkdir -p %buildroot{%_iconsdir,%_miconsdir,%_liconsdir}
cp -f pgadmin/include/images/pgAdmin3-16.png %buildroot%_miconsdir/%name.png
cp -f pgadmin/include/images/pgAdmin3-32.png %buildroot%_iconsdir/%name.png
cp -f pgadmin/include/images/pgAdmin3.png %buildroot%_liconsdir/%name.png

# Move locales to their correct place
mkdir -p %buildroot%_datadir/locale
mv -f %buildroot%_datadir/%name/i18n/??_?? %buildroot%_datadir/locale

%find_lang %name

%files -f %name.lang
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%exclude %_datadir/%name/docs

%files docs-en_US
%doc docs/en_US
%doc %_datadir/%name/docs/en_US

%files docs-all
%doc docs/de_DE
%doc docs/es_ES
%doc docs/fr_FR
%doc docs/sl_SI
%doc %_datadir/%name/docs/de_DE
%doc %_datadir/%name/docs/es_ES
%doc %_datadir/%name/docs/fr_FR
%doc %_datadir/%name/docs/sl_SI

%changelog
* Thu Apr 19 2012 Alexey Shabalin <shaba@altlinux.ru> 1.14.2-alt1
- git REL-1_14_0_PATCHES branch (cfe0a7ffd13fd7c30c28341a66a16c8d9fc3530c)

* Tue Sep 20 2011 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- git REL-1_14_0_PATCHES branch (c99d4e68fc315d6fe548ca218e5595863a32f200)

* Tue Aug 30 2011 Alexey Shabalin <shaba@altlinux.ru> 1.12.3-alt1
- git REL-1_12_0_PATCHES branch (1c6d2908ef9b6a91413916d0c5b611b89cf27f12)

* Fri Dec 10 2010 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt2
- package docs as noarch

* Thu Dec 09 2010 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt1
- git REL-1_12_0_PATCHES branch (0e888bd9bf070446e46bb1af7ec275285fe31151) (ALT #24717)

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.10.0.rev8070-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for pgadmin3
  * postclean-05-filetriggers for spec file

* Thu Oct 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.10.0.rev8070-alt1
- 8070 revision from REL-1_10_0_PATCHES branch.

* Thu Oct 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.10.0.rev8034-alt2
- Fix license tag (closes: #21624).
- Some cosmetic changes to spec file.

* Tue Sep 15 2009 Konstantin Pavlov <thresh@altlinux.org> 1.10.0.rev8034-alt1
- 8034 revision from REL-1_10_0_PATCHES branch.

* Mon Mar 23 2009 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.10.0.rev7737-alt1
-  1.10 beta.

* Wed Dec 10 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.0.rev7510-alt1
-  GQB improvements;
-  lots of bugfixes;
-  remove pgagent.

* Wed Aug 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.0.rev7404-alt1
-  graphical query builder (GQB) out of thr box.

* Tue May 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.0.rev7304-alt1
-  postgresql > 8.3 support.

* Tue Mar 18 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.0.rev7174-alt1
-  new snapshot:
	+ allow users to dump databases/tables with quotes/backslashes in their name.

* Wed Jan 09 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.8.1.rev6988-alt1
-  1.8.1;
-  fix build on new sisyphus.

* Thu Oct 04 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.8.0.rev6709-alt1
-  1.8.0 beta 5.5;
-  build with wxGTK 2.8.6.

* Tue Jul 31 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.8.0.rev6516-alt1
-  1.8.0 snapshot;
-  build with wxGTK 2.8.4.

* Wed Apr 25 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.7.0.rev6234-alt1
-  PlPgSQL debugger on-the-box.

* Mon Apr 16 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.7.0.rev6195-alt1
-  1.7.0.rev6195;
-  build with wxGTK 2.8.3.

* Tue Jan 30 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.7.0.rev5892-alt1
-  build with new cvs wxGTK version.

* Wed Jan 17 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.7.0.rev5872-alt1
-  1.7.0.rev5872.

* Tue Dec 19 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.7.0.rev5792-alt1.1
-  refresh build requirements.
-  move pgagent into several package

* Thu Dec 14 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.7.0.rev5792-alt1
-  1.7.0 developer snapshot.
-  build with wxGTK 2.8.

* Wed Oct 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.6.0.rev5527-alt1
-  1.6.0.rev5527.
-  fix for #10182.

* Mon Sep 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.6.0.rev5399-alt1
-  1.6.0.
-  name format changed.

* Tue Sep 05 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060905-alt1
-  bugfixes.

* Thu Aug 31 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060831-alt1
-  build with wxGTK 2.7.0 testing.

* Wed Aug 09 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060809-alt1
-  1.5.0.svn20060809.

* Tue Jun 06 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060606-alt1
-  svn20060606. fix crash.

* Tue May 30 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060530-alt1
-  svn20060530;
-  separate docs and main package;
-  fix russian comments in .desktop file.

* Fri Mar 31 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060331-alt1
-  svn20060331. fixes in query tool (upstream).

* Mon Mar 06 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060306-alt1
-  svn20060306.

* Thu Feb 02 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060202-alt1
-  1.5.0.svn20060202. autocompletion for table names, functions e.t.c. (upstream).

* Tue Jan 17 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20060117-alt1
-  menu fixes.

* Tue Dec 13 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20051213-alt1
-  fixes for slony1 (upstream).

* Wed Dec 07 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5.0.svn20051207-alt1
-  1.5.0 snapshot.

* Wed Nov 09 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.4.0.svn20051109-alt1
-  1.4.0.svn20051109. post 1.4.0 release.

* Fri Oct 28 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.4.0.svn20051028-alt1
-  1.4.0 svn.

* Thu Sep 29 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.svn20050929-alt1
-  1.3.0.svn20050929. bugfixes in system schemas handling.

* Tue Sep 20 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.svn20050920-alt1
-  bugfixes.

* Thu Aug 04 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.svn20050804-alt1
-  1.3.0.svn20050804.

* Fri Jun 24 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.svn20050624-alt1
-  1.3.0.svn20050624.

* Fri Jun 10 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.svn20050610-alt1
-  1.3.0.svn20050610.

* Wed Jun 01 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.cvs20050601-alt1
-  bugfixes.
-  libpq-devel.

* Wed May 25 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.cvs20050525-alt1
-  lots of bugfixes.

* Tue May 24 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.cvs20050524-alt1
-  bugfixes in pgagent code.

* Fri May 20 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0.cvs20050520-alt1
-  build with new wxGTK2u.
-  pgagent.

* Tue May 17 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0-alt1.cvs20050517
-  1.3.0-alt1.cvs20050517. pgagent.

* Sat May 14 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0-alt1.cvs20050514
-  1.3.0-alt1.cvs20050514.

* Mon Apr 18 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0-alt1.cvs20050418
-  cvs20050418. build with wxGTK 2.5.5.

* Wed Apr 06 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0-alt1.cvs20050406
-  cvs20050406.

* Tue Mar 29 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.3.0-alt1.cvs20050328
-  1.3.0rc
-  desktop file added.
-  rebuild with new wxGTK.

* Mon Mar 14 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.1-alt1.cvs20050314
-  1.2.1 cvs snapshot.
-  spec changes.

* Tue Nov 30 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0-alt1
-  1.2.0 release.

* Mon Nov 22 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0-alt0.2.cvs20041122
-  cvs20041122. rc2.

* Wed Nov 10 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0-alt0.2.cvs20041105
-  ivalid build requires fixed.

* Fri Nov 05 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0-alt0.1.cvs20041105
-  cvs20041105. rc1.

* Tue Nov 02 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0-alt0.1.cvs20041102
-  cvs20041102. pre RC.

* Wed Oct 20 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0-alt0.1.cvs20041020
-  new cvs snapshot (beta3).
-  rebuild with wxGTK 2.5.3.

* Mon Oct 04 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0beta2-alt1.cvs20041004
-  beta2.

* Tue Sep 21 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0beta1-alt1.cvs20040921
-  new cvs snapshot.
-  rebuild with new wxGTK2.

* Fri Sep 17 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0beta1-alt1.cvs20040917
-  fixed bug with type quoting.
-  spec changes.

* Wed Sep 08 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.2.0beta1-alt1.cvs20040908
-  build with new wxWidgets pgAdmin snapshot;
-  lots of bugfixes.

* Mon Sep 06 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.cvs20040906
-  cvs20040906.

* Wed Aug 18 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.cvs20040818
-  cvs20040818.

* Mon Aug 16 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.16.08.2004cvs
-  combobox and resource fixes (upstream).

* Fri Aug 13 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.13.08.2004cvs
-  13.08.2004cvs.
-  pre-beta release. feature freeze.

* Wed Aug 11 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.11.08.2004cvs
-  11.08.2004cvs.

* Mon Aug 02 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.02.08.2004cvs
-  02.08.2004 cvs snapshot.

* Mon Jul 26 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.26.07.2004cvs
-  26.07.2004 cvs.

* Fri Jul 23 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.23.07.2004cvs
-  23.07.2004 cvs snapshot. fixes in gtk dialogs.

* Thu Jul 22 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.22.07.2004cvs
-  22.07.2004 cvs snapshot.

* Wed Jul 21 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1.0-alt1.21.07.2004cvs
- 21.07.2004 cvs snapshot.
