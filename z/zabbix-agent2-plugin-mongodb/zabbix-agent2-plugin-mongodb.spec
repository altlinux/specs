%define zabbix_group    zabbix

Name:   zabbix-agent2-plugin-mongodb
Version: 7.0.3
Release: alt1

Summary: Provides native Zabbix solution for monitoring MongoDB
License: AGPL-3.0-only
Group:   Monitoring
URL:     https://git.zabbix.com/projects/AP/repos/mongodb/browse

BuildRequires(pre): rpm-build-golang
BuildRequires: golang /proc
ExclusiveArch: %go_arches

Requires: zabbix-agent2

Source: %name-%version.tar
Patch0: zabbix-agent2-plugin-mongodb-6.0.32-alt-config.patch

%description
This plugin provides a native Zabbix solution to monitor MongoDB servers and clusters
(document-based, distributed database). It can monitor several MongoDB instances
simultaneously, remotes or locals to the Zabbix Agent. The plugin keeps connections
in the opened state to reduce network congestion, latency, CPU and memory usage.
It is best for use in conjunction with the official MongoDB template. You can extend
it or create your own template to cater specific needs.

%prep
%setup
%patch0 -p1

%build
%make

%install
mkdir -p %{buildroot}%{_sbindir}/
mv zabbix-agent2-plugin-mongodb %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_sysconfdir}/zabbix/zabbix_agent2.conf.d/plugins.d
mv mongodb.conf %{buildroot}%{_sysconfdir}/zabbix/zabbix_agent2.conf.d/plugins.d

%files
%doc ChangeLog LICENSE README.md
%_sbindir/zabbix-agent2-plugin-mongodb
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/zabbix/zabbix_agent2.conf.d/plugins.d/mongodb.conf

%changelog
* Wed Aug 28 2024 Alexei Takaseev <taf@altlinux.org> 7.0.3-alt1
- 7.0.3

* Thu Aug 22 2024 Alexei Takaseev <taf@altlinux.org> 7.0.2-alt1
- Initial build for c10f1
