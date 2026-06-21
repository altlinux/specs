# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_with doc
Name: beremiz
Version: 1.5
Release: alt0.1.20260619.1

Summary: Integrated development environment for machine automation
Summary(ru_RU.UTF-8): Интегрированная среда разработки для ПЛК

License: GPL-3.0-or-later
Group: Engineering
URL: https://github.com/beremiz/beremiz
VCS: https://github.com/beremiz/beremiz.git

Source: %name-%version.tar
Source1: %name-256x256.png

Patch: %name-%version-%release.patch

Buildarch: noarch
BuildPreReq: rpm-build-python3 desktop-file-utils

%if_with doc
BuildRequires(pre): python3-module-sphinx
%endif #doc

Requires: matiec
Requires: gcc-c++
#Requires: CanFestival-3-source
#Requires: beremiz-modbus-source
#Requires: bacnet-stack-source
#Requires: avahi-daemon
# for build svghmi
Requires: inkscape
%py3_requires service_identity
# for wamp
%py3_requires twisted.internet.wxsupport
%py3_requires msgpack

# False Dependency
%add_python3_req_skip posix_spawn

# for ethercat
%add_python3_req_skip MotionLibrary

# for canfestival
%add_python3_req_skip commondialogs
%add_python3_req_skip eds_utils 
%add_python3_req_skip gen_cfile 
%add_python3_req_skip networkeditortemplate
%add_python3_req_skip nodeeditortemplate
%add_python3_req_skip nodelist
%add_python3_req_skip nodemanager
%add_python3_req_skip subindextable

Obsoletes: python-module-beremiz < 1.4
Obsoletes: python-module-beremiz-tests < 1.4

AutoProv: nopython3

%add_python3_path %_datadir/%name

%description
Beremiz is an integrated development environment for machine
automation. It is Free Software, conforming to IEC-61131 among
other standards.

It relies on open standards to be independent of the targeted
device, and let you turn any processor into a PLC. Beremiz
includes tools to create HMI, and to connect your PLC programs
to existing supervisions, databases, or fieldbuses.

%description -l ru_RU.UTF-8
Beremiz - это интегрированная среда разработки для ПЛК.
Является свободным программным обеспечением, соответсвует стандарту
МЭК-61131 и другим стандартам.

Beremiz опирается на открытые стандарты, которые не зависят от целевых
устройств. Так что вы можете превратить любой процессор в ПЛК. Beremiz
включает инструменты для создания HMI и подключения ваших программ PLC
к наблюдению, базам данным или полевым шинам.

%prep
%setup -n %name-%version
%autopatch -p1

%build
%if_with doc
pushd doc
make html
make man
popd
%endif #doc

%install
mkdir -p %buildroot%_datadir/%name
cp -r . %buildroot%_datadir/%name
rm -r %buildroot%_datadir/%name/doc \
       %buildroot%_datadir/%name/i18n

mv %buildroot%_datadir/%name/tests/projects %buildroot%_datadir/%name/
rm -r %buildroot%_datadir/%name/tests

%if_with doc
mkdir -p %buildroot%_man1dir
cp -r doc/_build/man/*.1 %buildroot%_man1dir
%endif #doc

## == install icons
install -pDm 644 %SOURCE1 %buildroot%_iconsdir/hicolor/256x256/apps/%name.png

### == executable file beremiz
cat>%name<<END
#!/bin/sh
[ -z "\$WAYLAND_DISPLAY" ] || export GDK_BACKEND=x11
%__python3 %_datadir/%name/Beremiz.py $*
END

mkdir -p %buildroot%_bindir/
install -m 755 %name %buildroot%_bindir/%name

### == executable file beremiz-service
cat>%name-service<<END
#!/bin/sh
[ -z "\$WAYLAND_DISPLAY" ] || export GDK_BACKEND=x11
%__python3 %_datadir/%name/Beremiz_service.py $*
END

mkdir -p %buildroot%_bindir/
install -m 755 %name-service %buildroot%_bindir/%name-service

### == desktop file beremiz
cat>%name.desktop<<END
[Desktop Entry]
Name=Beremiz
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=IDE;Development;
END

desktop-file-install --dir=%buildroot%_desktopdir %name.desktop

### == desktop file beremiz-doc
cat>%name-doc.desktop<<END
[Desktop Entry]
Name=Documentation for Beremiz
Name[ru_RU]=Документация для Beremiz
Exec=%_bindir/xdg-open %_docdir/%name-%version/html/index.html
Icon=%name
Terminal=false
Type=Application
Categories=IDE;Development;
END

desktop-file-install --dir=%buildroot%_desktopdir %name-doc.desktop

### == drop shebang
sed -i '/!\/usr\/bin\//d' \
  $(find %buildroot%_datadir/%name -type f -name "*.py")

### == drop executetable bit
chmod 644  $(find %buildroot%_datadir/%name -type f -name "*.py")

%files
%_bindir/%name
%_bindir/%name-service
%_iconsdir/hicolor/256x256/apps/%name.png
%_desktopdir/%name.desktop
%doc README.md COPYING_*
%if_with doc
%_man1dir/*.1.*
%doc doc/_build/html/
%_desktopdir/%name-doc.desktop
%endif #doc
%_datadir/%name
# opc_ua required python3-module-asyncio
#exclude %_datadir/%name/opc_ua
# canfestival required canfestival_config ???
#exclude %_datadir/%name/canfestival
# etherlab required MotionLibrary
#exclude %_datadir/%name/etherlab

%changelog
* Sat Jun 20 2026 Anton Midyukov <antohami@altlinux.org> 1.5-alt0.1.20260619.1
- New snapshot.

* Fri Jun 05 2026 Anton Midyukov <antohami@altlinux.org> 1.5-alt0.1.20260530.1
- New snapshot.

* Tue Feb 24 2026 Anton Midyukov <antohami@altlinux.org> 1.5-alt0.1.20260224.1
- New snapshot.

* Thu Jan 08 2026 Anton Midyukov <antohami@altlinux.org> 1.5-alt0.1.20260106.1
- New develop version 1.5.

* Mon Dec 22 2025 Anton Midyukov <antohami@altlinux.org> 1.4-alt0.1.20251222.1
- New snapshot.

* Mon Nov 24 2025 Anton Midyukov <antohami@altlinux.org> 1.4-alt0.1.20250821.2
- do not use dos2unix

* Sun Aug 24 2025 Anton Midyukov <antohami@altlinux.org> 1.4-alt0.1.20250821.1
- new snapshot

* Wed Jun 18 2025 Anton Midyukov <antohami@altlinux.org> 1.4-alt0.0.20250506.1
- new snapshot

* Mon Nov 25 2019 Anton Midyukov <antohami@altlinux.org> 1.2-alt7.20190221
- fix shebang
- beremiz.desktop: run in terminal

* Sat Sep 21 2019 Anton Midyukov <antohami@altlinux.org> 1.2-alt6.20190221
- add_python_req_skip autobahn

* Mon May 13 2019 Anton Midyukov <antohami@altlinux.org> 1.2-alt5.20190221
- fix build without doc

* Wed Apr 03 2019 Anton Midyukov <antohami@altlinux.org> 1.2-alt4.20190221
- New snapshot

* Mon Dec 03 2018 Anton Midyukov <antohami@altlinux.org> 1.2-alt3.20181012
- New snapshot

* Fri Sep 07 2018 Anton Midyukov <antohami@altlinux.org> 1.2-alt2.20180816
- New snapshot
- Added support protocols: modbus and BACnet
- Fix tests

* Wed Jun 06 2018 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20180523
- New snapshot

* Sat Mar 10 2018 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20180305
- New snapshot

* Thu Sep 28 2017 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20170917
- New snapshot

* Mon Sep 04 2017 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20170828
- New snapshot

* Sun Jul 09 2017 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20170705
- New snapshot
- Added missing requires.

* Sat Jul 01 2017 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20170628
- Initial build for ALT Linux Sisyphus.

