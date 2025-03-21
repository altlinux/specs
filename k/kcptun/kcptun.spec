%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name:     kcptun
Version: 20231012
Release: alt1

Summary:  A Tunnel based on KCP with N:M multiplexing and FEC
License:  MIT
Group:    Networking/Other
Url:      https://github.com/xtaci/kcptun

Source:   %name-%version.tar
Patch3500: alt-github.com-templexxx-cpu-support-LoongArch.patch

BuildRequires: golang
%{?!_without_check:%{?!_disable_check:
BuildRequires: curl
BuildRequires: iproute2
BuildRequires: python3
}}

%description
%summary.

KCP is a reliable (ARQ) transmission protocol (on top of UDP) with the
focus on low-latency in contrast to TCP which focus on bandwidth.

FEC is a forward error correction (using Reed-Solomon codes), achieving
reliability in the network with packet losses.

%prep
%setup
%patch3500 -p1

%build
go build -v -buildmode=pie -ldflags="-X main.VERSION=%version" -o %name-client ./client
go build -v -buildmode=pie -ldflags="-X main.VERSION=%version" -o %name-server ./server
# Please do not upgrade beyond this version.
./kcptun-client --version | grep -Fx 'kcptun version 20231012'

%install
install -Dp %name-client %name-server -t %buildroot%_bindir
install -Dpm0644 .gear/sysctl.conf %buildroot%_sysconfdir/sysctl.d/88-%name.conf.example
install -Dpm0644 .gear/%name.service %buildroot%_unitdir/%name-client.service
install -Dpm0644 .gear/%name.service %buildroot%_unitdir/%name-server.service
install -Dpm0640 .gear/*.json -t %buildroot%_sysconfdir/%name

%check
.gear/kcptun-test.sh

%post
%post_service %name-client
%post_service %name-server

%preun
%preun_service %name-client
%preun_service %name-server

%files
%doc *.md
%_bindir/%name-client
%_bindir/%name-server
%attr(750,root,wheel) %dir %_sysconfdir/%name
%attr(640,root,wheel) %config(noreplace) %_sysconfdir/%name/*
%_sysconfdir/sysctl.d/*
%_unitdir/*.service

%changelog
* Fri Mar 21 2025 Vitaly Chikunov <vt@altlinux.org> 20231012-alt1
- Update to v20231012 (2023-10-12).
- Fixed a bug in fec tuning when fec parameters on client & server side are set
  differently.

* Fri May 10 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 20230811-alt2
- NMU: fixed FTBFS on LoongArch.

* Mon Sep 04 2023 Vitaly Chikunov <vt@altlinux.org> 20230811-alt1
- Update to v20230811 (2023-08-11).

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
