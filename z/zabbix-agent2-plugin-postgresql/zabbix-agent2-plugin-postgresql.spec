%define zabbix_group    zabbix

Name:   zabbix-agent2-plugin-postgresql
Version: 7.0.25
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
%make_build

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
* Tue Apr 07 2026 Alexei Takaseev <taf@altlinux.org> 7.0.25-alt1
- 7.0.25

* Thu Mar 19 2026 Alexei Takaseev <taf@altlinux.org> 7.0.24-alt1
- 7.0.24

* Wed Feb 18 2026 Alexei Takaseev <taf@altlinux.org> 7.0.23-alt1
- 7.0.23

* Fri Dec 19 2025 Alexei Takaseev <taf@altlinux.org> 7.0.22-alt1
- 7.0.22

* Mon Nov 03 2025 Alexei Takaseev <taf@altlinux.org> 7.0.21-alt1
- 7.0.21

* Thu Oct 30 2025 Alexei Takaseev <taf@altlinux.org> 7.0.20-alt1
- 7.0.20

* Fri Oct 03 2025 Alexei Takaseev <taf@altlinux.org> 7.0.19-alt1
- 7.0.19

* Tue Aug 26 2025 Alexei Takaseev <taf@altlinux.org> 7.0.18-alt1
- 7.0.18

* Fri Aug 01 2025 Alexei Takaseev <taf@altlinux.org> 7.0.17-alt1
- 7.0.17

* Fri Jun 27 2025 Alexei Takaseev <taf@altlinux.org> 7.0.16-alt1
- 7.0.16

* Mon Jun 23 2025 Alexei Takaseev <taf@altlinux.org> 7.0.15-alt1
- 7.0.15

* Thu Jun 19 2025 Alexei Takaseev <taf@altlinux.org> 7.0.14-alt1
- 7.0.14

* Tue May 20 2025 Alexei Takaseev <taf@altlinux.org> 7.0.13-alt1
- 7.0.13

* Tue Apr 22 2025 Alexei Takaseev <taf@altlinux.org> 7.0.12-alt1
- 7.0.12

* Fri Mar 28 2025 Alexei Takaseev <taf@altlinux.org> 7.0.11-alt1
- 7.0.11

* Tue Feb 25 2025 Alexei Takaseev <taf@altlinux.org> 7.0.10-alt1
- 7.0.10
- Use %%make_build for speedup compilation

* Tue Jan 28 2025 Alexei Takaseev <taf@altlinux.org> 7.0.9-alt1
- 7.0.9

* Wed Jan 08 2025 Alexei Takaseev <taf@altlinux.org> 7.0.8-alt1
- 7.0.8

* Thu Dec 19 2024 Alexei Takaseev <taf@altlinux.org> 7.0.7-alt1
- 7.0.7

* Wed Dec 04 2024 Alexei Takaseev <taf@altlinux.org> 7.0.6-alt1
- 7.0.6

* Thu Oct 24 2024 Alexei Takaseev <taf@altlinux.org> 7.0.5-alt1
- 7.0.5

* Sat Sep 28 2024 Alexei Takaseev <taf@altlinux.org> 7.0.4-alt1
- 7.0.4

* Wed Aug 28 2024 Alexei Takaseev <taf@altlinux.org> 7.0.3-alt1
- 7.0.3

* Thu Jul 11 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 6.4.9-alt2
- Default configuration update (ALT #50849 #50850)

* Thu Jul 04 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 6.4.9-alt1
- Initial build for Sisyphus (Closes: #50382)
