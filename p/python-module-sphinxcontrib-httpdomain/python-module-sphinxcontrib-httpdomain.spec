%define module_name sphinxcontrib-httpdomain

Name: python-module-%module_name
Version: 1.1.9
Release: alt1.1
Group: System/Base
License: BSD
Summary: Sphinx domain for HTTP APIs
URL: http://pypi.python.org/pypi/sphinxcontrib-httpdomain
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %module_name-%version.tar.gz
BuildArch: noarch

BuildRequires: python-module-distribute

Requires: python-module-sphinxcontrib

%description
This contrib extension, sphinxcontrib.httpdomain provides a Sphinx
omain for describing RESTful HTTP APIs.

You can find the documentation from the following URL:
http://pythonhosted.org/sphinxcontrib-httpdomain/

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install
#cp -f sphinxcontrib/__init__.py %buildroot/%python_sitelibdir_noarch/sphinxcontrib/

%files
%doc LICENSE README*
%python_sitelibdir_noarch/sphinxcontrib*

%changelog
* Sun Dec 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.1
- Fixed conflict with python-module-sphinxcontrib

* Thu Oct 10 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.9-alt1
- build for ALT
