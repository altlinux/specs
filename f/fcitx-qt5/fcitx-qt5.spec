Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global project_name FcitxQt5

Name:           fcitx-qt5
Version:        1.2.4
Release:        alt1_1
Summary:        Fcitx IM module for Qt5

# The entire source code is GPLv2+ except
# platforminputcontext/ which is BSD
License:        GPLv2+ and BSD
URL:            https://github.com/fcitx/fcitx-qt5
Source0:        http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  ctest cmake
BuildRequires:  fcitx-devel
BuildRequires:  qt5-base-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-tools libasprintf-devel
# The author requests that fcitx-qt5 should be rebuilt for each minor version
# of qt5. qt5-qtbase-private-devel is not actually required for build, but
# left for Qt maintainer to tract this case.
BuildRequires:  qt5-base-devel



Source44: import.info
%add_findprov_skiplist %{_qt5_plugindir}/platforminputcontexts/libfcitxplatforminputcontextplugin.so
%add_findprov_skiplist %{_libdir}/fcitx/qt/libfcitx-quickphrase-editor5.so

%description
This package provides Fcitx Qt5 input context.

%package devel
Group: Development/Other
Summary:        Development files for fcitx-qt5
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
%find_lang %{name}



%files -f %{name}.lang
%doc README
%doc --no-dereference COPYING COPYING.BSD
%{_libdir}/fcitx/libexec/%{name}-gui-wrapper
%{_libdir}/lib%{project_name}*.so.*
%{_libdir}/fcitx/qt/
%{_qt5_plugindir}/platforminputcontexts/libfcitxplatforminputcontextplugin.so

%files devel
%{_includedir}/%{project_name}
%{_libdir}/lib%{project_name}*.so
%{_libdir}/cmake/*


%changelog
* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_1
- update to new release by fcimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_10
- update to new release by fcimport

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_8
- update to new release by fcimport

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_6
- update to new release by fcimport

* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_4
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_2
- update to new release by fcimport

* Sat Jun 09 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_4
- update to new release by fcimport

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2
- update to new release by fcimport

