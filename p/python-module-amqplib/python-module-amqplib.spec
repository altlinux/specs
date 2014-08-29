%define module_name amqplib

%def_with python3

Name: python-module-%module_name
Version: 1.0.2
Release: alt2
Group: Development/Python
License: GPLv2
Summary: Python AMQP (Advanced Message Queuing Protocol) Client library
URL: http://code.google.com/p/py-amqplib/
Source: %module_name-%version.tgz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Python AMQP (Advanced Message Queuing Protocol) Client library.

%package -n python3-module-%module_name
Summary: Python AMQP (Advanced Message Queuing Protocol) Client library
Group: Development/Python3

%description -n python3-module-%module_name
Python AMQP (Advanced Message Queuing Protocol) Client library.

%prep
%setup -n %module_name-%version

%if_with python3
cp -fR . ../python3
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

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc CHANGES LICENSE README TODO
%python_sitelibdir/amqplib*

%if_with python3
%files -n python3-module-%module_name
%doc CHANGES LICENSE README TODO
%python3_sitelibdir/amqplib*
%endif

%changelog
* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added module for Python 3

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt1
- build for ALT
