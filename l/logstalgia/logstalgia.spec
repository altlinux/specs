Name: logstalgia
Version: 1.1.3
Release: alt2

Summary: Web server access log visualizer
License: GPLv3+
Group: Monitoring

Url: http://code.google.com/p/logstalgia/
Source0: http://logstalgia.googlecode.com/files/logstalgia-%version.tar.gz
Source1: logstalgia.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Apr 23 2014
# optimized out: boost-devel-headers gnu-config libGL-devel libGLU-devel libSDL2-devel libX11-devel libcloog-isl4 libstdc++-devel pkg-config xorg-xproto-devel
BuildRequires: boost-devel gcc-c++ libSDL2_image-devel libfreetype-devel libglew-devel libglm-devel libpcre2-devel libpng-devel
BuildRequires: boost-filesystem-devel

# [#311618] configure: error: Could not link against -lGLU !
ExcludeArch: ppc64le

%description
Logstalgia (aka ApachePong) replays or streams a standard website
access log (eg access.log) as a retro arcade game-like simulation.

%prep
%setup
%ifarch %e2k ppc64le riscv64
sed -i 's,aarch64,&|riscv64|ppc64le|e2k,' m4/ax_boost_base.m4
%endif

%build
%autoreconf
%configure
%make_build OPTFLAGS="%optflags"

%install
%makeinstall_std

%files
%doc README THANKS
%_bindir/%name
%_datadir/%name
%_man1dir/%name.1*

%changelog
* Tue Dec 13 2022 Michael Shigorin <mike@altlinux.org> 1.1.3-alt2
- fix build on newer arches through autoreconf proper;
  didn't help ppc64le though (thx ilyakurdyukov@)

* Tue Oct 18 2022 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- new version (watch file uupdate)
- ExcludeArch: ppc64le due to ftbfs

* Sat Jun 16 2018 Michael Shigorin <mike@altlinux.org> 1.1.2-alt1
- new version (watch file uupdate)

* Tue Feb 13 2018 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- new version (watch file uupdate)

* Wed Oct 11 2017 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- new version (watch file uupdate)

* Sat Oct 07 2017 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- new version (watch file uupdate)

* Fri Sep 29 2017 Michael Shigorin <mike@altlinux.org> 1.0.8-alt1
- new version (watch file uupdate)

* Thu Oct 22 2015 Michael Shigorin <mike@altlinux.org> 1.0.7-alt1
- new version (watch file uupdate)

* Thu Oct 16 2014 Michael Shigorin <mike@altlinux.org> 1.0.6-alt1
- new version (watch file uupdate)

* Thu Apr 24 2014 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5
- built against libSDL2
- added watch file (github is weird though)

* Fri Mar 21 2014 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- initial build for ALT Linux Sisyphus
  + based on Fedora package by Terje Rosten
- argh, better fix pcre.h location instead
