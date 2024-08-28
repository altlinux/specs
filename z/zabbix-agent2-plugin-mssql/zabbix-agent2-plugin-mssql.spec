%define zabbix_group    zabbix

Name:   zabbix-agent2-plugin-mssql
Version: 7.0.3
Release: alt1

Summary: Provides native Zabbix solution for monitoring MS-SQL
License: AGPL-3.0-only
Group:   Monitoring
URL:     https://git.zabbix.com/projects/AP/repos/mssql/browse

BuildRequires(pre): rpm-build-golang
BuildRequires: golang /proc
ExclusiveArch: %go_arches

Requires: zabbix-agent2

Source: %name-%version.tar
Patch0: zabbix-agent2-plugin-mssql-6.0.32-alt-config.patch

%description
This plugin provides a native Zabbix solution to monitor Microsoft SQL servers.

It can monitor several MSSQL instances simultaneously, remote or local.

%prep
%setup
%patch0 -p1

%build
%make

%install
mkdir -p %{buildroot}%{_sbindir}/
mv zabbix-agent2-plugin-mssql %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_sysconfdir}/zabbix/zabbix_agent2.conf.d/plugins.d
mv mssql.conf %{buildroot}%{_sysconfdir}/zabbix/zabbix_agent2.conf.d/plugins.d

%files
%doc ChangeLog LICENSE README.md
%_sbindir/zabbix-agent2-plugin-mssql
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/zabbix/zabbix_agent2.conf.d/plugins.d/mssql.conf

%changelog
* Wed Aug 28 2024 Alexei Takaseev <taf@altlinux.org> 7.0.3-alt1
- 7.0.3

* Fri Aug 23 2024 Alexei Takaseev <taf@altlinux.org> 7.0.2-alt1
- Initial build for c10f1
