
%global import_path github.com/containernetworking/cni

%global _unpackaged_files_terminate_build 1

Name: cni
Version: 1.1.2
Release: alt1
Summary: Container Network Interface - networking for Linux containers
Group: Development/Other
License: Apache-2.0
Url: https://%import_path
Source: %name-%version.tar
ExclusiveArch: %go_arches

Provides: containernetworking-cni = %EVR
Provides: cnitool = %EVR

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


%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux

CGO_ENABLED=0 GOGC=off go install -ldflags " \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.branch=$BRANCH \
    " -a -installsuffix nocgo ./...

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot%_datadir
rm -f %buildroot%_bindir/{noop,sleep}

%files
%doc LICENSE README.md ROADMAP.md SPEC.md Documentation/*
%_bindir/*

%changelog
* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- 1.1.2

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt1
- 1.1.1

* Thu Sep 10 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu Jul 18 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 0.6.0-alt3
- delete ubt macros from release

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt2
- rebuild for aarch64

* Sat May 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- Initial package
