%define zabbix_group    zabbix

Name:   zabbix-agent2-plugin-postgresql
Version: 7.0.3
Release: alt1

Summary: Provides native Zabbix solution for monitoring PostgreSQL
License: AGPL-3.0-only
Group:   Monitoring
URL:     https://git.zabbix.com/projects/AP/repos/postgresql/browse

BuildRequires(pre): rpm-build-golang
BuildRequires: golang /proc
ExclusiveArch: %go_arches

Requires: zabbix-agent2

Source: %name-%version.tar
Patch0: zabbix-agent2-plugin-postgresql-6.0.32-alt-config.patch

%description
Provides native Zabbix solution for monitoring PostgreSQL (object-relational database system).
It can monitor several PostgreSQL instances simultaneously, remote or local to the Zabbix Agent.
Native connection encryption is supported. The plugin keeps connections in the open state to
reduce network congestion, latency, CPU and memory usage. Best for use in conjunction with the
official PostgreSQL template. You can extend it or create your template for your specific needs.

%prep
%setup
%patch0 -p1

%build
%make

%install
mkdir -p %{buildroot}%{_sbindir}/
mv zabbix-agent2-plugin-postgresql %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_sysconfdir}/zabbix/zabbix_agent2.conf.d/plugins.d
mv postgresql.conf %{buildroot}%{_sysconfdir}/zabbix/zabbix_agent2.conf.d/plugins.d

%files
%doc ChangeLog LICENSE README.md
%_sbindir/zabbix-agent2-plugin-postgresql
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/zabbix/zabbix_agent2.conf.d/plugins.d/postgresql.conf

%changelog
* Wed Aug 28 2024 Alexei Takaseev <taf@altlinux.org> 7.0.3-alt1
- 7.0.3

* Thu Jul 11 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 6.4.9-alt2
- Default configuration update (ALT #50849 #50850)

* Thu Jul 04 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 6.4.9-alt1
- Initial build for Sisyphus (Closes: #50382)
