%define _unpackaged_files_terminate_build 1
%define oname guzzle_sphinx_theme
Name: python-module-%oname
Version: 0.7.11
Release: alt1.1
Summary: Sphinx theme used by Guzzle
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/guzzle_sphinx_theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/guzzle/guzzle_sphinx_theme.git
Source0: https://pypi.python.org/packages/f4/7d/aed8cd5e4ca52bb8550d2c33fcbb8d6dbd5c2cf5e1694202d2135b374eba/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx

%py_provides %oname

%description
Sphinx theme used by Guzzle: http://guzzlephp.org

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.11-alt1
- automated PyPI update

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20140911
- Initial build for Sisyphus

