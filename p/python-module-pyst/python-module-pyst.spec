%define module_name pyst

Name: python-module-%module_name
Version: 0.3.22
Release: alt1.1

Summary: A Python Interface to Asterisk
License: PSF, LGPL
Group: Development/Python
Url: http://www.sourceforge.net/projects/pyst/

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
%doc ChangeLog README*
%python_sitelibdir/asterisk
%python_sitelibdir/*.egg-info


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.22-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.22-alt1
- Initial build for Sisyphus.
