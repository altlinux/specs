%define _unpackaged_files_terminate_build 1
%define oname taschenmesser
Name: python-module-%oname
Version: 0.1.11
Release: alt1.1
Summary: Taschenmesser, a toolbelt with plugins for SCons
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/taschenmesser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/oberstet/taschenmesser.git
Source0: https://pypi.python.org/packages/87/d3/733fd375150196bea8cc89c4bc41b7d00460bcde6891240e80107c671315/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-boto
BuildPreReq: python-module-scour scons

%py_provides %oname

%description
Taschenmesser is a toolbelt containing builders for SCons. It helps you
getting stuff done.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.11-alt1
- automated PyPI update

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140825
- Initial build for Sisyphus

