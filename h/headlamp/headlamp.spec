%define _unpackaged_files_terminate_build 1
%global import_path github.com/kubernetes-sigs/headlamp

Name: headlamp
Version: 0.41.0
Release: alt1
Summary: Headlamp is an easy-to-use and extensible Kubernetes web UI
License: Apache-2.0
Group: System/Configuration/Other
Url: https://github.com/kubernetes-sigs/headlamp
ExcludeArch: i586
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
A Kubernetes web UI that is fully-featured, user-friendly and extensible

%prep
%setup
sed -i '1s|#!.*env node|#!/usr/bin/node|' $(find plugins/ -type f)

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-buildmode=pie"
export LDFLAGS="-X github.com/kubernetes-sigs/headlamp/backend/pkg/kubeconfig.Version=%version"

%golang_prepare

cd $BUILDDIR/src/%import_path
%golang_build backend/cmd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

pushd $BUILDDIR/src/%import_path
install -dm 755 %buildroot%_datadir/%name
cp -pr plugins %buildroot%_datadir/%name
cp -pr frontend/build %buildroot%_datadir/%name/frontend
popd

mv \
    %buildroot%_bindir/cmd \
    %buildroot%_bindir/%name-server

install -pDm 644 %name.service %buildroot%_user_unitdir/%name.service

%files
%doc *.md
%dir %_datadir/%name
%_datadir/%name/plugins/
%_datadir/%name/frontend/
%_user_unitdir/%name.service
%_bindir/%name-server

%changelog
* Wed Apr 08 2026 Vladislav Tsarev <tyaplyapych@altlinux.org> 0.41.0-alt1
- new version

* Wed Dec 17 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 0.38.0-alt1
- initial build
