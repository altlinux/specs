%define _unpackaged_files_terminate_build 1

Name:		swayidle
Version:	1.2
Release:	alt1.git3e392e3

Summary:	idle management daemon for Wayland 

Url:		https://github.com/swaywm/swayidle
License:	MIT
Group:		Graphical desktop/Other

Source0:	%name-%version-%release.tar

BuildRequires: libelogind-devel
BuildRequires: libsystemd-devel
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-server-devel
BuildRequires: meson
BuildRequires: wayland-devel
BuildRequires: wayland-protocols


%description
This is sway's idle management daemon, swayidle. It is compatible with
any Wayland compositor which implements the KDE idle protocol.

%prep
%setup -n %name-%version-%release

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

%changelog
* Tue Apr 02 2019 Alexey Gladkov <legion@altlinux.ru> 1.2-alt1.git3e392e3
- Initial build
