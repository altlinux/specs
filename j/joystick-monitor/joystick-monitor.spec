%global import_path github.com/Unrud/joystick-monitor

Name:    joystick-monitor
Version: 0.0.3
Release: alt1

Summary: Monitors gamepads/joysticks used by applications and inhibits the screen saver during activity
License: GPL-3.0
Group:   Other
Url:     https://github.com/Unrud/joystick-monitor
VCS:     https://github.com/Unrud/joystick-monitor.git

Source: %name-%version.tar
Source1: %name-vendor-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Monitors gamepads/joysticks used by applications and inhibits the screen
saver during activity.

Enable and start the service for the current user:
systemctl --user enable --now joystick-monitor

Enable service for all users:
sudo systemctl --global enable joystick-monitor

%prep
%setup -a1

sed -i '/^ExecStart=/c\ExecStart=%_bindir/%name' %name.service

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

install -Dpm644 %name.service %buildroot%_userunitdir/%name.service

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%files
%doc LICENSE README.md
%_bindir/joystick-monitor
%_userunitdir/%name.service

%changelog
* Wed Mar 05 2025 Sergey Palcheh <minergenon@altlinux.org> 0.0.3-alt1
- Initial build for Sisyphus
