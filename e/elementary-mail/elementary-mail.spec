%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.mail

Name: elementary-mail
Version: 8.0.1
Release: alt1

Summary: Mail app designed for elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/mail

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(camel-1.2)
BuildRequires: pkgconfig(webkit2gtk-4.1)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk3)
BuildRequires: pkgconfig(folks)
BuildRequires: vapi(folks)
BuildRequires: vapi(granite)

%description
Mail is an email client built for elementary's Pantheon desktop environment. It allows you to read and send email with a simple,
modern interface.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %appname.lang
%doc COPYING README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml
%_sysconfdir/apparmor.d/io.elementary.mail
%dir %_libdir/io.elementary.mail
%dir %_libdir/io.elementary.mail/webkit2
%_libdir/io.elementary.mail/webkit2/libio.elementary.mail-webkit-extension.so

%changelog
* Fri Nov 14 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- New version 8.0.1.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.0-alt2
- Fixed build with modern libcamel

* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.0-alt1
- Initial build for Sisyphus
