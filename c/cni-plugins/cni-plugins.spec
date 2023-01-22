
%global import_path github.com/containernetworking/plugins
%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec
%define cni_dir %_libexecdir/cni
%define cni_etc_dir %_sysconfdir/cni

Name: cni-plugins
Version: 1.2.0
Release: alt1
Summary: Container Network Interface plugins
Group: Development/Other
License: Apache-2.0
Url: https://%import_path
Source: %name-%version.tar
Source2: %name.tmpfiles
ExclusiveArch: %go_arches

Provides: containernetworking-plugins = %EVR
Provides: container-network-stack = 1
BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

%description
The CNI (Container Network Interface) project consists of a
specification and libraries for writing plugins to configure
network interfaces in Linux containers, along with a number of
supported plugins. CNI concerns itself only with network
connectivity of containers and removing allocated resources when
the container is deleted. Because of this focus, CNI has a wide
range of support and the specification is simple to implement.

These are the additional CNI network plugins provided by
the containernetworking team.

%prep
%setup -q

# Use correct paths in cni-dhcp unitfiles
sed -i 's,/opt/cni/bin,%cni_dir,' plugins/ipam/dhcp/systemd/cni-dhcp.service

%build
./build_linux.sh

%install
mkdir -p %buildroot{%cni_dir,%cni_etc_dir/net.d,%_unitdir,%_tmpfilesdir}
install -m0755 bin/* %buildroot%cni_dir/

install -p -m0644 plugins/ipam/dhcp/systemd/cni-dhcp.service %buildroot%_unitdir
install -p -m0644 plugins/ipam/dhcp/systemd/cni-dhcp.socket %buildroot%_unitdir
install -p -m0644 %SOURCE2 %buildroot%_tmpfilesdir/%name.conf

%post
%post_service cni-dhcp

%preun
%preun_service cni-dhcp

%files
%doc LICENSE README.md
%dir %cni_etc_dir
%dir %cni_etc_dir/net.d
%dir %cni_dir
%cni_dir/*
%_unitdir/*
%_tmpfilesdir/*

%changelog
* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Jul 31 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt2
- add Provides: container-network-stack

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Sun Sep 05 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Mon Jul 19 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt0.rc1
- new version 1.0.0-rc1
- package cni-dhcp.service and cni-dhcp.socket

* Tue May 18 2021 Alexey Shabalin <shaba@altlinux.org> 0.9.1-alt1
- new version 0.9.1

* Sun Jan 17 2021 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Thu Sep 10 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.7-alt1
- new version 0.8.7

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.6-alt1
- new version 0.8.6

* Sat Mar 14 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.5-alt1
- 0.8.5

* Fri Dec 13 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.3-alt1
- 0.8.3

* Tue Sep 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.2-alt1
- 0.8.2

* Fri Jul 19 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.1-alt1
- updated to v0.8.1-35-gb6f1a69

* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.5-alt1
- 0.7.5

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.4-alt1
- 0.7.4

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt2
- rebuild for aarch64

* Sat May 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- Initial package

