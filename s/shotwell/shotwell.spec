%set_verify_elf_method unresolved=relaxed
%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Shotwell

%def_enable face_detection
%def_enable check

%define ver_major 0.31
%define api_ver 1.0
%define gst_api_ver 1.0

Name: shotwell
Version: %ver_major.6
Release: alt1

Summary: digital photo organizer designed for the GNOME desktop environment
Group: Graphics
License: CC-BY-SA-3.0 and LGPL-2.1-or-later
Url: https://wiki.gnome.org/Apps/Shotwell

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: %name-0.31.3-alt-no-dark-theme-by-default.patch

%define gtk_ver 3.22
%define gexiv_ver 0.12.1
%define soup3_ver 3.0
%define webkit_api_ver 4.1

Requires: dconf
# for video-thumbnailer
Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver gst-libav

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: desktop-file-utils yelp-tools /usr/bin/appstream-util
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libsoup-3.0) >= %soup3_ver
BuildRequires: gstreamer%gst_api_ver-devel gst-plugins%gst_api_ver-devel
BuildRequires: libdconf-devel libdbus-glib-devel libgexiv2-devel >= %gexiv_ver
BuildRequires: libwebp-devel libgphoto2-devel libgudev-devel libjson-glib-devel
BuildRequires: libraw-devel libexif-devel libgomp-devel libavif-devel
BuildRequires: libsqlite3-devel libstdc++-devel pkgconfig(webkit2gtk-%webkit_api_ver)
BuildRequires: libgee0.8-devel gcr-libs-devel gcr-libs-vala
BuildRequires: libgdata-devel libchamplain-gtk3-devel
BuildRequires: libsecret-devel
BuildRequires: libportal-devel libportal-gtk3-devel
%{?_enable_face_detection:BuildRequires: gcc-c++ libopencv-devel}
%{?_enable_check:BuildRequires: python3 dbus}

%description
Shotwell is a digital photo organizer designed for the GNOME desktop
environment.  It allows you to import photos from disk or camera,
organize them in various ways, view them in full-window or fullscreen
mode, and export them to share with others.


%prep
%setup
%patch -b .no_dark_theme
%build
%add_optflags -D_GIT_VERSION=%(echo %version | tr -d .)
%define vala_ver %(rpm -q --qf '%%{VERSION}' vala)
%if "%(rpmvercmp %vala_ver 0.54)" <= "0"
%add_optflags -DEXPORT_DIALOG_DEFAULT_SCALE=1200
%endif
%meson -Dunity_support=false \
       -Dinstall_apport_hook=false \
       %{?_enable_face_detection:-Dface_detection=true}
%nil
#%%meson_build %name-pot %name-update-po
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name %name-extras

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name-video-thumbnailer
%if_enabled face_detection
%_libexecdir/%name/%name-facedetect
%_datadir/dbus-1/services/%xdg_name.Faces1.service
%dir %_datadir/%name
%_datadir/%name/facedetect-haarcascade.xml
%endif
%_libdir/lib%name-plugin-common.so.*
%_libdir/lib%name-plugin-dev-%api_ver.so.*
%_libdir/lib%name-authenticator.so.*

%exclude %_libdir/lib%name-*.so

%_libdir/%name/
%_desktopdir/%{xdg_name}*.desktop
%_iconsdir/hicolor/*x*/apps/%xdg_name.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/glib-2.0/schemas/*
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS COPYING NEWS README* THANKS


%changelog
* Sat Dec 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.31.6-alt1
- 0.31.6

* Tue Jul 19 2022 Yuri N. Sedunov <aris@altlinux.org> 0.31.5-alt1
- 0.31.5 (ported to libsoup-3.0/webkit2gtk-4.1)

* Tue Jun 21 2022 Yuri N. Sedunov <aris@altlinux.org> 0.31.4-alt1
- 0.31.4

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.31.3-alt3.1
- fixed build with meson >= 0.61

* Wed Jan 26 2022 Yuri N. Sedunov <aris@altlinux.org> 0.31.3-alt3
- org.gnome.shotwell.gschema.xml: use-dark-theme = false (ALT #41805)

* Mon Jan 24 2022 Yuri N. Sedunov <aris@altlinux.org> 0.31.3-alt2.2
- fixed build with vala < 0.54 for p10

* Tue Dec 14 2021 Yuri N. Sedunov <aris@altlinux.org> 0.31.3-alt2.1
- fixed build with vala-0.52.8 for p10

* Sat Dec 11 2021 Yuri N. Sedunov <aris@altlinux.org> 0.31.3-alt2
- updated to shotwell-0.31.3-111-gaf5a7ae0

* Wed Dec 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.31.3-alt1
- 0.31.3

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.31.2-alt1
- 0.31.2

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 0.31.1-alt1
- updated to 0.31.1-35-g15004a41
- enabled check

* Fri Jan 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.30.8-alt1
- 0.30.8
- fixed License tag

* Tue Aug 20 2019 Yuri N. Sedunov <aris@altlinux.org> 0.30.7-alt1
- 0.30.7

* Tue Aug 20 2019 Yuri N. Sedunov <aris@altlinux.org> 0.30.6-alt1
- 0.30.6

* Wed Aug 14 2019 Yuri N. Sedunov <aris@altlinux.org> 0.30.5-alt1
- 0.30.5

* Wed Jul 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.30.4-alt2
- updated to 0.30.4-5-gdc6ca6a9 with fresh russian translation (ALT #36853)

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.30.4-alt1
- 0.30.4

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 0.30.2-alt2
- updated to 0.30.2-9-gd03b4777
- backported "publishing: Fix references to GLib.BindingFlags"

* Thu Feb 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.30.2-alt1
- 0.30.2

* Sat Sep 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt1
- 0.30.1

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt2
- enabled face detection

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.29.92-alt2
- rebuilt against libraw.so.19

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.29.92-alt1
- 0.29.92

* Sat Jul 14 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.4-alt1
- 0.28.4

* Fri May 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.3-alt1.1
- fixed buildreqs

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.3-alt1
- 0.28.3

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Sun Mar 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 0.28.0

* Mon Feb 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.27.4-alt1
- 0.27.4

* Wed Jan 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.27.3-alt1
- 0.27.3

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.27.2-alt1
- 0.27.2

* Sat Oct 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.27.1-alt1
- 0.27.1

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.3-alt1
- 0.26.3

* Thu Jun 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.2-alt1
- 0.26.2

* Wed Apr 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Tue Feb 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25.5-alt1
- 0.25.5

* Wed Feb 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25.4-alt1
- 0.25.4

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25.3-alt1
- 0.25.3

* Tue Jan 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt4
- updated buildreqs

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt3
- rebuilt against libraw.so.16

* Wed Dec 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt2
- rebuilt from vala sources to avoid crash

* Mon Dec 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt1
- 0.25.2

* Mon Nov 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.1-alt1
- 0.25.1

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.0.1-alt1
- 0.25.0.1

* Mon Oct 24 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Sun Oct 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt1
- 0.24.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.1-alt1
- 0.23.1

* Tue Apr 26 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0

* Sat Apr 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.22.1-alt1
- 0.22.1

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt2
- rebuilt against libraw.so.15

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt2
- rebuilt against libgphoto2_port.so.12

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Sat Nov 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Fri Oct 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Sat Sep 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Wed Jul 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Wed Mar 19 2014 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.17.1-alt1
- 0.17.1

* Wed Feb 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0 snapshot (6321cbf4)

* Tue Jan 21 2014 Vladimir Lettiev <crux@altlinux.ru> 0.15.1-alt2
- rebuilt with libraw 0.16.0

* Sat Dec 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Tue Apr 09 2013 Vladimir Lettiev <crux@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Fri Jan 25 2013 Vladimir Lettiev <crux@altlinux.ru> 0.13.1-alt2
- rebuilt with libgexiv2 0.5.0

* Tue Oct 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Thu Sep 20 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Jun 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.3-alt1
- 0.12.3
- build with new shared libraw

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Wed Jan 25 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11.99-alt2
- git snapshot d867f19

* Thu Nov 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.99-alt1
- git snapshot c1f9e00

* Wed Oct 19 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.5-alt1
- 0.11.5

* Fri Oct 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.4-alt1
- 0.11.4

* Wed Oct 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.3-alt1
- 0.11.3

* Fri Oct 07 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.2-alt1
- 0.11.2
- Source cloned from upstream git
- No longer need to install or compile GConf schemas (b3d5985d)

* Wed Sep 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11.0-alt2
- Dependance on dconf added.

* Wed Aug 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11.0-alt1
- New version 0.11.0
- shotwell-plugins-mk.patch deleted

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.10.1-alt1
- New version 0.10.1
- Fixed plugins linking
- Dropped shotwell-0.9.1-vala.patch

* Thu May 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt3
- fixed build with vala-0.10.4 (4c74b5c)

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.8.1-alt2
- Rebuilt with libraw 0.13.1

* Wed Jan 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.8.1-alt1
- New version 0.8.1

* Fri Dec 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.8.0-alt1
- New version 0.8.0
- Updated buildrequires

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7.2-alt2
- Rebuilt with libraw 0.11.3

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7.2-alt1
- New version 0.7.2

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.6.1-alt1
- New version 0.6.1

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5.2-alt1
- New version 0.5.2

* Wed Mar 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5.0-alt1
- new version 0.5.0

* Tue Mar 16 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.3-alt1
- initial build

