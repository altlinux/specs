%set_verify_elf_method unresolved=relaxed
%define _name tracker-miners
%define ver_major 3.5
%define beta %nil
%define api_ver_major 3
%define api_ver %api_ver_major.0
%define xdg_name org.freedesktop.Tracker%api_ver_major
%define _libexecdir %_prefix/libexec

Name: %_name%api_ver_major
Version: %ver_major.0
Release: alt1%beta

Summary: Tracker is a powerfull desktop-oriented search tool and indexer
License: GPL-2.0 and LGPL-2.1-or-later
Group: Office
Url: https://wiki.gnome.org/Projects/Tracker

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz
# properly link tracker-miners-fs-control with private libraries
Patch: %_name-3.2.0-alt-link.patch

%add_findprov_lib_path %_libdir/%_name-%api_ver_major/

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

Provides: tracker%api_ver_major-miners = %EVR

# mediaextractor (gstreamer|libav|mplayer|external)
%define generic_media_extractor gstreamer
BuildRequires: gstreamer1.0-devel >= %gst_ver gst-plugins1.0-devel >= %gst_ver

BuildRequires(pre): rpm-macros-meson rpm-build-xdg rpm-build-systemd
BuildRequires: meson
BuildRequires: tracker%api_ver_major-devel >= %ver_major
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libupower-devel libstemmer-devel libicu-devel
BuildRequires: libenca-devel libseccomp-devel libdbus-devel
BuildRequires: pkgconfig(systemd) pkgconfig(blkid)
BuildRequires: libavformat-devel >= 0.8.4 libavcodec-devel libavutil-devel
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

%patch -b .link

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
	%{?_disable_man:-Dman=false} \
	-Dsystemd_user_services_dir='%_userunitdir'
%nil
%meson_build

%install
%meson_install
ln -sf %_name-%api_ver/libtracker-extract.so \
%buildroot%_libdir/libtracker-extract.so

%find_lang tracker%api_ver_major-miners

%files -f tracker%api_ver_major-miners.lang
%_xdgconfigdir/autostart/tracker-miner-fs-%api_ver_major.desktop
%_xdgconfigdir/autostart/tracker-miner-rss-%api_ver_major.desktop
%_libdir/%_name-%api_ver/
# symlink
%_libdir/libtracker-extract.so
%_libexecdir/tracker-extract-%api_ver_major
%_libexecdir/tracker-miner-fs-%api_ver_major
%_libexecdir/tracker-writeback-%api_ver_major
%_libexecdir/tracker-miner-fs-control-%api_ver_major
%_libexecdir/tracker%api_ver_major/
%{?_enable_rss:%_libexecdir/tracker-miner-rss-%api_ver_major}
%_datadir/tracker%api_ver_major-miners/
%_prefix/lib/systemd/user/tracker-extract*.service
%_prefix/lib/systemd/user/tracker-miner-fs*.service
%_prefix/lib/systemd/user/tracker-miner-rss*.service
%_prefix/lib/systemd/user/tracker-writeback*.service
%{?_enable_man:
%_man1dir/tracker-miner-fs-*.*
%_man1dir/tracker-miner-rss-*.*
%_man1dir/tracker-writeback-*.*
%_man1dir/tracker%api_ver_major-daemon.1.*
%_man1dir/tracker%api_ver_major-extract.1.*
%_man1dir/tracker%api_ver_major-index.1.*
%_man1dir/tracker%api_ver_major-info.1.*
%_man1dir/tracker%api_ver_major-reset.1.*
%_man1dir/tracker%api_ver_major-search.1.*
%_man1dir/tracker%api_ver_major-status.1.*
%_man1dir/tracker%api_ver_major-tag.1.*
}

%_datadir/dbus-1/services/%xdg_name.Miner.Extract.service
%_datadir/dbus-1/services/%xdg_name.Miner.Files.service
%_datadir/dbus-1/services/%xdg_name.Miner.RSS.service
%_datadir/dbus-1/services/%xdg_name.Writeback.service
%_datadir/dbus-1/services/%xdg_name.Miner.Files.Control.service
%_datadir/dbus-1/interfaces/%xdg_name.Miner.xml
%_datadir/dbus-1/interfaces/%xdg_name.Miner.Files.Index.xml

%_datadir/glib-2.0/schemas/%xdg_name.Extract.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.Miner.Files.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.FTS.gschema.xml
%_datadir/glib-2.0/schemas/org.freedesktop.TrackerMiners%api_ver_major.enums.xml

%doc AUTHORS NEWS README*

%changelog
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

