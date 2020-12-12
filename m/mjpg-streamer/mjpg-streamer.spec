Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires: libv4l-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mjpg-streamer
# export LANG=C && export LC_ALL=C && echo $(git show -s --format=%at-%H)
Version:        1.0_pre.1593783066.85f89a8
Release:        alt1
Summary:        Program for streaming webcam video to HTTP
License:        GPLv2
Group:          Video
Source0:        %name-%version.tar
Patch1:         fix-build.patch
Patch2:         set_group.patch
URL:            https://github.com/jacksonliam/mjpg-streamer
VCS:            https://github.com/jacksonliam/mjpg-streamer
BuildRequires:  libSDL-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libgphoto2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libopencv-devel
BuildRequires:  protobuf-c-compiler
BuildRequires:  python3-devel
BuildRequires:  libnumpy-py3-devel
BuildRequires:  python3-module-opencv
BuildRequires:  libzeromq-devel

%description
MJPG-streamer takes JPGs from Linux-UVC compatible webcams, from
local files or other input plugins and streams them as M-JPEG via
HTTP to webbrowsers, VLC and other software. It is the successor of
uvc-streamer, a Linux-UVC streaming application with Pan/Tilt.

This package provides a fork including support for Raspberry Pi Camera.

Enable the service by specifing the video device via

# systemctl start mjpg_streamer@0

The number reflects /dev/videoX and listening port 808X.

%prep
%setup -q -n %{name}-%version/mjpg-streamer-experimental
%patch1 -p2
%patch2 -p2

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

# service file
install -m 0644 -D mjpg_streamer@.service %buildroot%_unitdir/mjpg_streamer@.service

%pre
%_sbindir/groupadd -r -f video >/dev/null 2>&1 ||:
getent passwd mjpg_streamer >/dev/null || %_sbindir/useradd -r -G video \
	-d / -s /sbin/nologin mjpg_streamer

%files
%doc LICENSE
%doc README.md
%_bindir/mjpg_streamer
/usr/lib/mjpg-streamer
%_datadir/mjpg-streamer
%_unitdir/mjpg_streamer@.service

%changelog
* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.0_pre.1593783066.85f89a8-alt1
- upstream git update

* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.0_pre.1540449284.ddb69b7-alt1_1.7
- switched a fork (with raspberry pi support)
- new suse thumbleweed version

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> r160-alt1_6.2
- converted for ALT Linux by srpmconvert tools

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> r137-alt1_102.2
- converted from openSUSE Build Service (Projects > home:vodoo)

