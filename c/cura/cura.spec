# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global with_check 1
%add_python3_compile_include %_libexecdir/cura

Name: cura
Epoch: 1
Version: 5.4.0
Release: alt3
Summary: 3D printer control software
License: LGPL-3.0-or-later

Group: Engineering
Url: https://github.com/Ultimaker/Cura

# Source-url: https://github.com/Ultimaker/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2: mod_bundled_packages_json.py
Source3: CuraPluginInstall.cmake
Source4: CuraTests.cmake
Source5: com.ultimaker.cura.desktop.in
Source6: CMakeLists.txt
Source7: CuraVersion.py.in
Source8: com.ultimaker.cura.appdata.xml

# PATCH-FIX-OPENSUSE -- avoid bad UI layout and crash in preview
Patch4: 0001-Avoid-crash-caused-by-KDE-qqc2-desktop-style.patch

# Fedora patch
# Skip forced loading SentryLogger to avoid an error on startup
Patch10: 028e7f7.patch
# Fix asserts for called once in Python 3.12
# https://github.com/Ultimaker/Cura/pull/16103.patch
Patch11: 16103.patch
# Avoid "KeyError: material_name" crash
# https://github.com/Ultimaker/Cura/pull/17642.patch
Patch12: 17642.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3 rpm-macros-cmake
BuildRequires: rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: python3-devel
BuildRequires: Uranium >= 5.4.0
BuildRequires: python3-module-pynest2d
# Tests
%if 0%{?with_check}
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pip
BuildRequires: python3-module-savitar >= 5.3.0
BuildRequires: python3-module-requests
BuildRequires: python3-module-keyring >= 21
BuildRequires: python3-module-dbus
BuildRequires: python3(importlib_metadata)
%endif

%py3_requires serial zeroconf
%py3_requires stl
Requires: python3-module-savitar
Requires: Uranium = 5.4.0
Requires: CuraEngine = %epoch:%version
Requires: cura-fdm-materials
Requires: 3dprinter-udev-rules
Requires: python3-module-keyring >= 21
Requires: qt6-declarative
Requires: qt6-svg
# need for plugins
Requires: python3-module-Charon
Requires: python3-module-trimesh

%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura prepares your model for 3D printing. For novices, it makes it easy to get
great results. For experts, there are over 200 settings to adjust to your
needs. As it's open source, our community helps enrich it even more.

# see: https://github.com/Ultimaker/Cura/issues/5142
%define cura_cloud_api_root https://api.ultimaker.com
%define cura_cloud_api_version 1
%define cura_cloud_account_api_root https://account.ultimaker.com

%prep
%setup
%autopatch1 -p1

mkdir cmake
cp -a %SOURCE2 %SOURCE3 %SOURCE4 cmake
rm -rf CMakeLists.txt
cp -a %SOURCE5 %SOURCE6 %SOURCE8 .
cp -a %SOURCE7 cura

# Wrong end of line encoding
dos2unix docs/How_to_use_the_flame_graph_profiler.md

# Wrong shebang
%__subst '1s=^#!%_bindir/\(python\|env python\)3*=#!%__python3=' cura_app.py

# create empty keyrings
mkdir -p $HOME/.local/share/keyrings
echo 'default' > $HOME/.local/share/keyrings/default

cat > $HOME/.local/share/keyrings/default.keyring << EOF
[keyring]
display-name=default
ctime=1559811805
mtime=0
lock-on-idle=false
lock-after=false
EOF

%build
%cmake -DCURA_VERSION:STRING=%version \
       -DCURA_BUILDTYPE=RPM \
       -DCURA_CLOUD_API_ROOT:STRING=%cura_cloud_api_root \
       -DCURA_CLOUD_API_VERSION:STRING=%cura_cloud_api_version \
       -DCURA_CLOUD_ACCOUNT_API_ROOT:STRING=%cura_cloud_account_api_root \
       -DLIB_SUFFIX:STR=
%cmake_build

%install
%cmake_install

mkdir -p %buildroot%_datadir/%name/resources/images/whats_new
mkdir -p %buildroot%_datadir/%name/resources/texts/whats_new
mkdir -p %buildroot%_datadir/%name/resources/scripts

# Remove failing plugins
rm -r %buildroot%_prefix/lib/cura/plugins/{SentryLogger,UFPReader,UFPWriter}

%find_lang cura fdmextruder.def.json fdmprinter.def.json --output=%name.lang

%check
%if 0%{?with_check}
%__python3 -m pip freeze
%__python3 -m pytest -v
%endif

desktop-file-validate %buildroot%_datadir/applications/com.ultimaker.cura.desktop

%files -f %name.lang
%doc LICENSE README.md
%python3_sitelibdir/%name
%_datadir/%name
%_desktopdir/com.ultimaker.cura.desktop
%_datadir/metainfo/com.ultimaker.cura.appdata.xml
%_iconsdir/hicolor/*/apps/%name-icon.png
%_datadir/mime/packages/%name.xml
%_bindir/%name
%_libexecdir/%name

%changelog
* Tue Jun 18 2024 Anton Midyukov <antohami@altlinux.org> 1:5.4.0-alt3
- add dependency on python3(stl) (Closes: 49331)
- spec: convert License to SPDX format

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 1:5.4.0-alt2
- fix build with python 3.12

* Mon Dec 18 2023 Anton Midyukov <antohami@altlinux.org> 1:5.4.0-alt1
- new version (5.4.0) with rpmgs script

* Thu Apr 27 2023 Anton Midyukov <antohami@altlinux.org> 1:5.3.1-alt1
- new version (5.3.1) with rpmgs script (Closes: 43069)

* Mon Mar 06 2023 Anton Midyukov <antohami@altlinux.org> 1:4.13.0-alt3
- add 'BuildRequires: python3(importlib_metadata)' for fix build with check

* Sat Mar 05 2022 Anton Midyukov <antohami@altlinux.org> 1:4.13.0-alt2
- add requires for plugins

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 1:4.13.0-alt1
- new version (4.13.0) with rpmgs script

* Mon Dec 13 2021 Anton Midyukov <antohami@altlinux.org> 1:4.12.1-alt1
- new version (4.12.1) with rpmgs script

* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 1:4.11.0-alt1
- new version (4.11.0) with rpmgs script

* Tue Apr 20 2021 Anton Midyukov <antohami@altlinux.org> 1:4.8-alt2
- merge with p9

* Wed Apr 14 2021 Anton Midyukov <antohami@altlinux.org> 1:4.7.1-alt1.p9
- Use qt style gtk instead material

* Sun Nov 15 2020 Anton Midyukov <antohami@altlinux.org> 1:4.8-alt1
- New version 4.8

* Fri Sep 18 2020 Anton Midyukov <antohami@altlinux.org> 1:4.7.1-alt1
- New version 4.7.1

* Thu May 07 2020 Anton Midyukov <antohami@altlinux.org> 1:4.6.1-alt1
- New version 4.6.1

* Tue Mar 24 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt2
- Avoid crash caused by KDE qqc2 desktop style

* Sun Jan 26 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt1.1
- Fix requires

* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt1
- New version 4.4.1

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.6.0-alt2.1
- NMU: remove rpm-build-ubt from BR:

* Fri Apr 19 2019 Anton Midyukov <antohami@altlinux.org> 1:3.6.0-alt1.1
- Not rebuild locales files

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 1:3.6.0-alt1
- New version 3.6.0

* Wed Oct 31 2018 Anton Midyukov <antohami@altlinux.org> 1:3.5.1-alt1
- New version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 1:3.4.1-alt1
- New version 3.4.1

* Mon May 07 2018 Anton Midyukov <antohami@altlinux.org> 1:3.3.0-alt1.S1
- New version 3.3.0

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 1:3.2.1-alt1.S1
- New version 3.2.1
- Disable tests

* Sat Jan 06 2018 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt2
- Fix fail start with nvidia proprietary driver.

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt1
- New version 3.0.3

* Wed Dec 13 2017 Anton Midyukov <antohami@altlinux.org> 1:2.4.0-alt1
- New version 2.4.0

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt3
- NMU: sync with fc cura-15.04.4-4

* Thu Mar 17 2016 Andrey Cherepanov <cas@altlinux.org> 15.04.4-alt2
- Initial build in Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt1_2
- update to new release by fcimport

* Thu Nov 26 2015 Igor Vlasenko <viy@altlinux.ru> 15.02.1-alt1_4
- new version

