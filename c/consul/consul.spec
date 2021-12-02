%global import_path github.com/hashicorp/consul
Name:     consul
Version:  1.10.4
Release:  alt1

Summary:  Consul is a tool for service discovery and configuration
License:  MPL-2.0
Group:    Other
Url:      https://github.com/hashicorp/consul

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Consul is a distributed, highly available, and data center aware solution to
connect and configure applications across dynamic, distributed infrastructure.

%prep
%setup
mkdir -p api vendor/github.com/hashicorp/consul
cp -a api vendor/github.com/hashicorp/consul/api
cp -a sdk vendor/github.com/hashicorp/consul/sdk

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Tue Nov 30 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.10.4-alt1
- new version 1.10.4

* Fri Nov 20 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.6-alt1
- Updated to upstream version 1.8.6 (Fixes: CVE-2019-9764, CVE-2019-12291,
  CVE-2020-7219, CVE-2020-7955, CVE-2020-12797, CVE-2020-13170, CVE-2020-13250).

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.3-alt1
- new version 1.4.3

* Thu Dec 27 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
