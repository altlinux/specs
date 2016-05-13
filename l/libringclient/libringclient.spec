
%define sover 1.0.0
%define libname libringclient%sover

Name: libringclient
Version: 1.0.0
Release: alt2

Group: System/Libraries
Summary: Ring voice, video and chat client library
License: GPLv3
Url: http://ring.cx/
Source: %name-%version.tar

#BuildRequires: cmake gcc-c++ ring-daemon-devel

# Automatically added by buildreq on Tue Mar 15 2016 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ libgpg-error libqt5-core libqt5-dbus libqt5-xml libstdc++-devel python-base python3 python3-base qt5-base-devel qt5-tools ring-daemon-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: cmake python3.3-site-packages qt5-tools-devel ring-daemon-devel-static rpm-build-ruby
BuildRequires: cmake qt5-tools-devel ring-daemon-devel-static

%description
Ring is a secure and distributed voice, video and chat communication platform that requires no centralized server and leaves the power of privacy in the hands of the user.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
Conflicts: libringclient0.4.0
%description common
Common %name files

%package -n %libname
Group: System/Libraries
Summary: %summary
Requires: %name-common >= %EVR
%description -n %libname
%summary

%package devel
Group: Development/Other
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_VIDEO=ON
    #
pushd BUILD
%make_build
popd

%install
pushd BUILD
make install DESTDIR=%buildroot
popd

%if "%_lib" == "lib64"
sed -i 's|/usr/lib|/usr/lib64|' %buildroot/usr/lib/cmake/LibRingClient/LibRingClientConfig.cmake
mv %buildroot/usr/lib %buildroot/usr/lib64
%endif

%find_lang %name --with-qt --all-name

%files common -f %name.lang
%dir %_datadir/libringclient/
%dir %_datadir/libringclient/translations/

%files -n %libname
%_libdir/libringclient.so.%sover
%_libdir/libringclient.so.*

%files devel
%_includedir/libringclient/
%_libdir/cmake/*
%_libdir/libringclient.so

%changelog
* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2
- split data to separate package

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt0.1
- initial build
