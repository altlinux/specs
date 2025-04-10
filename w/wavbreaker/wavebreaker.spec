%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name wavbreaker
%define ver_major 0.16
%define rdn_name net.sourceforge.%_name

%def_enable check

Name: %_name
Version: %ver_major
Release: alt1

Summary: WAV and MP3 file splitter
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later
Url: https://wavbreaker.sourceforge.io

Vcs: https://github.com/thp/wavbreaker.git

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: %url/archive/%version/%_name-%version.tar.gz
%endif

%define gtk_ver 3.22

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: pkgconfig(ao)
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(libcue)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
This application's purpose in life is to take a WAV file and break it up
into multiple WAV files. It makes a clean break at the correct position
to burn the files to an Audio CD without any dead air between the
tracks.

wavbreaker now also directly supports breaking up MP3s without
re-encoding meaning it's fast and there is no generational loss.
Decoding (using mpg123) is only done for playback and waveform display.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name

%check
%__meson_test -v

%files -f %name.lang
%_bindir/%_name
%_bindir/wavcli
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%_man1dir/*
%doc README*

%changelog
* Thu Apr 10 2025 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- first build for Sisyphus (0.16-9-g243dcb9)

