%global pypi_name django-pyscss

Name: python3-module-%pypi_name
Version: 2.0.2
Release: alt3

Summary: Makes it easier to use PySCSS in Django
License: BSD
Group: Development/Python3
Url: https://github.com/fusionbox/django-pyscss
BuildArch: noarch

Source: %pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django python3-module-pyScss


%description
A collection of tools for making it easier to use
pyScss within Django.

%prep
%setup -n %pypi_name-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.2-alt3
- build for python2 disabled

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.2-alt2
- add python3 package

* Mon Sep 14 2015 Lenar Shakirov <snejok@altlinux.ru> 2.0.2-alt1
- New version

* Tue Mar 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- Initial package.
