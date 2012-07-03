Name: mod_auth_pam
Version: 1.1.1
Release: alt1

Summary: pluggable authentication module for Apache
License: GPL
Group: System/Servers

Requires: apache groupkit

Source0: http://pam.sourceforge.net/mod_auth_pam/dist/%{name}-%{version}.tar.gz
Source1: httpd.pamd
Patch0: mod_auth_pam-1.1.1-mod_auth_pam_c.patch

# Automatically added by buildreq on Wed Mar 10 2004
BuildRequires: apache-devel libpam-devel

%description
The PAM authentication module implements Basic authentication on top
of the Pluggable Authentication Module library. Thereby it supports 
standard unix passwd, shadow, NIS, SMB auth and radius authentication 
transparently and easily interchangeable, wherever the HTTP protocol 
allows it.

%prep
%setup -q
%patch0

%build
%make_build APXS=%{_sbindir}/apxs

%install
%__install -pD -m644 mod_auth_pam.so %{buildroot}/%{_libdir}/apache/mod_auth_pam.so
%__install -pD -m644 ${_sourcedir}/%{SOURCE1} %{buildroot}/%{_sysconfdir}/pam.d/httpd

%post
%{_sbindir}/apxs -e -a -n auth_pam mod_auth_pam.so >/dev/null 2>/dev/null
%{_sbindir}/addusertogroup apache shadow auth >/dev/null 2>/dev/null
%{_sbindir}/apachectl update >/dev/null 2>/dev/null

%preun
if [ $1 = 0 ]; then
    %{_sbindir}/deluserfromgroup apache shadow auth >/dev/null 2>/dev/null
    %{_sbindir}/apxs -e -A -n auth_pam mod_auth_pam.so >/dev/null 2>/dev/null
    %{_sbindir}/apachectl update >/dev/null 2>/dev/null
fi

%files
%config %{_sysconfdir}/pam.d/*
%{_libdir}/apache/*
%doc doc samples README

%changelog
* Wed Mar 10 2004 Dimitry V. Ketov <dketov@altlinux.ru> 1.1.1-alt1
- Initial build for Sisyphus

