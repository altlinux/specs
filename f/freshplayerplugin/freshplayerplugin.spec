%define _libname libfreshwrapper-flashplayer

Name: freshplayerplugin
Version: 0.3.6
Release: alt1
Summary: PPAPI-host NPAPI-plugin adapter
License: MIT
Group: System/Libraries
Url: https://github.com/i-rinat/freshplayerplugin

# git clone https://github.com/i-rinat/freshplayerplugin.git
Source: %name-%version.tar

ExclusiveArch: %ix86 x86_64

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Wed Oct 26 2016
# optimized out: cmake-modules fontconfig fontconfig-devel glib2-devel libGL-devel libX11-devel libXrender-devel libavutil-devel libcairo-devel libfreetype-devel libgpg-error libjson-c libopencore-amrnb0 libopencore-amrwb0 libstdc++-devel libvdpau-devel libwayland-client libwayland-server pkg-config python-base python-modules python3 python3-base xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: cmake gcc-c++ libXcursor-devel libXrandr-devel libalsa-devel libavcodec-devel libdrm-devel libevent-devel libgio-devel libicu-devel libpango-devel libpulseaudio-devel libssl-devel libv4l-devel libva-devel pesign python3-dev ragel

%{?!_without_check:%{?!_disable_check:BuildPreReq: ctest}}

Requires: ppapi-plugin-adobe-flash

%description
The main goal of this project is to get PPAPI (Pepper) Flash player
working in Firefox. This wrapper implements some kind of adapter which
will look like browser to PPAPI plugin and look like NPAPI plugin for
browser.

%prep
%setup
sed -i 's|^#pepperflash_path = .*|pepperflash_path = "%_libdir/pepper-plugins/libpepflashplayer.so"|' data/freshwrapper.conf.example

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS='%optflags' \
  -DCMAKE_CXX_FLAGS='%optflags' \
  -DWITH_GTK=3 \
  #
%cmake_build

%install
install -Dm 0644 BUILD/%_libname.so %buildroot%_libdir/browser-plugins/%_libname.so
install -Dm 0664 data/freshwrapper.conf.example %buildroot%_sysconfdir/freshwrapper.conf

%check
make -C BUILD check

%files
%doc COPYING LICENSE README.md
%_libdir/browser-plugins/%_libname.so
%config(noreplace) %_sysconfdir/freshwrapper.conf

%changelog
* Wed Oct 26 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.6-alt1
- Updated to 0.3.6 (ALT #32668).

* Thu Sep 29 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.5-alt2
- Replaced R: update-pepperflash with ppapi-plugin-adobe-flash
  (ALT#32516).

* Wed May 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.5-alt1
- Updated to 0.3.5.

* Wed Dec 30 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.4-alt1
- Updated to 0.3.4.

* Wed Oct 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Wed Aug 26 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Fri Jul 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Tue Mar 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.3-alt2
- Rebuilt with new update-pepperflash (arepo).
- Add R: update-pepperflash.

* Tue Mar 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.3-alt1
- Updated to 0.2.3.

* Wed Jan 21 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Mon Jan 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.1-alt2.gitad99227
- Updated to v0.2.1-152-gad99227.

* Thu Nov 06 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.1-alt1.git05da25f
- Initial build (v0.2.1-58-g05da25f).
