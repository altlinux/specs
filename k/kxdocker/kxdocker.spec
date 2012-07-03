Name: kxdocker
Version: 0.39
Release: alt2.qa3

Summary: KXDocker is an innovative docker for KDE
License: GPL
Group: Graphical desktop/KDE
Url: http://www.xiaprojects.com/www/prodotti/kxdocker/main.php
Packager: Ilya Mashkin <oddity at altlinux.ru>

Source0: %name-%version.tar.bz2
#Source1: kxdocker_conf.xml
Patch0: kxdocker-0.39-alt-DSO.patch
Requires: kxdocker-resources = 0.14
BuildRequires: gcc-c++ kdelibs-devel
BuildRequires: libjpeg-devel libpng-devel 
BuildRequires: xml-utils zlib-devel

%description
KXDocker is an innovative docker for KDE it's like Mac OSX Docker but more powerfull


%prep
%setup -q
%patch0 -p2
%__subst 's,\.la,\.so,' configure

%build
%add_optflags -I%_includedir/tqtinterface
unset QTDIR || : ; . /etc/profile.d/qt3dir.sh
export QTLIB=${QTDIR}/lib QTINC=${QTDIR}/include

%K3configure \
  --disable-rpath \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --disable-final \
  --without-arts \

make %{?_smp_mflags}

%install
%K3install

## File lists
# locale's
%K3find_lang %name || touch %name.lang
# HTML (1.0)
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d $RPM_BUILD_ROOT$HTML_DIR ]; then
for lang_dir in $RPM_BUILD_ROOT$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%%lang($lang) $HTML_DIR/$lang/*" >> %name.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
      done
    popd
  fi
done
fi

#__mkdir_p %buildroot/%_menudir
#freedesktop2menu.pl %name Applications/Accessibility %buildroot/%_datadir/applnk/Utilities/%name.desktop %buildroot/%_menudir/%name kde


%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_K3bindir/*
%_K3applnk/Utilities/%name.desktop
#_datadir/applications/*.desktop
%_K3apps/kxdocker
%_K3datadir/icons/hicolor/*/apps/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.39-alt2.qa3
- Fixed build

* Mon Apr 25 2011 Andrey Cherepanov <cas@altlinux.org> 0.39-alt2.qa2
- Disable aRts support
- Adapt to new KDE3 placement
- Remove xorg-x11-devel requirement

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.39-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for kxdocker
  * update_menus for kxdocker
  * postclean-05-filetriggers for spec file

* Mon Nov 19 2007 Ilya Mashkin <oddity at altlinux.ru> 0.39-alt2
- correct spec

* Sun Jan 08 2006 Ilya Mashkin <oddity at altlinux.ru> 0.39-alt1
- Very new version 0.39, experimental build!
- cleanup/dust spec

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.23-alt2.1
- Rebuilt with libstdc++.so.6.

* Tue Oct 19 2004 Dmitriy Porollo <spider@altlinux.ru> 0.23-alt2
-0.23-alt2 Network Usage applet added.

* Fri Aug 27 2004 Dmitriy Porollo <spider@altlinux.ru> 0.23-alt1
-0.23-alt1 Multiple default configurations see documentations.
-0.23-alt1 Sleep before raise the bar
-0.23-alt1 The docker may work in background
-0.23-alt1 Raise with display corner

* Mon Jun 21 2004 Dmitriy Porollo <spider@altlinux.ru> 0.22-alt1
-0.22-alt1 Fix: tons of small bugfix-enhancements
-0.22-alt1 Thumbnails: may be done without the icon
-0.22-alt1 Actions: plugins and icons may have own actions
-0.22-alt1 DCOP: more commands
-0.22-alt1 Fix: iconsizes tested: 16,32,48 to 48,64,96,128
-0.22-alt1 AUTO SEND TO BACKGROUND!!!!!!!!!!!

* Tue Jun 15 2004 Dmitriy Porollo <spider@altlinux.ru> 0.21-alt1
-0.21-alt1 Fix: special engine 2 update
-0.21-alt1 Add: Animations!!!!!!!!!!!!!!
-0.21-alt1 Optimizations: code cleanup
-0.21-alt1 Plugins: better support and speedup
-0.21-alt1 Fix: Bug fix
-0.21-alt1 Animations: restore animation update
-0.21-alt1 Pillow: [1/5] now it's external window
-0.21-alt1 Fix: some speedup and code cleanup
-0.21-alt1 New: bar can stay at the TOP of screen
-0.21-alt1 Animations: now they fly !!!
-0.21-alt1 Resources: work without resources
-0.21-alt1 Configurator: some improvements: configuration is auto applied before save
-0.21-alt1 Fix: Icon sizes almost work, please try to disable plugin before report bugs
-0.21-alt1 DCOP: added some commands to support SIM and POP3 email checker
-0.21-alt1 GDate: bug fix, now support auto update, support for themes, see screenshots

* Tue Jun 02 2004 Dmitriy Porollo <spider@altlinux.ru> 0.20-alt2
-0.20-alt2 ADD: CPU monitor.

* Wed Jun 02 2004 Dmitriy Porollo <spider@altlinux.ru> 0.20-alt1
-0.20-alt1 Fix: Important FIX
-0.20-alt1 Task: Auto Add a separator on task icons
-0.20-alt1 Engine: Special Engine 2 now by default! it's now work properly

* Wed May 26 2004 Dmitriy Porollo <spider@altlinux.ru> 0.19-alt1
-0.19-alt1 New docker release build

* Mon May 24 2004 Dmitriy Porollo <spider@altlinux.ru> 0.18-alt2
-0.18-alt2 Add: OpenOffice.org group added

* Wed May 19 2004 Dmitriy Porollo <spider@altlinux.ru> 0.18-alt1
-0.18-alt1 Add: If you change desktop it will not animate with poof (it make it faster and usable)
-0.18-alt1 Add: SEPARATOR!!! you can add icons and use className=GSeparator
-0.18-alt1 Add: New smooth engine!!!!

* Tue May 11 2004 Dmitriy Porollo <spider@altlinux.ru> 0.17-alt1
- 0.17-alt1 Add: pager:show desktop [tanks to Saurabh]
- 0.17-alt1 Cfg: Support for plugin configurations
- 0.17-alt1 Cfg: Plugin configuration (Animations Pager TaskManager)
- 0.17-alt1 Plugin configuration (Animations Pager TaskManager)
- 0.17-alt1 Alias configuration (with disabled window support ex: xmms)
- 0.17-alt1 Icon Plugin configuration (path of clock images)
- 0.17-alt1 Cfg: a tons of bugfix

* Fri Apr 23 2004 Dmitriy Porollo <spider@altlinux.ru> 0.15-alt1
- 0.15-alt1 Fix: pillow flickering
- 0.15-alt1 Plugin: better pager support
- 0.15-alt1 Cfg: "stay in dock"
- 0.15-alt1 fix: external pager bug fix
- 0.15-alt1 Support for icon sizes 16 to 64
- 0.15-alt1 TaskManager: show only current desktop's windows or all Desktop!!!!
- 0.15-alt1 Added some software into the dock (PSI)

* Mon Apr 19 2004 Dmitriy Porollo <spider@altlinux.ru> 0.14-alt2
- 0.14-alt2 Correct config added

* Mon Apr 19 2004 Dmitriy Porollo <spider@altlinux.ru> 0.14-alt1
- 0.14-alt1 release build

* Mon Apr 12 2004 Dmitriy Porollo <spider@altlinux.ru> 0.11-alt1
- 0.11-alt1 release build
