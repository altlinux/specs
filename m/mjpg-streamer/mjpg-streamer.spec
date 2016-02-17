# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-suse-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: libqt4-devel
%define suse_version 1150
#
# spec file for package mjpg-streamer (Version SVN Rev. 160)
#
# Copyright 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
#
# Date and time of the svn release
%define  SVNDATE  2012-04-23
%define  SVNTIME  16:00:48
Summary: Stream webcam video to HTTP
Name:    mjpg-streamer
Version: r160
Release: alt1_6.2
License: GPL-2.0
Group:   Video
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}.desktop
Source2: %{name}.png
Source3: %{name}-udp-client.desktop
Source4: mjpg_streamer.1
Source5: mjpg_streamer_udp_client.1
Source6: mstreamer.1
Source7: mjpg_streamer.sysconfig
Patch0:  %{name}.Makefile.patch
Patch1:  %{name}.start.sh.patch
Patch2:  %{name}.uvc.patch
Patch3:  %{name}.control.patch
Patch4:  %{name}.outputhttp.patch
URL:           http://mjpg-streamer.sourceforge.net/
BuildRequires: qt4-devel libSDL-devel unzip rpm-build-suse-compat
BuildRequires: libjpeg-devel
%if 0%{?suse_version} > 1140
BuildRequires: ImageMagick
BuildRequires: libv4l-devel >= 0.8.4
%else
BuildRequires: libv4l-devel
%endif

Requires: SDL procps
%if 0%{?suse_version} > 1110
Requires: kde4base-kdialog
%endif
%if 0%{?suse_version} < 1120
Requires: kde4-kdialog
%endif

Source44: import.info
Patch33: mjpg-streamer-r160-link.patch

%description
MJPG-streamer takes JPGs from Linux-UVC compatible webcams, from local files or other input plugins and streams them as M-JPEG via HTTP to webbrowsers, VLC and other software. It is the successor of uvc-streamer, a Linux-UVC streaming application with Pan/Tilt.
Control the application with mstreamer <start|stop|status> from the command line or use the desktop menu in KDE.

%package -n %{name}_udp_client
Summary:  UDP client for %{name} to take snapshots of images from the stream
Group:    Video
Requires: %{name}

%description -n %{name}_udp_client
UDP output plugin added thanks to Dimitrios Zachariadis. A Qt4 based client utility to the UDP plugin. Takes snapshots from the stream provided by mjpg-streamer.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
cp -a %{S:4} .
cp -a %{S:5} .
cp -a %{S:6} .

# Fix wrong address in www/LICENCE.txt (not needed)
rm www/LICENSE.txt

# patch videodev.h on the fly
%if 0%{?suse_version} > 1140
find plugins/ -name '*.c' -or -name '*.h' -print , -exec sed -i -e 's:<linux/videodev.h>:<libv4l1-videodev.h>:' '{}' ';' 2>/dev/null
find ./ -name mjpg_streamer.c -print , -exec sed -i -e 's:<linux/videodev.h>:<libv4l1-videodev.h>:' '{}' ';' 2>/dev/null
%endif

# patch date and time of the release
sed -i -e 's/__DATE__/"%{SVNDATE}"/g; s/__TIME__/"%{SVNTIME}"/g' mjpg_streamer.c 2>/dev/null

%patch33 -p1

%build
%{__make} %{?jobs:-j%jobs} %{?_smp_mflags} USE_LIBV4L2=true RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
cd ../udp_client
qmake-qt4 QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags" -Wall -o Makefile udp_client.pro
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
install -m 644 mjpg_streamer.1 %{buildroot}%{_mandir}/man1/
install -m 644 mjpg_streamer_udp_client.1 %{buildroot}%{_mandir}/man1/
install -m 644 mstreamer.1 %{buildroot}%{_mandir}/man1/
# Source7: mjpg_streamer.sysconfig
install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/mjpg-streamer
cd ../udp_client
install -m 755 udp_client %{buildroot}%{_bindir}/mjpg_streamer_udp_client

%files
%doc README CHANGELOG LICENSE start.sh
%doc %{_mandir}/man1/mjpg_streamer.1*
%doc %{_mandir}/man1/mstreamer.1*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/www
%dir %{_libdir}/%{name}
%{_bindir}/mjpg_streamer
%{_bindir}/mstreamer
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}/www/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%name.png
# When the format has changed use config; otherwise use config(noreplace)
%config(noreplace) /etc/sysconfig/mjpg-streamer

%files -n %{name}_udp_client
%doc %{_mandir}/man1/mjpg_streamer_udp_client.1*
%{_bindir}/mjpg_streamer_udp_client
%{_datadir}/applications/%{name}-udp-client.desktop

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> r160-alt1_6.2
- converted for ALT Linux by srpmconvert tools

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> r137-alt1_102.2
- converted from openSUSE Build Service (Projects > home:vodoo)

