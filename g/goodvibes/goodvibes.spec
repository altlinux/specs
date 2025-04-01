%define xdg_name io.gitlab.Goodvibes

%def_with docs

Name: goodvibes
Version: 0.8.2
Release: alt1

Summary: A Lightweight Radio Player

License: GPLv3
Group: Sound
URL: https://gitlab.com/goodvibes/goodvibes
VCS: https://gitlab.com/goodvibes/goodvibes.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: cmake
BuildRequires: gst-plugins1.0-devel
BuildRequires: libkeybinder3-devel
BuildRequires: libsoup3.0-devel
BuildRequires: meson

%if_with docs
BuildRequires: python3-module-sphinx_rtd_theme
%endif

%description
Goodvibes is a lightweight internet radio player for GNU/Linux. Save your
favorite stations, play it, that's it.

There is no function to search radio stations, you'll have to enter the URL of
the audio stream by yourself. Not very user-friendly, I know, but doing better
than that is not simple.

%package docs
Summary: Documentation for Goodvibes
Group: Documentation
BuildArch: noarch

%description docs
Goodvibes is a lightweight internet radio player for GNU/Linux. Save your
favorite stations, play it, that's it.

This package contains documentation for Goodvibes.

%prep
%setup

%build
%meson -Dtests=false
%meson_build

%if_with docs
%make -C docs/%name.readthedocs.io html
# remove the sphinx-build leftovers
rm -rv docs/%name.readthedocs.io/_build/html/{.buildinfo,objects.inv}
%endif

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc COPYING NEWS *.md
%_bindir/%name
%_bindir/%name-client
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.*.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/%{name}*.1.*
# ALT bug 48467: find-lang skips zh_Hant
# https://bugzilla.altlinux.org/48467
%_datadir/locale/zh_Hant/LC_MESSAGES/%name.mo

%if_with docs
%files docs
%doc docs/%name.readthedocs.io/_build/html
%endif

%changelog
* Sat Mar 29 2025 Alexander Kovalev <alexvk@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Wed Feb 05 2025 Alexander Kovalev <alexvk@altlinux.org> 0.8.1-alt1
- Initial build for ALT.
