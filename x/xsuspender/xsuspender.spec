Name:           xsuspender
Version:        1.3
Release:        alt1
Summary:        Automatically suspend inactive X11 applications.
URL:            https://kernc.github.io/xsuspender
License:        WTFPL
Group:          System/X11

Source:         %name-%version.tar.gz

# Automatically added by buildreq on Fri Aug 30 2024
# optimized out: at-spi2-atk cmake-modules glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgtk+3-devel libharfbuzz-devel libp11-kit libpango-devel libsasl2-3 libstartup-notification libwayland-client libwayland-cursor libwayland-egl pkg-config python3 python3-base python3-dev sh5 zlib-devel
BuildRequires: cmake libssl-devel libwnck3-devel

%description
When an application window loses focus, XSuspender tries to match it to
one of the rules in its configuration. If a match is found, the
application is sent a SIGSTOP signal (preventing the process from
obtaining further CPU time). Upon windows regaining focus, the process
is seamlessly continued where it had left off.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
mv %buildroot%_defaultdocdir/%name %buildroot%_defaultdocdir/%name-%version
install -D data/%name.desktop %buildroot%_desktopdir/%name.desktop
rm -rf %buildroot/usr/etc

%files
%doc *.md
%_bindir/*
%_man1dir/*
%_desktopdir/*

%changelog
* Fri Aug 30 2024 Fr. Br. George <george@altlinux.org> 1.3-alt1
- Initial build for ALT
