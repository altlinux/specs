%define oname pyasn

%def_with python3

Name: python-module-%oname
Version: 1.5.0
Release: alt1.b6.git20141105.1.1.1
Summary: Offline IP address to Autonomous System Number lookup module
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyasn/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hadiasghari/pyasn.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-backport_ipaddress
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-ipaddress
%endif

%py_provides %oname
%py_requires backport_ipaddress

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-backport_ipaddress python-module-coverage python-module-nose python-module-setuptools python3-devel python3-module-coverage python3-module-nose python3-module-setuptools rpm-build-python3

%description
pyasn is a Python extension module that enables very fast IP address to
Autonomous System Number lookups. Current state and Historical lookups
can be done, based on the BGP / MRT file used as input.

pyasn is different from other ASN lookup tools in that it providers
offline and historical lookups. It provides utility scripts for users to
build their own lookup databases based on any BGP/MRT dump file. This
makes pyasn much faster than online dig/whois/json lookups.

%package -n python3-module-%oname
Summary: Offline IP address to Autonomous System Number lookup module
Group: Development/Python3
%py3_provides %oname
%py3_requires ipaddress

%description -n python3-module-%oname
pyasn is a Python extension module that enables very fast IP address to
Autonomous System Number lookups. Current state and Historical lookups
can be done, based on the BGP / MRT file used as input.

pyasn is different from other ASN lookup tools in that it providers
offline and historical lookups. It provides utility scripts for users to
build their own lookup databases based on any BGP/MRT dump file. This
makes pyasn much faster than online dig/whois/json lookups.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.b6.git20141105.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.b6.git20141105.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1.b6.git20141105.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.b6.git20141105
- Initial build for Sisyphus

