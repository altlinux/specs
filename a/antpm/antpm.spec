%define _unpackaged_files_terminate_build 1

Name: antpm
Version: 1.24
Release: alt1

Summary: ANT+ information retrieval client for Garmin GPS products
License: GPL-3.0
Group: Sciences/Geosciences
VCS: https://salsa.debian.org/debian/antpm
Url: https://github.com/ralovich/antpm

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: boost-devel
BuildRequires: boost-program_options-devel

%description
This software uses the Garmin ANT+ proprietary USB keys and
communication protocol to retrieve information (such as GPS traces)
from some Garmin Forerunner watches such as Forerunner 405 and 310XT.

The underlying ANT+minus implements the ANT/ANT+/ANT-FS protocols to
provide these tools: garmin-ant-downloader, antpm-downloader,
antpm-fit2gpx, and antpm-usbmon2ant.

ANT+minus is a userspace implementation of a wire protocol similar
to the ANT/ANT+/ANT-FS protocols. The goal is to be able to communicate
with any ANT capable device in order to e.g. retrieve sports tracks. The
C++ implementation is currently available under both Linux and win.
Communication with watches other than the 310XT might work, but are
untested. Please report your experience to help improving the software.

The software was originally named "gant" but renamed when packaged
to avoid confusion with existing Java software

%prep
%setup -q -n %{name}-%{version}/src
patch -p1 < ../debian/patches/1000-appstream-metainfo.patch

%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release \
       -DUSE_BOOST_STATIC_LINK=OFF \
       -Wno-dev
%cmake_build

%install
%cmake_install

# install man-pages
install -D -m 0644 ../debian/antpm-garmin-ant-downloader.1 -t "%{buildroot}%{_man1dir}/"
install -D -m 0644 *.1 -t "%{buildroot}%{_man1dir}/"

# install metainfo
install -D -m 0644 com.github.ralovich.antpm.metainfo.xml -t "%{buildroot}%_datadir/metainfo/"

# install udev-rule
install -m 0644 -D ../scripts/80-ant-stick.rules %buildroot%_udevrulesdir/60-%{name}.rules

# rename
mv -v %buildroot%_bindir/gant %buildroot%_bindir/antpm-garmin-ant-downloader

%files
%doc ../LICENSE ../docs/*.txt
%_bindir/*
%_man1dir/*
%_datadir/metainfo/*.metainfo.xml
%_udevrulesdir/*.rules

%changelog
* Sun Jun 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.24-alt1
- Initial build for Sisyphus
