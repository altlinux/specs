Name: polybar
Version: 3.7.2
Release: alt2

Summary: A fast and easy-to-use status bar
License: MIT
Group: Graphical desktop/Other

Url: https://github.com/polybar/polybar
# Source-url: https://github.com/polybar/polybar/releases/download/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(xcb-xrm)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-proto)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(cairo)
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: pkgconfig(libuv)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(expat)
BuildRequires: i3-devel

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)

%ifarch %e2k
BuildRequires: clang
%define cxx -DCMAKE_CXX_COMPILER="clang++"
%endif

%description
A fast and easy-to-use status bar for tilling WM

%prep
%setup

%build
%cmake %cxx
%cmake_build

%install
%cmake_install
rm -rf %buildroot/%_docdir/%name/.buildinfo

%files
%doc README.md SUPPORT.md
%_bindir/%name
%_bindir/%name-msg
%_man1dir/*
%_man5dir/*
%_docdir/%name/
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.ini

%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/zsh/site-functions/_%{name}_msg

%changelog
* Wed Mar 25 2026 Michael Shigorin <mike@altlinux.org> 3.7.2-alt2
- E2K: build with clang (thx @numitorum)

* Sun Aug 25 2024 Roman Alifanov <ximper@altlinux.org> 3.7.2-alt1
- new version 3.7.2 (with rpmrb script)

* Fri Dec 29 2023 Roman Alifanov <ximper@altlinux.org> 3.7.1-alt1
- new version 3.7.1 (with rpmrb script)
- fake %check removed

* Mon May 22 2023 Roman Alifanov <ximper@altlinux.org> 3.6.3-alt1
- Initial build for Sisyphus

