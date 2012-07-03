Name: snmpb
Version: 0.8
Release: alt2
License: GPL2
Packager: Evgenii Terechkov <evg@altlinux.org>
Summary: Graphical SNMP MIB browser written in QT
Source: %name-%version.tar.bz2
Patch0: %name-0.8-paths-alt.patch
Patch1: %name-0.8-gcc45-alt.patch

Source1: %name.desktop

Group: Networking/Other
URL: http://sourceforge.net/projects/snmpb

# Automatically added by buildreq on Mon Nov 15 2010 (-bi)
BuildRequires: ImageMagick-tools flex gcc-c++ libqt4-devel libqwt-devel libsmi-devel

Obsoletes: %name-mibs <= 0.8-alt1

%description
SnmpB is an SNMP (Simple Network Management Protocol) MIB
browser written in QT. It supports SNMPv1, SNMPv2c & SNMPv3.

SnmpB can browse/edit/load/add MIB files and can query SNMP
agents. It also supports agent discovery, trap events
and graph plotting.

%prep
%setup -n %name-%version
%patch0 -p1
%patch1 -p1
%build

pushd libsmi
%autoreconf
popd

make INSTALL_PREFIX=%_prefix

%install
make INSTALL_PREFIX=%buildroot%_prefix install
install -D -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
pushd app/images
for i in 16 32 48 64
do
        convert -resize $ix$i %name.png %name$i.png
        install -D -m 644 %name$i.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done
popd

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%doc todo.txt

%changelog
* Mon Nov 15 2010 Terechkov Evgenii <evg@altlinux.org> 0.8-alt2
- Fix build with gcc4.5
- Drop builtin mibs subpackage

* Sun Sep  6 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1
- 0.8

* Tue May 19 2009 Terechkov Evgenii <evg@altlinux.ru> 0.5-alt4
- MIBs and PIBs moved to standard localtion

* Mon May 18 2009 Terechkov Evgenii <evg@altlinux.ru> 0.5-alt3
- MIBs subpackage created (noarch)

* Sat May  9 2009 Terechkov Evgenii <evg@altlinux.ru> 0.5-alt2
- Build with gcc4.4 fixed

* Mon Jan  5 2009 Terechkov Evgenii <evg@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux Sisyphus
