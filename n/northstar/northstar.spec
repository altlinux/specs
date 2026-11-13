Name: northstar
Version: 1.0.22
Release: alt1

Summary: Small GTK web browser written from scratch in C
License: GPL-3.0-or-later
Group: Networking/WWW
URL: https://nordstjernen.org
VCS: https://github.com/nordstjernen-web/northstar-web-browser

Source: %name-%version.tar

BuildRequires: gcc-c++ meson ninja-build
BuildRequires: pkgconfig(cairo) >= 1.18
BuildRequires: pkgconfig(dav1d)
BuildRequires: pkgconfig(enchant-2)
BuildRequires: pkgconfig(fontconfig) >= 2.15
BuildRequires: pkgconfig(fribidi) >= 1.0.6
BuildRequires: pkgconfig(glib-2.0) >= 2.80
BuildRequires: pkgconfig(gtk4) >= 4.14
BuildRequires: pkgconfig(harfbuzz) >= 8.3
BuildRequires: pkgconfig(lexbor)
BuildRequires: pkgconfig(libavif)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(libseccomp)
BuildRequires: pkgconfig(openh264)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(quickjs-ng)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(uchardet)
BuildRequires: pkgconfig(vpx)

Requires: icon-theme-hicolor

%description
Northstar Web Browser is a clean-room web browser written from scratch in C,
with a GTK 4 user interface and a libcurl network stack. It is built to be
small, secure, and readable by a single person end to end.
* A from-scratch HTML5, CSS, and JavaScript engine -- no forked browser engine.
* One window, one page, one process: the page engine runs in the shell
  process behind a seccomp + Landlock syscall sandbox on Linux.
* No JIT, which keeps the JavaScript attack surface small.
* No telemetry: it does not phone home and does not track the user.

%prep
%setup

%build
%meson -Djs_engine=quickjs-ng
%meson_build

%install
%meson_install
rm %buildroot%_bindir/open-internet-browser

%files
%doc LICENSE README.md
%_bindir/northstar
%_desktopdir/org.northstar.WebBrowser.desktop
%_datadir/metainfo/org.northstar.WebBrowser.metainfo.xml
%_datadir/northstar
%_iconsdir/*/*/*/*.*

%changelog
* Fri Nov 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.22-alt1
- 1.0.22 released

* Fri Nov 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.20-alt1
- 1.0.20 released
