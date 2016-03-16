%define oname thrift

%def_with python3

Name:           python-module-%oname
Version:        0.9.2
Release:        alt1.1
Summary:        Python bindings for the Apache Thrift RPC system
License:        Apache-2.0
Group:          Development/Python
Url:            http://thrift.apache.org
Source:         %{name}-%{version}.tar
BuildRequires:  fdupes
BuildRequires:  python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel python-tools-2to3
%endif

%description
Thrift Python Software Library

Thrift is provided as a set of Python packages. The top level package is
thrift, and there are subpackages for the protocol, transport, and server
code. Each package contains modules using standard Thrift naming conventions
(i.e. TProtocol, TTransport) and implementations in corresponding modules
(i.e. TSocket).  There is also a subpackage reflection, which contains
the generated code for the reflection structures.

%package -n python3-module-%oname
Summary: Python bindings for the Apache Thrift RPC system
Group: Development/Python3
%add_python3_req_skip SCons

%description -n python3-module-%oname
Thrift Python Software Library

Thrift is provided as a set of Python packages. The top level package is
thrift, and there are subpackages for the protocol, transport, and server
code. Each package contains modules using standard Thrift naming conventions
(i.e. TProtocol, TTransport) and implementations in corresponding modules
(i.e. TSocket).  There is also a subpackage reflection, which contains
the generated code for the reflection structures.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
CFLAGS="%{optflags} -fno-strict-aliasing" %python_build

%if_with python3
pushd ../python3
CFLAGS="%{optflags} -fno-strict-aliasing" %python3_build
popd
%endif

%install
%python_install
fdupes %{buildroot}%{python_sitelibdir}

%if_with python3
pushd ../python3
%python3_install
fdupes %{buildroot}%{python3_sitelibdir}
popd
%endif

%files
#doc README
%{python_sitelibdir}/%oname-%{version}-py?.?.egg-info
%{python_sitelibdir}/%oname

%if_with python3
%files -n python3-module-%oname
#doc README
%{python3_sitelibdir}/%oname-%{version}-py?.?.egg-info
%{python3_sitelibdir}/%oname
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.1
- Added module for Python 3

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.9.1-alt1
- First build for ALT (based on OpenSuSe 0.9.1-1.5.src)

