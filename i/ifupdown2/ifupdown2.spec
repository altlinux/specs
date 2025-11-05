Name: ifupdown2
Version: 3.3.0.11
Release: alt1
Summary: Network Interface Management tool similar to ifupdown
License: GPL-2
Group: System/Base
Url: https://git.proxmox.com/?p=ifupdown2.git
Vcs: https://github.com/CumulusNetworks/ifupdown2.git

Source0: %name-%version.tar
Source1: %name.tar

Source2: resolvconf.if-up
Source3: resolvconf.if-down

Patch1: ifupdown2-3.2.0.11-alt-dont-use-dpkg-for-getting-version.patch
Patch3: ALT-do-not-run-scripts-rpmnew-rpmsave.patch
Patch4: ifupdown2-3.2.0.11-alt-replace-distutils-strtobool.patch

BuildArch: noarch

Provides: network-config-subsystem
Provides: /sbin/ifup /sbin/ifdown /sbin/ifquery /sbin/ifreload
Conflicts: etcnet
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: /usr/bin/rst2man python3-module-Pygments

# from ifupdown2/ifupdown/utils.py
Requires: /sbin/ip /usr/sbin/bridge /sbin/brctl /bin/pidof /usr/bin/pstree
Requires: /sbin/modprobe /sbin/sysctl /usr/bin/ss

#Recomended
#/usr/sbin/mstpctl /usr/sbin/vrrpd /usr/sbin/ifplugd

%description
Network Interface Management tool similar to ifupdown
ifupdown2 is ifupdown re-written in Python. It replaces ifupdown and provides
the same user interface as ifupdown for network interface configuration.
Like ifupdown, ifupdown2 is a high level tool to configure (or, respectively
deconfigure) network interfaces based on interface definitions in
/etc/network/interfaces. It is capable of detecting network interface
dependencies and comes with several new features which are available as
new command options to ifup/ifdown/ifquery commands. It also comes with a new
command ifreload to reload interface configuration with minimum
disruption. Most commands are also capable of input and output in JSON format.
It is backward compatible with ifupdown /etc/network/interfaces format and
supports newer simplified format. It also supports interface templates with
python-mako for large scale interface deployments. See
/usr/share/doc/ifupdown2/README.rst for details about ifupdown2. Examples
are available under /usr/share/doc/ifupdown2/examples.


%package -n resolvconf-ifupdown2
Summary: Hooks for setting up /etc/resolv.conf options via ifupdown2
Group: System/Base

Requires: %name
Requires: /sbin/resolvconf

%description -n resolvconf-ifupdown2
Hooks for setting up DNS-related options via ifupdown2,
using resolvconf utility


%prep
%setup
tar -xf %SOURCE1
pushd %name
%patch1 -p1
for p in `cat ../debian/patches/series`; do
    patch -p1 < ../debian/patches/$p
done
%patch3 -p1
%patch4 -p1

sed -i "s/__version__ =.*/__version__ = '%version'/g" ifupdown2/__init__.py

sed -i 's|/sbin/mstpctl|/usr/sbin/mstpctl|g' ifupdown2/addons/mstpctl.py
sed -i 's|/usr/sbin/ip|/sbin/ip|g' ifupdown2/ifupdownaddons/modulebase.py
sed -i 's|/sbin/bridge|/usr/sbin/bridge|g' ifupdown2/ifupdown/utils.py
sed -i 's|/bin/ip|/sbin/ip|g' ifupdown2/ifupdown/utils.py
sed -i 's|/usr/sbin/service|/sbin/service|g' ifupdown2/ifupdown/utils.py
sed -i 's|/bin/ss|/usr/bin/ss|g' ifupdown2/ifupdown/utils.py
sed -i 's|/sbin/mstpctl|/usr/sbin/mstpctl|g' ifupdown2/ifupdown/utils.py
sed -i 's|/sbin/ethtool|/usr/sbin/ethtool|g' ifupdown2/ifupdown/utils.py
popd

%build

%install
pushd %name
python3 setup.py install --root=%buildroot --prefix=%_prefix
ifupdown2/man/genmanpages.sh ifupdown2/man .
popd

install -pD -m644 %name/etc/network/%name/addons.conf %buildroot%_sysconfdir/network/%name/addons.conf
install -pD -m644 %name/etc/network/%name/ifupdown2.conf %buildroot%_sysconfdir/network/%name/ifupdown2.conf
install -pD -m644 debian/proxmox-bridge-mac-from-port.json %buildroot%_sharedstatedir/%name/policy.d/proxmox-bridge-mac-from-port.json

install -dm755 %buildroot%_datadir/%name/sbin
install -dm755 %buildroot%_sbindir
ln -r -s %buildroot%python3_sitelibdir_noarch/%name/__main__.py %buildroot%_datadir/%name/%name
chmod a+x %buildroot%python3_sitelibdir_noarch/%name/__main__.py
ln -r -s %buildroot%_datadir/%name/%name %buildroot%_sbindir/ifup
ln -r -s %buildroot%_datadir/%name/%name %buildroot%_sbindir/ifdown
ln -r -s %buildroot%_datadir/%name/%name %buildroot%_sbindir/ifquery
ln -r -s %buildroot%_datadir/%name/%name %buildroot%_sbindir/ifreload

install -pD -m644 debian/%name.networking.service %buildroot%_unitdir/networking.service
install -pD -m644 debian/%name-pre.service %buildroot%_unitdir/%name-pre.service
install -pD -m644 debian/ifup@.service %buildroot%_unitdir/ifup@.service

install -dm755 %buildroot%_sysconfdir/network/interfaces.d %buildroot%_sysconfdir/network/%name/policy.d
install -dm755 %buildroot/var/lib/%name/{hooks,policy.d}

install -dm755 %buildroot%_man5dir %buildroot%_man8dir
mv %name/%name/man/*.5 %buildroot%_man5dir
mv %name/%name/man/*.8 %buildroot%_man8dir

rm -rf %buildroot%python3_sitelibdir_noarch/*.egg-info
rm -f %buildroot%_bindir/if*

# Hooks for resolvconf
install -D -m755 %SOURCE2 %buildroot%_sysconfdir/network/if-up.d/resolvconf
install -D -m755 %SOURCE3 %buildroot%_sysconfdir/network/if-down.d/resolvconf

%post
if [ "$1" -eq 1 ]; then
    mkdir -p %_sysconfdir/iproute2/rt_tables.d
    touch %_sysconfdir/iproute2/rt_tables.d/ifupdown2_vrf_map.conf

fi
# Generic stuff done on all configurations
if [ -f %_sysconfdir/network/interfaces ] ; then
    if ! grep -q -E "^[[:space:]]*iface[[:space:]]+l[o0]([[:space:]]+inet([[:space:]]+loopback)?)?[[:space:]]*$" %_sysconfdir/network/interfaces ; then
        echo "No 'iface lo' definition found in /etc/network/interfaces"
    fi

    if ! grep -q "^[[:space:]]*\(allow-\|\)auto[[:space:]]\+\(.*[[:space:]]\+\|\)lo0\?\([[:space:]]\+\|$\)" %_sysconfdir/network/interfaces ; then
        echo "No 'auto lo' statement found in /etc/network/interfaces"
    fi
else  # ! -f %_sysconfdir/network/interfaces
    echo "Creating /etc/network/interfaces."
    echo "# interfaces(5) file used by ifup(8) and ifdown(8)" > %_sysconfdir/network/interfaces
    echo "source /etc/network/interfaces.d/*" >> %_sysconfdir/network/interfaces
    echo "auto lo" >> %_sysconfdir/network/interfaces
    echo "iface lo inet loopback" >> %_sysconfdir/network/interfaces
fi

%files
%doc %name/docs/README.rst debian/copyright
%_sysconfdir/default/networking
%_sysconfdir/network
%_unitdir/*
%_localstatedir/%name
%_sbindir/*
%_datadir/%name
%_man5dir/*
%_man8dir/*
%python3_sitelibdir_noarch/*
%dir %_sysconfdir/network/if-up.d
%dir %_sysconfdir/network/if-down.d
%exclude %_sysconfdir/network/if-up.d/*
%exclude %_sysconfdir/network/if-down.d/*

%files -n resolvconf-ifupdown2
%_sysconfdir/network/if-up.d/*
%_sysconfdir/network/if-down.d/*

%changelog
* Wed Nov 05 2025 Alexey Shabalin <shaba@altlinux.org> 3.3.0.11-alt1
- 3.3.0-1+pmx11

* Wed Sep 10 2025 Alexey Shabalin <shaba@altlinux.org> 3.3.0.10-alt1
- 3.3.0-1+pmx10

* Thu May 22 2025 Alexander Stepchenko <geochip@altlinux.org> 3.2.0.11-alt4
- Replace function from distutils
- Don't use dpkg for querying ifupdown2 version

* Mon Apr 14 2025 Sergey Konev <darisishe@altlinux.org> 3.2.0.11-alt3
- New subpackage with hooks for /etc/resolv.conf managment

* Fri Dec 13 2024 Alexey Shabalin <shaba@altlinux.org> 3.2.0.11-alt2
- Fix utils path
- Update requires

* Wed Nov 20 2024 Alexey Shabalin <shaba@altlinux.org> 3.2.0.11-alt1
- 3.2.0-1+pmx11
- Add Provides: network-config-subsystem
- Drop ip-brctl script
- Move ifup/ifdown/ifreload to /sbin
- Add Conflicts etcnet
- Rename systemd unit to networking.service
- Add create /etc/network/interfaces in %%post

* Wed Oct 16 2024 Alexey Shabalin <shaba@altlinux.org> 3.2.0.9-alt1
- 3.2.0-1+pmx9
- Do not run scripts ending with .rpm{new,save}

* Wed Apr 17 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.0.8-alt2
- ALT: python-3.12 compatibility

* Mon Dec 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.2.0.8-alt1
- Initial build for ALT.

