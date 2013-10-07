Summary: Suricata is a multi-threaded intrusion detection/prevention engine
Name: suricata
Version: 1.4.6
Release: alt1
License: GPL
Group: System/Base
URL: http://www.openinfosecfoundation.org
Source: %name-%version.tar
Source1: %name

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: libpcre-devel libnet-devel libyaml-devel libpcap-devel libnfnetlink-devel libnetlink-devel libnetfilter_queue-devel glibc-devel libcap-ng-devel zlib-devel python-module-distribute
BuildRequires: libprelude-devel libgnutls-devel libtasn1-devel libgcrypt-devel libgpg-error-devel libmagic-devel libnss-devel libnspr-devel libjansson-devel libluajit-devel libGeoIP-devel
# libpfring-devel

Requires: python-module-suricata

%description
Suricata is a multi-threaded intrusion detection/prevention engine

%package -n libhtp
Summary: LibHTP is a security-aware parser for the HTTP protocol and the related bits and pieces
Group: System/Libraries
%description -n libhtp
LibHTP is a security-aware parser for the HTTP protocol and the related bits and pieces

%package -n libhtp-devel
Summary: Development headers for LibHTP
Group: Development/C
%description -n libhtp-devel
Development headers for LibHTP

%package -n python-module-suricata
Summary: python module for interacting with unix socket
Group: Development/Python
BuildArch: noarch
%description -n python-module-suricata
Python module for interacting with unix socket

%prep
%setup -q

%build
libtoolize -c -f -i
%autoreconf
%configure \
	--enable-nfqueue \
	--enable-prelude \
	--enable-profiling \
	--enable-unittests \
	--with-libpcre-includes=%_includedir/pcre \
	--with-libnspr-includes=%_includedir/nspr \
	--with-libnss-includes=%_includedir/nss \
	--enable-luajit \
	--enable-pcre-jit \
	--enable-geoip
#	--enable-pfring \
#	--enable-cuda \
#	--enable-dag \
#	--enable-napatech

%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/%name/rules
mkdir -p %buildroot%_sysconfdir/logrotate.d
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_initrddir
mkdir -p %buildroot/var/log/%name
mkdir -p %buildroot%_runtimedir/suricata

#Config
cp reference.config classification.config suricata.yaml threshold.config %buildroot%_sysconfdir/%name/

#Init
install -p -m 755 %SOURCE1  %buildroot%_initrddir/%name


cat << EOF > %buildroot%_sysconfdir/logrotate.d/%name
/var/log/%name/stats.log {
    create 644 root _%name
    weekly
    rotate 5
    copytruncate
    compress
    notifempty
    missingok
}
/var/log/%name/http.log {
    create 644 root _%name
    weekly
    rotate 5
    copytruncate
    compress
    notifempty
    missingok
    postrotate
        /sbin/service %name reload >/dev/null
    endscript
}
EOF

cat << EOF > %buildroot%_sysconfdir/sysconfig/%name
# Can run in several modes. Setup before use
#
#        -i <dev or ip>               : run in pcap live mode
#        -r <path>                    : run in pcap file/offline mode
#        -q <qid>                     : run in inline nfqueue mode

OPTIONS="-i eth0"

EOF

%pre
/usr/sbin/groupadd -r -f _%name &> /dev/null ||:
/usr/sbin/useradd -r -g _%name -d /dev/null -c 'Multi-threaded intrusion detection/prevention engine' -s /dev/null -n _%name &> /dev/null ||:

%post
%post_service %name

%preun
%preun_service %name


%files
%doc doc/*
%_bindir/*
%dir %attr(750,root,_%name) %_sysconfdir/%name
%dir %attr(750,root,_%name) %_sysconfdir/%name/rules
%_initrddir/%name
%config(noreplace) %_sysconfdir/%name/*.config
%config(noreplace) %_sysconfdir/%name/*.yaml
%config(noreplace) %_sysconfdir/sysconfig/%name
%config %_sysconfdir/logrotate.d/*
%dir %attr(3770,_%name,root) /var/log/%name
%dir %attr(3770,_%name,root) %_runtimedir/suricata

%files -n libhtp
%_libdir/*.so.*

%files -n libhtp-devel
%_includedir/*
%_libdir/pkgconfig/htp.pc
%_libdir/*.so

%files -n python-module-suricata
%python_sitelibdir_noarch/suricatasc*

%changelog
* Mon Oct 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.6-alt1
- New version
- Fix CVE-2013-5919

* Mon Aug 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.5-alt1
- New version
- Add support GeoIP
- Add subpackage python-module-suricata

* Mon Aug 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.4-alt1
- New version

* Thu Dec 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4-alt1
- New version

* Sun Jan 22 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.1-alt1
- New version

* Thu Dec 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1.beta1
- New version

* Wed Dec 07 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.1-alt1
- New version

* Thu Nov 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1-alt2
- New version

* Wed Nov 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1-alt1.rc1
- New version

* Sat Sep 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1-alt1.beta2
- New version

* Fri Jun 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.4-alt1
- New version

* Sat Apr 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.3-alt1
- New version
- Use upstream git for sources

* Wed Dec 08 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt2
- Rebuild with new libyaml

* Sat Sep 11 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt1
- New version

* Wed Aug 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- New version

* Fri Jul 23 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- Build for ALT

