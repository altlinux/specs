%define oname demjson

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.2.2
Release: alt1.git20140625.1
Summary: encoder, decoder, and lint/validator for JSON compliant with RFC 7159
License: LGPLv3.0
Group: Development/Python
Url: https://pypi.python.org/pypi/demjson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dmeranda/demjson.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base python3-module-setuptools
BuildRequires: python-devel python-tools-2to3 python3-module-pytest rpm-build-python3 time

%description
The "demjson" module, and the included "jsonlint" script, provide
methods for encoding and decoding JSON formatted data, as well as
checking JSON data for errors and/or portability issues. The jsonlint
command/script can be used from the command line without needing any
programming.

Although the standard Python library now includes basic JSON support
(which it did not when demjson was first written), this module provides
a much more comprehensive implementation with many features not found
elsewhere. It is especially useful for error checking or for parsing
JavaScript data which may not strictly be valid JSON data.

%package -n python3-module-%oname
Summary: encoder, decoder, and lint/validator for JSON compliant with RFC 7159
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The "demjson" module, and the included "jsonlint" script, provide
methods for encoding and decoding JSON formatted data, as well as
checking JSON data for errors and/or portability issues. The jsonlint
command/script can be used from the command line without needing any
programming.

Although the standard Python library now includes basic JSON support
(which it did not when demjson was first written), this module provides
a much more comprehensive implementation with many features not found
elsewhere. It is especially useful for error checking or for parsing
JavaScript data which may not strictly be valid JSON data.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.txt *.md docs/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md docs/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2.2-alt1.git20140625.1
- NMU: Use buildreq for BR.

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.git20140625
- Initial build for Sisyphus

