%global import_path github.com/0x90shell/gamepad-osk
Name:    gamepad-osk
Version: 2.1.1
Release: alt1

Summary: Gamepad-controlled on-screen keyboard for Linux
License: MIT
Group:   Other
Url:     https://github.com/0x90shell/gamepad-osk

Source: %name-%version.tar
Patch0: gamepad-osk-2.1.1-alt1-fix-path-for-fonts.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang libSDL3-devel libSDL3_ttf-devel libwayland-client-devel
Requires: ttf-promtfont fonts-ttf-bpg-dejavu-sans

%description
%summary

%prep
%setup
%patch0 -p1

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

install -Dm0644 %name.udev %buildroot%_udevrulesdir/80-%name.rules

install -Dm0644 %name.service %buildroot%_unitdir/%name.service

%post -n %name
%post_service %name.service

%preun -n %name
%preun_service %name.service


%files
%doc *.md
%_bindir/%name
%_unitdir/%name.service
%_udevrulesdir/80-%name.rules

%changelog
* Mon Aug 24 2026 Artyom Bystrov <arbars@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus
