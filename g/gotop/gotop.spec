%global import_path github.com/xxxserxxx/gotop
Name:     gotop
Version:  4.2.0
Release:  alt1

Summary:  A terminal based graphical activity monitor inspired by gtop and vtop
License:  MIT-Festival
Group:    Other
Url:      https://github.com/xxxserxxx/gotop

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-golang rpm-build-xdg
BuildRequires: golang >= 1.21 rpm-build-golang

%description
%summary.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.Version=v%version -X main.Version=$(date +%%Y%%m%%dT%%H%%M%%S)"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/gotop

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_xdgconfigdir/%name
install -m 0644 build/gotop.conf %buildroot%_xdgconfigdir/%name/
install -m 0644 layouts/default %buildroot%_xdgconfigdir/%name/
install -m 0644 layouts/disk %buildroot%_xdgconfigdir/%name/
install -m 0644 layouts/htop %buildroot%_xdgconfigdir/%name/
install -m 0644 layouts/kitchensink %buildroot%_xdgconfigdir/%name/
install -m 0644 layouts//procs %buildroot%_xdgconfigdir/%name/

mkdir -p %buildroot%_man1dir
%buildroot%_bindir/%name --create-manpage > %buildroot%_man1dir/%name.1

%files
%_bindir/*
%dir %_xdgconfigdir/%name
%config(noreplace) %_xdgconfigdir/%name/*
%_man1dir/*
%doc *.md

%changelog
* Wed May 22 2024 Alexey Shabalin <shaba@altlinux.org> 4.2.0-alt1
- new version 4.2.0
- fix show --version
- fix License
- package configs
- package man page

* Wed Oct 27 2021 Mikhail Gordeev <obirvalger@altlinux.org> 4.1.2-alt1
- new version 4.1.2

* Tue Jun 08 2021 Mikhail Gordeev <obirvalger@altlinux.org> 4.1.1-alt1
- new version 4.1.1

* Wed Oct 28 2020 Mikhail Gordeev <obirvalger@altlinux.org> 4.0.1-alt1
- new version 4.0.1

* Fri Apr 03 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.5.0-alt1
- new version 3.5.0

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.0-alt1
- new version 3.0.0

* Tue Feb 19 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- new version 2.0.2

* Fri Feb 15 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Tue Feb 05 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
