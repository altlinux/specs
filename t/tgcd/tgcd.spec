%define _unpackaged_files_terminate_build 1

Name: tgcd
Version: 1.0.4
Release: alt1
Summary: TGC is the TCP Gender Changer 
License: GPL-2.0
Group: Networking/Remote access
Url: https://github.com/kirgene/tgcd

Source: %name-%version.tar

BuildRequires: intltool
BuildRequires: gtk-doc

%description
tgcd is a simple Unix network utility to extend the accessibility of TCP/IP
based network services beyond firewalls.
This can also be used by network analysts and security experts for penetration
testing and analyze the security of their network.

%prep
%setup

%build
%autoreconf
%configure
%make_build CFLAGS="%optflags"

%install
%makeinstall_std

%files
%doc README
%_bindir/%name
%_man1dir/%name.*

%changelog
* Tue Nov 19 2024 Pavel Shilov <zerospirit@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
