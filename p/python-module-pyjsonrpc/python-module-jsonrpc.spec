%define _unpackaged_files_terminate_build 1
%define module_name pyjsonrpc

%def_without python3

Name: python-module-%module_name
Version: 0.10.0
Release: alt2.1
Summary: json-rpc package which implements JSON-RPC over HTTP
License: LGPL
Group: Development/Python
BuildArch: noarch
Url: http://json-rpc.org/wiki/python-json-rpc

# https://github.com/gerold-penz/python-jsonrpc.git
Source: python-jsonrpc-%{version}.tar.gz


%setup_python_module %module_name
BuildRequires: python-module-setuptools python-module-bunch
BuildRequires: python-modules-json
BuildRequires: python-module-munch
BuildRequires: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-bunch
BuildRequires: python-tools-2to3
%endif

Obsoletes: python-module-jsonrpc < %EVR

%description
Simple Reference JSON-RPC Implementation for Django

%if_with python3
%package -n python3-module-%module_name
Summary: json-rpc package which implements JSON-RPC over HTTP
Group: Development/Python3

%description -n python3-module-%module_name
Simple Reference JSON-RPC Implementation for Django
%endif

%prep
%setup -q -n python-jsonrpc-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst examples version.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%module_name
%doc *.rst examples version.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.0-alt2
- Updated build dependencies.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1
- automated PyPI update

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20150320
- Version 0.7.2
- Renamed jsonrpc -> pyjsonrpc

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20150204
- Version 0.6.2

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141026
- Version 0.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.01-alt1.svn19.1
- Rebuild with Python-2.7

* Mon Feb 22 2010 Denis Klimov <zver@altlinux.org> 0.01-alt1.svn19
- Initial build for ALT Linux

