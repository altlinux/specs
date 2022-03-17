%global import_path github.com/xtaci/kcptun
Name:     kcptun
Version:  20210922
Release:  alt1

Summary:  A Stable & Secure Tunnel based on KCP with N:M multiplexing and FEC.
License:  MIT
Group:    Other
Url:      https://github.com/xtaci/kcptun

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

%build
export LDFLAGS="-X main.VERSION=%version"
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build client server

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mv %buildroot%_bindir/server %buildroot%_bindir/%name-server
mv %buildroot%_bindir/client %buildroot%_bindir/%name-client

%files
%_bindir/%{name}*
%doc *.md
%doc examples

%changelog
* Wed Mar 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 20210922-alt1
- Initial build for Sisyphus
