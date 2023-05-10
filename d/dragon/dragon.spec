Name: dragon
Version: 1.2.0
Release: alt1
License: GPLv3
Summary: Simple drag-and-drop source/sink for X or Wayland
Url: https://github.com/mwh/dragon
Source: %name-%version.tar.gz
Group: System/X11

# Automatically added by buildreq on Thu Jan 14 2021
# optimized out: at-spi2-atk fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libpango-devel libwayland-client libwayland-cursor libwayland-egl pkg-config python2-base sh4
BuildRequires: libgtk+3-devel

%description
Many programs, particularly web applications, expect files to be dragged
into them now. If you don't habitually use a file manager that is
a problem. dragon is a lightweight drag-and-drop source for X where you
can run: dragon file.tar.gz to get a window with just that file in it,
ready to be dragged where you need it.

%prep
%setup

%build
%make DEFINES=-g

%install
install -D %name %buildroot%_bindir/%name

%files
%doc README*
%_bindir/*

%changelog
* Wed May 10 2023 Fr. Br. George <george@altlinux.org> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Thu Jan 14 2021 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Initial build for ALT

