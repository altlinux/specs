%def_disable static
%def_disable clamav
%def_enable pop3s
%def_enable ripmime
%def_enable pcre

Summary: Virus scanning transparent proxy server for POP3
Name: p3scan
Version: 3.0
Release: alt0.3.rc1
License: GPLv2+
Group: Networking/Mail
Url: http://p3scan.sourceforge.net/
Packager: Alexey Shabalin <shaba@altlinux.org>
Source: http://prdownloads.sourceforge.net/%name/%name-%{version}_rc1.tar.gz
Source1: %name.init

%{?_enable_clamav:BuildRequires: libclamav-devel}
%{?_enable_pop3s:BuildRequires: libssl-devel}
%{?_enable_ripmime:BuildRequires: libripmime-devel >= 1.4.0.6}
%{?_enable_pcre:BuildRequires: libpcre-devel}

BuildRequires: gcc-c++ libcom_err-devel

%description
This is a full-transparent proxy-server for POP3-Clients. It runs on
a Linux box with iptables (for port re-direction). It can be used to
provide POP3 email scanning from the internet, to any internal network
and is ideal for helping to protect your "Other OS" LAN from harm,
especially when used in conjunction with a firewall and other Internet
Proxy servers.

%prep
%setup -q -n %name-%{version}_rc1

%build
%configure \
	%{subst_enable static} \
	%{?_disable_clamav:--disable-clamav} \
	%{?_disable_pop3s:--disable-pop3s} \
	%{?_disable_ripmime:--disable-ripmime} \
	%{?_disable_pcre:--disable-pcre} \
	--with-user=mail \
	--bindir=%_sbindir

%make_build

%install
mkdir -p \
	%buildroot%_initdir \
	%buildroot%_sbindir \
	%buildroot/var/spool/%name/children \
	%buildroot/var/spool/%name/notify \
	%buildroot/var/run/%name
%make DESTDIR=%buildroot install

install -m 755 %SOURCE1 %buildroot%_initdir/%name

cat << EOF >%buildroot%_sysconfdir/%name/redirect_on.sh
#!/bin/bash 
iptables -t nat -A PREROUTING -p tcp -i lo --dport pop3 -j REDIRECT --to 8110
iptables -t nat -I OUTPUT -p tcp --dport 110 -j REDIRECT --to 8110
iptables -t nat -I OUTPUT -p tcp --dport 110 -m owner --uid-owner clamav -j ACCEPT
/etc/init.d/iptables restart
EOF
cat << EOF >%buildroot%_sysconfdir/%name/redirect_off.sh
#!/bin/bash 
iptables -t nat -D PREROUTING -p tcp -i lo --dport pop3 -j REDIRECT --to 8110
iptables -t nat -D OUTPUT -p tcp --dport 110 -j REDIRECT --to 8110
iptables -t nat -D OUTPUT -p tcp --dport 110 -m owner --uid-owner clamav -j ACCEPT
/etc/init.d/iptables restart
EOF

chmod 755 %buildroot%_sysconfdir/%name/redirect*


#dirty workaround
rm -rf %buildroot/usr/doc/%name-%{version}_rc1 
rm -rf %buildroot/etc/init.d

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS CONTRIBUTERS ChangeLog README README-ripmime README-ssl TODO spamfaq.html
%_sbindir/%name
%dir %_sysconfdir/%name
%attr(640,root,mail) %config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_initdir/%name
%_man8dir/*
%attr(775,mail,mail) %dir %_spooldir/%name
%attr(775,mail,mail) %dir %_spooldir/%name/*
%attr(775,mail,mail) %dir %_var/run/%name

%changelog
* Tue Oct 05 2010 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt0.3.rc1
- rebuild with new openssl

* Mon Jul 20 2009 Sergey Y. Afonin <asy@altlinux.ru> 3.0-alt0.2.rc1
- NMU
- ClamAV support disabled (can not build with new libclamav)

* Tue Nov 25 2008 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt0.1.rc1
- 3.0_rc1
- add iptables scripts for redirect

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.3.2-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Jul 20 2007 Alexey Shabalin <shaba@altlinux.org> 2.3.2-alt1
- initial build for ALTLinux
