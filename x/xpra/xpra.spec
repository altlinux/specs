# TODO: python-uinput

Name: xpra
Version: 4.4.4
Release: alt1

Summary: X Persistent Remote Applications
License: GPLv2
Group: Networking/Remote access

Url: http://xpra.org/
Source: https://xpra.org/src/xpra-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++ libXcomposite-devel libXdamage-devel libXrandr-devel libXtst-devel libXres-devel libxkbfile-devel libpam0-devel libsystemd-devel

BuildRequires: libgtk+3-devel python3-module-pygobject3-devel python3-module-pycairo-devel

# Video
BuildRequires: libvpx-devel libx264-devel libx265-devel libwebp-devel libjpeg-devel libpng-devel libyuv-devel liblz4-devel

# p9+
%def_without ffmpeg_static

%if_with ffmpeg_static
BuildRequires: libffmpeg-devel-static
%else
BuildRequires: libavformat-devel libavcodec-devel libswscale-devel
%endif

# Sound
BuildRequires: libogg-devel libopus-devel libflac-devel libspeex-devel libvorbis-devel libwavpack-devel liblame-devel libtwolame-devel libmad-devel

# GL
BuildRequires: python3-module-OpenGL python3-module-OpenGL_accelerate
Requires: python3-module-OpenGL python3-module-OpenGL_accelerate

BuildRequires: python3-module-Pillow python3-module-websockify

%ifarch %e2k
# no libv8/node so far => --without-minify;
# it's java actually
BuildRequires: python3-module-yuicompressor
BuildRequires: /proc
%else
BuildRequires: /usr/bin/uglifyjs
%endif

BuildRequires: xorg-server brotli

BuildRequires: pandoc

# See https://bugzilla.altlinux.org/show_bug.cgi?id=28632
BuildRequires: python3-module-Cython >= 0.20

AutoReq: yes, nomingw
# server is not a python package
AutoProv: yes, nopython3

# why they are required?
%add_python3_req_skip xpra.codecs.argb.argb xpra.codecs.xor.cyxor xpra.codecs.evdi.capture
%add_python3_req_skip xpra.rectangle xpra.server.cystats xpra.server.window.motion
%add_python3_req_skip xpra.x11.bindings.core_bindings xpra.x11.bindings.display_source
%add_python3_req_skip xpra.x11.bindings.keyboard_bindings xpra.x11.bindings.randr_bindings
%add_python3_req_skip xpra.x11.bindings.window_bindings xpra.x11.bindings.ximage

# disabled during build
%add_python3_req_skip xpra.net.mdns

%add_python3_req_skip win32security pyopencl xpra.platform.win32.common

# prefer dbus notification
%add_python3_req_skip pynotify

BuildRequires(pre): rpm-build-gir rpm-build-intro rpm-macros-kde-common-devel

# Unity specific?
%add_typelib_req_skiplist typelib(AppIndicator) typelib(AppIndicator3) typelib(GtkosxApplication)

# TODO:
%add_typelib_req_skiplist typelib(GdkGLExt) typelib(GtkGLExt)

# Note: we have no linking requires to libwebp.so.x
Requires: libwebp

Requires: xorg-xvfb setxkbmap

Requires: python3-module-pyinotify python3-module-rencode python3-module-lz4 python3-module-netifaces

Requires: libgtk+3-gir

%ifarch %e2k
%define py_flags --without-mdns --without-html5 --without-minify
%else
%define py_flags --without-mdns
%endif

%description
Xpra is 'screen for X': it allows you to run X programs,
usually on a remote host, direct their display to your local machine,
and then to disconnect from these programs and reconnect
from the same or another machine, without losing any state.
It gives you remote access to individual applications.
Xpra is "rootless" or "seamless": programs you run under
it show up on your desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt
to changing network bandwidth limits. (see also adaptive JPEG mode)
Xpra is open-source (GPLv2+), multi-platform and multi-language,
with current clients written in Python and Java.

On the machine which will export the application (xterm in this example):
> xpra start :100 --start-child=xterm

We can then attach to this session from the same machine, with:
> xpra attach :100

If connecting from a remote machine, you would use something like (or you can also use the GUI):
> xpra attach ssh:serverhostname:100


%prep
%setup
# instal service file in anyway
sed -i "s|/bin/systemctl|/bin/true|g" setup.py

%build
%if_with ffmpeg_static
export PKG_CONFIG_PATH=%_libdir/ffmpeg-static/%_lib/pkgconfig/
%endif

%python3_build_debug --without-strict %py_flags %_smp_mflags

%install
%python3_install %py_flags
mkdir -p %buildroot/%_tmpfilesdir/
mv -f %buildroot/usr/lib/tmpfiles.d/xpra.conf %buildroot/%_tmpfilesdir/
mkdir -p %buildroot%_udevrulesdir/
mv -f %buildroot/usr/lib/udev/rules.d/71-xpra-virtual-pointer.rules %buildroot%_udevrulesdir/
#install -m644 -D service/xpra.service %buildroot%_unitdir/%name.service

# TODO
rm -v %buildroot/usr/lib/sysusers.d/xpra.conf

# remove obsoleted (python2 only) examples
rm -rv %buildroot/%python3_sitelibdir/xpra/client/gtk_base/example/

%pre
%_sbindir/groupadd -r -f xpra &>/dev/null ||:

%files
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/*
%_bindir/xpra
%_bindir/xpra_launcher
%_bindir/run_scaled
#_bindir/xpra_signal_listener
#_bindir/xpra_udev_product_version
#_libexecdir/%name/
%python3_sitelibdir/*
%_desktopdir/*
%_iconsdir/*
%_man1dir/*
/usr/libexec/%name/
#_datadir/parti/
#_datadir/wimpiggy/
%_docdir/%name/
%_datadir/xpra/
%_tmpfilesdir/xpra.conf
%_datadir/metainfo/xpra.appdata.xml
%_K4xdg_mime/application-x-xpraconfig.xml
%_cupslibdir/backend/xpraforwarder
%_sysconfigdir/%name
%_sysconfdir/pam.d/%name
#_sysconfdir/init.d/%name
%_unitdir/%name.service
%_unitdir/%name.socket
%_udevrulesdir/71-xpra-virtual-pointer.rules
%_sysconfdir/dbus-1/system.d/xpra.conf
%_sysconfdir/X11/xorg.conf.d/90-xpra-virtual.conf

%changelog
* Wed Mar 15 2023 Vitaly Lipatov <lav@altlinux.ru> 4.4.4-alt1
- new version 4.4.4 (with rpmrb script)

* Wed Jul 28 2021 Michael Shigorin <mike@altlinux.org> 4.0.6-alt1.1
- drop ubt handling (was there for p8)
- minor spec cleanup
- E2K: yuicompressor is there but uglifyjs isn't => no minification

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.6-alt1
- new version 4.0.6 (with rpmrb script)

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.5-alt1
- new version 4.0.5 (with rpmrb script)

* Sat Oct 03 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.4-alt1
- new version 4.0.4 (with rpmrb script)

* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt2
- disable provide xpra python modules
- enable SMP build

* Fri Aug 21 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.1-alt1
- new version 4.0.1 (with rpmrb script)
- use uglifyjs instead of yuicompressor python module

* Wed May 06 2020 Vitaly Lipatov <lav@altlinux.ru> 3.0.9-alt1
- new version 3.0.9 (with rpmrb script)

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 3.0.7-alt1
- new version 3.0.7 (with rpmrb script)

* Fri Feb 14 2020 Vitaly Lipatov <lav@altlinux.ru> 3.0.6-alt1
- new version 3.0.6 (with rpmrb script)

* Wed Jan 29 2020 Vitaly Lipatov <lav@altlinux.ru> 3.0.5-alt1
- new version 3.0.5 (with rpmrb script)

* Wed Dec 11 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0.3-alt1
- new version 3.0.3 (with rpmrb script)
- switch to python3

* Sat Oct 12 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- new version 3.0 (with rpmrb script)

* Thu Sep 26 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt1
- new version 2.5.3 (with rpmrb script)

* Tue Jun 18 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.2-alt1
- new version 2.5.2 (with rpmrb script)

* Wed May 08 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1 (with rpmrb script)

* Mon Mar 11 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt4
- build with OpenGL support (ALT bug 36154)
- disable mdns

* Mon Mar 11 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt3
- allow build with static ffmpeg

* Sun Mar 10 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt2
- cleanup spec
- add python-module-lz4 require

* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- new version 2.3.4 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Mon Jul 10 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.17.6-alt3
- rebuild with ffmpeg

* Wed May 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.17.6-alt2
- add xpra group creating (ALT bug 33459)

* Sun Dec 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.17.6-alt1
- new version 0.17.6 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.16.3-alt1
- new version (0.16.3) with rpmgs script

* Wed Mar 09 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.19-alt2
- rebuilt with recent libx264

* Thu Mar 05 2015 Michael Shigorin <mike@altlinux.org> 0.14.19-alt1
- new version

* Wed Sep 24 2014 Vitaly Lipatov <lav@altlinux.ru> 0.14.7-alt1
- new version 0.14.7 (with rpmrb script)

* Mon Jul 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.13.6-alt1
- new version 0.13.6 (with rpmrb script)
- fix description (ALT bug #30130)
- build without avcodec2

* Mon May 12 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt2
- rebuilt with recent libx264

* Mon Feb 17 2014 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)
- build with Cython 0.20
- build without avcodec

* Fri Feb 14 2014 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Wed Feb 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.6-alt3
- Rebuilt for libwebp5.

* Thu Sep 12 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.6-alt2
- rebuilt with recent libx264

* Thu Jul 11 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- new version 0.9.6 (with rpmrb script)
- rebuild with new libwebp, apply patch to build with old libav

* Sat Dec 08 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- initial build for Sisyphus

