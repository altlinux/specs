%define _unpackaged_files_terminate_build 1
%define oname sphinx-bootstrap-theme

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt2
Summary: Sphinx Bootstrap Theme
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-bootstrap-theme/
BuildArch: noarch

# https://github.com/ryan-roemer/sphinx-bootstrap-theme.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%endif

%py_requires sphinx fabric

%description
This Sphinx theme integrates the Twitter Bootstrap CSS / JavaScript
framework with various layout options, hierarchical menu navigation, and
mobile-friendly responsive design. It is configurable, extensible and
can use any number of different Bootswatch CSS themes.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx Bootstrap Theme
Group: Development/Python3
%py3_requires sphinx

%description -n python3-module-%oname
This Sphinx theme integrates the Twitter Bootstrap CSS / JavaScript
framework with various layout options, hierarchical menu navigation, and
mobile-friendly responsive design. It is configurable, extensible and
can use any number of different Bootswatch CSS themes.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
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

%files
%doc LICENSE.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt2
- Updated runtime dependencies for python-3.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt1
- Updated to upstream version 0.6.0.
- Enabled build for python3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.13-alt1
- automated PyPI update

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1
- VErsion 0.4.3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

