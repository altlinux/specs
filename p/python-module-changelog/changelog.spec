%define _unpackaged_files_terminate_build 1
%define oname changelog
Name: python-module-%oname
Version: 0.3.5
Release: alt1
Summary: Provides simple Sphinx markup to render changelog displays
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/changelog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/73/4c/de965aaaff5fb3afbbd6fa5c96904d6bf204a5e35c181098761544861d4b/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests

%py_provides %oname

%description
A Sphinx extension to generate changelog files.

This is an experimental, possibly-not-useful extension that's used by
the SQLAlchemy project and related projects.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1
- automated PyPI update

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

