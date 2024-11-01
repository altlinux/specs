%define APP_ID com.mardojai.ForgeSparks
%def_enable check

Name: forge-sparks
Version: 0.4.0
Release: alt1

Summary: Get Git forges notifications
License: MIT
Group: Graphical desktop/GNOME

Url: https://github.com/rafaelmardojai/forge-sparks
Vcs: https://github.com/rafaelmardojai/forge-sparks/issues
Source0: %name-%version.tar
Source1: troll.tar

Requires: typelib(XdpGtk4)

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: libgjs-devel
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

BuildArch: noarch

%description
Simple notifier app with support for GitLab, Github, Gitea and Forgejo.

%prep
%setup -a1

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%__meson_test

%files -f %APP_ID.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/%APP_ID
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_iconsdir/hicolor/*/status/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Sat Oct 26 2024 Oleg Shchavelev <oleg@altlinux.org> 0.4.0-alt1
- Initial build
