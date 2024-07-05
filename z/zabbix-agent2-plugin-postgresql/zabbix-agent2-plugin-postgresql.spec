Name:   zabbix-agent2-plugin-postgresql
Version: 6.4.9
Release: alt1

Summary: Provides native Zabbix solution for monitoring PostgreSQL
License: AGPL-3.0-only
Group:   Monitoring
URL:     https://git.zabbix.com/projects/AP/repos/postgresql/browse

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-golang
BuildRequires: golang /proc
ExclusiveArch: %go_arches

Requires: zabbix-agent2

Source: %name-%version.tar

%description
Provides native Zabbix solution for monitoring PostgreSQL (object-relational database system).
It can monitor several PostgreSQL instances simultaneously, remote or local to the Zabbix Agent.
Native connection encryption is supported. The plugin keeps connections in the open state to
reduce network congestion, latency, CPU and memory usage. Best for use in conjunction with the
official PostgreSQL template. You can extend it or create your template for your specific needs.

%prep
%setup

%build
make

%install
mkdir -p %{buildroot}%{_sbindir}/
mv zabbix-agent2-plugin-postgresql %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_sysconfdir}/zabbix/zabbix_agent2.d/plugins.d/
mv postgresql.conf %{buildroot}%{_sysconfdir}/zabbix/zabbix_agent2.d/plugins.d/

%files
%doc LICENSE README.md
%_sbindir/zabbix-agent2-plugin-postgresql
%config(noreplace) %_sysconfdir/zabbix/zabbix_agent2.d/plugins.d/postgresql.conf

%changelog
* Thu Jul 04 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 6.4.9-alt1
- Initial build for Sisyphus (Closes: #50382)
