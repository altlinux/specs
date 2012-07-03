%define module_name path

Name: python-module-%module_name
Version: 2.2.2.990
Release: alt1.1

Summary: A module wrapper for os.path
License: MIT
Group: Development/Python
Url: https://github.com/dottedmag/path.py

Source: python-module-%module_name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

%description
%summary

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/path*
%python_sitelibdir/*.egg-info


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2.990-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.2.2.990-alt1
- Initial build for Sisyphus.
