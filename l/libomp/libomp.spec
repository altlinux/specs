# tmp hack til clang update
%filter_from_requires /^clang/d
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-generic-compat rpm-macros-mageia-compat
BuildRequires: gcc-c++ openmpi-devel perl(Net/Domain.pm) perl(Pod/Usage.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%ifarch ppc64le
%global libomp_arch ppc64
%else
%global libomp_arch %{_arch}
%endif


Name: libomp
Version: 7.0.0
Release: alt1_2
Summary: OpenMP runtime for clang
Group: Development/Other

License: NCSA
URL: http://openmp.llvm.org
Source0: http://llvm.org/releases/%{version}/openmp-%{version}%{?rc_ver:rc%{rc_ver}}.src.tar.xz
Source1: runtest.sh

Patch0: 0001-CMake-Make-LIBOMP_HEADERS_INSTALL_PATH-a-cache-varia.patch

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
Requires: clang6.0
Requires: llvm6.0
Requires: gcc
Requires: gcc-c++
Requires: python3-module-lit

%description test
OpenMP regression tests

%prep
%setup -q -n openmp-%{version}%{?rc_ver:rc%{rc_ver}}.src
%patch0 -p1

%build
# FC compatibility:
ln -sf build _build

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
%global gcc_lit_cfg %{buildroot}%{libomp_testdir}/gcc.site.cfg
%global clang_lit_cfg %{buildroot}%{libomp_testdir}/clang.site.cfg

install -d %{buildroot}%{libomp_srcdir}/runtime
cp -R runtime/test  %{buildroot}%{libomp_srcdir}/runtime
cp -R runtime/src  %{buildroot}%{libomp_srcdir}/runtime

# Add symlinks to the libomp headers/library so gcc can find them.
ln -s %{_libdir}/clang/%{version}/include/omp.h %{buildroot}%{libomp_testdir}/omp.h
ln -s %{_libdir}/clang/%{version}/include/ompt.h %{buildroot}%{libomp_testdir}/ompt.h
ln -s %{_libdir}/libomp.so %{buildroot}%{libomp_testdir}/libgomp.so

# Generic test config
echo "import tempfile" > %{gcc_lit_cfg}
cat _build/runtime/test/lit.site.cfg >> %{gcc_lit_cfg}
sed -i 's~\(config.test_filecheck = \)""~\1"%{_libdir}/llvm/FileCheck"~' %{gcc_lit_cfg}
sed -i 's~\(config.omp_header_directory = \)"[^"]\+"~\1"%{_includedir}"~' %{gcc_lit_cfg}
sed -i 's~\(config.libomp_obj_root = \)"[^"]\+"~\1tempfile.mkdtemp()[1]~' %{gcc_lit_cfg}
sed -i 's~\(lit_config.load_config(config, \)"[^"]\+"~\1"%{libomp_testdir}/lit.cfg"~' %{gcc_lit_cfg}

# GCC config
# test_compiler_features was already populated with gcc information if gcc was used
# to compile libomp.
sed -i 's~\(config.test_c_compiler = \)"[^"]\+"~\1"%{_bindir}/gcc"~' %{gcc_lit_cfg}
sed -i 's~\(config.test_cxx_compiler = \)"[^"]\+"~\1"%{_bindir}/g++"~' %{gcc_lit_cfg}
sed -i 's~\(config.library_dir = \)"[^"]\+"~\1"%{libomp_testdir}"~' %{gcc_lit_cfg}

# Clang config
cp %{gcc_lit_cfg} %{clang_lit_cfg}
sed -i 's~\(config.test_compiler_features = \)\[[^\[]\+]~\1["clang"]~' %{clang_lit_cfg}
sed -i 's~\(config.test_c_compiler = \)"[^"]\+"~\1"%{_bindir}/clang"~' %{clang_lit_cfg}
sed -i 's~\(config.test_cxx_compiler = \)"[^"]\+"~\1"%{_bindir}/clang++"~' %{clang_lit_cfg}
sed -i 's~\(config.library_dir = \)"[^"]\+"~\1"%{_libdir}"~' %{clang_lit_cfg}

install -m 0755 %{SOURCE1} %{buildroot}%{_datadir}/libomp


%files
%{_libdir}/libomp.so
%{_libdir}/libomptarget.so
%ifnarch %{arm} %{ix86}
%{_libdir}/libomptarget.rtl.%{libomp_arch}.so
%endif

%files devel
%{_libdir}/clang/%{version}/include/omp.h
%ifnarch %{arm}
%{_libdir}/clang/%{version}/include/ompt.h
%endif

%if 0
%files test
%{_datadir}/libomp
%endif


%changelog
* Sun Dec 23 2018 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_2
- new version

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_2
- new version

