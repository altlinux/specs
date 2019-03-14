%define _unpackaged_files_terminate_build 1
%def_with python3

Name: libtlsh
Version: 3.4.5
Release: alt1

Summary: Fuzzy text matching library
Group: System/Libraries
License: ASL 2.0
Url: https://github.com/trendmicro/tlsh

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: gcc-c++ cmake python-devel
%if_with python3
BuildRequires: python3-devel
%endif

%define _description TLSH is a fuzzy matching library. \
Given a byte stream with a minimum length of 50 bytes \
TLSH generates a hash value which can be used for similarity comparisons. \
Similar objects will have similar hash values which allows for \
the detection of similar objects by comparing their hash values.  Note that \
the byte stream should have a sufficient amount of complexity.  For example, \
a byte stream of identical bytes will not generate a hash value.

%description
%_description

%package devel
Summary: Development files for TLSH
Group: Development/C++
%description devel
This package contains development headers and libraries for TLSH.

%_description

%package -n python-module-%name
Summary: Python interface for TLSH
Group: Development/Python
%description -n python-module-%name
%_description

%if_with python3
%package -n python3-module-%name
Summary: Python 3 interface for TLSH
Group: Development/Python3
%description -n python3-module-%name
%_description
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -a py_ext py3_ext
%endif

%build
%cmake
%cmake_build

pushd py_ext
%python_build
popd

%if_with python3
pushd py3_ext
%python3_build
popd
%endif

%install
mkdir -p %buildroot%_libdir %buildroot%_includedir
cp -a lib/libtlsh.so* %buildroot%_libdir/
cp -a include %buildroot%_includedir/tlsh/

pushd py_ext
%python_install
popd

%if_with python3
pushd py3_ext
%python3_install
popd
%endif

%files
%doc LICENSE NOTICE.txt README.md
%doc TLSH_CTC_final.pdf
%doc TLSH_Introduction.pdf
%doc Attacking_LSH_and_Sim_Dig.pdf
%_libdir/libtlsh.so.*

%files devel
%_includedir/tlsh
%_libdir/libtlsh.so

%files -n python-module-%name
%doc LICENSE NOTICE.txt README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%doc LICENSE NOTICE.txt README.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 16 2019 Slava Aseev <ptrnine@altlinux.org> 3.4.5-alt1
- Initial build for ALT

