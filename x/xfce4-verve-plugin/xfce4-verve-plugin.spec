Name: xfce4-verve-plugin
Version: 1.0.0
Release: alt3

Summary: Command line plugin for XFce Desktop
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch1: xfce4-verve-plugin-1.0.0-alt-drop-old-macros.patch

Obsoletes: verve-plugin < 0.3.6
Provides: verve-plugin

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfcegui4-devel libexo-devel
BuildRequires: intltool libdbus-glib-devel libpcre-devel libxml2-devel perl-XML-Parser

Requires: xfce4-panel >= 4.8

%description
The Verve panel plugin is a comfortable command line plugin for the Xfce
panel. It supports several nice features, such as:
    * Command history
    * Auto-completion (including command history)
    * Open URLs and eMail addresses in your favourite applications
    * Focus grabbing via D-BUS (so you can bind a shortcut to it)
    * Custom input field width

%prep
%setup
%patch1 -p2

%build
# Fix desktop file path for xfce4-panel >= 4.8
sed -i 's|^desktopdir = \$(datadir)/xfce4/panel-plugins|desktopdir = \$(datadir)/xfce4/panel/plugins|' \
   panel-plugin/Makefile.am

%xfce4reconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_bindir/*
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Fix build: Replace BM_DEBUG_SUPPOR with XDT_FEATURE_DEBUG.
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with xfce4-panel-4.9.

* Fri Feb 11 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Remove old patches.
- Updated to 1.0.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.6-alt1
- new version

* Mon Oct 15 2007 Igor Zubkov <icesik@altlinux.org> 0.3.5-alt1.1
- NMU
  + fix build with new intltool

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.5-alt1
- new version

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.4-alt1.1
- Rebuilt due to libdbus-1.so.2 -> libdbus-1.so.3 soname change.

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.3.4-alt1
- First build for Sisyphus.

