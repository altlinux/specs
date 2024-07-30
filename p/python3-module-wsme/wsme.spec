%define pypi_name WSME
%define lpypi_name wsme
%def_with check
%def_without bootstrap

Name:           python3-module-%lpypi_name
Version:        0.12.1
Release:        alt1
Summary:        Web Services Made Easy
Group:          Development/Python3

License:        MIT
URL:            https://pypi.python.org/pypi/WSME
Source:        %lpypi_name-%version.tar
Patch:         %lpypi_name-namespace-disable.patch
BuildArch:      noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr

%if_with check
BuildRequires: python3-module-webob
BuildRequires: python3-module-simplegeneric
BuildRequires: python3-module-pytz
BuildRequires: python3-module-netaddr
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-flask
BuildRequires: python3-module-webtest
BuildRequires: python3-module-pecan-tests
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-flask-restful
BuildRequires: python3-module-transaction
%endif

#see wsmeext/soap/simplegeneric.py
Requires: python3-module-simplegeneric

%add_python3_req_skip flask
%add_python3_req_skip pecan
%add_python3_req_skip cherrypy
%add_python3_req_skip turbogears
%add_python3_req_skip sphinx

%if_with bootstrap
%add_python3_req_skip cherrypy.filters.basefilter
%add_python3_req_skip turbogears.startup turbogears.view
%endif

%description
Web Services Made Easy, simplifies the implementation of
multiple protocol REST web services by providing simple yet
powerful typing which removes the need to directly
manipulate the request and the response objects.

%prep
%setup -n %lpypi_name-%version
%patch

%build
%pyproject_build

%install
%pyproject_install

# Delete tests
rm -rv %buildroot%python3_sitelibdir/*/tests

%check
%tox_check_pyproject

%files
%python3_sitelibdir/wsme
%python3_sitelibdir/wsmeext
%python3_sitelibdir/WSME-%version.dist-info

%changelog
* Tue Jul 30 2024 Grigory Ustinov <grenka@altlinux.org> 0.12.1-alt1
- Build new version.
- Build with check.

* Tue Sep 14 2021 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Build new version.

* Wed Jun 02 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt3
- Drop python2 support.

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.8.0-alt2.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Feb 28 2016 Lenar Shakirov <snejok@altlinux.ru> 0.8.0-alt2
- add Req: python-module-simplegeneric

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- add python3 package
- add req_skip for modules from wsmeext

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Version 0.6.4

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.6-alt1
- First build for ALT (based on Fedora 0.6-3.fc21.src)

