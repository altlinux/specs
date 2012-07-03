# Spec file for mod_evasive module for Apache 2.0 server

%define real_name    mod_evasive
%define module_name  mod_evasive
%define version      1.10.1
%define release      alt1


Name: apache2-%module_name
Version: %version
Release: %release

Summary: Apache 2.x evasive module to minimize HTTP DoS or brute force attacks

License: %gpl2only
Group:   System/Servers
URL:     http://www.zdziarski.com/projects/mod_evasive/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %real_name.tar
Source1: evasive.load
Source2: evasive.conf

BuildRequires(pre): apache2-devel >= 2.2.5
BuildRequires(pre): rpm-build-licenses

Requires(pre): apache2 >= %apache2_version-%apache2_release

# Automatically added by buildreq on Fri Dec 12 2008
BuildRequires: apache2-httpd-prefork

%description
mod_evasive  is an evasive maneuvers module  for Apache to provide
evasive action in the event of an HTTP DoS or DDoS attack or brute
force attack.  It is also designed to be  a detection and  network
management tool, and can be easily configured to talk to ipchains,
firewalls, routers, and etcetera. mod_evasive presently reports 
abuses via email and syslog facilities. 

Detection is performed  by creating an internal dynamic hash table
of IP Addresses and URIs, and denying any single IP address from
any of the following:
- Requesting the same page more than a few times per second
- Making more than few concurrent requests on the same child per
  second
- Making any requests while temporarily blacklisted (on a blocking
  list) 

mod_evasive could be easly integrated with firewalls and routers
for maximum protection.

%prep
%setup -q -n %real_name

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
%apache2_apxs -a -c mod_evasive20.c


%install
/bin/install -pDm644 .libs/mod_evasive20.so %buildroot%apache2_libexecdir/mod_evasive20.so

/bin/install -pDm644 %SOURCE1 %buildroot%apache2_mods_available/evasive.load
/bin/install -pDm644 %SOURCE2 %buildroot%apache2_mods_available/evasive.conf

/bin/mkdir -p %buildroot%apache2_spooldir/%module_name

%post
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To use %real_name check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 %real_name module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi


%postun
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To complete %real_name uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi


%files
%doc README CHANGELOG
%doc --no-dereference LICENSE

%apache2_libexecdir/mod_evasive20.so
%apache2_mods_available/evasive.load
%config(noreplace) %apache2_mods_available/evasive.conf

%dir %apache2_spooldir/%module_name

%changelog
* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.10.1-alt1
- Initial build for ALT Linux Sisyphus

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.10.1-alt0.1
- Initial build
