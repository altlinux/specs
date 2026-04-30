%define _unpackaged_files_terminate_build 1

Name: tgcd
Version: 1.0.4
Release: alt2
Summary: TGC is the TCP Gender Changer 
License: GPL-2.0
Group: Networking/Remote access
Url: https://github.com/kirgene/tgcd

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: intltool
BuildRequires: gtk-doc

%description
tgcd is a simple Unix network utility to extend the accessibility of TCP/IP
based network services beyond firewalls.
This can also be used by network analysts and security experts for penetration
testing and analyze the security of their network.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure
%make_build CFLAGS="%optflags -std=gnu17" 

%install
%makeinstall_std

%files
%doc README
%_bindir/%name
%_man1dir/%name.*

%changelog
* Thu Apr 30 2026 Pavel Shilov <zerospirit@altlinux.org> 1.0.4-alt2
- Fix build by explicitly setting GCC standard.

* Fri Jul 25 2025 Pavel Shilov <zerospirit@altlinux.org> 1.0.4-alt1.1
- Update based on upstream.

* Tue Nov 19 2024 Pavel Shilov <zerospirit@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
