Name: stardict
Version: 3.0.3
Release: alt1

Summary: StarDict dictionary
License: GPLv3+
Group: System/Internationalization
Url: http://www.stardict.org

# http://stardict-3.googlecode.com/files/%name-%version.tar.bz2
Source: %name-%version.tar
Source3: docklet_normal.png
Source4: docklet_scan.png
Source5: docklet_stop.png
Source6: slovnyktodict.awk
Source7: mueller2stardict.sh

Patch1: stardict-3.0.3-rh-gcc46.patch
Patch2: stardict-3.0.3-rh-glib2.patch
Patch3: stardict-3.0.3-alt-dsl2dict.patch
Patch4: stardict-3.0.3-alt-linkage.patch
Patch5: stardict-3.0.3-alt-desktop.patch
Patch6: stardict-3.0.3-alt-tabfile.patch

Provides: %name-common = %version
Obsoletes: %name-common < %version
Provides: %name-gtk = %version
Obsoletes: %name-gtk < %version
Provides: %name-gnome = %version
Obsoletes: %name-gnome < %version

# Automatically added by buildreq on Mon May 28 2012
# optimized out: docbook-dtds fontconfig fontconfig-devel glib2-devel gnome-doc-utils-xslt libICE-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgtk+2-devel libpango-devel libstdc++-devel libwayland-client libwayland-server perl-Encode perl-XML-Parser pkg-config python-base python-module-libxml2 python-modules python-modules-encodings xml-common xml-utils xorg-xproto-devel xsltproc zlib-devel
BuildRequires: gcc-c++ gnome-doc-utils hardlink imake intltool libSM-devel libenchant-devel libespeak-devel libgucharmap7-devel libmysqlclient-devel libsigc++2-devel libxml2-devel xorg-cf-files

%description
StarDict is a Cross-Platform and international dictionary written in
Gtk2.  It has powerful features such as glob-style pattern matching,
scan selection, and fuzzy matching.

%package tools
Summary: Tools for making dictionary files for stardict
Group: Development/Other

%description tools
This package contains various tools for converting dictionaries in
stardict format.

%package plugin-espeak
Summary: Espeak plugin
Group: System/Internationalization
Requires: %name = %version-%release

%description plugin-espeak
This package contains espeak plugin for stardict.

%package plugin-gucharmap
Summary: Gucharmap plugin
Group: System/Internationalization
Requires: %name = %version-%release

%description plugin-gucharmap
This package contains gucharmap plugin for stardict.

%package plugin-spell
Summary: Spell plugin
Group: System/Internationalization
Requires: %name = %version-%release

%description plugin-spell
This package contains spell plugin for stardict.

%package plugin-dictdotcn
Summary: dictdotcn plugin
Group: System/Internationalization
Requires: %name = %version-%release

%description plugin-dictdotcn
This package contains dictdotcn netdict plugin for stardict,
querying dict.cn via network.
Warning: this package is insecure. Use at your own risk.

%prep
%setup
# remove bundled sigc++ header files
rm -r dict/src/sigc++*
sed -i '/src\/sigc++/d' dict/configure.ac
sed -i 's/ sigc++ sigc++config//' dict/src/Makefile.am
# remove bundled libtool files
rm */m4/{lt*,libtool}.m4 dict/m4/{gnome-doc-utils,intltool}.m4
# remove use of gconf macros
sed -i '/AM_GCONF_SOURCE_2/d' dict/configure.ac

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
install -pm644 %_sourcedir/docklet_*.png dict/src/pixmaps/

%build
%autoreconf
%configure \
 --disable-gnome-support \
 --enable-spell \
 --enable-gucharmap \
 --enable-espeak \
 --disable-festival \
 --disable-man \
 --disable-updateinfo \
 --disable-advertisement \
 --disable-gpe-support \
 --disable-maemo-support \
 #
%make_build

%install
%makeinstall_std scrollkeeper_localstate_dir=%buildroot%_var/lib/scrollkeeper
find %buildroot%_libdir -name '*.la' -delete

cd tools/src
install -pm755 *2dic stardict-dict-update stardict-verify \
	       stardict-repair stardict2txt tabfile \
	%buildroot%_bindir/
install -pm755 mova %buildroot%_bindir/mova2dic
cd - >/dev/null

install -pm755 %_sourcedir/{slovnyktodict.awk,mueller2stardict.sh} \
	%buildroot%_bindir/

%find_lang --with-gnome %name

hardlink -cv %buildroot%_datadir

%set_verify_elf_method strict

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_pixmapsdir/*
%_desktopdir/%name.desktop
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/stardict_html_parsedata.*
%_libdir/%name/plugins/stardict_powerword_parsedata.*
%_libdir/%name/plugins/stardict_wiki_parsedata.*
%_libdir/%name/plugins/stardict_xdxf_parsedata.*
%_libdir/%name/plugins/stardict_qqwry.*
%_libdir/%name/plugins/stardict_wordnet.*
%_libdir/%name/plugins/stardict_wordnet_parsedata.*
%_man1dir/*
%doc dict/AUTHORS dict/ChangeLog
%doc dict/doc/{StarDictFileFormat,FAQ,HACKING,HowToCreateDictionary}

%files tools
%_bindir/*
%exclude %_bindir/%name
%doc tools/AUTHORS tools/ChangeLog tools/README tools/src/example.ifo

%files plugin-espeak
%_libdir/%name/plugins/stardict_espeak.*
%files plugin-gucharmap
%_libdir/%name/plugins/stardict_gucharmap.*
%files plugin-spell
%_libdir/%name/plugins/stardict_spell.*
%files plugin-dictdotcn
%_libdir/%name/plugins/stardict_dictdotcn.*

%changelog
* Mon May 28 2012 Dmitry V. Levin <ldv@altlinux.org> 3.0.3-alt1
- Updated to 3.0.3.
- Dropped stardict-gnome, merged stardict-common and stardict-gtk back
  to stardict.
- Merged stardict-tools, fixed mueller2stardict.sh.

* Tue Jul 05 2011 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-alt8
- Fixed build.

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.0.1-alt7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for stardict

* Mon Apr 18 2011 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-alt7
- Fixed interpackage dependencies.
- Updated build dependencies.

* Thu Apr 22 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 3.0.1-alt6
- Added intltool to BuildRequires

* Tue Oct 06 2009 Egor Vyscrebentsov <evyscr@altlinux.org> 3.0.1-alt5
- Use tango docklet images (thanks to Andrey Yurkovsky)

* Sat Aug 08 2009 Egor Vyscrebentsov <evyscr@altlinux.org> 3.0.1-alt4.1
- fixed .desktop entries (#19526)
- fixed empty stardict.cfg processing by stardict-gtk (closes #15855)

* Wed Aug 05 2009 Egor Vyscrebentsov <evyscr@altlinux.org> 3.0.1-alt4
- new packager
- add Packager: tag
- fixed build with gcc >= 4.3

* Fri Nov 14 2008 Alex Murygin <murygin@altlinux.ru> 3.0.1-alt3
- added stardict-3.0.1-alt-gucharmap.patch
- added 05_g++-4.3.dpatch (from debian)
- deactivated man plugin due to locale problem [17918]
- deactivated updateinfo and advertisement plugin

* Thu Aug 14 2008 Alex Murygin <murygin@altlinux.ru> 3.0.1-alt2
- disabled network dictionaries be default [16436]
- packed plugin-dictdotcn and plugin-update_info as separate package [16436]

* Mon Apr 21 2008 Alex Murygin <murygin@altlinux.ru> 3.0.1-alt1
- new vesrion [13847]
- added patch for menu macros
- removed advertisement plugin [13542]
- added libGConf-devel to buildreq (gconf2_install macros)
- added librarian to buildreq (scrollkeeper-preinstall)
- enabled espeak plugins
- added new plugins to common
   dictdotcn
   qqwry
   wordnet
   wordnet_parsedata
- removed patches
   stardict-3.0.0-alt-gtk.patch
   stardict-3.0.0-espeak.patch
   stardict-3.0.0-floatwin.patch

* Tue Nov 06 2007 Alex Murygin <murygin@altlinux.ru> 3.0.0-alt1
- new version
- added new translation
- spec cleaning
- fixed 12871 (wrong category for gtk version)
- fixed 12282 (menu file generation)
- added stardict-3.0.0-alt-gtk.patch
- added stardict-3.0.0-espeak.patch (from src.rpm of Hu Zheng)
- added stardict-3.0.0-floatwin.patch (from src.rpm of Hu Zheng)
- added new ru translation
- added plugins (new functionality)
  most of them are in common package
   advertisement
   html_parsedata
   man
   powerword_parsedata
   update_info
   wiki_parsedata
   xdxf_parsedata
  and some are in separate packages
   plugin-espeak (disabled by default due to libespeak-devel wrong packaging)
   plugin-gucharmap
   plugin-spell

* Thu Jul 13 2006 Alex Murygin <murygin@altlinux.ru> 2.4.8-alt1
- new version
- corrected name and exec for gtk version in menu [9755]
- tools package moved to separate package (upstream)
- new docs added

* Thu Jan 19 2006 Alex Murygin <murygin@altlinux.ru> 2.4.6-alt1
- new version
- added make clean between making gtk and gnome versions
- added following files into tools package and updated description
  stardict_verify - check installed dictionaries for errors
  hanzim2dict.py  - as an example for making stardict dictionaries with python help
- I didn't add the following tools because I didn't know if anybody asked for them
  21tech
  buddhist
  directory2treedic
  ec50
  jdictionary
  jm2stardict.py
  kdic
  olddic2newdic
  powerword
  soothill
  tabfile
  xmlinout

* Mon Aug 08 2005 Alex Murygin <murygin@altlinux.ru> 2.4.5-alt2
- added conflict to stardict < 2.4.5 for stardict-common

* Mon Aug 01 2005 Alex Murygin <murygin@altlinux.ru> 2.4.5-alt1
- new version
- added stardict-gtk package
- renamed main package to stardict-gnome
- moved common files to stardict-common package

* Sat Jun 18 2005 Alex Murygin <murygin@altlinux.ru> 2.4.4-alt1
- new version

* Thu Nov 11 2004 Alex Murygin <murygin@altlinux.ru> 2.4.3-alt4
- changed menu group to "Applications/Text tools"

* Thu Jul 29 2004 Alex Murygin <murygin@altlinux.ru> 2.4.3-alt3
- fixed menu
- changed summary (thanks Abel Cheung - Mandrake)
- added russian summary/description

* Thu Apr 29 2004 Alex Murygin <murygin@altlinux.ru> 2.4.3-alt2
- removed -DGTK_DISABLE_DEPRECATED

* Tue Mar 16 2004 Alex Murygin <murygin@altlinux.ru> 2.4.3-alt1
- new version
- added mova2dic to tools

* Thu Nov 20 2003 Alex Murygin <murygin@altlinux.ru> 2.4.2-alt1
- new version
- added stardict_dict_update to %name-tools
- deleted example.idxhead and added example.ifo

* Fri Aug 29 2003 Alex Murygin <murygin@altlinux.ru> 2.4.0-alt1
- new version
- regenerated buildreq

* Sun Jul 06 2003 Alex Murygin <murygin@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Jun 09 2003 Alex Murygin <murygin@altlinux.ru> 2.2.0-alt2
- new version without version incrementation

* Sun Jun 01 2003 Alex Murygin <murygin@altlinux.ru> 2.2.0-alt1
- new version

* Wed May 28 2003 Alex Murygin <murygin@altlinux.ru> 2.1.0-alt2
- fixed clean_scrollkeeper postun script

* Wed May 21 2003 Alex Murygin <murygin@altlinux.ru> 2.1.0-alt1
- new version
- added package startdict-tools

* Sun May 04 2003 Alex Murygin <murygin@altlinux.ru> 2.0.0-alt1
- Initial revision.
