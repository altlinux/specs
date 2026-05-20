%define _unpackaged_files_terminate_build 1
%def_enable ebpf_build
%def_enable unwind

%ifarch x86_64
%def_enable hyperscan
%else
%def_disable hyperscan
%endif

Name: suricata
Version: 8.0.5
Release: alt1

Summary: Intrusion Detection System

License: GPL-2.0-only
Group: Security/Networking
Url: https://suricata.io
Vcs: https://github.com/OISF/suricata.git

Source: %name-%version.tar
Source1: suricata.service
Source2: suricata.sysconfig
Source3: suricata.logrotate
Source4: suricata-tmpfiles.conf
Source5: suricata.init
Patch0: suricata-alt-rules-path.patch

BuildRequires: /proc
BuildRequires: gcc gcc-c++
BuildRequires: rust >= 1.63.0 rust-cargo cbindgen >= 0.10.0
BuildRequires: python3-dev
BuildRequires: libpcap-devel libpcre2-devel libyaml-devel
BuildRequires: libjansson-devel libcap-ng-devel libgnutls-devel
BuildRequires: libnet-devel libmagic-devel liblua-devel
BuildRequires: zlib-devel liblzma-devel liblz4-devel
%{?_enable_ebpf_build:BuildRequires: libelf-devel libbpf-devel clang llvm /usr/bin/llc}
BuildRequires: libnfnetlink-devel libnetfilter_queue-devel libnetfilter_log-devel
BuildRequires: libhtp-devel >= 0.5.48
BuildRequires: libmaxminddb-devel
BuildRequires: libhiredis-devel libevent-devel
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
%patch0 -p1

%build
%add_optflags -llua
%autoreconf
%configure \
    --enable-gccprotect \
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
    %{subst_enable unwind} \
    %{?_enable_ebpf_build:--enable-ebpf --enable-ebpf-build} \
    --enable-non-bundled-htp \
    --localstatedir=%_var

%make_build

%install
%makeinstall_std

# Setup etc directory
mkdir -p %buildroot%_sysconfdir/%name/rules
install -m 600 rules/*.rules %buildroot%_sysconfdir/%name/rules
install -m 600 etc/*.config %buildroot%_sysconfdir/%name
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
rm -rf %buildroot%_datadir/%name/rules

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
* Wed May 20 2026 Andrey Cherepanov <cas@altlinux.org> 8.0.5-alt1
- 8.0.5 (fixes: CVE-2026-45764, CVE-2026-45766, CVE-2026-45769, CVE-2026-45768,
  CVE-2026-46387, CVE-2026-45759, CVE-2026-45762, CVE-2026-45765,
  CVE-2026-45747, CVE-2026-45770, CVE-2026-46352, CVE-2026-45767,
  CVE-2026-45763, CVE-2026-45751, CVE-2026-45752, CVE-2026-45761)

* Wed Mar 18 2026 Andrey Cherepanov <cas@altlinux.org> 8.0.4-alt1
- 8.0.4 (fixes: CVE-2026-31935, CVE-2026-31934, CVE-2026-31931, CVE-2026-31933,
  CVE-2026-31932, CVE-2026-31937).

* Wed Jan 14 2026 Andrey Cherepanov <cas@altlinux.org> 8.0.3-alt1
- 8.0.3 (fixes: CVE-2026-22260, CVE-2026-22263, CVE-2026-22258, CVE-2026-22259,
  CVE-2026-22261, CVE-2026-22262, CVE-2026-22264)

* Thu Nov 06 2025 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- 8.0.2 (Fixed: CVE-2025-64344, CVE-2025-64333, CVE-2025-64332, CVE-2025-64331,
  CVE-2025-64330, CVE-2025-64335, CVE-2025-64334)

* Wed Sep 17 2025 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- 8.0.1 (Fixed: CVE-2025-59147, CVE-2025-59148, CVE-2025-59149, CVE-2025-59150)

* Tue Jul 08 2025 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- 8.0.0
- Added user permission for logrotate rule (ALT #48246).

* Thu Mar 27 2025 Andrey Cherepanov <cas@altlinux.org> 7.0.10-alt1
- 7.0.10

* Thu Mar 20 2025 Andrey Cherepanov <cas@altlinux.org> 7.0.9-alt1
- 7.0.9 (Fixes: CVE-2025-29915, CVE-2025-29917, CVE-2025-29918, 
  CVE-2025-29916)

* Thu Jan 16 2025 Andrey Cherepanov <cas@altlinux.org> 7.0.8-alt1
- 7.0.8 (Fixes: CVE-2024-55627, CVE-2024-55605, CVE-2024-55629,
         CVE-2024-55628, CVE-2024-55626, CVE-2024-45797, CVE-2024-47187,
         CVE-2024-47188, CVE-2024-47522, CVE-2024-45795, CVE-2024-45796,
         CVE-2024-37151, CVE-2024-38536, CVE-2024-38534, CVE-2024-38535)

* Thu Jun 27 2024 Alexey Shabalin <shaba@altlinux.org> 7.0.5-alt1
- 7.0.5 (Fixes: CVE-2024-32664, CVE-2024-32663, CVE-2024-32867
         CVE-2024-28870, CVE-2024-28871, CVE-2022-24713)

* Fri May 24 2024 Alexander Danilov <admsasha@altlinux.org> 6.0.19-alt1
- 6.0.19 (Fixes: CVE-2023-35852, CVE-2023-35852)

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

