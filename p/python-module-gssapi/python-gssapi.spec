%define _unpackaged_files_terminate_build 1

%define mname gssapi
%def_without python3

Name: python-module-%mname
Version: 1.2.0
Release: alt1
Summary: Python Bindings for GSSAPI (RFC 2743/2744 and extensions)

Group: Development/Python
License: %bsdstyle
Url: https://github.com/pythongssapi/python-gssapi

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-setuptools python-module-Cython
BuildRequires: libkrb5-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%setup_python_module %mname

%description
A set of Python bindings to the GSSAPI C library providing both
a high-level pythonic interfaces and a low-level interfaces
which more closely matches RFC 2743.  Includes support for
RFC 2743, as well as multiple extensions.

%if_with python3
%package -n python3-module-%mname
Summary: Python3 Bindings for GSSAPI (RFC 2743/2744 and extensions)
Group: Development/Python3

%description -n python3-module-%mname
A set of Python bindings to the GSSAPI C library providing both
a high-level pythonic interfaces and a low-level interfaces
which more closely matches RFC 2743.  Includes support for
RFC 2743, as well as multiple extensions.
This is a Python3 module.
%endif

%prep
%setup
#patch -p1
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE.txt README.txt
%python_sitelibdir/*

%exclude %python_sitelibdir/%mname/tests/

%if_with python3
%files -n python3-module-%mname
%doc LICENSE.txt README.txt
%python3_sitelibdir/*

%exclude %python3_sitelibdir/%mname/tests/
%endif

%changelog
* Tue May 10 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Initial build.

