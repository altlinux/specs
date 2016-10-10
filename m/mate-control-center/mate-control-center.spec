Serial: 1
Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/update-mime-database imake libX11-devel libXt-devel libgio-devel pkgconfig(dbus-1) pkgconfig(dbus-glib-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(libxklavier) pkgconfig(libxml-2.0) pkgconfig(pango) pkgconfig(unique-1.0) pkgconfig(xcursor) pkgconfig(xi) xorg-cf-files xorg-kbproto-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-control-center
%define version 1.16.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.16

# Settings used for build from snapshots.
%{!?rel_build:%global commit 922d0e0219b1bedcece8624e4b5fd7e15e7a9bd5}
%{!?rel_build:%global commit_date 20131113}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:          mate-control-center
Version:       %{branch}.0
%if 0%{?rel_build}
Release:       alt1_1
%else
Release:       alt1_1
%endif
Summary:       MATE Desktop control-center
License:       LGPLv2+ and GPLv2+
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-control-center.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

#font-preview
Patch6:        mate-control-center_fv-import-SushiFontLoader-and-SushiFontWidget.patch
Patch7:        mate-control-center_fv-thumbnailer-use-SushiFontLoader.patch
Patch8:        mate-control-center_fv-port-to-SushiFontWidget-and-GtkApplication-1.13.patch
Patch9:        mate-control-center_fv-remove-ftstream-vfs.patch
Patch10:       mate-control-center_fv-import-GdMainToolbar.patch
Patch11:       mate-control-center_fv-use-new-style-interface-1.13.patch
Patch12:       mate-control-center_fv-add-FontViewModel.patch
Patch13:       mate-control-center_fv-thumbnailer-respect-the-passed-in-size-argument.patch
Patch14:       mate-control-center_fv-first-pass-at-integrating-an-overview-mode.patch
Patch15:       mate-control-center_fv-thumbnailer-port-to-cairo-rendering.patch
Patch16:       mate-control-center_fv-add-an-application-menu.patch
Patch17:       mate-control-center_fv-adjust-desktop-file.patch
Patch18:       mate-control-center_fv-make-sure-rendered-text-is-black-on-white.patch
Patch19:       mate-control-center_fv-font-widget-sync-from-Sushi.patch
Patch20:       mate-control-center_fv-font-model-fallback-icon-if-we-fail-thumbnailing-the-font-file.patch
Patch21:       mate-control-center_fv-Safely-init-FontConfig-once-for-the-whole-app.patch
Patch22:       mate-control-center_fv-do-not-recreate-different-SushiFontWidget-every-time.patch
Patch23:       mate-control-center_fv-font-widget-another-sync-from-Sushi.patch
Patch24:       mate-control-center_fv-main-toolbar-sync-with-Documents.patch
Patch25:       mate-control-center_fv-font-model-install-file-monitors-on-fontconfig-font-directories.patch
Patch26:       mate-control-center_fv-refresh-Install-button-appearance-when-model-changes.patch
Patch27:       mate-control-center_fv-font-model-add-API-to-get-an-iter-from-a-FT_Face.patch
Patch28:       mate-control-center_fv-match-the-font-face-when-getting-an-iter-to-update-the-button.patch
Patch29:       mate-control-center_fv-font-model-set-a-fallback-icon-if-we-fail-to-read-the-thumbnail.patch
Patch30:       mate-control-center_fv-main-toolbar-another-sync-with-Documents.patch
Patch31:       mate-control-center_fv-do-not-hardcode-fonts-hone-dir-as-target-install-directory.patch
Patch32:       mate-control-center_fv-font-model-do-not-use-sync-g_file_query_info.patch
Patch33:       mate-control-center_fv-font-model-use-g_io_scheduler_push_job-to-refactor-thumbnailing-code.patch
Patch34:       mate-control-center_fv-font-model-use-g_utf8_collation_key-to-sort-the-model.patch
Patch35:       mate-control-center_fv-font-widget-one-more-sync-from-Sushi.patch
Patch36:       mate-control-center_fv-font-model-cache-the-fallback-icon-in-the-private-struct.patch
Patch37:       mate-control-center_fv-font-model-cache-tree-iters-when-setting-values-on-the-model.patch
Patch38:       mate-control-center_fv-font-model-use-a-single-IO-scheduler-job-to-load-thumbnail-images.patch
Patch39:       mate-control-center_fv-font-model-load-font-names-asynchronously.patch
Patch40:       mate-control-center_fv-set-an-empty-title-on-the-info-dialog.patch
Patch41:       mate-control-center_fv-font-model-cancel-previous-loading-when-refreshing-font-list.patch
Patch42:       mate-control-center_fv-font-model-actually-cancel-the-thread-when-rebuilding-font-list.patch
Patch43:       mate-control-center_fv-font-model-emit-config-changed-when-reloading-the-font-list.patch
Patch44:       mate-control-center_fv-font-view-show-an-error-dialog-when-unable-to-load-a-font.patch
Patch45:       mate-control-center_fv-next-sync-from-Sushi.patch
Patch46:       mate-control-center_fv-do-not-crash-when-opening-a-non-existing-file.patch
Patch47:       mate-control-center_fv-font-view-return-early-if-we-have-a-model-already.patch
Patch48:       mate-control-center_fv-thumnailer-do-not-paint-a-white-background-under-thumbnails.patch
Patch49:       mate-control-center_fv-do-not-call-g_type_init.patch
Patch50:       mate-control-center_fv-font-widget-next-2-sync-from-sushi.patch
Patch51:       mate-control-center_fv-font-widget-next-3-sync-from-sushi.patch
Patch52:       mate-control-center_fv-font-model-drop-gtk_icon_info_free.patch
Patch53:       mate-control-center_fv-font-view-add-a-title-to-the-info-dialog.patch
Patch54:       mate-control-center_fv-fix-an-uninitialized-variable.patch
Patch55:       mate-control-center_fv-deprecated-gtk_misc_set_alignment-and-margin-left-right-1.13.patch
Patch56:       mate-control-center_fv-replace-deprecated-method-with-main-context-invocation.patch
Patch57:       mate-control-center_fv-ported-thumbnailing-io-scheduler-job-to-g_task_run_in_thread.patch
Patch58:       mate-control-center_fv-replace-io-scheduler-with-g_task_run_in_thread-in-load_font-infos.patch
Patch59:       mate-control-center_fv-sushi-font-loader-sync-from-sushi.patch
Patch60:       mate-control-center_fv-gd-toolbar-sync-to-latest-libgd-suitable-for-mate.patch
Patch61:       mate-control-center_add-style-class-font-viewer-at-top-level.patch

# not used
#Patch9:        mate-control-center_fv-fix-ununsed-variables-GCC-warnings.patch
#Patch12:       mate-control-center_fv-fix-deprecated-gtk_scrolled_window_add_with_viewport.patch

BuildRequires: libdconf-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires: libcanberra-devel libcanberra-gtk-common-devel libcanberra-gtk2-devel libcanberra-gtk3-devel
BuildRequires: libmatekbd-devel
BuildRequires: librsvg-devel librsvg-gir-devel
BuildRequires: libSM-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXxf86misc-devel
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-menus-devel
BuildRequires: mate-settings-daemon-devel
BuildRequires: mate-window-manager-devel
BuildRequires: libunique3-devel

Requires: gsettings-desktop-schemas
# rhbz (#1234438)
Requires: mate-settings-daemon
# keyring support
Requires: gnome-keyring
Provides: %{name}-filesystem%{?_isa} = %{version}
Source44: import.info
Patch62: gnome-control-center-2.22.1-alt-background-location.patch
Patch63: gnome-control-center-2.28.0-passwd.patch


%description 
MATE Control Center configures system settings such as themes,
keyboards shortcuts, etc.

%package filesystem
Group: Graphical desktop/Other
Summary:      MATE Control Center directories
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package an MUST not depend on the main package

%description filesystem
The MATE control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.

%package devel
Group: Development/C
Summary:      Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{version}

%description devel
Development files for mate-control-center


%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

%patch6 -p1 -b .import-SushiFontLoader-and-SushiFontWidget
%patch7 -p1 -b .thumbnailer-use-SushiFontLoader
%patch8 -p1 -b .port-to-SushiFontWidget-and-GtkApplication
%patch9 -p1 -b .remove-ftstream-vfs
%patch10 -p1 -b .import-GdMainToolbar
%patch11 -p1 -b .use-new-style-interface
%patch12 -p1 -b .add-FontViewModel
%patch13 -p1 -b .thumbnailer-respect
%patch14 -p1 -b .first-pass-at-integrating-an-overview-mode
%patch15 -p1 -b .thumbnailer-port-to-cairo-rendering
%patch16 -p1 -b .add-an-application-menu
%patch17 -p1 -b .adjust-desktop-file
%patch18 -p1 -b .make-sure-rendered-text-is-black-on-white.patch
%patch19 -p1 -b .font-widget-sync-from-Sushi.patch
%patch20 -p1 -b .font-model-fallback-icon-if-we-fail-thumbnailing-the-font-file.patch
%patch21 -p1 -b .Safely-init-FontConfig-once-for-the-whole-app.patch
%patch22 -p1 -b .do-not-recreate-different-SushiFontWidget-every-time.patch
%patch23 -p1 -b .font-widget-another-sync-from-Sushi.patch
%patch24 -p1 -b .main-toolbar-sync-with-Documents.patch
%patch25 -p1 -b .font-model-install-file-monitors-on-fontconfig-font-directories.patch
%patch26 -p1 -b .refresh-Install-button-appearance-when-model-changes.patch
%patch27 -p1 -b .font-model-add-API-to-get-an-iter-from-a-FT_Face.patch
%patch28 -p1 -b .match-the-font-face-when-getting-an-iter-to-update-the-button.patch
%patch29 -p1 -b .font-model-set-a-fallback-icon-if-we-fail-to-read-the-thumbnail.patch
%patch30 -p1 -b .main-toolbar-another-sync-with-Documents.patch
%patch31 -p1 -b .do-not-hardcode-fonts-hone-dir-as-target-install-directory
%patch32 -p1 -b .font-model-do-not-use-sync-g_file_query_info
%patch33 -p1 -b .font-model-use-g_io_scheduler_push_job-to-refactor-thumbnailing-code
%patch34 -p1 -b .font-model-use-g_utf8_collation_key-to-sort-the-model
%patch35 -p1 -b .font-widget-one-more-sync-from-Sushi
%patch36 -p1 -b .font-model-cache-the-fallback-icon-in-the-private-struct
%patch37 -p1 -b .font-model-cache-tree-iters-when-setting-values-on-the-model
%patch38 -p1 -b .font-model-use-a-single-IO-scheduler-job-to-load-thumbnail-images
%patch39 -p1 -b .font-model-load-font-names-asynchronously
%patch40 -p1 -b .set-an-empty-title-on-the-info-dialog
%patch41 -p1 -b .font-model-cancel-previous-loading-when-refreshing-font-list
%patch42 -p1 -b .font-model-actually-cancel-the-thread-when-rebuilding-font-list
%patch43 -p1 -b .font-model-emit-config-changed-when-reloading-the-font-list
%patch44 -p1 -b .font-view-show-an-error-dialog-when-unable-to-load-a-font
%patch45 -p1 -b .next-sync-from-Sushi
%patch46 -p1 -b .do-not-crash-when-opening-a-non-existing-file
%patch47 -p1 -b .font-view-return-early-if-we-have-a-model-already
%patch48 -p1 -b .thumnailer-do-not-paint-a-white-background-under-thumbnails
%patch49 -p1 -b .do-not-call-g_type_init
%patch50 -p1 -b .font-widget-next-2-sync-from-sushi
%patch51 -p1 -b .font-widget-next-3-sync-from-sushi
%patch52 -p1 -b .font-model-drop-gtk_icon_info_free
%patch53 -p1 -b .font-view-add-a-title-to-the-info-dialog
%patch54 -p1 -b .fix-an-uninitialized-variable
%patch55 -p1 -b .deprecated-gtk_misc_set_alignment-and-margin-left-right
%patch56 -p1 -b .replace-deprecated-method-with-main-context-invocation
%patch57 -p1 -b .ported-thumbnailing-io-scheduler-job-to-g_task_run_in_thread
%patch58 -p1 -b .replace-io-scheduler-with-g_task_run_in_thread-in-load_font-infos
%patch59 -p1 -b .sushi-font-loader-sync-from-sushi
%patch60 -p1 -b .gd-toolbar-sync-to-latest-libgd-suitable-for-mate
%patch61 -p1 -b .add-style-class-font-viewer
# end fontviewer

autoreconf -fi

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}
%patch62 -p1
%patch63 -p1

%build
autoreconf -fisv
%configure                           \
           --disable-static          \
           --disable-schemas-compile \
           --disable-update-mimedb   \
           --with-gtk=3.0

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

desktop-file-install                                \
    --delete-original                               \
    --dir=%{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/*.desktop

# delete mime cache
rm %{buildroot}%{_datadir}/applications/mimeinfo.cache

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%config %{_sysconfdir}/xdg/menus/matecc.menu
%{_bindir}/mate-*
%{_libdir}/libmate-window-settings.so.*
%{_libdir}/window-manager-settings
%{_libdir}/libmate-slab.so.*
%{_sbindir}/mate-display-properties-install-systemwide
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/matecc.directory
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-*.svg
%{_datadir}/glib-2.0/schemas/org.mate.*.xml
%{_datadir}/mate-control-center/*
%{_datadir}/mate/cursor-fonts/*.pcf
%{_datadir}/mime/packages/mate-theme-package.xml
%{_datadir}/thumbnailers/mate-font-viewer.thumbnailer
%{_datadir}/polkit-1/actions/org.mate.randr.policy
%{_mandir}/man1/mate-*.1.*
# %%files filesystem
%dir %{_datadir}/mate-control-center
%dir %{_datadir}/mate-control-center/keybindings

%files devel
%{_includedir}/mate-window-settings-2.0
%{_libdir}/pkgconfig/mate-window-settings-2.0.pc
%{_libdir}/libmate-window-settings.so
%{_libdir}/pkgconfig/mate-default-applications.pc
%{_libdir}/pkgconfig/mate-keybindings.pc
%{_includedir}/libmate-slab/
%{_libdir}/libmate-slab.so
%{_libdir}/pkgconfig/mate-slab.pc


%changelog
* Thu Oct 06 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.16.0-alt1_1
- update to mate 1.16

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_2
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.10.2-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.10.2-alt1_1
- new version

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1-alt2_1
- new fc release

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1-alt2_0
- use gnome-keyring

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1-alt1_0
- new fc release
- TODO: drop mate-keyring

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_2
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_1
- new fc release

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.5-alt1_3
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.4-alt1_1
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.3-alt1_3
- new fc release

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.2-alt1_1
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- use F19 import base

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1.1.1
- rebuild with new libmatekbd

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted background-location and passwd alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

