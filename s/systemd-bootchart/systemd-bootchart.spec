# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: systemd-bootchart
Version: 235
Release: alt2
Summary: Boot performance graphing tool

Group: System/Configuration/Boot and Init
License: GPL-2.0-or-later and LGPL-2.1-or-later
Url: https://github.com/systemd/systemd-bootchart

Source: %name-%version.tar
BuildRequires: libsystemd-devel
BuildRequires: xsltproc
BuildRequires: docbook-style-xsl

%description
systemd-bootchart is a tool, usually run at system startup, that
collects the CPU load, disk load, memory usage, as well as per-process
information from a running system. Collected results are output as an SVG
graph. Normally, systemd-bootchart is invoked by the kernel by passing
init=/lib/systemd/systemd-bootchart on the kernel command line, adding
initcall_debug to collect data on kernel init threads. systemd-bootchart
will then fork the real init off to resume normal system startup, while
monitoring and logging startup information in the background.

%prep
%setup
sed -Ei 's,/usr(/lib/systemd),\1,g' man/*.xml

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%post
%post_service %name

%preun
%preun_service %name

%files
%define _customdocdir %_docdir/%name
%doc LICENSE.GPL2 LICENSE.LGPL2.1 README
%config(noreplace) %_sysconfdir/systemd/bootchart.conf
%_unitdir/%name.service
%_systemd_dir/systemd-bootchart
%_man1dir/systemd-bootchart.1*
%_man5dir/bootchart.conf.5*
%_man5dir/bootchart.conf.d.5*

%changelog
* Sat Jul 13 2024 Vitaly Chikunov <vt@altlinux.org> 235-alt2
- spec: Fix FTBFS after usrmerge.

* Fri Nov 03 2023 Vitaly Chikunov <vt@altlinux.org> 235-alt1
- Update to v235 (2023-11-01).

* Fri May 07 2021 Vitaly Chikunov <vt@altlinux.org> 234-alt1
- First import of v234 (2020-12-16).
