Name: python3-module-ruamel-yaml
Version: 0.15.100
Release: alt1

Summary: is a YAML 1.2 loader/dumper package for Python

License: GPLv3
Group: Development/Python3
Url: https://bitbucket.org/ruamel/yaml
Provides: python3(ruamel)

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://bitbucket.org/ruamel/yaml/get/%version.tar.bz2
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Thu Aug 16 2018
# optimized out: python-base python-modules python3 python3-base python3-dev python3-module-greenlet python3-module-pycparser python3-module-setuptools
# BuildRequires: python3-module-zmq

BuildRequires: libssl-devel python3-dev python3-module-setuptools

%description
ruamel.yaml is a YAML 1.2 loader/dumper package for Python
It is a derivative of Kirill Simonov's PyYAML 3.11

%prep
%setup

%build
%python3_build

%install
export RUAMEL_NO_PIP_INSTALL_CHECK="1"
%python3_install

%files
%doc LICENSE CHANGES README.rst
%python3_sitelibdir/*

%changelog
* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.100-alt1
- 0.15.100 released

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 0.15.57-alt1
- update build requires

* Thu Aug 16 2018 Pavel Vainerman <pv@altlinux.ru> 0.15.57-alt0.1
- new version (0.15.57) with rpmgs script
