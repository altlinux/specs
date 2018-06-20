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
Version: 6.0.0
Release: alt1_2
Summary: OpenMP runtime for clang
Group: Development/Other

License: NCSA
URL: http://openmp.llvm.org
Source0: http://llvm.org/releases/%{version}/openmp-%{version}%{?rc_ver:rc%{rc_ver}}.src.tar.xz

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
Requires: clang-devel%{?isa} = %{version}

%description devel
OpenMP header files.

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



%changelog
* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_2
- new version

