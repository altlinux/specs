Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global project_name FcitxQt5

Name:           fcitx-qt5
Version:        1.1.1
Release:        alt1_2
Summary:        Fcitx IM module for Qt5

# The entire source code is GPLv2+ except
# platforminputcontext/keyserver_x11.h which is LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/fcitx/fcitx-qt5
Source0:        http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  ctest cmake
BuildRequires:  fcitx-devel
BuildRequires:  qt5-base-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  extra-cmake-modules
# The author requests that fcitx-qt5 should be rebuilt for each minor version of qt5
BuildRequires:  qt5-base-devel


Source44: import.info
%add_findprov_skiplist %{_qt5_plugindir}/platforminputcontexts/libfcitxplatforminputcontextplugin.so

%description
This package provides Fcitx Qt5 input context.

%package devel
Summary:        Development files for fcitx-qt5
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ctest cmake

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using fcitx-qt5 libraries.

%prep
%setup -q

%build
mkdir -pv build
pushd build
%{fedora_cmake} ..
popd
%make_build -C build

%install
make install/fast DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" -C build

%files
%doc README
%doc COPYING
%{_libdir}/fcitx/libexec/%{name}-gui-wrapper
%{_libdir}/lib%{project_name}*.so.*
%{_qt5_plugindir}/platforminputcontexts/libfcitxplatforminputcontextplugin.so

%files devel
%{_includedir}/%{project_name}
%{_libdir}/lib%{project_name}*.so
%{_libdir}/cmake/*


%changelog
* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2
- update to new release by fcimport

