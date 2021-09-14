%define pypi_name WSME
%define lpypi_name wsme
%def_with bootstrap

Name:           python3-module-%lpypi_name
Version:        0.11.0
Release:        alt1
Summary:        Web Services Made Easy
Group:          Development/Python3

License:        MIT
URL:            https://pypi.python.org/pypi/WSME
Source:        %lpypi_name-%version.tar
Patch:         %lpypi_name-namespace-disable.patch
BuildArch:      noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-pbr

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
%python3_build

%install
%python3_install

# Delete tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%python3_sitelibdir/*

%changelog
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

