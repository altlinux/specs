%define _unpackaged_files_terminate_build 1

Name: libtlsh
Version: 4.9.3
Release: alt1

Summary: Fuzzy text matching library
Group: System/Libraries
License: ASL 2.0
Url: https://github.com/trendmicro/tlsh

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: gcc-c++ cmake python3-devel ctest libstdc++-devel-static

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

%package -n python3-module-%name
Summary: Python 3 interface for TLSH
Group: Development/Python3
%description -n python3-module-%name
%_description

%prep
%setup
%patch1 -p1

%build
%cmake -DTLSH_SHARED_LIBRARY=1
%cmake_build

pushd py_ext
%python3_build
popd

%check
make -C %_cmake__builddir test

%install
mkdir -p %buildroot%_libdir %buildroot%_includedir
cp -a lib/libtlsh.so* %buildroot%_libdir/
cp -a include %buildroot%_includedir/tlsh/

pushd py_ext
%python3_install
popd

%files
%doc LICENSE NOTICE.txt README.md
%doc TLSH_CTC_final.pdf
%doc TLSH_Introduction.pdf
%doc Attacking_LSH_and_Sim_Dig.pdf
%_libdir/libtlsh.so.*

%files devel
%_includedir/tlsh
%_libdir/libtlsh.so

%files -n python3-module-%name
%doc LICENSE NOTICE.txt README.md
%python3_sitelibdir/*

%changelog
* Wed Sep 22 2021 Slava Aseev <ptrnine@altlinux.org> 4.9.3-alt1
- update to latest upstream version
- remove python2 build
- enable tests

* Wed Jan 16 2019 Slava Aseev <ptrnine@altlinux.org> 3.4.5-alt1
- Initial build for ALT

