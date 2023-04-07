%define pypi_name strictyaml
%def_disable check

Name: python3-module-%pypi_name
Version: 1.7.3
Release: alt1

Summary: StrictYAML Python 3 library
Group: Development/Python3
License: MIT
Url: https://hitchdev.com/strictyaml

Vcs: https://github.com/crdoconnor/strictyaml.git
Source: https://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 python3-devel python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-ruamel-yaml.clib}

%description
StrictYAML is a type-safe YAML parser that parses and validates a
restricted subset of the YAML specification.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir_noarch/*
%doc README*

%changelog
* Fri Apr 07 2023 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- first build for Sisyphus

