Name: ifupdown2
Version: 3.2.0.9
Release: alt1
Summary: Network Interface Management tool similar to ifupdown
License: GPL-2
Group: System/Base
Url: https://git.proxmox.com/?p=ifupdown2.git
Vcs: https://github.com/CumulusNetworks/ifupdown2.git

Source0: %name-%version.tar
Source1: %name.tar
Source2: ip-brctl
Source3: ip-brctl.8
Patch1: 0001-ALT-change-path-to-ifup-ifdown-ifreload.patch
Patch2: 0002-ALT-python-3.12-compatibility.patch
Patch3: ALT-do-not-run-scripts-rpmnew-rpmsave.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: /usr/bin/rst2man python3-module-Pygments

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

%prep
%setup
tar -xf %SOURCE1
pushd %name
%patch1 -p1
%patch2 -p1
for p in `cat ../debian/patches/series`; do
    patch -p1 < ../debian/patches/$p
done
%patch3 -p1
popd

%build

%install
pushd %name
python3 setup.py install --root=%buildroot --prefix=%_prefix
ifupdown2/man/genmanpages.sh ifupdown2/man .
popd

install -pD -m644 %name/etc/network/%name/addons.conf %buildroot%_sysconfdir/network/%name/addons.conf
install -pD -m644 %name/etc/network/%name/ifupdown2.conf %buildroot%_sysconfdir/network/%name/ifupdown2.conf
install -pD -m644 debian/proxmox-bridge-mac-from-port.json %buildroot/var/lib/%name/policy.d/proxmox-bridge-mac-from-port.json

install -dm755 %buildroot%_datadir/%name/sbin
install -dm755 %buildroot%_sbindir
ln -s %python3_sitelibdir_noarch/%name/__main__.py %buildroot%_datadir/%name/%name
ln -s %_datadir/%name/%name %buildroot%_datadir/%name/sbin/ifup
ln -s %_datadir/%name/%name %buildroot%_datadir/%name/sbin/ifdown
ln -s %_datadir/%name/%name %buildroot%_datadir/%name/sbin/ifquery
ln -s %_datadir/%name/%name %buildroot%_datadir/%name/sbin/ifreload
ln -s %_datadir/%name/%name %buildroot%_sbindir/ifquery
ln -s %_datadir/%name/%name %buildroot%_sbindir/ifreload
chmod a+x %buildroot%python3_sitelibdir_noarch/%name/__main__.py

install -pD -m644 debian/%name.networking.service %buildroot%_unitdir/%name.networking.service
install -pD -m644 debian/%name-pre.service %buildroot%_unitdir/%name-pre.service
install -pD -m644 debian/ifup@.service %buildroot%_unitdir/ifup@.service

install -pD -m644 %SOURCE2 %buildroot%_sbindir/ip-brctl
install -pD -m644 %SOURCE3 %buildroot%_man8dir/ip-brctl.8
ln -s %_sbindir/ip-brctl %buildroot%_sbindir/brctl

install -dm755 %buildroot%_sysconfdir/network/interfaces.d %buildroot%_sysconfdir/network/%name/policy.d
install -dm755 %buildroot/var/lib/%name/{hooks,policy.d}

install -dm755 %buildroot%_man5dir %buildroot%_man8dir
mv %name/%name/man/*.5 %buildroot%_man5dir
mv %name/%name/man/*.8 %buildroot%_man8dir

rm -rf %buildroot%python3_sitelibdir_noarch/*.egg-info
rm -f %buildroot%_bindir/if*

%post
if [ "$1" -eq 1 ]; then
    mkdir -p /etc/iproute2/rt_tables.d/
    touch /etc/iproute2/rt_tables.d/ifupdown2_vrf_map.conf
fi

%files
%doc %name/docs/README.rst debian/copyright
%_sysconfdir/default/networking
%_sysconfdir/network
%_unitdir/*
/var/lib/%name
%_sbindir/*
%_datadir/%name
%_man5dir/*
%_man8dir/*
%python3_sitelibdir_noarch/*

%changelog
* Wed Oct 16 2024 Alexey Shabalin <shaba@altlinux.org> 3.2.0.9-alt1
- 3.2.0-1+pmx9
- Do not run scripts ending with .rpm{new,save}

* Wed Apr 17 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.0.8-alt2
- ALT: python-3.12 compatibility

* Mon Dec 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.2.0.8-alt1
- Initial build for ALT.

