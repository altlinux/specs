%define git_commit 0ab13c7d8960c3fb9ae06cb91e37ff6ac07a3da3
%define so_version 2

#%ifarch %e2k ppc64le
%def_disable qtwebengine
#%else
#%def_enable qtwebengine
#%endif

Name: vreen
Version: 2.0.0
Epoch: 8
Release: alt2.git0ab13c7

Summary: Qt wrapper library for vk.com API
License: LGPLv3
Group: System/Libraries

Url: http://github.com/gorthauer/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/alekseysidorov/%name/archive/%git_commit/%name-%git_commit.tar.gz
Source0: %name-%git_commit.tar
Patch1: alt-ftbfs.patch

BuildRequires: cmake
BuildRequires: qt5-declarative-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif

%description
Qt wrapper library for VKontakte social network (vk.com) API.

%package -n lib%name%so_version
Summary: Qt wrapper library for vk.com API
Group: System/Libraries

%description -n lib%name%so_version
Qt wrapper library for VKontakte social network (vk.com) API.

%package -n lib%name-devel
Summary: vreen development libraries and includes
Group: Development/C++

%description -n lib%name-devel
Development files for vreen library

%prep
%setup -n %name-%git_commit
%patch1 -p1

%build
%cmake \
	-DQT_IMPORTS_DIR:PATH=%_qt5_qmldir \
	-DVREEN_WITH_AUTH_WIDGET:BOOL=%{?_enable_qtwebengine:ON}%{!?_enable_qtwebengine:OFF} \
	-Wno-dev

%cmake_build

%install
%cmakeinstall_std
%__rm -rf %buildroot%_libdir/lib%{name}oauth.a

%files -n lib%name%so_version
%doc AUTHORS README.md
%_libdir/lib%name.so.*
%_qt5_qmldir/Vreen

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so

%changelog
* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 8:2.0.0-alt2.git0ab13c7
- build without qtwebengine on e2k and ppc64le

* Sat Nov 13 2021 Nazarov Denis <nenderus@altlinux.org> 8:2.0.0-alt1.git0ab13c7
- Update to version 2.0.0 git 0ab13c7

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 8:0.9.5-alt5.git20140410.qa1
- NMU: applied repocop patch

* Fri Jan 20 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 8:0.9.5-alt5.git20140410
- Rebuilt for new format of LTO object (gcc6).

* Wed Nov 9 2016 Vladimir Didenko <cow@altlinux.org> 8:0.9.5-alt4.git20140410
- Fix build.

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 8:0.9.5-alt3.git20140410
- Rebuilt for new format of LTO object (gcc5).

* Thu Jan 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 8:0.9.5-alt2.git20140410
- Fixed build (gcc 4.9).

* Tue Jul 8 2014 Vladimir Didenko <cow@altlinux.org> 8:0.9.5-alt1.git20140410
- Initial build
