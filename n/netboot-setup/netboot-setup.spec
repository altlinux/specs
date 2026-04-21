# SPDX-License-Identifier: GPL-3.0-or-later
%define _unpackaged_files_terminate_build 1

Name: netboot-setup
Version: 0.9
Release: alt1

Summary: Setting up a netboot server
Group: System/Configuration/Networking
License: GPLv3+

%define nbslib /usr/libexec/%name

BuildArch: noarch
ExcludeArch: %ix86 %mips armh riscv64 ppc64le

Requires: bash
Requires: coreutils
Requires: iproute2
Requires: systemd
Requires: dhcp-server
Requires: ipxe-bootimgs
Requires: alterator-net-iptables
Requires: nginx

Conflicts: alterator-dhcp
Conflicts: alterator-netinst

AutoReq: noshell, noshebang

Source: %name-%version.tar
Url: https://www.altlinux.org/NetInstall
Vcs: https://github.com/klark973/netboot-setup
Packager: Leonid Krivoshein <klark@altlinux.org>

%description
Scripts and dependencies for setting up a network boot server.
Only for x86_64, aarch64, loongarch64 and elbrus servers.

%package -n netboot-pxe
Summary: Legacy/PXE netboot server add-ons
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: xinetd
Requires: tftpd
AutoReq: noshell, noshebang

%description -n netboot-pxe
Add-ons for Legacy/PXE network boot server.

%package -n netboot-talos
Summary: Talos netboot server add-ons
Group: System/Configuration/Networking
Requires: netboot-pxe = %version-%release
Requires: curl
#Conflicts: netboot-std
#Conflicts: netboot-elbrus
AutoReq: noshell, noshebang

%description -n netboot-talos
Add-ons for Talos network boot server.

# This will be later
%ifdef PACKAGE_READY

%package -n netboot-adm
Summary: Administrative netboot server add-ons
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: sudo
AutoReq: noshell, noshebang

%description -n netboot-adm
Administrative add-ons for network boot server.

%package -n netboot-std
Summary: Standard netboot server add-ons
Group: System/Configuration/Networking
Requires: netboot-adm = %version-%release
Requires: nfs-server
Requires: vsftpd
Requires: samba
Requires: ldap-user-tools
Requires: samba-common-tools
Requires: samba-client
Conflicts: anonftp
Conflicts: netboot-talos
AutoReq: noshell, noshebang

%description -n netboot-std
Add-ons for standard network boot server and altboot.

%package -n netboot-elbrus
Summary: E2K netboot server add-ons
Group: System/Configuration/Networking
Requires: netboot-adm = %version-%release
Requires: e2fsprogs
Requires: fakeroot
Requires: sfdisk
Requires: vblade
Requires: kmod
Conflicts: netboot-talos
AutoReq: noshell, noshebang

%description -n netboot-elbrus
E2K-specific add-ons for a standard network boot server.

%endif

%prep
%setup -q
%autopatch -p1

%build
mkdir -p -- "%buildroot"/etc/nginx/sites-available.d
mkdir -p -- "%buildroot"/etc/sysconfig "%buildroot"/usr/libexec
sed -i -e "s,@NETBOOT_SETUP_BUILD_DATE@,$(date '+%%Y%%m%%d')," \
       -e "s,@NETBOOT_SETUP_VERSION@,%version," lib/common.sh
rm -f -- bin/{altboot-img,elbrus-img,netboot-adm}.sh
rm -f -- lib/{nb-admin,nfs-v4,samba-v4,vsftpd}.sh
for i in bin/*
do
    sed -i -E \
        -e 's|^(defconf)=.*$|readonly \1=/etc/sysconfig/%name|' \
        -e 's|^(libdir)=.*$|readonly \1=%nbslib|' "$i"
    mv -f -- "$i" "${i%%.sh}"
    chmod -- 0755 "${i%%.sh}"
done
mv -f -- bin "%buildroot"/usr/
mv -f -- lib "%buildroot%nbslib"/
:> "%buildroot/etc/sysconfig/%name"
:> "%buildroot/etc/nginx/sites-available.d/%name.conf"

%post
mkdir -p /srv/img /srv/boot /srv/public/netinst/mnt
cp -Lf /usr/share/ipxe/ipxe-arm64.efi /srv/boot/
cp -Lf /usr/share/ipxe/ipxe-x86_64.efi /srv/boot/

%preun
rmdir /srv/public/netinst/mnt 2>/dev/null ||:
rmdir /srv/public/netinst 2>/dev/null ||:
rm -f /srv/boot/ipxe-x86_64.efi
rm -f /srv/boot/ipxe-arm64.efi
rmdir /srv/boot 2>/dev/null ||:
rmdir /srv/img 2>/dev/null ||:

%post -n netboot-pxe
cp -Lf /usr/share/ipxe/ipxe-i386.efi /srv/boot/
cp -Lf /usr/share/ipxe/undionly.kpxe /srv/boot/

%preun -n netboot-pxe
rm -f /srv/boot/undionly.kpxe
rm -f /srv/boot/ipxe-i386.efi

%post -n netboot-talos
if [ ! -d /srv/talos ]; then
    mkdir -p /srv/talos
    chmod 775 /srv/talos
    u="$(%name --showuser)"
    [ -z "$u" ] || chgrp -f -- "$u" /srv/talos
fi

%preun -n netboot-talos
rmdir /srv/talos 2>/dev/null ||:

# This will be later
%ifdef PACKAGE_READY

%post -n netboot-elbrus
if [ "$1" = 1 ]; then
    # Load module after installation
    modprobe aoe >/dev/null 2>&1 ||:

    if [ ! -e /etc/modules ]; then
        echo "aoe" >/etc/modules
    else
        grep -qs -E '^aoe$' /etc/modules ||
            echo "aoe" >>/etc/modules
    fi
fi

%preun -n netboot-elbrus
if [ "$1" = 0 ]; then
    # Unload module before deleting package
    [ ! -e /etc/modules ] ||
        sed -i -e '/^aoe$/d' /etc/modules
    modprobe -r aoe >/dev/null 2>&1 ||:
fi

%endif

%files
%config(noreplace) %ghost /etc/nginx/sites-available.d/%name.conf
%config(noreplace) %ghost /etc/sysconfig/%name
%_bindir/%name
%dir %nbslib
%nbslib/common.sh
%nbslib/network.sh
%nbslib/nb-setup.sh
%nbslib/dhcpd-v4.sh
%nbslib/http-nginx.sh
%doc AUTHORS example.conf LICENSE README.md

%files -n netboot-pxe
%nbslib/tftpd-v4.sh

%files -n netboot-talos
%_bindir/talos-img

# This will be later
%ifdef PACKAGE_READY

%files -n netboot-adm
%nbslib/nb-admin.sh
%_bindir/netboot-adm

%files -n netboot-std
%nbslib/vsftpd.sh
%nbslib/nfs-v4.sh
%nbslib/samba-v4.sh
%_bindir/altboot-img

%files -n netboot-elbrus
%_bindir/elbrus-img

%endif

%changelog
* Wed Apr 22 2026 Leonid Krivoshein <klark@altlinux.org> 0.9-alt1
- Initial build for Sisyphus.

