%define _unpackaged_files_terminate_build 1
%define oname pytest-diffeo

Name: python3-module-%oname
Version: 0.2.0
Release: alt2

Summary: Common py.test support for Diffeo tests
License: MIT/X11
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-diffeo/
# https://github.com/diffeo/pytest-diffeo.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/e3/ee/25a3cab817e1ef69da019dbcfdbd8fa429f3c02dc6653c978262d3d9a83a/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3
BuildRequires: python3-module-six
BuildRequires: python3-module-pytest

%py3_provides pytest_diffeo


%description
If this package is installed, then you can run py.test with additional
command-line arguments --runperf, --runslow, -runload, or
-run-integration. Tests marked with @pytest.mark.performance,
@pytest.mark.slow, @pytest.mark.load, and pytest.mark.integration
respectively, will not be run unless the corresponding command-line
option is present.

This package also provides a redis_address fixture to get the location
of an external Redis installation. This must be provided via a
--redis-address command-line argument.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|@VERSION@|%version|' setup.py

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt1.git20141106.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.git20141106
- Initial build for Sisyphus

