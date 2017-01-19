%define commit 0350b1a96472e52fdf64b106a9ead50e09c16f4b

Name: pdfpc
Version: 4.0.5.0.18.g0350b1a
Release: alt1
Summary: A GTK based presentation viewer application for GNU/Linux

Group: Other
License: GPLv2+
Url: https://github.com/pdfpc/pdfpc
# Repacked %url/archive/%commit.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Mon Oct 03 2016
# optimized out: at-spi2-atk cmake-modules fontconfig glib2-devel gstreamer1.0-devel libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgst-plugins1.0 libpango-devel libpoppler8-glib libwayland-client libwayland-cursor libwayland-egl libwayland-server pkg-config python-base python-modules xorg-xproto-devel
BuildRequires: cmake gst-plugins1.0-devel libgee0.8-devel libgtk+3-devel libpoppler-glib-devel vala

Provides: pdf-presenter-console

%description
pdfpc is a GTK based presentation viewer application for GNU/Linux which
uses Keynote like multi-monitor output to provide meta information to
the speaker during the presentation. It is able to show a normal
presentation window on one screen, while showing a more sophisticated
overview on the other one providing information like a picture of the
next slide, as well as the left over time till the end of the
presentation. The input files processed by pdfpc are PDF documents,
which can be created using nearly any of today's presentation software.

%prep
%setup

%build
%cmake \
	-DSYSCONFDIR=/etc \
	#
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.rst CHANGELOG.txt
%_bindir/%name
%config(noreplace) %_sysconfdir/%{name}rc
%_mandir/man1/%{name}*
%_mandir/man5/%{name}*
%_datadir/pixmaps/%name

%changelog
* Thu Jan 19 2017 Elvira Khabirova <lineprinter@altlinux.org> 4.0.5.0.18.g0350b1a-alt1
- New version 4.0.5-18-g0350b1a.

* Tue Oct 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.3-alt1
- Initial build.
