%define _altdata_dir %_sysconfdir/alterator

Name: alterator-openldap-functions
Version: 0.2
Release: alt2

BuildArch: noarch

Source: %name-%version.tar

Summary: helper functions for alterator openldap based backends
License: GPL
Group: System/Base

BuildPreReq: libshell >= 0.0.5-alt1

Conflicts: alterator < 3.4-alt1

%description
helper functions for alterator openldap based backends

%prep
%setup -q

%build

%install
	install -Dpm644 %name %buildroot/%_bindir/%name
    mkdir -p %buildroot/%_altdata_dir/openldap

%files
%_bindir/*
%dir %_altdata_dir/openldap

%changelog
* Wed Apr 14 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.2-alt2
- added functions
  + slapd_daemon_status
  + slapd_daemon_on
  + slapd_daemon_off

* Thu Jun 18 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt1
- added /etc/alterator/openldap dir
- added functions
  + read_sysconfig
  + write_config
  + write_sysconfig
  + tls_ssl_status
  + localhost_status
  + write_sysconfig_url
  + slapd_daemon_condrestart

* Wed Apr 22 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt1
- initial build

