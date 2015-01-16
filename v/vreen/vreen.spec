%define git_version 20140410
%define abiversion 0

Name: vreen
Version: 0.9.5
# to replace old libvreen from qutim package
Epoch: 8
Release: alt2.git%git_version
Summary: Qt wrapper library for vk.com API

Group: System/Libraries
License: %lgpl3plus
Url: http://github.com/gorthauer/vreen
Packager: Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses rpm-macros-cmake
BuildRequires: cmake gcc-c++ libqt4-devel

%description
Qt wrapper library for VKontakte social network (vk.com) API.

%package -n lib%name
Summary: Qt wrapper library for vk.com API
Group: System/Libraries

%description -n lib%name
Qt wrapper library for VKontakte social network (vk.com) API.

%package -n lib%name-devel
Summary: vreen development libraries and includes
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for vreen library

%prep
%setup
%patch0 -p1

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc AUTHORS
%_libdir/lib%name.so.%{abiversion}*
%_libdir/qt4/imports/com/vk

%files -n lib%name-devel
%_includedir/vreen
%_libdir/lib%{name}.so
%_libdir/lib%{name}oauth.a
%_libdir/pkgconfig/vreen.pc
%_libdir/pkgconfig/vreenoauth.pc

%changelog
* Thu Jan 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 8:0.9.5-alt2.git20140410
- Fixed build (gcc 4.9).

* Tue Jul 8 2014 Vladimir Didenko <cow@altlinux.org> 8:0.9.5-alt1.git20140410
- Initial build
