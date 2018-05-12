
%global import_path github.com/containernetworking/cni
%global commit a7885cb6f8ab03fba07852ded351e4f5e7a112bf
#%%global shortcommit %(c=%commit; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%define _libexecdir /usr/libexec
%define cni_dir %_libexecdir/cni
%define cni_etc_dir %_sysconfdir/cni

Name: cni
Version: 0.6.0
Release: alt1%ubt
Summary: Container Network Interface - networking for Linux containers
Group: Development/Other
License: ASL 2.0
Url: https://%import_path
Source: %name-%version.tar
ExclusiveArch: %go_arches

Provides: containernetworking-cni = %EVR

BuildRequires(pre): rpm-build-golang rpm-build-ubt
BuildRequires: /proc

%description
The CNI (Container Network Interface) project consists of a
specification and libraries for writing plugins to configure
network interfaces in Linux containers, along with a number of
supported plugins. CNI concerns itself only with network
connectivity of containers and removing allocated resources when
the container is deleted. Because of this focus, CNI has a wide
range of support and the specification is simple to implement.


%prep
%setup -q

%build
./build.sh

%install
mkdir -p %buildroot{%cni_dir,%cni_etc_dir/net.d,%_sbindir}
install -m0755 bin/noop %buildroot%cni_dir/
install -m0755 bin/cnitool %buildroot%_sbindir/

%files
%doc LICENSE README.md ROADMAP.md SPEC.md Documentation/*
%dir %cni_etc_dir
%dir %cni_etc_dir/net.d
%dir %cni_dir
%cni_dir/*
%_sbindir/*

%changelog
* Sat May 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1%ubt
- Initial package
