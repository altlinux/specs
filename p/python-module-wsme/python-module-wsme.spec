%define pypi_name WSME
%define lpypi_name wsme
%def_with python3

Name:           python-module-%lpypi_name
Version:        0.8.0
Release:        alt2
Summary:        Web Services Made Easy
Group:          Development/Python

License:        MIT
URL:            https://pypi.python.org/pypi/WSME
Source:        %name-%version.tar
Patch:         %name-namespace-disable.patch
BuildArch:      noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-netaddr python-module-pbr python-module-pytz python-modules-wsgiref python3-module-html5lib python3-module-netaddr python3-module-pbr python3-module-pytz rpm-build-python3

#see wsmeext/soap/simplegeneric.py
Requires: python-module-simplegeneric
#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools
#BuildRequires:  python-module-pbr
#BuildRequires:  python-module-six >= 1.9.0
#BuildRequires:  python-module-webob >= 1.2.3
#BuildRequires:  python-module-netaddr >= 0.7.12
#BuildRequires:  python-module-pytz
#BuildRequires:  python-module-simplegeneric

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-six >= 1.9.0
#BuildRequires: python3-module-webob >= 1.2.3
#BuildRequires: python3-module-netaddr >= 0.7.12
#BuildRequires: python3-module-pytz
#BuildRequires: python3-module-simplegeneric
%endif

%add_python_req_skip flask
%add_python_req_skip pecan
%add_python_req_skip cherrypy
%add_python_req_skip turbogears
%add_python_req_skip sphinx

%description
Web Services Made Easy, simplifies the implementation of
multiple protocol REST web services by providing simple yet
powerful typing which removes the need to directly
manipulate the request and the response objects.

%if_with python3
%package -n python3-module-%lpypi_name
Summary:        Web Services Made Easy
Group:          Development/Python3

Requires: python3-module-simplegeneric

%add_python3_req_skip flask
%add_python3_req_skip pecan
%add_python3_req_skip cherrypy
%add_python3_req_skip turbogears
%add_python3_req_skip sphinx

%description -n python3-module-%lpypi_name
Web Services Made Easy, simplifies the implementation of
multiple protocol REST web services by providing simple yet
powerful typing which removes the need to directly
manipulate the request and the response objects.
%endif

%prep
%setup
%patch

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst LICENSE examples/
%python_sitelibdir/*

%files -n python3-module-%lpypi_name
%python3_sitelibdir/*

%changelog
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

