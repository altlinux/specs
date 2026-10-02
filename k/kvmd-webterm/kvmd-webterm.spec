Name: kvmd-webterm
Version: 0.52
Release: alt1

Summary: Web terminal for the PiKVM daemon
License: GPLv3
Group: System/Servers
URL: https://pikvm.org/
VCS: https://github.com/pikvm/packages

Requires: ttyd

Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%install
install -pm0644 -D sysusers.conf %buildroot%_sysusersdir/kvmd-webterm.conf
install -pm0644 -D tmpfiles.conf %buildroot%_tmpfilesdir/kvmd-webterm.conf
install -pm0644 -D kvmd-webterm.service %buildroot%_unitdir/kvmd-webterm.service
install -pm0644 -D terminal.svg %buildroot%_datadir/kvmd/web/extras/webterm/terminal.svg
install -pm0644 -D manifest.yaml %buildroot%_datadir/kvmd/extras/webterm/manifest.yaml
install -pm0644    nginx.*.conf %buildroot%_datadir/kvmd/extras/webterm/ 

%files
%_sysusersdir/*.conf
%_tmpfilesdir/*.conf
%_unitdir/*.service

%_datadir/kvmd/extras/webterm
%_datadir/kvmd/web/extras/webterm

%changelog
* Tue Sep 29 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.52-alt1
- 0.52 released

* Thu Mar 07 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.48-alt1
- 0.48 released

* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.42-alt1
- initial
