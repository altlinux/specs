%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%global import_path github.com/xtaci/kcptun
Name:     kcptun
Version: 20230214
Release: alt1

Summary:  A Stable & Secure Tunnel based on KCP with N:M multiplexing and FEC
License:  MIT
Group:    Networking/Other
Url:      https://github.com/xtaci/kcptun

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
%{?!_without_check:%{?!_disable_check:BuildRequires: banner curl python3 iproute2}}

%description
%summary

KCP is a reliable (ARQ) transmission protocol (on top of UDP) with the
focus on low-latency in contrast to TCP which focus on bandwidth.

FEC is a forward error correction (using Reed-Solomon codes), achieving
reliability in the network with packet losses.

%prep
%setup

%build
export LDFLAGS="-X main.VERSION=%version"
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build client server

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mv %buildroot%_bindir/server %buildroot%_bindir/%name-server
mv %buildroot%_bindir/client %buildroot%_bindir/%name-client
mkdir -p %buildroot%_sysconfdir/sysctl.d %buildroot%_sysconfdir/%name %buildroot%_unitdir
install -m0644 .gear/sysctl.conf* %buildroot%_sysconfdir/sysctl.d/88-%name.conf.example
install -m0644 .gear/%name.service %buildroot%_unitdir/%name-client.service
install -m0644 .gear/%name.service %buildroot%_unitdir/%name-server.service
install -m0640 .gear/*.json  %buildroot%_sysconfdir/%name

%check
.gear/kcptun-test.sh

%post
%post_service %name-client
%post_service %name-server

%preun
%preun_service %name-client
%preun_service %name-server

%files
%_bindir/%{name}*
%doc *.md
%attr(750,root,wheel) %dir %_sysconfdir/%name
%attr(640,root,wheel) %config(noreplace) %_sysconfdir/%name/*
%_sysconfdir/sysctl.d/*
%_unitdir/*.service

%changelog
* Sun Feb 19 2023 Vitaly Chikunov <vt@altlinux.org> 20230214-alt1
- Update to v20230214 (2023-02-14).

* Wed Feb 08 2023 Vitaly Chikunov <vt@altlinux.org> 20230207-alt1
- Update to v20230207 (2023-02-07).

* Wed Oct 12 2022 Vitaly Chikunov <vt@altlinux.org> 20221008-alt1
- Update to v20221008:
  + Add multi-port support.

* Sat Aug 20 2022 Vitaly Chikunov <vt@altlinux.org> 20220628-alt1
- Update to v20220628.

* Sun Mar 20 2022 Vitaly Chikunov <vt@altlinux.org> 20210922-alt2
- Improve packaging:
  + Install client/server configs and sysctl.conf example.
  + Create hardened systemd units.
  + Run simple smoke test in %%check.

* Wed Mar 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 20210922-alt1
- Initial build for Sisyphus
