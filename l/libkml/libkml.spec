Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3 rpm-macros-cmake rpm-macros-fedora-compat rpm-macros-java
BuildRequires: boost-devel java-devel-default python-devel rpm-build-java
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%undefine _ld_as_needed

Name:           libkml
Version:        1.3.0
Release:        alt1_29
Summary:        Reference implementation of OGC KML 2.2

License:        BSD
URL:            https://github.com/libkml/libkml
Source0:        https://github.com/libkml/libkml/archive/%{version}/libkml-%{version}.tar.gz
# TODO: Port to minizip-2.x, meanwhile bundle version 1.3.0
# wget http://sourceforge.net/projects/libkml-files/files/1.3.0/minizip.tar.gz/download
Source1:        minizip-1.3.0.tar.gz

## See https://github.com/libkml/libkml/pull/239
Patch0:         0001-Fix-build-failure-due-to-failure-to-convert-pointer-.patch
Patch1:         0002-Fix-mistaken-use-of-std-cerr-instead-of-std-endl.patch
Patch2:         0003-Fix-python-tests.patch
Patch3:         0004-Correctly-build-and-run-java-test.patch
# Fix a fragile test failing on i686
Patch4:         fragile_test.patch
# Don't bytecompile python sources as part of build process, leave it to rpmbuild
Patch5:         libkml_dont-bytecompile.patch
# Add crypt.h which was removed from Fedora minizip package (see #1424609)
Patch6:         libkml_crypth.patch
# Use local file for bundled minizip
Patch7:         libkml-bundle-minizip.patch
# Fix possible OOB array access in strcmp due to undersized array
Patch8:         libkml_test_strcmp.patch

BuildRequires:  ctest cmake
BuildRequires:  curl-devel
BuildRequires:  boost-complete
BuildRequires:  libexpat-devel
BuildRequires:  libgtest-devel
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  junit
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  liburiparser-devel
BuildRequires:  zlib-devel

Provides:       bundled(minizip) = 1.3.0

%global __requires_exclude_from ^%{_docdir}/.*$
%global __provides_exclude_from ^%{python_sitelibdir}/.*\\.so$
Source44: import.info


%description
Reference implementation of OGC KML 2.2.
It also includes implementations of Google's gx: extensions used by Google
Earth, as well as several utility libraries for working with other formats.


%package -n python3-module-libkml
Group: Other
Summary:        Python 3 bindings for %{name}
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-module-libkml
The python3-%{name} package contains Python 3 bindings for %{name}.


%package java
Group: Other
Summary:        Java bindings for %{name}
Requires:       %{name} = %{version}-%{release}

%description java
The %{name}-java package contains Java bindings for %{name}.


%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       boost-complete

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

mkdir -p %{__cmake_builddir}
cp -a %{SOURCE1} %{__cmake_builddir}


%build
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%global optflags %{optflags} -fPIC
%{fedora_cmake} -DWITH_SWIG=ON -DWITH_PYTHON=ON -DWITH_JAVA=ON \
  -DJNI_INSTALL_DIR=%{_libdir}/%{name} \
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/kml \
  -DPYTHON_LIBRARY=%{_libdir}/libpython%{__python3_version}$(python3-config --abiflags).so \
  -DPYTHON_INCLUDE_DIR=%{_includedir}/python%{__python3_version}$(python3-config --abiflags)/ \
  -DPYTHON_INSTALL_DIR=%{python3_sitelibdir} \
  -DBUILD_TESTING=ON \
  -DBUILD_EXAMPLES=ON
# Parallel build broken
%global _smp_mflags -j1
%fedora_cmake_build


%install
%fedora_cmake_install


%check
# Ignore test failures on ppc64le, base_zip_file test segfaults there
%ifarch ppc64le
%fedora_ctest || :
%else
%fedora_ctest
%endif


%files
%doc --no-dereference LICENSE
%doc AUTHORS README.md
%{_libdir}/libkml*.so.*

%files -n python3-module-libkml
%{python3_sitelibdir}/*.so
%{python3_sitelibdir}/*.py
%{python3_sitelibdir}/__pycache__/*.pyc

%files java
%{_javadir}/LibKML.jar
%{_libdir}/%{name}/

%files devel
%doc examples
%{_includedir}/kml/
%{_libdir}/libkml*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_29
- new version

