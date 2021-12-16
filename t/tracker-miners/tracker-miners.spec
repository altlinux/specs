%set_verify_elf_method unresolved=relaxed

%define ver_major 2.3
%define ver_api 2.0
%define _libexecdir %_prefix/libexec

Name: tracker-miners
Version: %ver_major.5
Release: alt1.1

Summary: Tracker is a powerfull desktop-oriented search tool and indexer
License: GPL-2.0
Group: Office
Url: http://wiki.gnome.org/Projects/Tracker

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%add_findprov_lib_path %_libdir/%name-%ver_api/

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
%def_enable docs
%def_disable autostart

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
%define gst_ver 1.10

# mediaextractor (gstreamer|libav|mplayer|external)
%define generic_media_extractor gstreamer
BuildRequires: gstreamer1.0-devel >= %gst_ver gst-plugins1.0-devel >= %gst_ver

BuildRequires(pre): meson rpm-build-xdg
BuildRequires: tracker-devel >= %ver_major
BuildRequires: intltool
BuildRequires: libupower-devel libstemmer-devel libicu-devel
BuildRequires: libenca-devel libseccomp-devel libdbus-devel pkgconfig(systemd)
BuildRequires: libavformat-devel >= 0.8.4 libavcodec-devel libavutil-devel
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
%{?_enable_docs:BuildRequires: gtk-doc docbook-utils graphviz}
%{?_enable_libgif:BuildRequires: libgif-devel}
%{?_enable_libcue:BuildRequires: libcue-devel}
%{?_enable_libosinfo:BuildRequires: libosinfo-devel >= %libosinfo_ver}
%{?_enable_playlist:BuildRequires: libtotem-pl-parser-devel}

%description
Tracker is a powerful desktop-neutral first class object
database, tag/metadata database, search tool and indexer.

This package provides miners for TRacker.

%prep
%setup

#fixed install_rpath for modules
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
	%{?_enable_libvorbis:-Dvorbis=enabled} \
	%{?_enable_libflac:-Dflac=enabled} \
	%{?_enable_exempi:-Dxmp=enabled} \
	%{?_enable_libcue:-Dcue=enabled} \
	%{?_enable_abiword:-Dabiword=true} \
	%{?_enable_dvi:-Ddvi=true} \
	%{?_enable_mp3:-Dmp3=true} \
	%{?_enable_ps:-Dps=true} \
	%{?_enable_text:-Dtext=true} \
	%{?_enable_icon:-Dicon=true} \
	%{?_enable_libosinfo:-Diso=enabled} \
	%{?_enable_playlist:-Dplaylist=enabled} \
	%{?_enable_docs:-Ddocs=true} \
	%{?_enable_autostart:-Dautostart=true}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%if_enabled autostart
%_xdgconfigdir/autostart/tracker-extract.desktop
%_xdgconfigdir/autostart/tracker-miner-fs.desktop
%_xdgconfigdir/autostart/tracker-miner-rss.desktop
%endif
%_libdir/%name-%ver_api/
%_libexecdir/tracker-extract
%_libexecdir/tracker-miner-fs
%_libexecdir/tracker-writeback
%{?_enable_rss:%_libexecdir/tracker-miner-rss}
%_man1dir/tracker-miner-fs.*
%{?_enable_rss:%_man1dir/tracker-miner-rss.1.*}
%_datadir/tracker/miners/
%_datadir/%name/extract-rules/
%_prefix/lib/systemd/user/tracker-extract.service
%_prefix/lib/systemd/user/tracker-miner-fs.service
%_prefix/lib/systemd/user/tracker-miner-rss.service
%_prefix/lib/systemd/user/tracker-writeback.service
%_man1dir/tracker-extract.*
%_man1dir/tracker-writeback.*

%_datadir/dbus-1/services/org.freedesktop.Tracker1.Miner.Extract.service
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Miner.RSS.service
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Writeback.service
%_datadir/glib-2.0/schemas/org.freedesktop.Tracker.Extract.gschema.xml
%_datadir/glib-2.0/schemas/org.freedesktop.Tracker.Miner.Files.gschema.xml
%_datadir/glib-2.0/schemas/org.freedesktop.Tracker.Writeback.gschema.xml
%_datadir/glib-2.0/schemas/org.freedesktop.TrackerMiners.enums.xml


%changelog
* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 2.3.5-alt1.1
- fixed meson options

* Mon Sep 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.5-alt1
- 2.3.5

* Tue Aug 25 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

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

