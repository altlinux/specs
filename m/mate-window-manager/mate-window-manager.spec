Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSM-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-3.0) pkgconfig(libgtop-2.0) pkgconfig(pango) pkgconfig(xcomposite) pkgconfig(xcursor) pkgconfig(xfixes) pkgconfig(xrender)
# END SourceDeps(oneline)
BuildRequires: libcanberra-gtk2-devel
%define _libexecdir %_prefix/libexec
%{echo 
%filter_from_requires /^libmarco-private.so/d;

}


Name:           mate-window-manager
Version:        1.5.2
Release:        alt5_10
Summary:        MATE Desktop window manager
License:        LGPLv2+ and GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# https://bugzilla.gnome.org/show_bug.cgi?id=622517
Patch0:         Allow-breaking-out-from-maximization-during-mouse.patch
# https://bugs.launchpad.net/ubuntu/+source/metacity/+bug/583847
Patch1:         initialise_all_workspace_names.patch

# upstream patch
# https://github.com/mate-desktop/mate-window-manager/commit/6404a98fb79e7bb4c3e9c5ca9919e12c946679d7
Patch2:         0001-fix-startup-rendering-effect-with-composite-enabled.patch

BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: mate-common
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(MateCORBA-2.0)
BuildRequires: mate-dialogs
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(xdamage)

Requires:      gsettings-desktop-schemas


Obsoletes: mate-window-manager-libs < 1.4.1-2

# http://bugzilla.redhat.com/873342
Provides: firstboot(windowmanager) = mate-window-manager
Source44: import.info
# http://bugzilla.gnome.org/show_bug.cgi?id=558723
Patch33: stop-spamming-xsession-errors.patch
# from fedora. do we need it?
Patch34: mate-window-manager-fresh-tooltips.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=598995
Patch35: Dont-focus-ancestor-window-on-a-different-workspac.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=559816
Patch36: metacity-2.28-empty-keybindings.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=604319
Patch37: metacity-2.28-xioerror-unknown-display.patch
Requires: libmarco-private = %{version}-%{release}

%description
MATE Desktop window manager

%package devel
Group: Development/C
Summary: Development files for mate-window-manager
Requires: libmarco-private = %{version}-%{release}

%description devel
Development files for mate-window-manager

%package -n libmarco-private
Group: System/Libraries
Summary: mate-window-manager internal library

%description -n libmarco-private
Internal library for MATE Window Manager.



%prep
%setup -q
%patch0 -p1
#patch1 -p1
%patch2 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-static	\
	--disable-scrollkeeper	\
	--with-gnu-ld		\
	--with-gtk=2.0		\
	--with-x

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -vf {} ';'

desktop-file-install                                \
        --remove-category="MATE"                    \
        --delete-original                           \
        --dir=%{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/marco.desktop

%find_lang %{name} --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/marco
%{_bindir}/marco-message
%{_datadir}/applications/marco.desktop
%{_datadir}/themes/ClearlooksRe/
%{_datadir}/themes/Dopple-Left/
%{_datadir}/themes/Dopple/
%{_datadir}/themes/DustBlue/
%{_datadir}/themes/Spidey-Left/
%{_datadir}/themes/Spidey/
%{_datadir}/themes/Splint-Left/
%{_datadir}/themes/Splint/
%{_datadir}/themes/WinMe/
%{_datadir}/themes/eOS/
%{_datadir}/marco/
%{_datadir}/mate-control-center/keybindings/50-marco*.xml
%{_datadir}/mate/help/creating-marco-themes/C/creating-marco-themes.xml
%{_datadir}/mate/wm-properties/
%{_datadir}/glib-2.0/schemas/org.mate.marco.gschema.xml
%{_libdir}/libmarco-private.so.0*
%{_mandir}/man1/marco.1.*
%{_mandir}/man1/marco-message.1.*
# moved to lib
%exclude %{_libdir}/libmarco-private.so.*

%files -n libmarco-private
%{_libdir}/libmarco-private.so.*


%files devel
%{_bindir}/marco-theme-viewer
%{_bindir}/marco-window-demo
%{_includedir}/marco-1/
%{_libdir}/libmarco-private.so
%{_libdir}/pkgconfig/libmarco-private.pc
%{_mandir}/man1/marco-theme-viewer.1.*
%{_mandir}/man1/marco-window-demo.1.*


%changelog
* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt5_10
- added libmarco-private (closes: 28322)

* Wed Dec 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt4_10
- new fc release

* Thu Nov 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt4_9
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt4_7
- dropped libmarco-private subpackage (no more needed, 1.5.0 transaction is complete)

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt3_7
- added libmarco-private subpackage

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_7
- fuzzless patches

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_7
- use F19 import base

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.2
- dependence on mate-control-center-filesystem temporary removed

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Fri Aug 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- rebuild

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

