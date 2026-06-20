# TODO: add netbird-management, netbird-signal and netbird-relay 
%global import_path github.com/netbirdio/netbird
%define _unpackaged_files_terminate_build 1
%define commit      4eed459f27bd7e90faa7fe99e1edf4a59dc71265
%define shortcommit %(c=%commit; echo ${c:0:8})

Name: netbird
Version: 0.73.1
Release: alt1

Summary: Mesh VPN based on WireGuard
License: BSD-3-Clause
Group: System/Servers

Url: https://netbird.io
Vcs: https://github.com/netbirdio/netbird.git

Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: netbird.service
Source3: config.json

Patch: %name-%version-%release.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang

%description
NetBird combines a configuration-free peer-to-peer private network 
and a centralized access control system in a single platform, making 
it easy to create secure private networks for your organization or home.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS="-X github.com/netbirdio/netbird/version.version=%{version} \
    -X main.commit=%shortcommit \
    -X main.date=$(date -u +%%Y%%m%%d) -X main.builtBy=ALT"

%golang_build client

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1

%golang_install

mv %buildroot%_bindir/client %buildroot%_bindir/%name

%buildroot%_bindir/%name completion bash | install -Dm644 /dev/stdin %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completion zsh  | install -Dm644 /dev/stdin %buildroot%_datadir/zsh/site-functions/_%name
%buildroot%_bindir/%name completion fish | install -Dm644 /dev/stdin %buildroot%_datadir/fish/vendor_completions.d/%name.fish

install -Dm644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm600 %SOURCE3 %buildroot%_sysconfdir/%name/config.json
install -dm750 %buildroot%_sharedstatedir/%name

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc README.md SECURITY.md LICENSE
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish
%_unitdir/%name.service
%attr(0750,root,root) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.json
%dir %attr(0750,root,root) %_sharedstatedir/%name

%changelog
* Sat Jun 20 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.73.1-alt1
- New version 0.73.1.

* Fri Jun 12 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.72.4-alt1
- New version 0.72.4.

* Mon Jun 08 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.72.2-alt1
- New version 0.72.2.

* Sun May 24 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.71.4-alt1
- New version 0.71.4.

* Tue May 19 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.71.2-alt1
- New version 0.71.2.

* Fri May 15 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.71.1-alt1
- New version 0.71.1.

* Sun May 10 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.70.5-alt1
- New version 0.70.5.

* Tue May 05 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.70.4-alt1
- New version 0.70.4.

* Fri Apr 24 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.69.0-alt1
- updated from 0.68.3 to 0.69.0

* Wed Apr 15 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.68.3-alt1
- New version 0.68.3.

* Tue Apr 14 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.68.2-alt1
- New version 0.68.2.
- Add /var/lib/netbird to files.

* Mon Apr 13 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.68.1-alt1
- Initial build.
