%define _unpackaged_files_terminate_build 1
%define oname avro

Name: python3-module-%oname
Version: 1.7.7
Release: alt2

Summary: Avro is a serialization and RPC framework
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/avro/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-snappy python-tools-2to3

%py_provides %oname


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

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
2to3 -w -n ./scripts/%oname

sed -i 's|#!.*/usr/bin/env python|#!/usr/bin/env python3|' \
    ./scripts/%oname

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD/src

python3 setup.py test
#py.test-%_python3_version -vv

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Oct 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.7.7-alt2
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.7-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.7-alt1
- Initial build for Sisyphus

