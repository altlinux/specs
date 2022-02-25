%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,unresolved=relaxed

%def_disable debug

%define platform %(%_datadir/automake/config.sub %_target_platform | sed -e 's,-%_vendor,,')
%define rep_archlibdir %(pkg-config --variable=repcommonexecdir librep)
%define PRIO 05

Name: sawfish
Version: 1.13.0
Release: alt1
Summary: An extensible window manager for the X Window System
Group: Graphical desktop/Sawfish
License: GPLv2
Url: https://sawfish.wikia.com/

ExcludeArch: armh

Provides: %_x11sysconfdir/sawfish/site-init.d
Provides: %_datadir/sawfish/site-lisp
Provides: %_datadir/sawfish/sounds
Provides: %_datadir/sawfish/themes

# https://github.com/SawfishWM/sawfish.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

# These are not shell scripts, but shell-wrapped compiled rep scripts.
%add_findreq_skiplist %_bindir/sawfish-client
%add_findreq_skiplist %_bindir/sawfish-themer
%add_findreq_skiplist %_bindir/sawfish-config
%add_findreq_skiplist %_libdir/sawfish/sawfish-about
%add_findreq_skiplist %_libdir/sawfish/sawfish-menu
%add_findreq_skiplist %_datadir/sawfish/lisp/*

Requires: %{get_dep rep-gtk}

BuildRequires(pre): rep-gtk-devel
# Automatically added by buildreq on Mon Apr 27 2009
BuildRequires: libXtst-devel libSM-devel libXext-devel libXinerama-devel libXrandr-devel libgtk+2-devel
BuildRequires: libgdk-pixbuf-xlib-devel
BuildRequires: librep-devel >= 0.92.3-alt2.git20120908
BuildRequires: /usr/bin/makeinfo

%description
Sawfish is an extensible window manager which uses a Lisp-based
scripting language.  All window decorations are configurable and the
basic idea is to have as much user-interface policy as possible
controlled through the Lisp language.  Configuration can be
accomplished by writing Lisp code in a personal .sawfishrc file, or
using a GTK+ interface.  Sawfish is mostly GNOME compliant.

%package gnome
Summary: GNOME integration package
Group: Graphical desktop/GNOME
PreReq: %name = %EVR
PreReq: gnome-filesystem
Requires: gnome-session
Provides: gnome-wm

%description gnome
Sawfish GNOME integration package.

%package devel
Summary: Development files for sawfish
Group: Development/Other
Requires: %name = %EVR
Requires: rpm-build-%name = %EVR

%description devel
Header files for sawfish development.

%package -n rpm-build-%name
Summary: RPM macros for sawfish-related packages
Group: Development/Other
Conflicts: %name < %EVR
Conflicts: %name > %EVR

%description -n rpm-build-%name
RPM macros for sawfish-related packages.

%prep
%setup
%patch -p1
#cp -pfv %_datadir/automake/config.{guess,sub} .
sed -ie 's,^subversion=.*$,subversion="-%release",' configure.ac

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%if_enabled debug
%add_optflags -DDEBUG=1
%endif
%autoreconf
%configure \
	--with-xinerama \
	--with-pango \
	--with-gdk-pixbuf \
	--with-nine-mousebuttons \
	#
# Fix platform name
sed -ie 's,^sawfishhosttype=.*$,sawfishhosttype=%platform,g' data/sawfish.pc
%make_build \
	host_type=%platform

%install
%makeinstall_std \
	host_type=%platform

mkdir -p %buildroot{%_datadir/sawfish/site-lisp,%_sysconfdir/menu-methods,%_x11sysconfdir/{wmsession.d,sawfish/site-init.d},%_pixmapsdir}

install -p -m644 sawfish-48.xpm %buildroot%_pixmapsdir/sawfish.xpm

install -p -m755 menu-method %buildroot%_sysconfdir/menu-methods/sawfish

install -p -m644 altlinux/site-init.jl %buildroot%_datadir/sawfish/site-lisp/
install -p -m644 altlinux/defaults.jl %buildroot%_x11sysconfdir/sawfish/site-init.d/00defaults.jl
install -p -m644 altlinux/menu.jl %buildroot%_x11sysconfdir/sawfish/site-init.d/00menu.jl

mkdir -p %buildroot%_rpmmacrosdir
cat <<EOF >%buildroot%_rpmmacrosdir/sawfish
%%sawfish_version %version
%%sawfish_version_release %version-%release

%%sawfish_dir %_datadir/sawfish

%%sawfish_sitelispdir %_datadir/sawfish/site-lisp
%%sawfish_sitethemedir %_datadir/sawfish/themes
%%sawfish_sitesoundsdir %_datadir/sawfish/sounds
EOF

cat <<EOF > %buildroot%_x11sysconfdir/wmsession.d/%PRIO%name
NAME=Sawfish
ICON=%_pixmapsdir/sawfish.xpm
DESC=Sawfish Window Manager
EXEC=%_bindir/sawfish
SCRIPT:
exec %_bindir/sawfish
EOF

mkdir -p %buildroot%_rpmlibdir
cat <<EOF >%buildroot%_rpmlibdir/sawfish-files.req.list
# sawfish dirlist for %_rpmlibdir/files.req
%_x11sysconfdir/sawfish/site-init.d sawfish
%_datadir/sawfish/site-lisp sawfish
%_datadir/sawfish/sounds sawfish
%_datadir/sawfish/themes sawfish
EOF

# remove unpackaged files
rm -fv %buildroot%_bindir/sawfish-about
rm -fv %buildroot%_bindir/sawfish-kde4-session
rm -fv %buildroot%_bindir/sawfish-kde5-session
rm -fv %buildroot%_bindir/sawfish-lumina-session
rm -fv %buildroot%_bindir/sawfish-mate-session
rm -fv %buildroot%_bindir/sawfish-xfce-session
rm -fvr %buildroot%_datadir/kde4
rm -fvr %buildroot%_datadir/ksmserver
rm -fv %buildroot%_datadir/locale/sr@Latn/LC_MESSAGES/sawfish.mo
rm -fv %buildroot%_datadir/xsessions/sawfish-kde4.desktop
rm -fv %buildroot%_datadir/xsessions/sawfish-kde5.desktop
rm -fv %buildroot%_datadir/xsessions/sawfish-lumina.desktop
rm -fv %buildroot%_datadir/xsessions/sawfish-mate.desktop
rm -fv %buildroot%_datadir/xsessions/sawfish-xfce.desktop

%find_lang %name

%files -f %name.lang
%doc AUTHORS README README.IMPORTANT doc/OPTIONS doc/KEYBINDINGS doc/AUTOSTART doc/XSettings
%config %_x11sysconfdir/wmsession.d/%PRIO%name
%dir %_x11sysconfdir/sawfish
%dir %_x11sysconfdir/sawfish/site-init.d
%config %_x11sysconfdir/sawfish/site-init.d/00*
%config %_sysconfdir/menu-methods/sawfish
%_bindir/sawfish
%_bindir/sawfish-client
%_bindir/sawfish-config
%rep_archlibdir/*
%dir %_datadir/sawfish
%dir %_libdir/sawfish
%_libdir/sawfish/*
%dir %_datadir/sawfish/site-lisp
%_datadir/sawfish/site-lisp/site-init.jl
%dir %_datadir/sawfish/themes
%dir %_datadir/sawfish/sounds
%_datadir/sawfish/sawfish.png
%_datadir/sawfish/images
%_datadir/sawfish/lisp
%_datadir/sawfish/themes/*
%_datadir/sawfish/sounds/*
%_datadir/xsessions/%name.desktop
%_man1dir/sawfish.1*
%_man1dir/sawfish-client.1*
%_man1dir/sawfish-config.1*
%_desktopdir/sawfish.desktop
%_desktopdir/sawfish-config.desktop
%_pixmapsdir/*
%_niconsdir/sawfish-config.png
%_infodir/sawfish.info*
%_rpmlibdir/sawfish-files.req.list

%files gnome
%_datadir/gnome/wm-properties/sawfish-wm.desktop

%files devel
%_includedir/sawfish
%_pkgconfigdir/sawfish.pc

%files -n rpm-build-%name
%_rpmmacrosdir/sawfish

%changelog
* Fri Feb 25 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.13.0-alt1
- Updated to upstream version 1.13.0.

* Mon Feb 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.90-alt4
- Fixed build with gcc-10.

* Wed Dec 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.90-alt3
- Updated build dependencies.
- Explicitly disabled build on armh architecture due to insufficient dependencies.

* Tue Aug 20 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.90-alt2
- Fixed build with new pango.

* Wed Sep 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.90-alt1
- Updated to upstream version 1.12.90.

* Mon Dec 10 2012 Dmitry Derjavin <dd@altlinux.org> 1.9.90-alt1
- [1.9.90] (1.10 beta1);
- Firefox/Thunderbird-17 window size bug fixed.

* Fri Aug 24 2012 Dmitry Derjavin <dd@altlinux.org> 1.9.1-alt1
- [1.9.1]

* Mon Nov 28 2011 Dmitry Derjavin <dd@altlinux.org> 1.8.91-alt1
- [1.8.91]

* Sun May 23 2010 Alexey I. Froloff <raorn@altlinux.org> 1.6.3-alt2
- Native dockapps support

* Sat May 22 2010 Alexey I. Froloff <raorn@altlinux.org> 1.6.3-alt1
- [1.6.3]

* Tue Feb 16 2010 Alexey I. Froloff <raorn@altlinux.org> 1.6.2-alt1
- [1.6.2]

* Sun Feb 14 2010 Alexey I. Froloff <raorn@altlinux.org> 1.6.1-alt1
- [1.6.1]
- devel subpackage

* Wed Nov 25 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.3-alt1
- [1.5.3]

* Fri May 01 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.0-alt0.r4474.1
- SVN revision 4474 (trunk)
- Packaged couple of README's

* Sat Apr 25 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.5.2-alt1
- SVN revision 4456 (branches/sawfish-1.3)
  + Dropped GNOME widget support (removed form rep-gtk)
- Use menu-messages catalog for menu translations
- sawfish.desktop moved to -gnome subpackage
- Translate option descriptions in sawfish-ui

* Sat Dec 27 2008 Sir Raorn <raorn@altlinux.ru> 1.3.5-alt2
- Rebuilt with new librep
- Sanitized platform name
- Fixed client connection (closes: #18361)
- Dropped invalid el translation from .desktop files (noted by repocop)
- Dropped %%sawfish_execdir macro since 3rd-party sawfish extensions
  can not be created
- Use files.req for 3rd-party script dependencies

* Fri Dec 26 2008 Sir Raorn <raorn@altlinux.ru> 1.3.5-alt1
- [1.3.5]

* Sun Dec 07 2008 Sir Raorn <raorn@altlinux.ru> 1.3.4-alt3
- Updated build dependencies
- Removed obsolete update_*/clean_* calls from post-scripts

* Wed Nov 12 2008 Sir Raorn <raorn@altlinux.ru> 1.3.4-alt2
- Provide gnome-wm (closes: #15948)
- GNOME instegration updated for recent gnome-session changes

* Sun Sep 21 2008 Sir Raorn <raorn@altlinux.ru> 1.3.4-alt1
- [1.3.4]
 + Removed obsolete GNOME capplet and configuration menu entries
 + New themes:
  o Elberg-tabbed
  o get-S-tabbed
  o mxflat

* Sat May 31 2008 Sir Raorn <raorn@altlinux.ru> 1.3.3-alt1
- Built for Sisyphus

