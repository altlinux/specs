Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 2

Name:       fcitx5-table-extra
Version:    5.0.11
Release:    alt1_%autorelease
Summary:    Extra tables for Fcitx5
License:    GPLv3+
URL:        https://github.com/fcitx/fcitx5-table-extra
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9
BuildArch:  noarch

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  boost-complete
BuildRequires:  cmake(Fcitx5Core)
#BuildRequires:  cmake(LibIMETable)
BuildRequires:  libime-devel
BuildRequires:  gettext gettext-tools
BuildRequires:  /usr/bin/appstream-util
Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Source44: import.info

%description
Extra tables for Fcitx5.
fcitx5-table-extra provides extra table for 
Fcitx5, including Boshiamy, Zhengma, Cangjie, 
and Quick.

%prep
%setup -q


%build
# %%{_libdir} expands to /usr/lib, even on 64bit platform, that we need to
# to this tricky thing
%{fedora_v2_cmake} -GNinja -DCMAKE_PREFIX_PATH="%{_libdir}/cmake;%{_libdir}64/cmake"
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
%files
%doc --no-dereference LICENSES/GPL-3.0-or-later.txt
%doc README NEWS AUTHORS 
%{_datadir}/fcitx5/table/*
%{_datadir}/fcitx5/inputmethod/*
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.TableExtra.metainfo.xml

%changelog
* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.11-alt1_2
- new version

