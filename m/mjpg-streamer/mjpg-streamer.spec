# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-suse-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define suse_version 1150
#
# spec file for package mjpg-streamer (Version SVN Rev. 137)
#
# Copyright 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# norootforbuild
Summary: Stream webcam video to HTTP
Name: mjpg-streamer
Version: r137
Release: alt1_102.2
License: GPLv2
Group: Video
Source0: %{name}.tar.bz2
Source1: %{name}.desktop
Source2: %{name}.png
Source3: %{name}-udp-client.desktop
Source4: mjpg_streamer.1
Source5: mjpg_streamer_udp_client.1
Source6: mstreamer.1
Source7: mjpg_streamer.sysconfig
Source8: videodev.h
Patch0: %{name}.Makefile.patch
#Patch1: {name}.encoder.patch
Patch2: %{name}.start.sh.patch
#Patch3: {name}.httpd.c.patch
#Patch4: {name}.autofocus.patch
Patch5: %{name}.uvc.patch
Patch6: %{name}.control.patch
Patch7: %{name}.outputhttp.patch
#Patch8: {name}.utils.h.patch
#Patch9: {name}.outputviewer.patch
URL: http://mjpg-streamer.sourceforge.net/
BuildRequires: libv4l-devel libjpeg-devel libSDL-devel unzip rpm-build-suse-compat
BuildRequires: qt4-devel
%if 0%{?suse_version} > 1140
BuildRequires: ImageMagick
%endif
Requires: SDL procps
%if 0%{?suse_version} > 1110
Requires: kde4base-kdialog
%endif
%if 0%{?suse_version} < 1120
Requires: kde4-kdialog
%endif

Source44: import.info

%description
MJPG-streamer takes JPGs from Linux-UVC compatible webcams, from local files or other input plugins and streams them as M-JPEG via HTTP to webbrowsers, VLC and other software. It is the successor of uvc-streamer, a Linux-UVC streaming application with Pan/Tilt.
Control the application with mstreamer <start|stop|status> from the command line or use the desktop menu in KDE.

%prep
%setup -q -n %{name}
%patch0 -p0
#patch1 -p0
%patch2 -p0
#patch3 -p0
#patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
#patch8 -p0
#patch9 -p0
cp -a %{S:4} .
cp -a %{S:5} .
cp -a %{S:6} .
cp -a %{S:8} .
# Fix wrong address in www/LICENCE.txt (not needed)
rm www/LICENSE.txt
# patch videodev.h on the fly
%if 0%{?suse_version} > 1140
#find ./ -name '.svn' -exec rm -rf '{}' ';'
find plugins/ -name '*.c' -or -name '*.h' -print , -exec sed -i -e 's:<linux/videodev.h>:"../../videodev.h":' '{}' ';' 2>/dev/null
find ./ -name mjpg_streamer.c -print , -exec sed -i -e 's:<linux/videodev.h>:"videodev.h":' '{}' ';' 2>/dev/null
%endif

%build
%{__make} %{?jobs:-j%jobs} %{?_smp_mflags} USE_LIBV4L2=true RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
gzip -9 mjpg_streamer.1
gzip -9 mjpg_streamer_udp_client.1
gzip -9 mstreamer.1
cd ../udp_client
qmake-qt4 -unix -o Makefile udp_client.pro
make
strip udp_client

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/www
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/actions
make DESTDIR="%{buildroot}" LIBDIR="%{_libdir}" install
%suse_update_desktop_file -i %{name} AudioVideo Player Video
%suse_update_desktop_file -i %{name}-udp-client AudioVideo Player Video
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 $RPM_SOURCE_DIR/%{name}.png %{buildroot}%{_datadir}/pixmaps/
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 mjpg_streamer.1.gz %{buildroot}%{_mandir}/man1/
install -m 644 mjpg_streamer_udp_client.1.gz %{buildroot}%{_mandir}/man1/
install -m 644 mstreamer.1.gz %{buildroot}%{_mandir}/man1/
# Source7: mjpg_streamer.sysconfig
install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/mjpg-streamer
cd ../udp_client
install -m 755 udp_client %{buildroot}%{_bindir}/mjpg_streamer_udp_client
# kill OnlyShowIn=...
sed -i -e '/^OnlyShowIn/d' `find %buildroot%_desktopdir -name '*.desktop'`


%post

%postun  

%files
%doc README CHANGELOG LICENSE start.sh
%doc %{_mandir}/man1/mjpg_streamer.1.gz
%doc %{_mandir}/man1/mjpg_streamer_udp_client.1.gz
%doc %{_mandir}/man1/mstreamer.1.gz
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/www
%dir %{_libdir}/%{name}
%{_bindir}/mjpg_streamer
%{_bindir}/mjpg_streamer_udp_client
%{_bindir}/mstreamer
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}/www/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-udp-client.desktop
%{_datadir}/pixmaps/%name.png
# The format has changed; otherwise use config(noreplace)
%config /etc/sysconfig/mjpg-streamer

%changelog
* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> r137-alt1_102.2
- converted from openSUSE Build Service (Projects > home:vodoo)

