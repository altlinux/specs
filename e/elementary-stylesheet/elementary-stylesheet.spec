%define _unpackaged_files_terminate_build 1

Name: elementary-stylesheet
Version: 8.2.2
Release: alt1

Summary: GTK Stylesheet for elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/stylesheet

Source: %name-%version.tar

BuildRequires(pre): meson

BuildRequires: sassc

BuildArch: noarch

%description
The official elementary GTK stylesheet.
Supports GTK versions 2 and 3.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc CONTRIBUTING.md COPYING README.md
%_datadir/metainfo/io.elementary.stylesheet.appdata.xml
%dir %_datadir/themes/io.elementary.stylesheet.banana
%_datadir/themes/io.elementary.stylesheet.banana/*
%dir %_datadir/themes/io.elementary.stylesheet.blueberry
%_datadir/themes/io.elementary.stylesheet.blueberry/*
%dir %_datadir/themes/io.elementary.stylesheet.bubblegum
%_datadir/themes/io.elementary.stylesheet.bubblegum/*
%dir %_datadir/themes/io.elementary.stylesheet.cocoa
%_datadir/themes/io.elementary.stylesheet.cocoa/*
%dir %_datadir/themes/io.elementary.stylesheet.grape
%_datadir/themes/io.elementary.stylesheet.grape/*
%dir %_datadir/themes/io.elementary.stylesheet.latte
%_datadir/themes/io.elementary.stylesheet.latte/*
%dir %_datadir/themes/io.elementary.stylesheet.lime
%_datadir/themes/io.elementary.stylesheet.lime/*
%dir %_datadir/themes/io.elementary.stylesheet.mint
%_datadir/themes/io.elementary.stylesheet.mint/*
%dir %_datadir/themes/io.elementary.stylesheet.orange
%_datadir/themes/io.elementary.stylesheet.orange/*
%dir %_datadir/themes/io.elementary.stylesheet.slate
%_datadir/themes/io.elementary.stylesheet.slate/*
%dir %_datadir/themes/io.elementary.stylesheet.strawberry
%_datadir/themes/io.elementary.stylesheet.strawberry/*

%changelog
* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 8.2.2-alt1
- Initial build for Sisyphus
