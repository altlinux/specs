%def_disable debug

# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: fluxbox
Version: 1.3.1
Release: alt2.1

Summary: Fast and lightweight window manager
Summary(ru_RU.UTF-8): Легкий и быстрый оконный менеджер

License: MIT
Group: Graphical desktop/Other
Url: http://fluxbox.org
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: http://dl.sourceforge.net/fluxbox/fluxbox-%version.tar.bz2
Source1: fluxbox.menu
Source2: fluxbox.menu-methods
Source3: fluxbox.wmsession
Source4: fluxbox-icons.tar.bz2
Source5: README.ALT-ru_RU.UTF-8
Source6: Cthulhain
Source7: fluxbox.vim

Patch0: fluxbox-alt-makefile-no_generate_menu.patch
Patch1: fluxbox-alt-style-disable_fonts.patch
Patch2: fluxbox-alt-scripts-find_requires_protect.patch
Patch3: fluxbox-alt-configure-use_pkgconfig.patch
Patch4: fluxbox-alt-doc-drop_outdated_url.patch
Patch5: fluxbox-alt-gcc4.6.patch

# Explanation:
# - xmessages uses by fbsetbg plus can be invoked from menu
# - xprop used in menu item "Window name"
# - xinitrc is owner of /etc/X11/wmsession.d directory
# - menu: support for locate_icon() function
Requires: xmessage xprop xinitrc
Requires: menu >= 2.1.35-alt3

BuildRequires(pre): rpm-build-vim

BuildRequires: gcc-c++ imlib2-devel libXt-devel libXft-devel
BuildRequires: libXrandr-devel libXpm-devel libXinerama-devel libXext-devel

%description
Fluxbox designed for those peoples that unlike huge and feature-overloaded
window manages. It has a lot of good features and one of them it's high speed.
It's very simply for configurate and it compiled with support to KDE and GNOME
applets.

%description -l ru_RU.UTF-8
Fluxbox предназначен для тех, кто не любит навороченные и неповоротливые
оконные менеджеры. Он обладает множеством различных достоинств, главным из
которых является его скорость. Он прост в настройке и скомпилирован с
поддержкой аплетов из KDE и Gnome.

%package -n vim-plugin-fluxbox-syntax
Summary: VIm syntax for fluxbox files
Summary(ru_RU.UTF-8): Подсветка синтаксиса в VIm для fluxbox
Group: Editors
BuildArch: noarch

%description -n vim-plugin-fluxbox-syntax
VIm syntax for fluxbox apps, keys and menu files.

%description -l ru_RU.UTF-8 -n vim-plugin-fluxbox-syntax
Подсветка синтаксиса для конфигурационных файлов fluxbox: app, keys и menu.

%prep
%setup -a4

%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2

# Using mouse wheel for changes Tabs
sed -i '22a\
session.screen0.windowScrollAction:\tNextTab
' data/init.in

%build
# Regenerate:
# - configure after applying use_pkgconfig patch
# - Makefiles after applying no_generate_menu patch
%autoreconf

%configure --with-init=%_sysconfdir/X11/%name/init \
			--with-keys=%_sysconfdir/X11/%name/keys \
			--with-menu=%_sysconfdir/X11/%name/menu \
			--enable-nls \
			--enable-shape \
			%{?_enable_debug:--enable-debug}

%make_build %{?!_enable_debug: --no-print-directory --silent}

bzip2 ChangeLog

%install
%makeinstall_std %{?!_enable_debug: --no-print-directory --silent}

install -m644 -D 3rd/vim/syntax/fluxapps.vim %buildroot%vim_syntax_dir/fluxapps.vim
install -m644 -D 3rd/vim/syntax/fluxkeys.vim %buildroot%vim_syntax_dir/fluxkeys.vim
install -m644 -D 3rd/vim/syntax/fluxmenu.vim %buildroot%vim_syntax_dir/fluxmenu.vim
install -m644 -D %SOURCE7 %buildroot%vim_ftdetect_dir/fluxbox.vim

%find_lang --custom-dir-script="
s:%buildroot::
s:\(.*/share/fluxbox/nls/\)\(C\|[a-z][^/_@]\+\):%%lang(\2) \1\2:
s:^\([^%%].*\)::
s:%%lang(C) ::" %name

install -pD -m 644 %name-48.xpm %buildroot%_liconsdir/%name.xpm
install -pD -m 644 %name-32.xpm %buildroot%_niconsdir/%name.xpm
install -pD -m 644 %name-16.xpm %buildroot%_miconsdir/%name.xpm

install -pD -m 644 %SOURCE1 %buildroot%_menudir/%name
install -pD -m 755 %SOURCE2 %buildroot%_sysconfdir/menu-methods/%name
install -pD -m 644 %SOURCE3 %buildroot%_sysconfdir/X11/wmsession.d/07%name
install -pD -m 644 %SOURCE5 .
install -pD -m 644 %SOURCE6 %buildroot%_datadir/%name/styles/Cthulhain

%files -f %name.lang
%doc AUTHORS ChangeLog.bz2 COPYING NEWS README* TODO
%_bindir/*
%_man1dir/*
%_man5dir/fluxbox-*.5.*
%_liconsdir/%name.xpm
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%_menudir/%name
%_sysconfdir/menu-methods/%name
%config %_sysconfdir/X11/wmsession.d/07%name

%dir %_sysconfdir/X11/%name/
%config %_sysconfdir/X11/%name/[!m]*
%ghost %verify(not mtime md5 size) %_sysconfdir/X11/%name/menu

%dir %_datadir/%name/
%dir %_datadir/%name/nls/
%_datadir/%name/styles/
%_datadir/%name/apps
%_datadir/%name/overlay
%_datadir/%name/windowmenu

%files -n vim-plugin-fluxbox-syntax
%vim_syntax_dir/flux*.vim
%vim_ftdetect_dir/%name.vim

%changelog
* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2.1
- Fixed build

* Sun May 08 2011 Slava Semushin <php-coder@altlinux.ru> 1.3.1-alt2
- Mark subpackage vim-plugin-fluxbox-syntax as noarch (noted by repocop)
- I not maintain this package anymore

* Mon Feb 28 2011 Slava Semushin <php-coder@altlinux.ru> 1.3.1-alt1
- Updated to 1.3.1
- Introduced vim-plugin-fluxbox-syntax subpackage
  (patch from Afanasov Dmitry <ender@altlinux.org>)
- Added patch to delete outdated URLs from man pages
- Converted README.ALT to UTF-8
- Converted Summary and %%description to UTF-8

* Mon May 25 2009 Slava Semushin <php-coder@altlinux.ru> 1.1.1-alt5
- Fixed build with automake 1.11
- Don't package outdated Russian manual page

* Sat Apr 11 2009 Slava Semushin <php-coder@altlinux.ru> 1.1.1-alt4
- Use pkg-config instead of imlib2-config

* Fri Dec 05 2008 Slava Semushin <php-coder@altlinux.ru> 1.1.1-alt3
- Fixed build (added libXext-devel to BuildRequires)

* Sat Nov 22 2008 Slava Semushin <php-coder@altlinux.ru> 1.1.1-alt2
- Remove obsolete %%update_menus/%%clean_menus calls (noted by repocop)
- Remove obsolete %%update_wms/%%clean_wms calls (noted by repocop)

* Thu Sep 18 2008 Slava Semushin <php-coder@altlinux.ru> 1.1.1-alt1
- Updated to 1.1.1

* Mon Sep 08 2008 Slava Semushin <php-coder@altlinux.ru> 1.1.0.1-alt1
- Updated to 1.1.0.1
- Corrected %%description
- Replaced %%__autoreconf macros to %%autoreconf (noted by repocop)

* Sat Nov 10 2007 Slava Semushin <php-coder@altlinux.ru> 1.0.0-alt2
- Fixed displaying window icons with transparency pixels by explicitly
  enable XShape extension (deb #450684)

* Wed Oct 10 2007 Slava Semushin <php-coder@altlinux.ru> 1.0.0-alt1
- Updated to new stable version 1.0.0
  + New default theme bloe
  + Xinerama support now enabled by default
- Teach menu-method how to search XPM icons from desktop files (#13011)
- Replaced %%add_findreq_skiplist to find_requires_protect.patch
- Resurrected Cthulhain theme
- Set more proper Requires
- Removed useless --with-x and --enable-imlib2 (now enabled by
  default in upstream) options for configure script
- Imported into git and built with gear

* Sat Mar 24 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.0-alt1rc3
- NMU based on Slava Semushin's <php-coder@> spec.

* Wed Mar 21 2007 Slava Semushin <php-coder@altlinux.ru> 1.0-alt0rc3
- Updated to 1.0rc3
- Removed dont_generate_utf_twice patch (merged to upstream)
- Adapted disable_fonts patch
- Change my name in Packager tag and in README.alt.koi8-r file
- Spec cleanup:
  + Formatted and corrected %%description
  + Use builtin %%patch instead of external command
  + s/%%setup -q/%%setup/

* Tue Jul 18 2006 Slava Semushin <php-coder@altlinux.ru> 1.0-alt0rc2
- Updated to 1.0rc2
- Removed gettext_support patch (unfortunately :( )
- Added patch dont_generate_utf_twice to fix identical cat-files
  for el_GR locale
- Updated README.alt.koi8-r

* Sun Jun 18 2006 php-coder <php-coder@altlinux.ru> 0.9.15.1-alt2
- Updated gettext_support patch:
  + configure.in: do not check nl_types.h header
  + src/FbTk/gettext.hh: include config.h
  + src/RegExp.cc.orig: removed
  + po/Makefile: remove unneded echo and do not use -v flag for rm
  + util/fbsetroot.cc: reordering #ifdef's
- Removed title patch. Use session.screen0.windowScrollAction
  preference instead
- Updated README.alt.koi8-r
- Corrected Requires for menu
- Corrected %%changelog entry

* Thu Apr 06 2006 php-coder <php-coder@altlinux.ru> 0.9.15.1-alt1
- Updated to 0.9.15.1 (bugfix release)
- Adapted gettext_support patch
- Replace all tabs in README.ALT.koi8-r to spaces
- Enable _unpackaged_files_terminate_build (thnx wrar@ for help)

* Thu Mar 23 2006 php-coder <php-coder@altlinux.ru> 0.9.15-alt1
- Updated to 0.9.15
- Modified menu-methods (#8782)
- Updated Requires and BuildRequires for Xorg7
- Added conditions for build with debug and xinerama
  (both disabled by default)
- Removed screen_option, fix_svn_translate and
  unused_variables patches (merged to upstream)
- Removed substitution bsetroot to fbsetroot in styles
  (fixed in upstream)
- Adapted title and disabled_fonts patches
- Replaced coding patch to gettext_support patch
- Updated README.ALT.koi8-r
- Compressed ChangeLog
- Use macros %%__autoreconf
- Use macros %%_niconsdir instead of %%_iconsdir
- Removed big icon (64x64) from package
- More strict names in %%files section
- Dont use macros for patch, mkdir -p and install commands
- Removed Summary and %%description in koi8-r and utf8 charsets
- Fixed orthographical errors in %%changelog (spotted by mike@)

* Fri Dec 16 2005 php-coder <php-coder@altlinux.ru> 0.9.14-alt3
- Added unused_variables patch which fixed warnings from compiler
  about unused variables
- Updated BuildRequires
- Added 'menu' to post/postun Requires
- Using sed instead of subst
- Running make with --no-print-directory and --silent options to make
  terminal output clean
- Using -fisv keys for autoreconf instead of --install --force
  (thnx ldv@ for advice)
- Spec cleanup

* Tue Oct 04 2005 php-coder <php-coder@altlinux.ru> 0.9.14-alt2
- Fixed mismatch version libtool.m4 and ltmain.sh
- Added patches:
  + fix_svn_translate: fixed wrong charset in translation
  + screen_option: added info about website and -screen option to
    output fluxbox -help, added translation for -screen option and
    updated russian translation
- Added full url to Source tag

* Sat Sep 17 2005 php-coder <php-coder@altlinux.ru> 0.9.14-alt1
- Version bumped to 0.9.14
  You can find full list of changes in NEWS and ChangeLog files
- Removed patches (in upstream now): uk_UA_locale, cthulhain and
  svn_translate
- Adapted title and encoding patches

* Fri Aug 26 2005 php-coder <php-coder@altlinux.ru> 0.9.13-alt3.3
- Updated menu-method (#7524, thnx zerg@)
  + Added icons to submenus
  + Header in menu is "ALT Linux"
  + Search icons in /usr/share/icons/hicolor/16x16/apps
- Using one menu-method in entry "Update menu"
  (thnx Afanasov Dmitry <ender@comp-mir.ru> for bugreport)
- Added uk_UA localization file (patch uk_UA_locale)

* Tue Jul 26 2005 php-coder <php-coder@altlinux.ru> 0.9.13-alt3.2
- SVN snapshot 20050725 (fixed #7389)
- Added patches:
  + title: using the mouse wheel in the window title switches between
    tabbed windows (patch from Eike
    <jan_eike_von.seggern@mailbox.tu-dresden.de>)
  + cthulhain: fixed border around workspace in toolbar
  + svn_translate: added translation about SVN revision to -info
    output
  + disable_fonts: fixed fonts
- Adapted encoding and no_genarate_menu patches
- Removed patches (in upstream now): with_locale_path_option,
  fixed_configure_options, be_by_locale
- Removed utf8_slow_start patch
- Added README.ALT.koi8-r (1,8 Kb)
- Removed INSTALL file (4,1 Kb)
- Use %%__patch instead of builtin %%patch
- Formatted %%changelog

* Thu Jun 02 2005 php-coder <php-coder@altlinux.ru> 0.9.13-alt3.1
- Delete all russian comments in spec file (#6649)

* Sun May 22 2005 php-coder <php-coder@altlinux.ru> 0.9.13-alt3
- Added be_BY localization file (patch be_by_locale -- thnx kas@)
- Fixed --with-{init,keys,menu} options for configure when they not
  installed configuration files (patch fixed_configure_options)

* Wed May 18 2005 php-coder <php-coder@altlinux.ru> 0.9.13-alt2
- The package has less dependencies (through using
  %%add_findreq_skiplist macros)
- Submenu "Session" entries update: About, Update menu and
  Tools/Window name
- Used patch no_generate_menu to switch off menu generation on build
  by fluxbox-generate_menu
- Patches and specs do not update Makefile.in files as they are
  generated out of Makefile.am on build

* Sat May 14 2005 php-coder <php-coder@altlinux.ru> 0.9.13-alt1
- Version bumped to 0.9.13
  You can find full list of changes in NEWS and ChangeLog files
- Fluxbox developers were kind enough to include my patches
  translation-clock, default_style and with_menu_keys_init_options
  into current version, so the have been removed from the package.
- Updated encoding and with_locale_path_option patches
- Remove Coding_style, README.menu and README.style files from the
  documentation

* Thu May 12 2005 php-coder <php-coder@altlinux.ru> 0.9.12-alt1
- First build for Sisyphus
- Updated BuildRequires
- Header in them menu is "ALTLinux"
- When menu is generated icons are looked for in /usr/share/pixmaps
- Added genericname in menu-file
- Menu entry "Session" in one before last in the menu
- Using macros AC_CONFIG_HEADER instead of obsolete AM_CONFIG_HEADER

* Fri Apr 29 2005 php-coder <php-coder@altlinux.ru> 0.9.12-alt0.M24.1
- First ALTLinux build
- It's using title() instead of $title in menu-methods
- It's using term() instead of xterm in menu-methods
- Control points names on the menu translating "on the fly" when menu
  is generating
- longtitle is in English menu file
- %%setup is called with -q option to make terminal output clean
- Added utf8_slow_start patch, which fixes the problem with delay at
  startup in UTF locale (thnx Sergey Kuleshov <svytogor@gentoo.org>)

