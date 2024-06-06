Name: wlr-protocols
Version: 20240126
Release: alt1

Summary: Wayland protocols designed for use in wlroots (and other compositors)
License: MIT
Group: Development/Other
Url: https://gitlab.freedesktop.org/wlroots/wlr-protocols

Vcs: https://gitlab.freedesktop.org/wlroots/wlr-protocols.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: wayland-devel

%define _unpackaged_files_terminate_build 1

%description
%summary.

%prep
%setup
#patch -p1

%build
%make_build

%install
%makeinstall_std

%files
%_datadir/pkgconfig/*.pc
%_datadir/%name/

%changelog
* Tue May 28 2024 Mikhail Efremov <sem@altlinux.org> 20240126-alt1
- Initial build.

