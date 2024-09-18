%define _name localsearch
%define old_name tracker-miners
%define ver_major 3.8
%define beta %nil
%define api_ver_major 3
%define api_ver %api_ver_major.0
%define xdg_name org.freedesktop.Tracker%api_ver_major
%define rdn_name org.freedesktop.LocalSearch%api_ver_major
%define _libexecdir %_prefix/libexec

Name: %_name
Version: %ver_major.0
Release: alt1%beta

Summary: Tracker is a powerfull desktop-oriented search tool and indexer
License: GPL-2.0-or-later and LGPL-2.0-or-later
Group: Databases
Url: https://wiki.gnome.org/Projects/Tracker

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz

%add_python3_path %_libdir/%_name-%api_ver/

%def_enable xml
%def_enable rss
%def_enable poppler
%def_enable libgxps
%def_enable libexif
%def_enable libiptcdata
%def_enable libgsf
%def_enable libjpeg
%def_enable libtiff
%def_enable libpng
%def_enable raw
%def_enable libvorbis
%def_enable libflac
%def_enable exempi
%def_enable libgif
%def_enable libcue
%def_enable abiword
%def_enable dvi
%def_enable mp3
%def_enable ps
%def_enable text
%def_enable icon
%def_enable libosinfo
%def_enable playlist
%def_enable network_manager
#Has header "linux/landlock.h" : YES 
#Checking if "landlock is enabled in kernel" runs: NO (1)
#meson.build:210:4: ERROR: Problem encountered: Landlock was auto-enabled in build options, but is disabled in the kernel
%def_disable landlock
%def_enable man

%define glib_ver 2.62
%define libxml2_ver 2.6
%define poppler_ver 0.16.0
%define vorbis_ver 0.22
%define flac_ver 1.2.1
%define libexif_ver 0.6
%define libgsf_ver 1.14.24
%define exempi_ver 2.1.0
%define gee_ver 0.3
%define libgrss_ver 0.7
%define rest_ver 0.7
%define libosinfo_ver 0.2.9
%define libpng_ver 0.89
%define libcue_ver 2.0.0
%define gst_ver 1.10
%define libav_ver 0.8.4

Obsoletes: tracker%api_ver_major-miners < %ver_major
Obsoletes: %old_name%api_ver_major < %ver_major
Provides: tracker%api_ver_major-miners = %EVR
Provides: %old_name%api_ver_major = %EVR

# mediaextractor (gstreamer|libav|mplayer|external)
%define generic_media_extractor gstreamer
BuildRequires: gstreamer1.0-devel >= %gst_ver gst-plugins1.0-devel >= %gst_ver

BuildRequires(pre): rpm-macros-meson rpm-build-xdg rpm-build-systemd rpm-build-gir rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: tinysparql-devel >= %ver_major
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libupower-devel libstemmer-devel libicu-devel
BuildRequires: libenca-devel libseccomp-devel libdbus-devel
BuildRequires: pkgconfig(systemd) pkgconfig(blkid)
BuildRequires: libavformat-devel >= %libav_ver libavcodec-devel libavutil-devel
BuildRequires: gobject-introspection-devel
# discoverer
BuildRequires: pkgconfig(gupnp-dlna-gst-2.0)
%{?_enable_xml:BuildRequires: libxml2-devel >= %libxml2_ver}
%{?_enable_rss:BuildRequires: libgrss-devel >= %libgrss_ver}
%{?_enable_libpng:BuildRequires: libpng-devel >= %libpng_ver}
%{?_enable_raw:BuildRequires: libgexiv2-devel}
%{?_enable_poppler:BuildRequires: libpoppler-glib-devel >= %poppler_ver}
%{?_enable_libgxps:BuildRequires: libgxps-devel}
%{?_enable_libexif:BuildRequires: libexif-devel >= %libexif_ver}
%{?_enable_libiptcdata:BuildRequires: libiptcdata-devel}
%{?_enable_libgsf:BuildRequires: libgsf-devel >= %libgsf_ver}
%{?_enable_libjpeg:BuildRequires: libjpeg-devel}
%{?_enable_libtiff:BuildRequires: libtiff-devel}
%{?_enable_libvorbis:BuildRequires: libvorbis-devel >= %vorbis_ver}
%{?_enable_libvorbis:BuildRequires: libflac-devel >= %flac_ver}
%{?_enable_exempi:BuildRequires: libexempi-devel >= %exempi_ver}
%{?_enable_libgif:BuildRequires: libgif-devel}
%{?_enable_libcue:BuildRequires: libcue-devel >= %libcue_ver }
%{?_enable_libosinfo:BuildRequires: libosinfo-devel >= %libosinfo_ver}
%{?_enable_playlist:BuildRequires: libtotem-pl-parser-devel}
%{?_enable_network_manager:BuildRequires: libnm-devel}
%{?_enable_man:BuildRequires: asciidoc-a2x xsltproc}

%description
Tracker is a powerful desktop-neutral first class object
database, tag/metadata database, search tool and indexer.

This package provides miners for TRacker.

%prep
%setup -n %_name-%version%beta
# fix install_rpath for modules
find src/ -name "meson.build" -print0 | xargs -r0 \
sed -i 's/tracker_install_rpath/tracker_internal_libs_dir/' --

%build
%meson \
	-Dgeneric_media_extractor='%generic_media_extractor' \
	%{?_enable_xml:-Dxml=enabled} \
	%{?_enable_rss:-Dminer_rss=true} \
	%{?_enable_poppler:-Dpdf=enabled} \
	%{?_enable_libgxps:-Dxps=enabled} \
	%{?_enable_libexif:-Dexif=enabled} \
	%{?_enable_libiptcdata:-Diptc=enabled} \
	%{?_enable_libgsf:-Dgsf=enabled} \
	%{?_enable_libjpeg:-Djpeg=enabled} \
	%{?_enable_libtiff:-Dtiff=enabled} \
	%{?_enable_libgif:-Dgif=enabled} \
	%{?_enable_libpng:-Dpng=enabled} \
	%{?_enable_raw:-Draw=enabled} \
	%{?_enable_exempi:-Dxmp=enabled} \
	%{?_enable_libcue:-Dcue=enabled} \
	%{?_enable_abiword:-Dabiword=true} \
	%{?_enable_mp3:-Dmp3=true} \
	%{?_enable_ps:-Dps=true} \
	%{?_enable_text:-Dtext=true} \
	%{?_enable_icon:-Dicon=true} \
	%{?_enable_libosinfo:-Diso=enabled} \
	%{?_enable_playlist:-Dplaylist=enabled} \
	%{subst_enable_meson_feature landlock landlock} \
	%{?_disable_man:-Dman=false} \
	-Dsystemd_user_services_dir='%_userunitdir'
%nil
%meson_build

%install
%meson_install
ln -sf %_name-%api_ver/libtracker-extract.so \
%buildroot%_libdir/libtracker-extract.so

%find_lang %name%api_ver_major

%files -f %name%api_ver_major.lang
%_xdgconfigdir/autostart/%name-%api_ver_major.desktop
%_xdgconfigdir/autostart/tracker-miner-rss-%api_ver_major.desktop
%_bindir/%name
%_libdir/%_name-%api_ver/
# symlink
%_libdir/libtracker-extract.so
%_libexecdir/%name-%api_ver_major
%_libexecdir/%name-control-%api_ver_major
%_libexecdir/%name-extractor-%api_ver_major
%_libexecdir/%name-writeback-%api_ver_major
%{?_enable_rss:%_libexecdir/tracker-miner-rss-%api_ver_major}
%_datadir/%name%api_ver_major/
%_userunitdir/%name-%api_ver_major.service
%_userunitdir/%name-control-%api_ver_major.service
%_userunitdir/%name-writeback*.service
%_userunitdir/tracker-miner-rss*.service
%{?_enable_man:
%_man1dir/%name-%{api_ver_major}.1*
%_man1dir/%name-daemon.1*
%_man1dir/%name-extract.1*
%_man1dir/%name-index.1*
%_man1dir/%name-info.1*
%_man1dir/%name-reset.1*
%_man1dir/%name-search.1*
%_man1dir/%name-status.1*
%_man1dir/%name-tag.1*
%_man1dir/%name-writeback-%{api_ver_major}.1*
%_man1dir/tracker-miner-rss-*.*
}
%_datadir/dbus-1/services/%xdg_name.Miner.Files.service
%_datadir/dbus-1/services/%xdg_name.Miner.RSS.service
%_datadir/dbus-1/services/%xdg_name.Writeback.service
%_datadir/dbus-1/services/%xdg_name.Miner.Files.Control.service
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/dbus-1/services/%rdn_name.Control.service
%_datadir/dbus-1/services/%rdn_name.Writeback.service
%_datadir/dbus-1/interfaces/%xdg_name.Miner.xml
%_datadir/dbus-1/interfaces/%xdg_name.Miner.Files.Index.xml

%_datadir/glib-2.0/schemas/%xdg_name.Extract.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.Miner.Files.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.FTS.gschema.xml
%_datadir/glib-2.0/schemas/org.freedesktop.TrackerMiners%api_ver_major.enums.xml

%doc AUTHORS NEWS README*

%changelog
* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0
- tracker-miners -> localsearch

* Thu May 02 2024 Yuri N. Sedunov <aris@altlinux.org> 3.7.3-alt1
- 3.7.3

* Wed Apr 24 2024 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- 3.7.2

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 3.7.1-alt1
- 3.7.1

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt1
- 3.7.0

* Tue Oct 31 2023 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Sat Sep 16 2023 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sat May 13 2023 Yuri N. Sedunov <aris@altlinux.org> 3.5.2-alt1
- 3.5.2

* Tue Apr 25 2023 Yuri N. Sedunov <aris@altlinux.org> 3.5.1-alt1
- 3.5.1

* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- 3.5.0

* Thu Jan 12 2023 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon Dec 05 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Oct 26 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Jun 01 2022 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Mon Mar 07 2022 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1.1
- fixed meson options

* Sun Oct 31 2021 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 03 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.2-alt2
- fixed link tracker-miners-{rss,fs-control} with private libraries (ALT #40639)

* Sat Jun 12 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.2-alt1
- 3.1.2

* Fri Apr 09 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Jan 11 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Wed Dec 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Fri Oct 02 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Sep 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.99.5-alt1
- 2.99.5

* Sat Jun 27 2020 Yuri N. Sedunov <aris@altlinux.org> 2.99.2-alt1
- 2.99.2

* Sun May 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.99.1-alt1
- 2.99.1

* Tue Mar 10 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Tue Mar 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Sat Oct 12 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Fri May 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Thu Mar 07 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sat Feb 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt1
- 2.1.6

* Thu Jan 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.5-alt2
- rebuilt against libexempi.so.8

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.5-alt1
- 2.1.5

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt1
- 2.1.4

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt2
- rebuilt against libicu*.so.62

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt2
- rebuilt against libicu*.so.60

* Wed Nov 15 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Thu Oct 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Tue Aug 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.99.3-alt1
- 1.99.3

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.99.2-alt1
- first build for Sisayphus

