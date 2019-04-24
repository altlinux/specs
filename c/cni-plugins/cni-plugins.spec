
%global import_path github.com/containernetworking/plugins
%global commit 9ebe139e77e82afb122e335328007bca86905ae4
#%%global shortcommit %(c=%commit; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%define _libexecdir /usr/libexec
%define cni_dir %_libexecdir/cni

Name: cni-plugins
Version: 0.7.5
Release: alt1
Summary: Container Network Interface plugins
Group: Development/Other
License: ASL 2.0
Url: https://%import_path
Source: %name-%version.tar
ExclusiveArch: %go_arches

Provides: containernetworking-plugins = %EVR

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

Requires: cni

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

%build
./build.sh

%install
mkdir -p %buildroot%cni_dir
install -m0755 bin/* %buildroot%cni_dir/

%files
%doc LICENSE README.md
%cni_dir/*

%changelog
* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.5-alt1
- 0.7.5

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.4-alt1
- 0.7.4

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt2%ubt
- rebuild for aarch64

* Sat May 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1%ubt
- Initial package

