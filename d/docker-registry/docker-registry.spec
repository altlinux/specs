%global import_path github.com/docker/distribution
Name:     docker-registry
Version:  2.7.1
Release:  alt1

Summary:  The Docker toolset to pack, ship, store, and deliver content
License:  Apache-2.0
Group:    Other
Url:      https://github.com/docker/distribution

Packager: Mikhail Gordeev <obirvalger@altlinux.org>


Source:   %name-%version.tar
Source1:  docker-registry.service
Source2:  config.yml

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/registry

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mv %buildroot%_bindir/{,docker-}registry

install -pDm 0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -pDm 0644 %SOURCE2 %buildroot%_sysconfdir/%name/config.yml

mkdir -p %buildroot/%_localstatedir/%name

%files
%_bindir/docker-registry
%doc README.md
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.yml
%_unitdir/%name.service
%dir %_localstatedir/%name

%changelog
* Thu Apr 02 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.7.1-alt1
- new version 2.7.1

* Thu Sep 27 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.6.2-alt1
- Initial build for Sisyphus
