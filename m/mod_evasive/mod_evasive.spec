# override definition from apache-devel
%define apache_addonconfdir %apache_confdir/addon-modules.d
%define apache_moduledir %_libdir/apache

Name: mod_evasive
Version: 1.10.1
Release: alt0.1

Summary: mod_evasive is an evasive maneuvers module for Apache

Group: System/Servers
License: GPL
Url: http://www.zdziarski.com/projects/mod_evasive/
Source: http://www.zdziarski.com/projects/mod_evasive/%{name}_%{version}.tar.gz
Source1: mod_evasive.conf

Requires: apache

BuildRequires: apache-devel

%description
mod_dosevasive is an evasive maneuvers module for Apache to provide evasive action in the event of an HTTP DoS or DDoS attack or brute force attack. It is also designed to be a detection and network management tool, and can be easily configured to talk to ipchains, firewalls, routers, and etcetera. mod_dosevasive presently reports abuses via email and syslog facilities.

%prep
%setup -q -n %name

%build
%apache_apxs -Wc,"$RPM_OPT_FLAGS" -c mod_evasive.c -o mod_evasive.so

%install
%__mkdir_p %buildroot{%apache_moduledir,%apache_addonconfdir}

%__install -m755 %name.so %buildroot%apache_moduledir
%__install -m644 %SOURCE1 %buildroot%apache_addonconfdir

%post
/sbin/service httpd condrestart

%postun
/sbin/service httpd condrestart

%files
%apache_moduledir/*
%config(noreplace) %apache_addonconfdir/*
%doc README

%changelog
* Fri Mar 28 2008 Nick S. Grechukh <gns@altlinux.org> 1.10.1-alt0.1
- initial build for Sisyphus
