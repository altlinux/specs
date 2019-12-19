%define _unpackaged_files_terminate_build 1
%define oname django-geckoboard

Name: python3-module-%oname
Version: 2.0.0
Release: alt2

Summary: Geckoboard custom widgets for Django projects
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-geckoboard/
BuildArch: noarch

# https://github.com/jcassee/django-geckoboard.git
Source0: https://pypi.python.org/packages/ac/27/f65a549b7b795febc3173817550e58975c8230dc4b338e126527cc0b0fdd/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Geckoboard is a hosted, real-time status board serving up indicators
from web analytics, CRM, support, infrastructure, project management,
sales, etc. It can be connected to virtually any source of quantitative
data.

This Django application provides view decorators to help create custom
widgets.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Geckoboard is a hosted, real-time status board serving up indicators
from web analytics, CRM, support, infrastructure, project management,
sales, etc. It can be connected to virtually any source of quantitative
data.

This Django application provides view decorators to help create custom
widgets.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
export LC_ALL=en_US.UTF-8
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.7-alt1.git20131010.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt1.git20131010
- Initial build for Sisyphus

