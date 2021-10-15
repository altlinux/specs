# ExclusiveArch until someone update (lib)atlas-devel
# due to armadillo dependency
ExclusiveArch: %ix86 x86_64
BuildRequires: libhdf5-devel libsuperlu-devel
Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ensmallen
Version:        2.17.0
Release:        alt1_1
Summary:        Header-only C++ library for efficient mathematical optimization

License:        BSD
URL:            https://www.ensmallen.org
Source0:        https://www.ensmallen.org/files/%{name}-%{version}.tar.gz

BuildRequires:  ctest cmake
BuildRequires:	gcc-c++
BuildRequires:	libarmadillo-devel >= 8.400.0

# ensmallen is header-only, and the build just builds the tests, so there's no
# use for a debuginfo package.
%global debug_package %{nil}

Patch0:		catch_constexpr.patch
Source44: import.info

%description
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%prep
%setup -q
%patch0 -p1


%build
%{fedora_v2_cmake} -DENSMALLEN_CMAKE_DIR=%{_libdir}/cmake/ensmallen/ -DBUILD_TESTS=ON

%fedora_v2_cmake_build -t ensmallen_tests

%install
%fedora_v2_cmake_install

%check
# Disable the SmallLovaszThetaSdp test---it exposes a bug in one of ensmallen's
# dependencies.  In addition, sometimes the tests may fail, as they are
# probabilistic---so just make sure the test suite passes at least once out of
# five runs.
%ifarch armv7hl
# There's an issue with the tests on armv7hl.
%else
success=0;
cd %{_vpath_builddir};
for i in `seq 1 5`; do
  code=""; # Reset exit code.
  ./ensmallen_tests --rng-seed=time ~SmallLovaszThetaSdp ~BBSBBLogisticRegressionTest || code=$?
  if [ "a$code" == "a" ]; then
    success=1;
    break;
  fi
done
if [ $success -eq 0 ]; then
  false # Force a build error.
fi
cd ..;
%endif

%package devel
Group: Other
Summary:  Header-only C++ library for efficient mathematical optimization
Provides: ensmallen-static = %{version}-%{release}

%description devel
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%files devel
%doc --no-dereference LICENSE.txt
%{_includedir}/ensmallen.hpp
%{_includedir}/ensmallen_bits/
%{_libdir}/cmake/ensmallen/ensmallen-config-version.cmake
%{_libdir}/cmake/ensmallen/ensmallen-config.cmake
%{_libdir}/cmake/ensmallen/ensmallen-targets.cmake

%changelog
* Thu Oct 14 2021 Igor Vlasenko <viy@altlinux.org> 2.17.0-alt1_1
- update to new release by fcimport

* Mon Nov 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.14.2-alt1_1
- fc import

