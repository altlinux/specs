Name: corectrl
Version: 1.3.3
Release: alt1
Summary: Core control application
Group: System/Configuration/Hardware
License: GPLv3
Url: https://gitlab.com/%name/%name
Source: https://gitlab.com/%name/%name/-/archive/v%{version}/%name-%version.tar
Patch: %name-%version-%release.patch
Source1: 90-%name.rules
Source2: %name.control

BuildRequires(pre): cmake
# Automatically added by buildreq on Sun Oct 02 2022
BuildRequires: libbotan-devel libdbus-devel libdrm-devel libpolkit-devel qt5-charts-devel qt5-svg-devel qt5-tools-devel quazip-qt5-devel
BuildRequires: libfmt-devel >= 5.0, libpugixml-devel >= 1.11 ctest

%description
CoreCtrl is a Free and Open Source GNU/Linux application that allows you to
control with ease your computer hardware using application profiles. It aims to
be flexible, comfortable and accessible to regular users.

%prep
%setup
%patch -p1
# stdc++fs is a part of libstdc++ on linux
find . -name CMakeLists.txt -exec sed -i -e 's/stdc++fs/stdc++/g' {} \;

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_TESTING=TRUE \
  -DWITH_PCI_IDS_PATH=%_datadir/hwdatabase/pci.ids
%cmake_build

%check
make -C "%_cmake__builddir" test

%install
%cmake_install
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/polkit-1/rules.d/90-%name.rules
install -pD -m755 %SOURCE2 %buildroot%_controldir/%name

%pre
/usr/sbin/groupadd -r -f %name
if [ $1 -ge 2 -o -e %_bindir/%name ]; then
    %_sbindir/control-dump %name
fi

%post
echo 'Do not forget to add yourself into %name group before running %name for the first time!'
echo 'Or use control(8) command to tune access later.'
if [ $1 -ge 2 -o -e %_bindir/%name ]; then
    %_sbindir/control-restore %name
else
    %_sbindir/control %name %{name}only
fi

%files
%doc README.md CHANGELOG.md COPYING LICENSE CONTRIBUTING.md
%config %_controldir/*
%config %_sysconfdir/polkit-1/rules.d/*
%attr(710,root,%name) %_bindir/%name
%_libdir/lib%{name}.so
%_prefix/libexec/%name
%_desktopdir/org.%name.%name.desktop
%_datadir/dbus-1/system-services/org.%name.*.service
%_datadir/dbus-1/system.d/org.%name.*.conf
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/org.%name.%name.appdata.xml
%_datadir/polkit-1/actions/org.%name.*.policy

%changelog
* Fri Mar 03 2023 L.A. Kostis <lakostis@altlinux.ru> 1.3.3-alt1
- 1.3.3.
- Enable tests.
- Disable debug flags for build.

* Mon Feb 20 2023 L.A. Kostis <lakostis@altlinux.ru> 1.3.2-alt1
- 1.3.2.
- Use system fmt, pugixml.

* Fri Oct 14 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3.1-alt1
- 1.3.1.

* Sat Oct 08 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3.0-alt4
- Apply a proper patch from upstream to fix compilation w/
  linux 6.0+ headers (upstream #325).

* Wed Oct 05 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3.0-alt3
- Fix build w/ recent linux headers.

* Mon Oct 03 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3.0-alt1
- Sync with existing package from lav@.
- Applied a fix from master (Fix CPU performance scaling mode
  not being restored from file).

* Sun Oct 02 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3.0-alt0.1
- Initial build for ALTLinux.
