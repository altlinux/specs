%define oname zodbpickle

%def_with check

Name: python3-module-%oname
Version: 4.1.1
Release: alt1
Summary: Fork of Python 3 pickle module

License: PSF-2.0 and ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zodbpickle
Vcs: https://github.com/zopefoundation/zodbpickle

Source: %name-%version.tar

# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%description
This package presents a uniform pickling interface for ZODB.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package presents a uniform pickling interface for ZODB.

This package contains tests for %oname.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# Don't bother with development files
rm %buildroot%python3_sitelibdir/%oname/*.c

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd src/zodbpickle
python3 -m unittest -v
popd

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Wed Oct 30 2024 Anton Vyatkin <toni@altlinux.org> 4.1.1-alt1
- New version 4.1.1.
- Return to Sisyphus.

* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt2
- disable python2, ebable python3

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1.dev0.git20150414.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.dev0.git20150414.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.dev0.git20150414.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1.dev0.git20150414.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.dev0.git20150414
- Version 0.6.1.dev0
- Enabled check

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20130817
- Initial build for Sisyphus

