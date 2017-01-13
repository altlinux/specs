%define _unpackaged_files_terminate_build 1
%define module_name sphinxcontrib-httpdomain

Name: python-module-%module_name
Version: 1.5.0
Release: alt1
Group: Development/Python
License: BSD
Summary: Sphinx domain for HTTP APIs
URL: http://pypi.python.org/pypi/sphinxcontrib-httpdomain
Source0: https://pypi.python.org/packages/a5/52/0ded71896b9d25621b44d681cdd352c37a9ed81219a6b62014bd15dd2b9e/%{module_name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python-module-distribute

Requires: python-module-sphinxcontrib

%description
This contrib extension, sphinxcontrib.httpdomain provides a Sphinx
omain for describing RESTful HTTP APIs.

You can find the documentation from the following URL:
http://pythonhosted.org/sphinxcontrib-httpdomain/

%prep
%setup -q -n %{module_name}-%{version}

%build
%python_build

%install
%python_install
#cp -f sphinxcontrib/__init__.py %buildroot/%python_sitelibdir_noarch/sphinxcontrib/

%files
%doc LICENSE README*
%python_sitelibdir_noarch/sphinxcontrib*

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1
- automated PyPI update

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Sun Dec 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.1
- Fixed conflict with python-module-sphinxcontrib

* Thu Oct 10 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.9-alt1
- build for ALT
