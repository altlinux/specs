Name: suricata
Version: 4.0.3
Release: alt1%ubt

Summary: Intrusion Detection System

License: GPLv2
Group: Security/Networking
Url: https://suricata-ids.org/

Source: %name-%version.tar
Source1: suricata.service
Source2: suricata.sysconfig
Source3: suricata.logrotate
Source4: suricata-tmpfiles.conf
Source5: suricata.init

Patch: alt-suricata-4.0.3-config.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: libtool_2.4 libpcap-devel libpcre-devel libyaml-devel
BuildRequires: libjansson-devel libnss-devel libcap-ng-devel libgnutls-devel
BuildRequires: libnet-devel libmagic-devel zlib-devel liblua-devel
BuildRequires: libnetfilter_queue-devel libhtp-devel libGeoIP-devel
BuildRequires: libhiredis-devel python-module-setuptools libprelude-devel

%description
The Suricata Engine is an Open Source Next Generation Intrusion
Detection and Prevention Engine. This engine is not intended to
just replace or emulate the existing tools in the industry, but
will bring new ideas and technologies to the field. This new Engine
supports Multi-threading, Automatic Protocol Detection (IP, TCP,
UDP, ICMP, HTTP, TLS, FTP and SMB! ), Gzip Decompression, Fast IP
Matching, and GeoIP identification.

%prep
%setup

%patch -p1

sh autogen.sh

%build
%configure --enable-gccprotect \
           --enable-pie \
           --enable-nfqueue \
           --enable-af-packet \
           --enable-jansson \
           --enable-geoip \
           --enable-lua \
           --enable-hiredis \
           --enable-prelude \
           --enable-non-bundled-htp \
           --disable-gccmarch-native \
           --disable-coccinelle \
           --with-libpcre-includes=%_includedir/pcre \
           --with-libprelude-prefix=%prefix \
           --localstatedir=%_var

%make_build

%install
%makeinstall_std

%if "%_libexecdir" != "%_libdir"
    mv %buildroot%_libexecdir %buildroot%_libdir
%endif 

# Setup etc directory
mkdir -p %buildroot%_sysconfdir/%name/rules
install -m 600 rules/*.rules %buildroot%_sysconfdir/%name/rules
install -m 600 *.config %buildroot%_sysconfdir/%name
install -m 600 suricata.yaml %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_unitdir
install -m 0644 %SOURCE1 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 0755 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

# Set up logging
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_logrotatedir
install -m 644 %SOURCE3 %buildroot%_logrotatedir/%name

# Setup tmpdirs
mkdir -p %buildroot%_tmpfilesdir
install -m 0644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
mkdir -p %buildroot%_runtimedir
install -d -m 0755 %buildroot%_runtimedir/%name/

# Install init.d service
mkdir -p %buildroot%_initdir
install -m 755 %SOURCE5 %buildroot%_initdir/%name

%pre
getent passwd _suricata > /dev/null \
|| useradd -r -M -s /sbin/nologin _suricata

%post
%post_service %name

%preun
%preun_service %name

%files
%doc doc/Basic_Setup.txt doc/Setting_up_IPSinline_for_Linux.txt
%doc ChangeLog README.md LICENSE 
%_bindir/%name
%_bindir/suricatasc
%python_sitelibdir/suricatasc*.egg-info
%python_sitelibdir/suricatasc
%config(noreplace) %attr(-,_suricata,root) %_sysconfdir/%name/suricata.yaml
%config(noreplace) %attr(-,_suricata,root) %_sysconfdir/%name/*.config
%config(noreplace) %attr(-,_suricata,root) %_sysconfdir/%name/rules/*.rules
%config(noreplace) %attr(0600,_suricata,root) %_sysconfdir/sysconfig/%name
%config %attr(644,root,root) %_unitdir/suricata.service
%attr(755,root,root) %_initdir/%name
%config(noreplace) %attr(644,root,root) %_sysconfdir/logrotate.d/%name
%attr(750,_suricata,root) %dir %_var/log/%name
%attr(750,_suricata,root) %dir %_sysconfdir/%name
%attr(750,_suricata,root) %dir %_sysconfdir/%name/rules
%attr(750,_suricata,root) %dir %_runtimedir/%name/
%_tmpfilesdir/%name.conf

%changelog
* Thu Feb 08 2018 Maxim Voronov <mvoronov@altlinux.org> 4.0.3-alt1%ubt
- initial build for ALT

