%define oname swadr

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20150111
Summary: Import data from CSV, TSV, etc. files into SQLite3 database
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/swadr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ericpruitt/swadr.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires sqlite3

%description
S.W.A.D.R., SQLite3 With Arbitrarily Delimited Records, is designed to
be a replacement and significant improvement over SQLet, "a free,
open-source script that allows you to directly execute SQL on multiple
text files, right from the Linux command line." In addition to
augmenting the features of SQLet, I also elected to use the BSD 2-Clause
License instead of the GPL (SWADR is derived neither in whole nor part
from SQLet).

%package -n python3-module-%oname
Summary: Import data from CSV, TSV, etc. files into SQLite3 database
Group: Development/Python3
%py3_provides %oname
%py3_requires sqlite3

%description -n python3-module-%oname
S.W.A.D.R., SQLite3 With Arbitrarily Delimited Records, is designed to
be a replacement and significant improvement over SQLet, "a free,
open-source script that allows you to directly execute SQL on multiple
text files, right from the Linux command line." In addition to
augmenting the features of SQLet, I also elected to use the BSD 2-Clause
License instead of the GPL (SWADR is derived neither in whole nor part
from SQLet).

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

%check
python src/tests.py -v
%if_with python3
pushd ../python3
python3 src/tests.py -v
popd
%endif

%files
%doc *.md src/samples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md src/samples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150111
- Initial build for Sisyphus

