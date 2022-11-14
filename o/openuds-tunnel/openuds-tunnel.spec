%define _unpackaged_files_terminate_build 1
%add_python3_path %_datadir/openuds/tunnel

Name: openuds-tunnel
Version: 3.5.0
Release: alt2
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
Release: alt4
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
mkdir -p %buildroot%_sysconfdir/%name/ssl/{certs,private}
install -p -D -m 644 udstunnel.conf %buildroot%_sysconfdir/%name/udstunnel.conf
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
SSLDIR=%_sysconfdir/%name/ssl cert-sh generate openuds-tunnel ||:
SSLDIR=%_sysconfdir/%name/ssl cert-sh make_dhparam openuds-tunnel ||:
chown openuds:tomcat %_sysconfdir/%name/ssl/private/openuds-tunnel.* ||:
chmod 640 %_sysconfdir/%name/ssl/private/openuds-tunnel.* ||:
if [ $1 -eq 1 ]; then
# ugly hack to set a unique uds_token
	UDS_TOKEN=$(openssl rand -hex 24)
	sed -i "/^uds_token.*$/{s/^.*$/uds_token = $UDS_TOKEN/}" %_sysconfdir/%name/udstunnel.conf
	grep -q uds-base-url %_sysconfdir/guacamole/guacamole.properties || echo "uds-base-url=http://172.27.0.1:8000/uds/guacamole/auth/$UDS_TOKEN" >> %_sysconfdir/guacamole/guacamole.properties
fi
%post_service openuds-tunnel
%post_service tomcat

%preun
%preun_service openuds-tunnel

%files
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/ssl
%dir %_sysconfdir/%name/ssl/certs
%attr(0750, openuds, tomcat) %dir %_sysconfdir/%name/ssl/private
%config(noreplace) %attr(0640, root, openuds) %_sysconfdir/%name/udstunnel.conf

%_unitdir/openuds-tunnel.service
%_datadir/openuds/tunnel

%files -n guacamole-auth-openuds
%_sysconfdir/guacamole/extensions/guacamole-auth-uds-2.5.0.jar
%_datadir/guacamole/extensions/guacamole-auth-uds-2.5.0.jar

%changelog
* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt2
- Moved config files to /etc/openuds-tunnel dir.
- Generate ssl cert and key to /etc/openuds-tunnel/ssl dir.
- Allow read ssl private key for tomcat user.
- Generate uds tunnel token in %%post.

* Fri Oct 14 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt1
- 3.5.0

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 2.5.0-alt2.1
- NMU: spec: adapted to new cmake macros.

* Mon Jan 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.5.0-alt2
- Fixed sshd_uds.service

* Mon Dec 07 2020 Alexey Shabalin <shaba@altlinux.org> 2.5.0-alt1
- Initial build
