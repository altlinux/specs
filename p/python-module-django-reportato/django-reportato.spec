%define oname django-reportato

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0
Release: alt2.git20140707
Summary: Very simple CSV reports with Django
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-reportato/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/potatolondon/reportato.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-modules-json python-module-django-tests
#BuildPreReq: python-modules-sqlite3 python-module-mock
#BuildPreReq: python-module-django-dbbackend-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools 
#python3-module-mock
#BuildPreReq: python3-module-django-tests python3-modules-sqlite3
#BuildPreReq: python3-module-django-dbbackend-sqlite3 
BuildPreReq: python-tools-2to3
%endif

%description
The goal of Reportato is to provide a Django-ish approach to easily get
CSV or Google Spreadsheet generated reports.

%package -n python3-module-%oname
Summary: Very simple CSV reports with Django
Group: Development/Python3

%description -n python3-module-%oname
The goal of Reportato is to provide a Django-ish approach to easily get
CSV or Google Spreadsheet generated reports.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python runtests.py

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 1.0-alt2.git20140707
- Rebuild with "def_disable check"
- Cleanup build deps

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20140707
- Initial build for Sisyphus

