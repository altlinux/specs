%define ver_major 2.0
%define ver_api 2.0
%define _libexecdir %_prefix/libexec

Name: tracker-miners
Version: %ver_major.3
Release: alt1

Summary: Tracker is a powerfull desktop-oriented search tool and indexer
License: GPLv2+
Group: Office
Url: http://wiki.gnome.org/Projects/Tracker

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz


%def_enable libxml2
%def_enable rss
%def_enable poppler
%def_enable libgxps
%def_enable libexif
%def_enable libiptcdata
%def_enable libgsf
%def_enable libjpeg
%def_enable libtiff
%def_enable libpng
%def_enable libvorbis
%def_enable libflac
%def_enable exempi
%def_enable taglib
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

%define libxml2_ver 2.6
%define poppler_ver 0.16.0
%define vorbis_ver 0.22
%define flac_ver 1.2.1
%define libexif_ver 0.6
%define libgsf_ver 1.14.24
%define exempi_ver 2.1.0
%define gee_ver 0.3
%define taglib_ver 1.6
%define libgrss_ver 0.7
%define rest_ver 0.7
%define libosinfo_ver 0.2.9
%define libpng_ver 0.89
%define gst_ver 1.10

# mediaextractor (gstreamer|libav|mplayer|external)
%define generic_media_extractor gstreamer
BuildRequires: gstreamer1.0-devel >= %gst_ver gst-plugins1.0-devel >= %gst_ver

BuildRequires: meson intltool rpm-build-xdg
BuildRequires: tracker-devel >= %ver_major
BuildRequires:  libupower-devel libstemmer-devel libicu-devel libenca-devel libseccomp-devel
BuildRequires: libavformat-devel >= 0.8.4 libavcodec-devel libavutil-devel
%{?_enable_libxml2:BuildPreReq: libxml2-devel >= %libxml2_ver}
%{?_enable_rss:BuildPreReq: libgrss-devel >= %libgrss_ver}
%{?_enable_libpng:BuildPreReq: libpng-devel >= %libpng_ver}
%{?_enable_poppler:BuildPreReq: libpoppler-glib-devel >= %poppler_ver}
%{?_enable_libgxps:BuildPreReq: libgxps-devel}
%{?_enable_libexif:BuildPreReq: libexif-devel >= %libexif_ver}
%{?_enable_libiptcdata:BuildPreReq: libiptcdata-devel}
%{?_enable_libgsf:BuildPreReq: libgsf-devel >= %libgsf_ver}
%{?_enable_libjpeg:BuildPreReq: libjpeg-devel}
%{?_enable_libtiff:BuildPreReq: libtiff-devel}
%{?_enable_libvorbis:BuildPreReq: libvorbis-devel >= %vorbis_ver}
%{?_enable_libvorbis:BuildPreReq: libflac-devel >= %flac_ver}
%{?_enable_exempi:BuildPreReq: libexempi-devel >= %exempi_ver}
%{?_enable_taglib:BuildPreReq: libtag-devel >= %taglib_ver}
%{?_enable_gtk_doc:BuildPreReq: gtk-doc docbook-utils graphviz}
%{?_enable_libgif:BuildPreReq: libgif-devel}
%{?_enable_libcue:BuildPreReq: libcue-devel}
%{?_enable_libosinfo:BuildPreReq: libosinfo-devel >= %libosinfo_ver}
%{?_enable_playlist:BuildPreReq: libtotem-pl-parser-devel}

%description
Tracker is a powerful desktop-neutral first class object
database, tag/metadata database, search tool and indexer.

This package provides miners for TRacker.


%prep
%setup

%build
%configure \
	--enable-generic-media-extractor=%generic_media_extractor \
	--disable-static \
	%{subst_enable libxml2} \
	%{?_enable_rss:--enable-miner-rss} \
	%{subst_enable taglib} \
	%{subst_enable poppler} \
	%{subst_enable libgxps} \
	%{subst_enable libexif} \
	%{subst_enable libiptcdata} \
	%{subst_enable libgsf} \
	%{subst_enable libjpeg} \
	%{subst_enable libtiff} \
	%{subst_enable libgif} \
	%{subst_enable libpng} \
	%{subst_enable libvorbis} \
	%{subst_enable libflac} \
	%{subst_enable exempi} \
	%{subst_enable libcue} \
	%{subst_enable abiword} \
	%{subst_enable dvi} \
	%{subst_enable mp3} \
	%{subst_enable ps} \
	%{subst_enable text} \
	%{subst_enable icon} \
	%{subst_enable libosinfo} \
	%{subst_enable playlist}
%make_build

%install
%makeinstall_std
%find_lang %name


%files -f %name.lang

%_xdgconfigdir/autostart/tracker-extract.desktop
%_xdgconfigdir/autostart/tracker-miner-apps.desktop
%_xdgconfigdir/autostart/tracker-miner-fs.desktop
%_xdgconfigdir/autostart/tracker-miner-rss.desktop
%_libdir/%name-%ver_api/
%_libexecdir/tracker-extract
%_libexecdir/tracker-miner-fs
%_libexecdir/tracker-writeback
%_libexecdir/tracker-miner-apps
%{?_enable_rss:%_libexecdir/tracker-miner-rss}
%_man1dir/tracker-miner-fs.*
%{?_enable_rss:%_man1dir/tracker-miner-rss.1.*}
%_datadir/tracker/miners/
%_datadir/%name/extract-rules/
%_prefix/lib/systemd/user/tracker-extract.service
%_prefix/lib/systemd/user/tracker-miner-apps.service
%_prefix/lib/systemd/user/tracker-miner-fs.service
%_prefix/lib/systemd/user/tracker-miner-rss.service
%_prefix/lib/systemd/user/tracker-writeback.service
%_man1dir/tracker-extract.*
%_man1dir/tracker-writeback.*

%_datadir/dbus-1/services/org.freedesktop.Tracker1.Miner.Applications.service
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Miner.Extract.service
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Miner.RSS.service
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Writeback.service
%_datadir/glib-2.0/schemas/org.freedesktop.Tracker.Extract.gschema.xml
%_datadir/glib-2.0/schemas/org.freedesktop.Tracker.Miner.Files.gschema.xml
%_datadir/glib-2.0/schemas/org.freedesktop.Tracker.Writeback.gschema.xml
%_datadir/glib-2.0/schemas/org.freedesktop.TrackerMiners.enums.xml

%exclude %_datadir/tracker-tests/01-writeback.py


%changelog
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

