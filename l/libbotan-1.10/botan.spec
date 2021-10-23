%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define python3_version_nodots3 %(LC_ALL=C python3 -c "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))" 2>/dev/null || echo unknown)
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl-devel
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
%define oldname botan
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major_version 1.10

Name:           libbotan-1.10
Version:        %{major_version}.17
Release:        alt1_28
Summary:        Crypto library written in C++

License:        BSD
URL:            http://botan.randombit.net/
# tarfile is stripped using repack.sh. original tarfile to be found
# here: http://botan.randombit.net/releases/Botan-%%{version}.tgz
Source0:        Botan-%{version}.stripped.tar.gz
Source1:        README.fedora
# Enable only cleared ECC algorithms
Patch0:         botan-1.10.5-ecc-fix.patch
# Make boost_python selectable
Patch1:         botan-boost_python.patch
# Fix wrong path
Patch2:         botan-1.10.13-python-init.patch
# 2to3 doc/conf.py
Patch3:         botan-1.10.17-doc-conf-2to3.patch

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
BuildRequires:  boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-polygon-devel boost-program_options-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires:  bzlib-devel
BuildRequires:  zlib-devel

# do not check .so files in the python_sitelib directories
%global __provides_exclude_from ^(%{python3_sitelibdir}/.*\\.so)$

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}
Source44: import.info
Provides: botan-1.10 = %{version}-%{release}

#ERROR: Unknown or unidentifiable processor "armh"
ExcludeArch: %arm

%description
Botan is a BSD-licensed crypto library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and
CRLs, PKCS \#10 certificate requests, a filter/pipe message processing
system, and a wide variety of other features, all written in portable
C++. The API reference, tutorial, and examples may help impart the
flavor of the library.


%package        devel
Group: Development/C
Summary:        Development files for %{oldname}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Provides: botan-1.10-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%package        doc
Group: Development/C
Summary:        Documentation for %{oldname}
BuildArch:      noarch
Provides: botan-1.10-doc = %{version}-%{release}

%description    doc
%{summary}

This package contains HTML documentation for %{oldname}.


%package -n python3-module-botan-%{major_version}
Group: Development/C
Summary:        Python3 bindings for %{oldname}
%{?python_provide:%python_provide python3-%{oldname}}

%description -n python3-module-botan-%{major_version}
%{summary}

This package contains the Python3 binding for %{oldname}.

Note: The Python binding should be considered alpha software, and the
interfaces may change in the future.


%prep
%setup -q -n Botan-%{version}
%setup -q -n Botan-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


# These tests will fail.
rm -rf checks/ec_tests.cpp

%build

# we have the necessary prerequisites, so enable optional modules
%global enable_modules bzip2,zlib

# fixme: maybe disable unix_procs, very slow.
%global disable_modules gnump

%{__python3} ./configure.py \
        --prefix=%{_prefix} \
        --libdir=%{_lib} \
        --cc=gcc \
        --os=linux \
        --cpu=%{_arch} \
        --enable-modules=%{enable_modules} \
        --disable-modules=%{disable_modules} \
        --with-boost-python \
        --with-python-version=dummy.dummy \
        --with-sphinx

# (ab)using CXX as an easy way to inject our CXXFLAGS
make CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags}

make -f Makefile.python \
     CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags} \
     PYTHON_INC="$(python3-config --includes)" \
     PYTHON_ROOT=. \
     BOOST_PYTHON=boost_python%{python3_version_nodots3}

%install
make install \
     DESTDIR=%{buildroot}%{_prefix} \
     DOCDIR=%{buildroot}%{_docdir}/%{oldname} \
     INSTALL_CMD_EXEC="install -p -m 755" \
     INSTALL_CMD_DATA="install -p -m 644"

make -f Makefile.python install \
     PYTHON_SITE_PACKAGE_DIR=%{buildroot}%{python3_sitelibdir}


# fixups
find doc/examples -type f -exec chmod -x {} \;
mv doc/examples/python doc/python2-examples
cp -a doc/{examples,python2-examples,license.txt} \
   %{buildroot}%{_docdir}/%{oldname}
cp -a %{SOURCE1} %{buildroot}%{_docdir}/%{oldname}
rm -r %{buildroot}%{_docdir}/%{oldname}/manual/{.doctrees,.buildinfo}








%files
%dir %{_docdir}/%{oldname}
%{_docdir}/%{oldname}/readme.txt
%{_docdir}/%{oldname}/README.fedora
%if 0%{?_licensedir:1}
%exclude %{_docdir}/%{oldname}/license.txt
%doc --no-dereference doc/license.txt
%else
%{_docdir}/%{oldname}/license.txt
%endif # licensedir
%{_libdir}/libbotan-%{major_version}.so.*


%files devel
%{_docdir}/%{oldname}/examples
%{_bindir}/botan-config-%{major_version}
%{_includedir}/*
%exclude %{_libdir}/libbotan-%{major_version}.a
%{_libdir}/libbotan-%{major_version}.so
%{_libdir}/pkgconfig/botan-%{major_version}.pc


%files doc
%dir %{_docdir}/%{oldname}
%{_docdir}/%{oldname}/manual
# next files duplicated on purpose, because -doc doesn't depend on the
# main package
%{_docdir}/%{oldname}/readme.txt
%{_docdir}/%{oldname}/README.fedora
%if 0%{?_licensedir:1}
%exclude %{_docdir}/%{oldname}/license.txt
%doc --no-dereference doc/license.txt
%else
%{_docdir}/%{oldname}/license.txt
%endif # licensedir
%{_docdir}/%{oldname}/python2-examples

%if 0
# conflicts with botan2 python
%files -n python3-module-botan-%{major_version}
%{python3_sitelibdir}/%{oldname}
%endif

%check
make CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags} check

# these checks would fail
mv checks/validate.dat{,.orig}
awk '/\[.*\]/{f=0} /\[(RC5.*|RC6)\]/{f=1} (f && !/^#/){sub(/^/,"#")} {print}' \
    checks/validate.dat.orig > checks/validate.dat
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./check --validate


%changelog
* Sat Oct 23 2021 Igor Vlasenko <viy@altlinux.org> 1.10.17-alt1_28
- compat version

