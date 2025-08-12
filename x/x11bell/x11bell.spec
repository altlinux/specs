%define _unpackaged_files_terminate_build 1

Name: x11bell
Version: 1.1
Release: alt1

Summary: Replacement for the x11-bell pulseaudio module

License: MIT
Group: Development/Other
Url: https://github.com/jovanlanik/x11bell
Vcs: https://github.com/jovanlanik/x11bell

Source: %name-%version.tar

Patch1: x11bell-1.1-alt-adopt-make-install.patch

BuildRequires: libxcb-devel
BuildRequires: libX11-devel

%description
%summary

%prep
%setup
%patch1 -p1

%build
%make
%make_build

%install
install -D -m 0755 x11bell %buildroot%_bindir/x11bell

%files
%doc LICENCE README.md
%_bindir/%name

%changelog
* Thu May 27 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.1-alt1
- Initial build for ALT Sisyphus.
