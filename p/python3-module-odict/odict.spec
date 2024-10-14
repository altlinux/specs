%define _unpackaged_files_terminate_build 1
%define pypi_name odict
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.9.0
Release: alt2

Summary: Ordered dictionary

License: Python-2.0
Group: Development/Python3
Url: https://pypi.org/project/odict/
Vcs: https://github.com/conestack/odict
Source: %name-%version.tar
%add_python3_self_prov_path %buildroot%python3_sitelibdir/%mod_name
BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools

BuildArch: noarch

%description
Dictionary in which the insertion order of items is preserved (using an
internal double linked list). In this implementation replacing an
existing item keeps it at its original position.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# see .github/workflows/test.yaml
%pyproject_run -- python -m %mod_name.tests

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%changelog
* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 1.9.0-alt2
- migrated from removed setuptools' test command (see #50996).

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.9.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Jun 08 2022 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Automatically updated to 1.9.0.

* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.6.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1.dev0.git20150103.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.0-alt1.dev0.git20150103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.dev0.git20150103.1
- NMU: Use buildreq for BR.

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.dev0.git20150103
- Version 1.6.0.dev0
- Added module for Python 3

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20140501
- Initial build for Sisyphus

