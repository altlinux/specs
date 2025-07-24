%define _unpackaged_files_terminate_build 1

Name: pwnat
Version: 0.3.0
Release: alt2
Summary: Allows clients behind NAT to communicate without any port forwarding 
License: GPL-3.0
Group: Networking/Remote access
Url: https://github.com/samyk/pwnat

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
The only tool/technique to punch holes through firewalls/NATs
where multiple clients & server can be behind separate NATs
without any 3rd party involvement. Pwnat is a newly developed technique,
exploiting a property of NAT translation tables, with no 3rd party,
port forwarding, DMZ, DNS, router admin requirements, STUN/TURN/UPnP/ICE,
or spoofing.

%prep
%setup
%patch -p1

%build
%make_build CFLAGS="%optflags"

%install
%make_install
install -Dm755 %name %buildroot%_bindir/%name
install -Dm0644 manpage.txt %buildroot%_man1dir/%name.1

%files
%doc README.md README-udptunnel COPYING-pingtunnel
%_bindir/%name
%_man1dir/%name.1

%changelog
* Thu Jul 24 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.0-alt2
- Update based on upstream.

* Fri Jul 26 2024 Pavel Shilov <zerospirit@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
