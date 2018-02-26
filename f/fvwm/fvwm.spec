Name: fvwm
Version: 2.6.5
#define cvsdate 20031019
Release: alt1

%def_with fribidi
%def_with libstroke

%define _unpackaged_files_terminate_build 1

Summary: F(?) Virtual Window Manager
Summary(ru_RU.UTF-8): Мощный оконный менеджер для X Window System
License: GPLv2+
Group: Graphical desktop/FVWM based
Url: http://www.fvwm.org/
Packager: Sergey Vlasov <vsu@altlinux.ru>

%ifdef cvsdate
Source: %name-%cvsdate.tar
%else
# ftp://ftp.fvwm.org/pub/fvwm/version-2/%name-%version.tar.bz2
Source: %name-%version.tar
%endif

Source1: fvwm-2.0.46.icons.tar

Source11: fvwm-compat-icons.tar
Source12: fvwm-menuicon-32.xpm
Source13: fvwm-menuicon.xpm
Source14: Fvwm.xpm
Source15: fvwm.menu
Source16: fvwm.menu-method
Source17: startfvwm
Source18: fvwm.wmsession

Patch1: fvwm-2.5.10-alt-obsolete-modules.patch
Patch2: fvwm-2.6.0-alt-config.patch
Patch3: fvwm-2.6.0-alt-xft-config.patch
Patch4: fvwm-2.5.18-alt-fvwmbug-tmp.patch
Patch6: fvwm-2.5.7-alt-greyed_menu_back.patch
Patch7: fvwm-2.5.14-alt-fonts.patch
Patch8: fvwm-2.6.5-alt-perl-requires.patch
Patch9: fvwm-2.5.16-alt-configure-gdk_imlib.patch
Patch11: fvwm-2.5.23-alt-configure-datarootdir.patch
Patch12: fvwm-2.5.26-alt-bound.patch
Patch13: fvwm-2.5.27-alt-format.patch
Patch14: fvwm-2.5.27-alt-fvwm_msg-echo.patch

%{?_with_fribidi:BuildPreReq: fribidi libfribidi-devel}
%{?_with_libstroke:BuildPreReq: libstroke-devel}

BuildRequires: imlib-devel libXcursor-devel libXft-devel libXinerama-devel libXpm-devel libXt-devel libncurses-devel libreadline-devel perl-GTK perl-Gtk2 perl-Tk perl-X11-Protocol perl-XML-Parser xsltproc

%description
Fvwm is an ICCCM-compliant X window manager providing a 3D look for
window decorations, multiple discontiguous virtual desktops, a high
degree of configurability, and an external module interface for
implementing functional extensions.

%description -l ru_RU.UTF-8
Fvwm - мощный оконный менеджер для X Window System, соответствующий
стандартам ICCCM, с поддержкой множественных виртуальных десктопов.

Эта версия включает в себя новые особенности, такие как цветовые
комплекты (colorsets), соответствие ICCCM2 и совместимость с GNOME,
управление сессий, улучшения во всех модулях, несколько новых модулей,
переработанный код меню, поддержка stroke, Xft2 и многое другое.


%package full
Summary: Fvwm with all available modules
Summary(ru_RU.UTF-8): Fvwm с полным набором модулей
Group: Graphical desktop/FVWM based
Requires: %name-base = %version-%release
Requires: %name-perl = %version-%release
Requires: %name-gtk  = %version-%release
Provides: fvwm95 = %version-%release
Provides: fvwm2  = %version-%release
Provides: fvwm   = %version-%release
Obsoletes: fvwm95, fvwm2, fvwm
BuildArch: noarch

%description full
Fvwm is an ICCCM-compliant X window manager providing a 3D look for
window decorations, multiple discontiguous virtual desktops, a high
degree of configurability, and an external module interface for
implementing functional extensions.

This virtual package installs fvwm with all available modules.

%description -l ru_RU.UTF-8 full
Fvwm - мощный оконный менеджер для X Window System, соответствующий
стандартам ICCCM, с поддержкой множественных виртуальных десктопов.

Эта версия включает в себя новые особенности, такие как цветовые
комплекты (colorsets), соответствие ICCCM2 и совместимость с GNOME,
управление сессий, улучшения во всех модулях, несколько новых модулей,
переработанный код меню, поддержка stroke, Xft2 и многое другое.

Этот виртуальный пакет устанавливает fvwm вместе с полным набором
модулей для него.


%package base
Summary: F(?) Virtual Window Manager - base parts
Summary(ru_RU.UTF-8): Оконный менеджер fvwm с базовым набором модулей
Group: Graphical desktop/FVWM based
Requires: %name-icons = %version-%release, %name-doc = %version-%release
Conflicts: fvwm-themes <= 0.7.0-alt1

%description base
Fvwm is an ICCCM-compliant X window manager providing a 3D look for
window decorations, multiple discontiguous virtual desktops, a high
degree of configurability, and an external module interface for
implementing functional extensions.

This package contains base parts of fvwm, enough for many
configurations.  You may additionally install the %name-perl and
%name-gtk packages to get more features.

%description -l ru_RU.UTF-8 base
Fvwm - мощный оконный менеджер для X Window System, соответствующий
стандартам ICCCM, с поддержкой множественных виртуальных десктопов.

Эта версия включает в себя новые особенности, такие как цветовые
комплекты (colorsets), соответствие ICCCM2 и совместимость с GNOME,
управление сессий, улучшения во всех модулях, несколько новых модулей,
переработанный код меню, поддержка stroke, Xft2 и многое другое.

Этот пакет содержит базовый набор модулей fvwm, достаточный для многих
конфигураций.  При необходимости можно установить пакеты с
дополнительными модулями: %name-perl и %name-gtk.


%package doc
Summary: F(?) Virtual Window Manager - documentation
Summary(ru_RU.UTF-8): Документация для fvwm
Group: Graphical desktop/FVWM based
Conflicts: %name-base < 2.5.26-alt1
BuildArch: noarch

%description doc
This package contains documentation for the fvwm window manager.

%description -l ru_RU.UTF-8 doc
Этот пакет содержит документацию для оконного менеджера fvwm.

%package gtk
Summary: F(?) Virtual Window Manager - FvwmGtk module
Summary(ru_RU.UTF-8): Модуль FvwmGtk для fvwm
Group: Graphical desktop/FVWM based
PreReq: %name-base = %version-%release

%description gtk
Fvwm is an ICCCM-compliant X window manager providing a 3D look for
window decorations, multiple discontiguous virtual desktops, a high
degree of configurability, and an external module interface for
implementing functional extensions.

This package contains the FvwmGtk module, which implements GTK-based
alternatives to the GUI elements in fvwm, namely the builtin menus and
the FvwmForm dialogs.

%description -l ru_RU.UTF-8 gtk
Fvwm - мощный оконный менеджер для X Window System, соответствующий
стандартам ICCCM, с поддержкой множественных виртуальных десктопов.

Эта версия включает в себя новые особенности, такие как цветовые
комплекты (colorsets), соответствие ICCCM2 и совместимость с GNOME,
управление сессий, улучшения во всех модулях, несколько новых модулей,
переработанный код меню, поддержка stroke, Xft2 и многое другое.

Этот пакет содержит модуль FvwmGtk, который позволяет использовать меню
и диалоговые окна в стиле GTK вместо встроенного стиля fvwm.


%package perl
Summary: F(?) Virtual Window Manager - Perl parts
Summary(ru_RU.UTF-8): Модули Perl для fvwm
Group: Graphical desktop/FVWM based
PreReq: %name-base = %version-%release
BuildArch: noarch

%description perl
Fvwm is an ICCCM-compliant X window manager providing a 3D look for
window decorations, multiple discontiguous virtual desktops, a high
degree of configurability, and an external module interface for
implementing functional extensions.

This package contains the FvwmPerl module, fvwm Perl library and other
parts which depend on Perl.

%description -l ru_RU.UTF-8 perl
Fvwm - мощный оконный менеджер для X Window System, соответствующий
стандартам ICCCM, с поддержкой множественных виртуальных десктопов.

Эта версия включает в себя новые особенности, такие как цветовые
комплекты (colorsets), соответствие ICCCM2 и совместимость с GNOME,
управление сессий, улучшения во всех модулях, несколько новых модулей,
переработанный код меню, поддержка stroke, Xft2 и многое другое.

Этот пакет содержит модуль FvwmPerl, библиотеку для написания модулей
fvwm на Perl и другие части fvwm, использующие Perl.


%package icons
Summary: Graphic files used by the fvwm window manager
Summary(ru_RU.UTF-8): Графические файлы для fvwm
Group: Graphical desktop/FVWM based
Provides: fvwm95-icons = %version-%release, fvwm2-icons = %version-%release
Obsoletes: fvwm95-icons, fvwm2-icons
BuildArch: noarch

%description icons
This package contains icons, bitmaps and pixmaps used by the fvwm X
Window System window manager.

%description -l ru_RU.UTF-8 icons
Этот пакет содержит графические файлы, используемые оконным менеджером
fvwm.


%prep
%setup -q %{?cvsdate:-n fvwm} -a1 -a11

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

# Fix default fonts.
find -type f -print0 |
	xargs -r0 grep -FZl -e -adobe- -- |
	xargs -r0 subst 's,-adobe-,-*-,g'

%build
%add_optflags -fno-strict-aliasing

# required because of modified Makefile.am
autoreconf -iv

export FVWM_BUGADDR='%packager'
%configure \
	--prefix=%_prefix \
	--bindir=%_bindir \
	--mandir=%_mandir \
	--datadir=%_datadir \
	--libexecdir=%_libexecdir \
	--sysconfdir=%_sysconfdir/X11/%name \
	--with-imagepath=%_miconsdir:%_iconsdir:%_x11includedir/bitmaps \
	--without-termcap-library \
	--with-xft \
	%{?_without_fribidi:--disable-bidi} \
	--enable-htmldoc \
	--without-gnome

%make_build

%install
%make_install install DESTDIR=$RPM_BUILD_ROOT

# Prepare sample configs.
rm -rf fvwmrc.sample
cp -a sample.fvwmrc fvwmrc.sample
rm -f fvwmrc.sample/Makefile*

# Install default config.
install -pD -m644 $RPM_BUILD_ROOT%_datadir/fvwm/ConfigFvwmSetup \
	$RPM_BUILD_ROOT%_sysconfdir/X11/%name/system.fvwm2rc

# Fake generated menu file.
install -m644 /dev/null $RPM_BUILD_ROOT%_sysconfdir/X11/%name/menu

# Install icons.
rm -rf $RPM_BUILD_ROOT%_iconsdir
mkdir -p $RPM_BUILD_ROOT%_miconsdir
install -pD -m644 icons/*.xpm $RPM_BUILD_ROOT%_iconsdir/
mv $RPM_BUILD_ROOT%_iconsdir/mini*.xpm $RPM_BUILD_ROOT%_miconsdir/

# mdk: Install compatibility icons
install -pD -m644 fvwm-compat-icons/*.xpm $RPM_BUILD_ROOT%_iconsdir
install -pD -m644 fvwm-compat-icons/mini/*.xpm $RPM_BUILD_ROOT%_miconsdir

# mdk: remove conflicting icons.
pushd $RPM_BUILD_ROOT
	rm -f .%_iconsdir/xv.xpm
	rm -f .%_iconsdir/bell.xpm
	rm -f .%_iconsdir/desktop.xpm
	rm -f .%_iconsdir/keyboard.xpm
	rm -f .%_iconsdir/xpaint.xpm
	rm -f .%_iconsdir/xemacs.xpm
	rm -f .%_iconsdir/gv.xpm
popd

# mdk: menu entry icon
install -pD -m644 %SOURCE12 $RPM_BUILD_ROOT%_iconsdir/%name-menuicon.xpm
install -pD -m644 %SOURCE13 $RPM_BUILD_ROOT%_miconsdir/%name-menuicon.xpm
install -p -m644 %SOURCE14 $RPM_BUILD_ROOT%_iconsdir/

# mdk: menu stuff
install -pD -m644 %SOURCE15 $RPM_BUILD_ROOT%_menudir/%name
install -pD -m755 %SOURCE16 $RPM_BUILD_ROOT%_sysconfdir/menu-methods/%name

install -pD -m755 %SOURCE17 $RPM_BUILD_ROOT%_bindir/start%name
install -pD -m644 %SOURCE18 $RPM_BUILD_ROOT%_sysconfdir/X11/wmsession.d/09Fvwm

# move HTML docs to proper place if they were generated
mkdir -p $RPM_BUILD_ROOT/%_docdir/%name
mv $RPM_BUILD_ROOT/%_docdir/%name $RPM_BUILD_ROOT%_docdir/%name-%version

# install additional docs
install -p -m644 AUTHORS COPYING NEWS README \
	docs/ANNOUNCE docs/BUGS docs/FAQ docs/TODO \
	docs/error_codes docs/fvwm.lsm \
	$RPM_BUILD_ROOT%_docdir/%name-%version/

find $RPM_BUILD_ROOT%_docdir/%name-%version -type d -empty -print -delete

%find_lang --output=%name.lang fvwm FvwmScript FvwmTaskBar

%define _perl_lib_path %perl_vendor_privlib:%_datadir/fvwm/perllib

%files base -f %name.lang
%dir %_sysconfdir/X11/%name/
%config(noreplace) %_sysconfdir/X11/%name/system.fvwm2rc
%ghost %_sysconfdir/X11/%name/menu
%_sysconfdir/X11/wmsession.d/*
%_sysconfdir/menu-methods/*
%_bindir/*
%exclude %_bindir/fvwm-convert-2.4
%exclude %_bindir/fvwm-convert-2.6
%exclude %_bindir/fvwm-menu-desktop
%exclude %_bindir/fvwm-menu-directory
%exclude %_bindir/fvwm-menu-headlines
%exclude %_bindir/fvwm-menu-xlock
%exclude %_bindir/fvwm-perllib
%_libexecdir/fvwm
%exclude %_libexecdir/fvwm/%version/FvwmCommand.pm
%exclude %_libexecdir/fvwm/%version/FvwmConsoleC.pl
%exclude %_libexecdir/fvwm/%version/FvwmDebug
%exclude %_libexecdir/fvwm/%version/FvwmGtk
%exclude %_libexecdir/fvwm/%version/FvwmGtkDebug
%exclude %_libexecdir/fvwm/%version/FvwmPerl
%exclude %_libexecdir/fvwm/%version/FvwmTabs
%exclude %_libexecdir/fvwm/%version/FvwmWindowMenu
%_datadir/fvwm/
%exclude %_datadir/fvwm/perllib/
%exclude %_datadir/fvwm/ConfigFvwmTabs
%exclude %_datadir/fvwm/FvwmTabs-DefaultSetup
%exclude %_datadir/fvwm/fvwm-script-ComExample.pl
%exclude %_datadir/fvwm/fvwm-script-setup95.pl
%_menudir/*

%files doc
%_mandir/man?/*
%exclude %_mandir/man1/FvwmConsoleC.pl.1*
%exclude %_mandir/man1/FvwmDebug.1*
%exclude %_mandir/man1/FvwmGtkDebug.1*
%exclude %_mandir/man1/FvwmPerl.1*
%exclude %_mandir/man1/FvwmTabs.1*
%exclude %_mandir/man1/FvwmWindowMenu.1*
%exclude %_mandir/man1/fvwm-convert-2.4.1*
%exclude %_mandir/man1/fvwm-convert-2.6.1*
%exclude %_mandir/man1/fvwm-menu-desktop.1*
%exclude %_mandir/man1/fvwm-menu-directory.1*
%exclude %_mandir/man1/fvwm-menu-headlines.1*
%exclude %_mandir/man1/fvwm-menu-xlock.1*
%exclude %_mandir/man1/fvwm-perllib.1*
%_docdir/%name-%version

%files full
# virtual package

%files gtk
%_libexecdir/fvwm/%version/FvwmGtk

%files perl
%_bindir/fvwm-convert-2.4
%_bindir/fvwm-convert-2.6
%_bindir/fvwm-menu-desktop
%_bindir/fvwm-menu-directory
%_bindir/fvwm-menu-headlines
%_bindir/fvwm-menu-xlock
%_bindir/fvwm-perllib
%_libexecdir/fvwm/%version/FvwmCommand.pm
%_libexecdir/fvwm/%version/FvwmConsoleC.pl
%_libexecdir/fvwm/%version/FvwmDebug
%_libexecdir/fvwm/%version/FvwmGtkDebug
%_libexecdir/fvwm/%version/FvwmPerl
%_libexecdir/fvwm/%version/FvwmTabs
%_libexecdir/fvwm/%version/FvwmWindowMenu
%_datadir/fvwm/perllib/
%_datadir/fvwm/ConfigFvwmTabs
%_datadir/fvwm/FvwmTabs-DefaultSetup
%_datadir/fvwm/fvwm-script-ComExample.pl
%_datadir/fvwm/fvwm-script-setup95.pl
%_mandir/man1/FvwmConsoleC.pl.1*
%_mandir/man1/FvwmDebug.1*
%_mandir/man1/FvwmGtkDebug.1*
%_mandir/man1/FvwmPerl.1*
%_mandir/man1/FvwmTabs.1*
%_mandir/man1/FvwmWindowMenu.1*
%_mandir/man1/fvwm-convert-2.4.1*
%_mandir/man1/fvwm-convert-2.6.1*
%_mandir/man1/fvwm-menu-desktop.1*
%_mandir/man1/fvwm-menu-directory.1*
%_mandir/man1/fvwm-menu-headlines.1*
%_mandir/man1/fvwm-menu-xlock.1*
%_mandir/man1/fvwm-perllib.1*

%files icons
%_iconsdir/*.xpm
%_miconsdir/*.xpm

%changelog
* Thu May 10 2012 Sergey Vlasov <vsu@altlinux.ru> 2.6.5-alt1
- Updated to 2.6.5.
- Changed XFT fonts in the default config to generic "serif".
- Updated BuildRequires.

* Fri Sep 17 2010 Sergey Vlasov <vsu@altlinux.ru> 2.5.31-alt1
- Updated to 2.5.31.
- Note: Significant changes in Perl API were made in version 2.5.28:
  new naming convention was introduced (userDataDir -> user_data_dir).
  There is some AUTOLOAD magic for compatibility with old names, but
  it might be incomplete.
- Added patches from upstream CVS:
   + fix FvwmTaskBar width
   + add support for Move arguments like 'Move w+-5p w+-2p' (such
     commands are generated by FvwmProxy when ProxyMove is enabled)
   + update documentation
- Fixed Echo command breakage introduced with format warnings fix.

* Thu Jun 25 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.27-alt1
- Updated to 2.5.27.

* Sat Feb 21 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.26-alt1
- Updated to 2.5.26.
- Moved documentation to %name-doc subpackage.
- Packaged fvwm-doc, fvwm-full, fvwm-icons and fvwm-perl subpackages as noarch.

* Tue Sep 25 2007 Sergey Vlasov <vsu@altlinux.ru> 2.5.23-alt1
- 2.5.23.
- Removed cvs-CVE-2006-5969 patch (obsolete).
- Enabled HTML documentation build (new in 2.5.22); added HTML docs to the
  fvwm-base package.
- Added alt-configure-datarootdir patch: fake datarootdir for autoconf-2.59
  (temporary build fix while autoconf >= 2.60 is not available).
- Added alt-htmldoc patch: fix HTML documentation build and installation.
- Updated BuildRequires.

* Sat Nov 25 2006 Sergey Vlasov <vsu@altlinux.ru> 2.5.18-alt2
- Fixed CRLF injection vulnerability in the fvwm-menu-directory script
  (CVE-2006-5969); patch from upstream CVS repository.

* Mon Sep 18 2006 Sergey Vlasov <vsu@altlinux.ru> 2.5.18-alt1
- 2.5.18.
- Updated alt-config, alt-fvwmbug-tmp patches.
- Removed obsolete cvs-* patches.
- Added alt-perl-nonascii patch: replace non-ASCII character in the FvwmTabs
  perl script by the corresponding Unicode escape (assuming that the author was
  using ISO8859-1); fixes build failure on perl checks.
- Updated BuildRequires.
- Added -fno-strict-aliasing option to avoid possible miscompilation.
- Repacked fvwm-compat-icons tarball with proper paths.

* Wed Aug 23 2006 Sergey Vlasov <vsu@altlinux.ru> 2.5.16-alt3
- Fixed menu method to use term() instead of hardcoded (and wrong) path to
  xterm (#9873).

* Thu Jun 01 2006 Sergey Vlasov <vsu@altlinux.ru> 2.5.16-alt2
- Added bugfix patches from CVS:
  + cvs-non-icccm2-wm-detect: fix for Fvwm not detecting non ICCCM2 wm (Fvwm
    bug 3151)
  + cvs-four-part-versions: fix configure to cope with 4 digit version numbers
  + cvs-WarpToWindow-update-pos: make WarpToWindow update pointer position
    correctly in case it is followed by Move
  + cvs-TitleWarp: make TitleWarp menu style not warp the pointer for root
    menus (as it is documented)
  + cvs-conditions: fix Iconifiable, Fixed, FixedSize, Maximizable and Closable
    conditions (they were checked only for the first window in the list)
  + cvs-invalid-free: fix Fvwm bug 1557/3950 (possible invalid free of a string
    constant or already used name)
- Added alt-configure-gdk_imlib patch: fix configure failure to find gdk_imlib
  (now ld does not see g_strdup() from glib with only -lgdk_imlib).
- Removed all %%__* macro abuse from spec.
- Fixed icons installation for new %%_miconsdir location.
- Updated BuildRequires.

* Sat Jan 28 2006 Sergey Vlasov <vsu@altlinux.ru> 2.5.16-alt1
- 2.5.16.
- Added alt-perl-requires patch: workaround for FVWM::Module::Toolkit magic
  which breaks automatic dependency generation for Perl scripts, causing
  incomplete dependencies.
- Placed FvwmTabs module (new in 2.5.15) in the fvwm-perl subpackage.

* Sun Jan 08 2006 Sergey Vlasov <vsu@altlinux.ru> 2.5.14-alt2
- Fixed typo in startfvwm script (xsetroot call was broken).

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.5.14-alt1.1
- Rebuilt with libreadline.so.5.

* Fri Dec 16 2005 Sergey Vlasov <vsu@altlinux.ru> 2.5.14-alt1
- 2.5.14.
- Moved all files from /usr/X11R6 to /usr (/usr/X11R6 is going away).
- Added Conflicts: fvwm-themes <= 0.7.0-alt1 because of directory changes.
- Made fribidi and libstroke support optional.
- Added alt-fonts patch to fix font problems in default configuration when
  using an UTF-8 locale (non-XLFD font names result in unusable fonts).

* Mon Jul 18 2005 Sergey Vlasov <vsu@altlinux.ru> 2.5.13-alt1
- 2.5.13.
- Updated BuildRequires.

* Thu Dec 02 2004 Sergey Vlasov <vsu@altlinux.ru> 2.5.12-alt1
- 2.5.12.

* Fri Apr 30 2004 Sergey Vlasov <vsu@altlinux.ru> 2.5.10-alt3
- Fixed font specification in default config (#2633).
- Reenabled bidirectional text support.
- Updated BuildRequires.

* Fri Apr 23 2004 Sergey Vlasov <vsu@altlinux.ru> 2.5.10-alt2
- Fixed missing menu entry for fvwm in Session/Windowmanagers.
- Fixed missing icons in menu (added more icon directories to the menu method).

* Tue Apr 20 2004 Sergey Vlasov <vsu@altlinux.ru> 2.5.10-alt1
- 2.5.10.
- Renamed package to fvwm.
- Split package to several parts:
  - fvwm-base (core and modules with no special dependencies)
  - fvwm-perl (Perl parts)
  - fvwm-gtk  (FvwmGtk module)
  - fvwm-full (virtual package to get everything; replaces old fvwm2)
- Updated the menu method to use the builtin gettext support ($[gt.foo])
  instead of translation at menu generation time (no more problems with
  multiuser setups with different languages and encodings).
- Build without bidirectional text support (the required fribidi library is no
  longer in Sisyphus).
- Updated alt-fvwmbug-tmp patch.
- Updated alt-config patch (fixed bug with root cursor setting).
- Patch1 (alt-obsolete-modules): remove FvwmCascade and FvwmTile (replacement
  for rh-modules patch which modified Makefile.in)
- Updated BuildRequires.

* Sun Oct 19 2003 Sergey Vlasov <vsu@altlinux.ru> 2.5.8-alt0.20031019
- 20031019 CVS snapshot (fixes many bugs, including build problems with new
  fontconfig).
- Updated BuildRequires.
- Removed cvs-FvwmIdent_draw patch (already included).

* Fri Jun 20 2003 Sergey Vlasov <vsu@altlinux.ru> 2.5.7-alt1
- 2.5.7.
- Updated patches: alt-config, alt-xft-config, alt-fvwmbug-tmp.
- Set %%_perl_lib_path to fix perl dependencies.
- Added localization files.
- Added Patch5: %name-2.5.7-cvs-FvwmIdent_draw.patch - fixed FvwmIdent drawing.
- Added Patch6: %name-2.5.7-alt-greyed_menu_back.patch - fixed drawing greyed
  menu item background when the item is selected and HilightBack is used in the
  MenuStyle (Foreground color was used for the background in this case).
- Updated BuildRequires.

* Tue Oct 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5.3-alt3
- Fixed fvwm-bug script.

* Tue Oct 15 2002 AEN <aen@altlinux.ru> 2.5.3-alt2
- Added xft fonts to default config.

* Tue Oct 15 2002 AEN <aen@altlinux.ru> 2.5.3-alt1
- 2.5.3: new development version with xft2 support.

* Tue Mar 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.6-alt1
- 2.4.6.

* Wed Mar 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.5-alt2
- Added --enable-multibyte.

* Mon Feb 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.5-alt1
- 2.4.5.

* Thu Jan 10 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.3-alt2
- Fixed default fonts.

* Mon Jan 07 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.3-alt1
- Updated wmsession.d and startup scripts.
- Updated configuration.

* Wed Nov 07 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.4.3-alt0.1
- Merged rh (2.4.3-2) and mdk (2.2.4-14mdk) packages.

* Mon Nov  5 2001 Than Ngo <than@redhat.com> 2.4.3-2
- disable package subdir (bug #54589)
- add some missing FvwmForm-*, FvwmScript-* ...
- build with libstroke

* Thu Sep 20 2001 Than Ngo <than@redhat.com> 2.4.3-1
- update to 2.4.3

* Thu Sep 20 2001 Than Ngo <than@redhat.com> 2.4.2-1
- update to 2.4.2 (bug #53030)

* Tue Aug  7 2001 Than Ngo <than@redhat.com>
- add patch from greg@lugs.org.sg (bug #51104)

* Fri Jun 22 2001 Preston Brown <pbrown@redhat.com>
- don't own /usr/share/icons dir

* Fri May 25 2001 Helge Deller <hdeller@redhat.de>
- Application icons don't show up unless configured
  with --with-iconpath=/usr/share... (Bug #42230)

* Tue May 21 2001 SATO Satoru <ssato@redhat.com>
- new upstream (2.2.5)
- apply I18N patch
- add Japanese rc file (system.fvwm2rc.ja)

* Tue Aug 22 2000 Than Ngo <than@redhat.com>
- fix system.fvwm2rc (Bug #16707)
- disable debug

* Fri Aug 4 2000 Than Ngo than@redhat.de>
- fixed bugs in FvwmTaskBar (Bug #11066) (thanks to jtl@cs.man.ac.uk)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul  4 2000 Jakub Jelinek <jakub@redhat.com>
- Rebuild with new C++

* Thu Jun 01 2000 Than Ngo <than@redhat.de>
- rebuild for 7.0

* Fri Feb  4 2000 Matt Wilson <msw@redhat.com>
- removed '-s' flag to the install program - broken on sparc

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- rebuild to gzip man pages

* Thu Jan 13 2000 Preston Brown <pbrown@redhat.com>
- 2.2.4

* Thu Sep 23 1999 Preston Brown <pbrown@redhat.com>
- added ability to read wmconfig generated menu (# 2665)

* Thu Sep 09 1999 Preston Brown <pbrown@redhat.com>
- removed compatibility icon pak.

* Fri Aug 27 1999 Preston Brown <pbrown@redhat.com>
- 2.2.2 bugfix release

* Fri Apr 09 1999 Preston Brown <pbrown@redhat.com>
- added some icons from kdebase back to this package for upgrade
- compatibility.

* Wed Mar 24 1999 Bill Nottingham <notting@redhat.com>
- don't require xterm-color

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- better default system.fvwm2rc

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- package is still not finished yet
- upgraded to 2.2, got rid of all the cruft in the spec file

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.0.47
- mark config files as %%config files

* Mon Jun 29 1998 Michael Maher <mike@redhat.com>
- removed duplicate files found in the package Another level.
- fixes bug: 651

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- long time no new version released :-(. -> misc patch
- major spec file cleanups

* Mon Nov 03 1997 Cristian Gafton <gafton@redhat.com>
- Fixed more bugs (bugs patch)

* Fri Oct 24 1997 Cristian Gafton <gafton@redhat.com>
- fixed Alpha build

* Thu Oct 16 1997 Cristian Gafton <gafton@redhat.com>
- fixed FvwmTaskBar severe bug (taskbar patch)
- misc fixes

* Mon Oct 13 1997 Cristian Gafton <gafton@redhat.com>
- built against glibc; added -rh and -fixes patches
