%define _unpackaged_files_terminate_build 1
%def_enable ebpf_build
%def_enable unwind
%def_disable prelude

%ifarch x86_64
%def_enable hyperscan
%else
%def_disable hyperscan
%endif

Name: suricata
Version: 6.0.10
Release: alt1

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

BuildRequires: /proc
BuildRequires: gcc gcc-c++
BuildRequires: rust >= 1.41.1 rust-cargo cbindgen
BuildRequires: python3-dev
BuildRequires: libpcap-devel libpcre-devel libyaml-devel
BuildRequires: libjansson-devel libnss-devel libcap-ng-devel libgnutls-devel
BuildRequires: libnet-devel libmagic-devel liblua-devel
BuildRequires: zlib-devel liblzma-devel liblz4-devel
%{?_enable_ebpf_build:BuildRequires: libelf-devel libbpf-devel clang llvm}
BuildRequires: libnfnetlink-devel libnetfilter_queue-devel libnetfilter_log-devel
BuildRequires: libhtp-devel >= 0.5.42
BuildRequires: libmaxminddb-devel
BuildRequires: libhiredis-devel
%{?_enable_prelude:BuildRequires: libprelude-devel}
%{?_enable_hyperscan:BuildRequires: libhyperscan-devel}
%{?_enable_unwind:BuildRequires: libunwind-devel}

%add_python3_path %_prefix/lib/%name/python

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

%build
%autoreconf
%configure --enable-gccprotect \
           --enable-pie \
           --disable-gccmarch-native \
           --disable-coccinelle \
           --enable-nfqueue \
	   --enable-nflog \
           --enable-af-packet \
           --enable-jansson \
           --enable-geoip \
           --enable-lua \
           --enable-hiredis \
	   --enable-http2-decompression \
	   %{subst_enable prelude} \
	   %{subst_enable unwind} \
	   %{?_enable_ebpf_build:--enable-ebpf --enable-ebpf-build} \
           --enable-non-bundled-htp \
           --with-libpcre-includes=%_includedir/pcre \
           --with-libprelude-prefix=%prefix \
           --localstatedir=%_var

%make_build

%install
%makeinstall_std

# Setup etc directory
mkdir -p %buildroot%_sysconfdir/%name/rules
install -m 600 rules/*.rules %buildroot%_sysconfdir/%name/rules
install -m 600 *.config %buildroot%_sysconfdir/%name
install -m 600 threshold.config %buildroot%_sysconfdir/%name
install -m 600 suricata.yaml %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_unitdir
install -m 0644 %SOURCE1 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

# Set up logging
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_logrotatedir
install -m 644 %SOURCE3 %buildroot%_logrotatedir/%name

# Setup suricata-update data directory
mkdir -p %buildroot%_localstatedir/%name

# Setup tmpdirs
mkdir -p %buildroot%_tmpfilesdir
install -m 0644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf

# Install init.d service
mkdir -p %buildroot%_initdir
install -m 755 %SOURCE5 %buildroot%_initdir/%name

# Cleanup
rm -r %buildroot%_datadir/doc/%name
rm -rf %buildroot%_includedir

%pre
groupadd -r -f _suricata 2>/dev/null ||:
useradd -r -g _suricata -c 'Suricata User' \
        -s /sbin/nologin -M -d %_localstatedir/%name _suricata 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc doc/Basic_Setup.txt doc/Setting_up_IPSinline_for_Linux.txt
%doc ChangeLog README.md LICENSE
%_bindir/%name
%_bindir/suricatasc
%_bindir/suricatactl
%_prefix/lib/%name/python
%config(noreplace) %attr(-,_suricata,root) %_sysconfdir/%name/suricata.yaml
%config(noreplace) %attr(-,_suricata,root) %_sysconfdir/%name/*.config
%config(noreplace) %attr(-,_suricata,root) %_sysconfdir/%name/rules/*.rules
%config(noreplace) %attr(0600,_suricata,root) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_logrotatedir/%name
%attr(750,_suricata,root) %dir %_logdir/%name
%attr(750,_suricata,root) %dir %_sysconfdir/%name
%attr(750,_suricata,root) %dir %_sysconfdir/%name/rules
%attr(2770,_suricata,_suricata) %dir %_localstatedir/%name
%_tmpfilesdir/%name.conf
%_datadir/%name

%changelog
* Mon Mar 27 2023 Alexey Shabalin <shaba@altlinux.org> 6.0.10-alt1
- 6.0.10

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 6.0.4-alt1
- 6.0.4 (Fixes: CVE-2021-35063, CVE-2021-37592, CVE-2021-45098)
- Build without prelude.
- Build with eBPF support.
- Build with Hyperscan support for x86_64 arch.

* Mon Dec 21 2020 Alexey Shabalin <shaba@altlinux.org> 5.0.5-alt1
- 5.0.5

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.0.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Sun Mar 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.0.3-alt2
- NMU: rebuild with preludedb

* Thu Feb 08 2018 Maxim Voronov <mvoronov@altlinux.org> 4.0.3-alt1
- initial build for ALT

