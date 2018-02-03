%define _unpackaged_files_terminate_build 1
%define oname mozprocess
Name: python-module-%oname
Version: 0.24
Release: alt1.1
Summary: Mozilla-authored process handling
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/mozprocess/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/1b/05/bc9159c8c1b9b421307f13bd1013aede48f249b5b05a804ed84f5b357b21/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-mozinfo

%py_provides %oname

%description
Mozilla-authored process handling.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21-alt1
- Initial build for Sisyphus

