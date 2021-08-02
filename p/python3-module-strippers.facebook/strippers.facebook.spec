%define pname strippers
%define oname %pname.facebook

%def_with bootstrap

Name: python3-module-%oname
Version: 0.9
Release: alt4
Summary: Python library for Facebook Graph API
License: LGPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/strippers.facebook/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3
%if_with bootstrap
%add_python3_req_skip mimetools
%endif

Requires: python3-module-%pname = %EVR

%description
Python library for Facebook Graph API.

%package -n python3-module-%pname
Summary: Core files of %pname
Group: Development/Python3

%description -n python3-module-%pname
Core files of %pname.

%prep
%setup

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
export LC_ALL=en_US.UTF-8

%python3_build_debug

%install
export LC_ALL=en_US.UTF-8

%python3_install

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%pname/__init__.py \
	%buildroot%python3_sitelibdir/%pname/

%files
%doc *.rst
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%pname/facebook

%files -n python3-module-%pname
%dir %python3_sitelibdir/%pname
%python3_sitelibdir/%pname/__init__.py
%dir %python3_sitelibdir/%pname/__pycache__
%python3_sitelibdir/%pname/__pycache__/__init__.*

%changelog
* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 0.9-alt4
- Drop python2 support.

* Mon May 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt3
- fixed packaging on 64bit arches other than x86_64

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.b.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.b
- Initial build for Sisyphus

