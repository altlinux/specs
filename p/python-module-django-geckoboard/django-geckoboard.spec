%define _unpackaged_files_terminate_build 1
%define oname django-geckoboard

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1
Summary: Geckoboard custom widgets for Django projects
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/django-geckoboard/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jcassee/django-geckoboard.git
Source0: https://pypi.python.org/packages/ac/27/f65a549b7b795febc3173817550e58975c8230dc4b338e126527cc0b0fdd/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Geckoboard is a hosted, real-time status board serving up indicators
from web analytics, CRM, support, infrastructure, project management,
sales, etc. It can be connected to virtually any source of quantitative
data.

This Django application provides view decorators to help create custom
widgets.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Geckoboard is a hosted, real-time status board serving up indicators
from web analytics, CRM, support, infrastructure, project management,
sales, etc. It can be connected to virtually any source of quantitative
data.

This Django application provides view decorators to help create custom
widgets.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Geckoboard custom widgets for Django projects
Group: Development/Python3

%description -n python3-module-%oname
Geckoboard is a hosted, real-time status board serving up indicators
from web analytics, CRM, support, infrastructure, project management,
sales, etc. It can be connected to virtually any source of quantitative
data.

This Django application provides view decorators to help create custom
widgets.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Geckoboard is a hosted, real-time status board serving up indicators
from web analytics, CRM, support, infrastructure, project management,
sales, etc. It can be connected to virtually any source of quantitative
data.

This Django application provides view decorators to help create custom
widgets.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.7-alt1.git20131010.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt1.git20131010
- Initial build for Sisyphus

