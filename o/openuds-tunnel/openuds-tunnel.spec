%define _unpackaged_files_terminate_build 1
%add_python3_path %_datadir/openuds/tunnel

Name: openuds-tunnel
Version: 3.5.0
Release: alt1
Summary: Clientless remote desktop gateway
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/dkmstr/openuds
BuildArch: noarch

Source: tunnel-server.tar
Source2: guacamole-auth-uds-2.5.0.jar
# Source2: guacamole-auth-uds.tar
Source6: openuds-tunnel.service

#BuildRequires(pre): rpm-build-java
#BuildRequires: /proc
#BuildRequires: java-devel
#BuildRequires: maven-local maven
#BuildRequires: maven-plugin-plugin maven-resources-plugin maven-compiler-plugin maven-dependency-plugin
#BuildRequires: google-guice
#BuildRequires: tomcat

BuildRequires(pre): rpm-build-python3

Requires: guacamole-auth-openuds
Requires: cert-sh-functions
Obsoletes: pam_uds
Obsoletes: libnss_uds

%description
Guacamole is an HTML5 web application that provides access
to desktop environments using remote desktop protocols such as VNC or RDP.
A centralized server acts as a tunnel and proxy,
allowing access to multiple desktops through a web browser.
No plugins are needed: the client requires nothing more than a web browser
supporting HTML5 and AJAX.
This is the client-part.

This portion of UDS (HTML5 tunnel) is based on Apache Guacamole.

%package -n guacamole-auth-openuds
Summary: OpenUDS Integration Extension for Apache Guacamole
License: Apache-2.0
Version: 2.5.0
Release: alt3
Group: Networking/Remote access
Provides: guacamole-auth-uds = %EVR
Provides: guacamole-openuds = %EVR
Requires: guacamole-client >= 1.4.0
Requires: guacamole-server
AutoReqProv: noosgi, noosgi-fc
Obsoletes: openuds-guacamole-tunnel

%description -n guacamole-auth-openuds
OpenUDS Integration Extension for Apache Guacamole.

%prep
#%%setup -c -a 2
%setup -c

%build
#mvn -o package

%install
mkdir -p %buildroot%_datadir/openuds/tunnel
cp -r uds_tunnel %buildroot%_datadir/openuds/tunnel/
cp udstunnel.py %buildroot%_datadir/openuds/tunnel/
# config
install -p -D -m 644 udstunnel.conf %buildroot%_sysconfdir/udstunnel.conf
# systemd unit
install -p -D -m 644 %SOURCE6 %buildroot%_unitdir/openuds-tunnel.service

# guacamole-auth-openuds
mkdir -p %buildroot{%_datadir,%_sysconfdir}/guacamole/extensions
install -p -D -m 644 %SOURCE2 %buildroot%_datadir/guacamole/extensions/guacamole-auth-uds-2.5.0.jar
ln -r -s %buildroot%_datadir/guacamole/extensions/guacamole-auth-uds-2.5.0.jar %buildroot%_sysconfdir/guacamole/extensions

%pre
groupadd -r -f openuds >/dev/null 2>&1 ||:
useradd -M -r -g openuds -c 'OpenUDS Tunnel Daemon' \
        -s /bin/false  -d %_sharedstatedir/openuds openuds >/dev/null 2>&1 ||:

%post
# Create SSL certificate for openuds-tunnel server
cert-sh generate openuds-tunnel ||:
cert-sh ssl_make_dhparam ||:
%post_service openuds-tunnel

%preun
%preun_service openuds-tunnel

%post -n guacamole-auth-openuds
grep -q uds-base-url %_sysconfdir/guacamole/guacamole.properties || echo "uds-base-url=https://www.example.org" >> %_sysconfdir/guacamole/guacamole.properties

%files
%config(noreplace) %attr(0644, root, root) %_sysconfdir/udstunnel.conf
%_unitdir/openuds-tunnel.service
%_datadir/openuds/tunnel

%files -n guacamole-auth-openuds
%_sysconfdir/guacamole/extensions/guacamole-auth-uds-2.5.0.jar
%_datadir/guacamole/extensions/guacamole-auth-uds-2.5.0.jar

%changelog
* Fri Oct 14 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt1
- 3.5.0

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 2.5.0-alt2.1
- NMU: spec: adapted to new cmake macros.

* Mon Jan 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.5.0-alt2
- Fixed sshd_uds.service

* Mon Dec 07 2020 Alexey Shabalin <shaba@altlinux.org> 2.5.0-alt1
- Initial build
