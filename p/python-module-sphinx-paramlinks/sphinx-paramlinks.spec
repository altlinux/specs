%define _unpackaged_files_terminate_build 1
%define oname sphinx-paramlinks
Name: python-module-%oname
Version: 0.3.2
Release: alt1.1
Summary: Allows param links in Sphinx function/method descriptions to be linkable
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-paramlinks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/68/66/35fd8994e7c380f0272af0fc4b729272fd61a5f209a5ca4b2ee38d92ca68/%{oname}-%{version}.tar.gz

BuildPreReq: python-module-setuptools
BuildArch: noarch

%py_provides sphinx_paramlinks

%description
A Sphinx extension which allows :param: directives within Python
documentation to be linkable.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

