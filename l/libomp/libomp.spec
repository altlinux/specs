# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-generic-compat rpm-macros-mageia-compat
BuildRequires: gcc-c++ perl(Pod/Usage.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 10.0.0
#global rc_ver 5
%global baserelease 1
%global libomp_srcdir openmp-%{version}%{?rc_ver:rc%{rc_ver}}.src


%ifarch ppc64le
%global libomp_arch ppc64
%else
%global libomp_arch %{_arch}
%endif


Name: libomp
Version: 10.0.0
Release: alt1_%{baserelease}%{?rc_ver:.rc%{rc_ver}}
Summary: OpenMP runtime for clang
Group: Development/Other

License: NCSA
URL: http://openmp.llvm.org
Source0: http://%{?rc_ver:pre}releases.llvm.org/%{version}/%{?rc_ver:rc%{rc_ver}}/%{libomp_srcdir}.tar.xz
Source1: run-lit-tests
Source2: lit.fedora.cfg.py
Source3: https://%{?rc_ver:pre}releases.llvm.org/%{version}/%{?rc_ver:rc%{rc_ver}}/%{libomp_srcdir}.tar.xz.sig
Source4: https://prereleases.llvm.org/%{version}/hans-gpg-key.asc

Patch0: 0001-CMake-Make-LIBOMP_HEADERS_INSTALL_PATH-a-cache-varia.patch
Patch1: 99b03c1c18.patch

BuildRequires: ccmake cmake ctest
BuildRequires: libasm-devel libdw-devel libelf-devel
BuildRequires: perl
BuildRequires: perl-base
BuildRequires: perl-Encode perl-Encode-CN perl-Encode-JP perl-Encode-KR perl-Encode-TW
BuildRequires: libffi-devel

# libomp does not support s390x.
ExcludeArch: s390x
Source44: import.info

%description
OpenMP runtime for clang.

%package devel
Group: Development/Other
Summary: OpenMP header files
#Requires: clang-devel%{?isa} = %{version}

%description devel
OpenMP header files.

%package test
Group: Development/Other
Summary: OpenMP regression tests
Requires: %{name}%{?isa} = %{version}
Requires: %{name}-devel%{?isa} = %{version}
#Requires: clang10.0
#Requires: llvm10.0
Requires: gcc
Requires: gcc-c++
#Requires: python3-module-lit

%description test
OpenMP regression tests

%prep
%setup -q -n openmp-%{version}%{?rc_ver:rc%{rc_ver}}.src
%patch0 -p1
%patch1 -p1


%build
mkdir -p _build
cd _build

# FC compatibility:
%global _vpath_builddir .
%global _vpath_srcdir ..

%{mageia_cmake} \
	-DLIBOMP_INSTALL_ALIASES=OFF \
	-DLIBOMP_HEADERS_INSTALL_PATH:PATH=%{_libdir}/clang/%{version}/include \
%if 0%{?__isa_bits} == 64
	-DOPENMP_LIBDIR_SUFFIX=64 \
%else
	-DOPENMP_LIBDIR_SUFFIX= \
%endif

%make_build


%install
%makeinstall_std -C _build

# Test package setup
%global libomp_srcdir %{_datadir}/libomp/src/
%global libomp_testdir %{libomp_srcdir}/runtime/test/
%global lit_cfg %{libomp_testdir}/%{_arch}.site.cfg.py
%global lit_fedora_cfg %{_datadir}/libomp/lit.fedora.cfg.py

install -d %{buildroot}%{libomp_srcdir}/runtime
cp -R runtime/test  %{buildroot}%{libomp_srcdir}/runtime
cp -R runtime/src  %{buildroot}%{libomp_srcdir}/runtime

# Generate lit config files.  Strip off the last line that initiates the
# test run, so we can customize the configuration.
head -n -1 _build/runtime/test/lit.site.cfg >> %{buildroot}%{lit_cfg}

# Install custom fedora config file
cp %{SOURCE2} %{buildroot}%{lit_fedora_cfg}

# Patch lit config files to load custom fedora config
echo "lit_config.load_config(config, '%{lit_fedora_cfg}')" >> %{buildroot}%{lit_cfg}

# Install test script
install -d %{buildroot}%{_libexecdir}/tests/libomp
install -m 0755 %{SOURCE1} %{buildroot}%{_libexecdir}/tests/libomp

# Remove static libraries with equivalent shared libraries
rm -rf %{buildroot}%{_libdir}/libarcher_static.a


%files
%{_libdir}/libomp.so
%{_libdir}/libomptarget.so
%ifnarch %{arm}
%{_libdir}/libarcher.so
%endif
%ifnarch %{arm} %{ix86}
%{_libdir}/libomptarget.rtl.%{libomp_arch}.so
%endif

%files devel
%{_libdir}/clang/%{version}/include/omp.h
%ifnarch %{arm}
%{_libdir}/clang/%{version}/include/omp-tools.h
%{_libdir}/clang/%{version}/include/ompt.h
%endif

%files test
%{_datadir}/libomp
%{_libexecdir}/tests/libomp/


%changelog
* Thu Apr 09 2020 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_1
- final version

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_0.1.rc2
- update by mgaimport

* Wed Feb 20 2019 Igor Vlasenko <viy@altlinux.ru> 7.0.1-alt1_1
- new version

* Sun Dec 23 2018 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_2
- new version

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_2
- new version

