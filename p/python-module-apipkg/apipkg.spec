%define oname apipkg
%define fname python-module-%oname
%define descr With apipkg you can control the exported namespace of a python package and \
greatly reduce the number of imports for your users. It is a small python \
module that works on virtually all Python versions, including CPython2.3 to \
Python3.1, Jython and PyPy. It co-operates well with Python's help() system,\
custom importers (PEP302) and common command line completion tools.

Name:           %fname
Version:        1.4
Release:        alt3

Summary:        A Python namespace control and lazy-import mechanism

License:        MIT
Group:          Development/Python
URL:            http://pypi.python.org/pypi/apipkg

Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires: python-module-setuptools

%description
%descr

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%oname.*
%python_sitelibdir/*.egg-info*

%changelog
* Tue Jun 19 2018 Grigory Ustinov <grenka@altlinux.org> 1.4-alt3
- Raise release to allow the safe upgrade from "Autoimports/Sisyphus".

* Fri Jun 08 2018 Grigory Ustinov <grenka@altlinux.org> 1.4-alt1
- Initial build for Sisyphus.
