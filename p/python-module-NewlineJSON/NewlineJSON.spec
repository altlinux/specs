%define oname NewlineJSON

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20150115
Summary: Newline delimited JSON I/O that is hot swappable with csv.DictReader/Writer
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/NewlineJSON/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/geowurster/NewlineJSON.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-click-tests python-module-coverage
BuildPreReq: python-module-nose python-module-simplejson
BuildPreReq: python-module-ujson python-module-yajl
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-click-tests python3-module-coverage
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-ujson python3-module-yajl
%endif

%py_provides newlinejson
%py_requires json click

%description
Read and write files with a single JSON object on every line.

See %oname-sample-data for valid input examples.

%package -n python3-module-%oname
Summary: Newline delimited JSON I/O that is hot swappable with csv.DictReader/Writer
Group: Development/Python3
%py3_provides newlinejson
%py3_requires json click

%description -n python3-module-%oname
Read and write files with a single JSON object on every line.

See %oname-sample-data for valid input examples.

%package -n %oname-sample-data
Summary: Valid input examples for %oname
Group: Development/Python

%description -n %oname-sample-data
Read and write files with a single JSON object on every line.

This package contains valid input examples for %oname.

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
	mv $i $i.py3
done
popd
%endif

%python_install

install -d %buildroot%_datadir/%oname
cp -fR sample-data %buildroot%_datadir/%oname/

%check
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
#nosetests3 -v
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%files -n %oname-sample-data
%_datadir/%oname

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150115
- Initial build for Sisyphus

