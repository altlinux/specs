%define _unpackaged_files_terminate_build 1
%define oname mozinfo

Name: python-module-%oname
Version: 0.10
Release: alt1.1
Summary: Library to get system information for use in Mozilla testing
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozinfo/
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-mozfile python-modules-json

%py_provides %oname
%py_requires mozfile json

%description
Library to get system information for use in Mozilla testing.

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
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10-alt1
- Updated to upstream version 0.10.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Added necessary requirements
- Enabled testing

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

