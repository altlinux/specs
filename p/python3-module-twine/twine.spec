%define oname twine

%def_with check

Name: python3-module-%oname
Version: 4.0.2
Release: alt1

Summary: Collection of utilities for interacting with PyPI
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/twine/
Vcs: https://github.com/pypa/twine

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-keyring
BuildRequires: python3-module-rich
BuildRequires: python3-module-pkginfo
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-rfc3986
BuildRequires: python3-module-requests
BuildRequires: python3-module-requests_toolbelt
BuildRequires: python3-module-readme-renderer
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-secretstorage
BuildRequires: python3-module-jaraco.classes
BuildRequires: python3-module-pretend
BuildRequires: python3-module-build
BuildRequires: python3-module-munch
%endif

%py3_provides %oname

%description
Twine is a utility for interacting with PyPI.
It provides build system independent uploads of source and binary distribution
artifacts for both new and existing projects.

%prep
%setup

# pytest-socket dep relevant only to test_integration, and upstream
# disables it anyway
sed -i '/--disable-socket/d' pytest.ini

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -m pytest --ignore-glob '*integration*.py' -k "\
not test_exception_handling \
and not test_http_exception_handling"

%files
%doc AUTHORS *.rst docs/*.rst LICENSE
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Tue Mar 28 2023 Anton Vyatkin <toni@altlinux.org> 4.0.2-alt1
- New version 4.0.2.

* Wed Dec 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.1-alt2
- build for python2 disabled

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.1-alt1
- Updated to upstream releases 1.9.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt2.git20140815.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.1-alt2.git20140815
- cleanup buildreqs
- disable check

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140815
- Initial build for Sisyphus

