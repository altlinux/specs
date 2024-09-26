%global import_path github.com/ikemen-engine/Ikemen-GO
Name:    Ikemen-GO
Version: 0.99.0
Release: alt1

Summary: An open-source fighting game engine that supports MUGEN resources.
License: MIT
Group:   Games/Arcade
Url:     https://github.com/ikemen-engine/Ikemen-GO

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: vendor.tar
Source2: Ikemen_GO.sh

ExcludeArch: aarch64

BuildRequires(pre): rpm-build-golang
BuildRequires: golang libX11-devel libXcursor-devel libXrandr-devel libXinerama-devel libXi-devel libGL-devel libalsa-devel libgtk+3-devel libXxf86vm-devel
Requires: Ikemen_GO-Elecbyte-Screenpack

%description
%summary

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
make Ikemen_GO_Linux

%install
mkdir -p %buildroot%_datadir/%name
install -Dm0755 ./bin/Ikemen_GO_Linux %buildroot%_libexecdir/%name
install -Dm0755 %SOURCE2 %buildroot%_bindir/%name
for res in data font external; do
cp -r $res %buildroot%_datadir/%name
done

%files
%doc *.md
%_bindir/%name
%_libexecdir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/*
%dir %_datadir/%name/font
%_datadir/%name/font/*
%dir %_datadir/%name/external
%_datadir/%name/external/*

%changelog
* Wed Sep 25 2024 Artyom Bystrov <arbars@altlinux.org> 0.99.0-alt1
- Initial build for Sisyphus
