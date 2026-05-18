%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%def_enable dc
%def_disable fw_mgr
%def_enable xml2
%def_enable cs
%def_enable inband
%def_enable openssl
%def_disable i2c
%def_disable cables
%def_disable nvml
%def_disable vfio
%def_disable dpa
%def_disable nvfwreset

Name: mstflint
Version: 4.36.0.1
Release: alt1

Summary: Mellanox firmware burning application
License: GPLv2 or BSD
Group: System/Base

Url: http://openib.org/
# VCS-git: https://github.com/Mellanox/mstflint.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: autoconf-archive
BuildRequires: gcc-c++
%{?_enable_dc:BuildRequires: zlib-devel}
%{?_enable_fw_mgr:BuildRequires: libcurl-devel liblzma-devel zlib-devel boost-devel}
%{?_enable_xml2:BuildRequires: libxml2-devel}
%{?_enable_inband:BuildRequires: rdma-core-devel}
%{?_enable_cs:BuildRequires: libssl-devel}
%{?_enable_openssl:BuildRequires: libssl-devel openssl}

BuildRequires: libiniparser-devel jsoncpp-devel libmuparser-devel libsqlite3-devel
AutoReq: yes, nopython

%add_python_compile_exclude %_libdir/%name/python_tools
%add_python3_compile_exclude %_libdir/%name/python_tools
%add_python3_path %_libdir/%name/python_tools


%description
This package contains a tool for burning updated firmware on to
Mellanox manufactured InfiniBand adapters.

%prep
%setup

%ifarch %e2k
sed -i "s/__x86_64__/__e2k__/" common/compatibility.h \
	mtcr_ul/packets_common.h tools_layouts/adb_to_c_utils.h
%endif

%build
mkdir config
echo "#define TOOLS_GIT_SHA \"%release\"" > common/gitversion.h

%autoreconf
%configure \
    %{subst_enable dc} \
    %{?_enable_fw_mgr:--enable-fw-mgr} \
    %{subst_enable xml2} \
    %{subst_enable inband} \
    %{subst_enable cs} \
    %{subst_enable openssl} \
    %{subst_enable i2c} \
    %{subst_enable cables} \
    %{subst_enable nvml} \
    %{subst_enable vfio} \
    %{subst_enable dpa} \
    %{subst_enable nvfwreset} \
    MSTFLINT_VERSION_STR="%name %version-%release"

%make_build
sed -i "s|^#!/usr/bin/env python.*|#!/usr/bin/python3|" tracers/fwtrace/mstfwtrace.py
sed -i "s|^#!/usr/bin/python$|#!/usr/bin/python3|" common/autocomplete/mft_help_to_completion.py

%install
%makeinstall_std
rm -rf %buildroot%_includedir
rm -f  %buildroot%_libdir/*.a
rm -f  %buildroot%_libdir/%name/*.a

%files
%_bindir/*
%_datadir/%name
%dir %_libdir/%name
%_libdir/%name/python_tools
%_libdir/%name/sdk
%_man1dir/*

%changelog
* Mon May 18 2026 Andrew A. Vasilyev <andy@altlinux.org> 4.36.0.1-alt1
- v4.36.0-1

* Tue Feb 24 2026 Andrew A. Vasilyev <andy@altlinux.org> 4.35.0.1-alt1
- v4.35.0-1

* Tue Feb 03 2026 Andrew A. Vasilyev <andy@altlinux.org> 4.34.1.3-alt1
- v4.34.1-3

* Thu Jan 15 2026 Andrew A. Vasilyev <andy@altlinux.org> 4.34.1.2-alt1
- v4.34.1-2

* Tue Dec 30 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.34.0.2-alt1
- v4.34.0-2

* Mon May 12 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.32.0.1-alt1
- v4.32.0-1

* Tue Mar 04 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.31.0.1-alt1
- v4.31.0-1

* Wed Nov 13 2024 Andrew A. Vasilyev <andy@altlinux.org> 4.30.0.1-alt1
- v4.30.0-1

* Sat Sep 07 2024 Andrew A. Vasilyev <andy@altlinux.org> 4.29.0.1-alt1
- v4.29.0-1

* Tue Jun 04 2024 Andrew A. Vasilyev <andy@altlinux.org> 4.28.0-alt1
- v4.28.0-1

* Fri Dec 01 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.26.0-alt1
- v4.26.0-1

* Thu Jun 08 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.24.0-alt1
- v4.24.0-1

* Tue Mar 07 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.23.0-alt1
- v4.23.0-1

* Mon Aug 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.21.0-alt1
- v4.21.0-1

* Fri Jun 17 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.20.1-alt1
- v4.20.1-1

* Fri Dec 31 2021 Andrew A. Vasilyev <andy@altlinux.org> 4.18.0-alt1
- v4.18.0-1

* Fri Dec 31 2021 Michael Shigorin <mike@altlinux.org> 4.17.0-alt2
- e2k ftbfs fix (ilyakurdyukov@)
- minor spec cleanup

* Mon Nov 15 2021 Andrew A. Vasilyev <andy@altlinux.org> 4.17.0-alt1
- v4.17.0-1

* Wed Oct 27 2021 Andrew A. Vasilyev <andy@altlinux.org> 4.16.0-alt3
- FTBFS: fix build with LTO

* Wed Jun 09 2021 Alexey Shabalin <shaba@altlinux.org> 4.16.0-alt2
- v4.16.0-2

* Sun Mar 14 2021 Alexey Shabalin <shaba@altlinux.org> 4.16.0-alt1
- v4.16.0-1

* Sun Apr 12 2020 Alexey Shabalin <shaba@altlinux.org> 4.14.0-alt1
- v4.14.0-1

* Fri Oct 18 2019 Alexey Shabalin <shaba@altlinux.org> 4.13.1-alt1
- v4.13.1-1

* Mon Feb 11 2019 Alexey Shabalin <shaba@altlinux.org> 4.11.0-alt1
- v4.11.0-2

* Wed Oct 31 2018 Alexey Shabalin <shaba@altlinux.org> 4.10.0-alt1
- v4.10.0-3

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Aug 17 2010 Andriy Stepanov <stanv@altlinux.ru> 1.4-alt2
- New version (OFED 1.5.1)

* Tue Dec 08 2009 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1
- Initial build

