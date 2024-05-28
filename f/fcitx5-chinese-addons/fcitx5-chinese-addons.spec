Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext boost-devel qt5-base-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-chinese-addons
Version:        5.1.1
Release:        alt2_1
Summary:        Chinese related addon for fcitx5
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5-chinese-addons
Source:         https://download.fcitx-im.org/fcitx5/fcitx5-chinese-addons/fcitx5-chinese-addons-%{version}_dict.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/fcitx5-chinese-addons/fcitx5-chinese-addons-%{version}_dict.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  boost-complete
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-qt-devel
BuildRequires:  fcitx5-lua-devel
BuildRequires:  gcc-c++
BuildRequires:  libime-devel
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  gettext-tools libasprintf-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  /usr/bin/appstream-util
Requires:       icon-theme-hicolor
Requires:       %{name}-data = %{version}-%{release}
Requires:       fcitx5-lua
Requires:       fcitx5-data
Source44: import.info

Patch1: fcitx-upstream-use-isAndroid-functions.patch

%description
This provides pinyin and table input method
support for fcitx5. Released under LGPL-2.1+.

im/pinyin/emoji.txt is derived from Unicode 
CLDR with modification.

%package data
Group: Graphical desktop/Other
Summary:        Data files of %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       icon-theme-hicolor
Requires:       fcitx5-lua
Requires:       fcitx5-data

%description data
The %{name}-data package provides shared data for %{name}.

%package devel
Group: Graphical desktop/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
devel files for fcitx5-chinese-addons

%prep
%setup -q
%autopatch -p1


%build
%{fedora_v2_cmake} -GNinja
%fedora_v2_cmake_build 

%install
%fedora_v2_cmake_install

# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done 
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%check
# workaround for a testing failure due to not finding .dict files
%fedora_v2_ctest

%files -f %{name}.lang
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_bindir}/scel2org5
%{_libdir}/fcitx5/*.so
%{_libdir}/fcitx5/qt5/libpinyindictmanager.so
%{_libdir}/fcitx5/qt5/libcustomphraseeditor.so

%files data
%dir %{_datadir}/fcitx5/pinyin
%dir %{_datadir}/fcitx5/punctuation
%dir %{_datadir}/fcitx5/pinyinhelper
%{_datadir}/fcitx5/addon/*.conf
%{_datadir}/fcitx5/inputmethod/*.conf
%{_datadir}/fcitx5/lua/imeapi/extensions/pinyin.lua
%{_datadir}/fcitx5/pinyin/*.dict
%{_datadir}/fcitx5/pinyinhelper/py_*.mb
%{_datadir}/fcitx5/punctuation/punc.mb.*
%dir %{_datadir}/fcitx5/chttrans
%{_datadir}/fcitx5/chttrans/gbks2t.tab
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.ChineseAddons.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/*
%{_libdir}/cmake/Fcitx5Module*

%changelog
* Tue May 28 2024 Ivan A. Melnikov <iv@altlinux.org> 5.1.1-alt2_1
- NMU: fix FTBFS (ALT#49537)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_1
- update

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.15-alt1_2
- new version

