%define _unpackaged_files_terminate_build 1
%define _localstatedir /var
%define _libexecdir /usr/libexec

Name: ovirt-vmconsole
Version: 1.0.9
Release: alt1
Summary: oVirt VM console
License: GPLv3
Group: Networking/Other
Url: http://www.ovirt.org
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-systemd
BuildRequires: python3-devel
BuildRequires: gettext
BuildRequires: openssh-clients
BuildRequires: openssh-server
BuildArch: noarch

%description
oVirt VM console proxy

%package host
Summary: oVirt VM console host components
Group: Networking/Other

Requires: %name = %EVR
Requires: openssh-server

%description host
oVirt VM console host components

%package proxy
Summary: oVirt VM console proxy components
Group: Networking/Other

Requires: %name = %EVR
Requires: openssh-clients

%description proxy
oVirt VM console proxy components

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --with-local-version="%name-%version-%release"
%make_build

%install
%makeinstall_std

find "%buildroot" -name .keep -exec rm {} \;

#
# Register services
#
install -dm 755 "%buildroot%_unitdir"
install -m 644 "src/ovirt-vmconsole-host/ovirt-vmconsole-host-sshd/ovirt-vmconsole-host-sshd.systemd" "%buildroot%_unitdir/ovirt-vmconsole-host-sshd.service"
install -m 644 "src/ovirt-vmconsole-proxy/ovirt-vmconsole-proxy-sshd/ovirt-vmconsole-proxy-sshd.systemd" "%buildroot%_unitdir/ovirt-vmconsole-proxy-sshd.service"

%pre
groupadd -r -f %name >/dev/null 2>&1 ||:
useradd -r -g %name -d %_datadir/%name/empty \
        -s /bin/sh -c "oVirt VM Console" %name >/dev/null 2>&1 ||:

%post host
%systemd_post ovirt-vmconsole-host-sshd.service

%postun host
%systemd_postun ovirt-vmconsole-host-sshd.service

%preun host
%systemd_preun ovirt-vmconsole-host-sshd.service

%post proxy
%systemd_post ovirt-vmconsole-proxy-sshd.service

%postun proxy
%systemd_postun ovirt-vmconsole-proxy-sshd.service

%preun proxy
%systemd_preun ovirt-vmconsole-proxy-sshd.service

%files
%dir %_datadir/%name
%dir %_sysconfdir/%name
%dir %python3_sitelibdir/ovirt_vmconsole
%python3_sitelibdir/ovirt_vmconsole/*
%exclude %python3_sitelibdir/ovirt_vmconsole/ovirt_vmconsole_host_*
%exclude %python3_sitelibdir/ovirt_vmconsole/ovirt_vmconsole_proxy_*

%_docdir/%name/
%_sysconfdir/pki/%name/

%files host
%_datadir/%name/ovirt-vmconsole-host/
%_libexecdir/ovirt-vmconsole-host-*
%_sysconfdir/%name/ovirt-vmconsole-host/
%python3_sitelibdir/ovirt_vmconsole/ovirt_vmconsole_host_*
%_unitdir/ovirt-vmconsole-host-sshd.service

%files proxy
%_datadir/%name/ovirt-vmconsole-proxy/
%_libexecdir/ovirt-vmconsole-proxy-*
%_sysconfdir/%name/ovirt-vmconsole-proxy/
%python3_sitelibdir/ovirt_vmconsole/ovirt_vmconsole_proxy_*
%_unitdir/ovirt-vmconsole-proxy-sshd.service

%changelog
* Sat Aug 28 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.9-alt1
- Initial build.

