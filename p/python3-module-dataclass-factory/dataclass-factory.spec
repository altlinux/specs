%define pip_name dataclass_factory

Name: python3-module-dataclass-factory
Version: 2.16
Release: alt2

Summary: An utility class for creating instances of dataclasses
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/dataclass-factory/
Vcs: https://pypi.org/project/dataclass-factory/

#https://files.pythonhosted.org/packages/f1/66/50b9f5d8a0e9fbe5469c5b8a7f198511fff9959347fc2443531d651b21d7/dataclass_factory-2.16-py3-none-any.whl

BuildArch: noarch

Source0: %name-%version.tar
Source1: dataclass_factory-2.16-py3-none-any.whl

BuildRequires(pre):  rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Modern way to convert python dataclasses or other objects to and from more common types like dicts or json-like structures.

%prep
%setup

wheel unpack %SOURCE1

mv dataclass_factory-2.16/* %_builddir/%name-%version/ 
mv dataclass_factory-2.16.dist-info/* %_builddir/%name-%version/ 

echo 'import setuptools; setuptools.setup()' > setup.py

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE
%python3_sitelibdir/%pip_name/

%changelog
* Sat Feb 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.16-alt2
- rebuild with removed %%add_python3_path

* Thu Jan 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.16-alt1
- Initial build for Sisyphus.
