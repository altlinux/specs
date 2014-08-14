Name:           python-module-thrift
Version:        0.9.1
Release:        alt1
Summary:        Python bindings for the Apache Thrift RPC system
License:        Apache-2.0
Group:          Development/Python
Url:            http://thrift.apache.org
Source:         %{name}-%{version}.tar
BuildRequires:  fdupes
BuildRequires:  python-devel

%description
Thrift Python Software Library

Thrift is provided as a set of Python packages. The top level package is
thrift, and there are subpackages for the protocol, transport, and server
code. Each package contains modules using standard Thrift naming conventions
(i.e. TProtocol, TTransport) and implementations in corresponding modules
(i.e. TSocket).  There is also a subpackage reflection, which contains
the generated code for the reflection structures.

%prep
%setup

%build
CFLAGS="%{optflags} -fno-strict-aliasing" %python_build

%install
%python_install
fdupes %{buildroot}%{python_sitelibdir}

%files
%doc README
%{python_sitelibdir}/thrift-%{version}-py?.?.egg-info
%{python_sitelibdir}/thrift

%changelog
* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.9.1-alt1
- First build for ALT (based on OpenSuSe 0.9.1-1.5.src)

