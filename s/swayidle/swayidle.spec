%define _unpackaged_files_terminate_build 1

Name: swayidle
Version: 1.8.0
Release: alt1
Summary: Idle management daemon for Wayland
License: MIT
Url: https://github.com/swaywm/swayidle
Group: Graphical desktop/Other

Source0: %name-%version.tar

BuildRequires: libsystemd-devel
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-server-devel
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: wayland-devel
BuildRequires: wayland-protocols


%description
This is sway's idle management daemon, swayidle. It is compatible with
any Wayland compositor which implements the KDE idle protocol.

%prep
%setup

%ifarch armh %{ix86}
sed -i -e "s/'werror=true'/'werror=false'/" meson.build
%endif

%build
%meson
%meson_build

%install
%meson_install

rm -rf -- \
	%buildroot/%_datadir/bash-completion \
	%buildroot/%_datadir/fish \
	%buildroot/%_datadir/zsh \
	#

%files
%doc LICENSE
%doc README.md
%_bindir/swayidle
%_man1dir/*

%changelog
* Sun Dec 04 2022 Alexey Gladkov <legion@altlinux.ru> 1.8.0-alt1
- New version (1.8.0)

* Sat Jan 15 2022 Alexey Gladkov <legion@altlinux.ru> 1.7.1-alt1
- New version (1.7.1)

* Fri Mar 27 2020 Alexey Gladkov <legion@altlinux.ru> 1.6-alt1
- New version (1.6)

* Mon Nov 18 2019 Alexey Gladkov <legion@altlinux.ru> 1.3-alt2
- Remove libelogind-devel.

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 1.3-alt1
- 1.3

* Tue Apr 02 2019 Alexey Gladkov <legion@altlinux.ru> 1.2-alt1.git3e392e3
- Initial build
