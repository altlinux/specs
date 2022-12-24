# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-generic-compat rpm-macros-mageia-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name alglib
%define major     3
%define libname   lib%{name}%{major}
%define develname lib%{name}-devel

Name:           alglib
Version:        3.20.0
Release:        alt1_1
Summary:        A numerical analysis and data processing library
Group:          System/Libraries
License:        GPLv2+
URL:            https://www.alglib.net/
Source0:        https://www.alglib.net/translator/re/%{name}-%{version}.cpp.gpl.tgz
Source1:        ALGLIBConfig.cmake
# Extracted from manual.cpp.html
Source2:        bsd.txt

# Make test output more verbose
# Patch0:         alglib_verbose-tests.patch
# From Debian:
Patch1:         01_add_cmake.patch

BuildRequires:  ccmake cmake ctest
BuildRequires:  gcc-c++
Source44: import.info

%description
ALGLIB is a cross-platform numerical analysis and data processing library.
ALGLIB features include:
 - Data analysis (classification/regression, including neural networks)
 - Optimization and nonlinear solvers
 - Interpolation and linear/nonlinear least-squares fitting
 - Linear algebra (direct algorithms, EVD/SVD), direct and iterative linear
   solvers, Fast Fourier Transform and many other algorithms (numerical
   integration, ODEs, statistics, special functions)


%package -n     %{libname}
Summary:        Shared %{name} library
Group:          System/Libraries

%description -n %{libname}
ALGLIB is a cross-platform numerical analysis and data processing library.
ALGLIB features include:
 - Data analysis (classification/regression, including neural networks)
 - Optimization and nonlinear solvers
 - Interpolation and linear/nonlinear least-squares fitting
 - Linear algebra (direct algorithms, EVD/SVD), direct and iterative linear
   solvers, Fast Fourier Transform and many other algorithms (numerical
   integration, ODEs, statistics, special functions)

This package provides the shared %{name} library.

%package -n     %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} >= %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Group: System/Libraries
Summary:        API documentation for %{name}
License:        BSD
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the %{name} API documentation.


%prep
%setup -q -n %{name}-cpp
%patch1 -p1

cp %{SOURCE1} .
cp %{SOURCE2} .

# Set version and soversion in cmake file
%define soversion %(echo %{version}|cut -d. -f1,4)
sed -i 's|\${VERSION}|%{version}|' CMakeLists.txt
sed -i 's|\${SOVERSION}|%{soversion}|' CMakeLists.txt

# Fix permissions and line endings
chmod 644 gpl2.txt
chmod 644 manual.cpp.html
sed -i 's|\r||g' manual.cpp.html


%build
# disable FMA support to get it pass all tests
%ifarch aarch64 %{power64} s390 s390x
export CXXFLAGS="%{optflags} -ffp-contract=off"
export CFLAGS="%{optflags} -ffp-contract=off"
%endif
%{mageia_cmake}
%mageia_cmake_build


%install
%mageia_cmake_install

%if 0
%check
pushd build
# FIXME Temporarily ignore test failures on test_c due to GCC7 test failure on i686, see
# http://bugs.alglib.net/view.php?id=689
%ifarch %{ix86}
LD_LIBRARY_PATH=$PWD ./test_c || true
%else
LD_LIBRARY_PATH=$PWD ./test_c || false
%endif
LD_LIBRARY_PATH=$PWD ./test_i || false
popd
%endif

%files -n %{libname}
%doc --no-dereference gpl2.txt
%{_libdir}/libalglib.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}/
%{_libdir}/libalglib.so
%{_libdir}/cmake/ALGLIB/

%files doc
%doc --no-dereference bsd.txt
%doc manual.cpp.html


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 3.20.0-alt1_1
- update by mgaimport

* Fri Sep 02 2022 Igor Vlasenko <viy@altlinux.org> 3.19.0-alt1_1
- update by mgaimport

* Wed Jan 13 2021 Igor Vlasenko <viy@altlinux.ru> 3.17.0-alt1_1
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.16.0-alt1_2
- fixed build

* Thu Dec 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.16.0-alt1_1
- update by mgaimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 3.15.0-alt1_1
- update by mgaimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.14.0-alt1_1
- update by mgaimport

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.13.0-alt1_1
- new version

