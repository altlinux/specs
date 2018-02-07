%define oname avro

%def_with python3

Name: python-module-%oname
Version: 1.7.7
Release: alt1.1.1
Summary: Avro is a serialization and RPC framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/avro/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-snappy
BuildPreReq: python-modules-json
BuildPreReq: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-snappy
%endif

%py_provides %oname
%py_requires snappy json

%description
Apache Avro(tm) is a data serialization system.

Avro provides:

* Rich data structures.
* A compact, fast, binary data format.
* A container file, to store persistent data.
* Remote procedure call (RPC).
* Simple integration with dynamic languages. Code generation is not
  required to read or write data files nor to use or implement RPC
  protocols. Code generation as an optional optimization, only worth
  implementing for statically typed languages.

%if_with python3
%package -n python3-module-%oname
Summary: Avro is a serialization and RPC framework
Group: Development/Python3
%py3_provides %oname
%py3_requires snappy json

%description -n python3-module-%oname
Apache Avro(tm) is a data serialization system.

Avro provides:

* Rich data structures.
* A compact, fast, binary data format.
* A container file, to store persistent data.
* Remote procedure call (RPC).
* Simple integration with dynamic languages. Code generation is not
  required to read or write data files nor to use or implement RPC
  protocols. Code generation as an optional optimization, only worth
  implementing for statically typed languages.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
2to3 -w -n ../python3/scripts/%oname
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	../python3/scripts/%oname
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
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
export PYTHONPATH=$PWD/src
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD/src
#py.test-%_python3_version -vv
popd
%endif

%files
%doc PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.7-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.7-alt1
- Initial build for Sisyphus

