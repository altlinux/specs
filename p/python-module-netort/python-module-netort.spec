Name:           python-module-netort
License:        LGPLv2
Group:          Development/Python
Summary:        common library for yandex-load org
Version:        0.2.6
Release:        alt1
URL:            http://github.com/yandex-load/netort
Source:         %name-%version.tar
BuildArch:      noarch
BuildRequires:  python-module-setuptools

%description
common library for yandex-load org

%prep
%setup

%build
%python_build

%install
%python_install

%files
%{python_sitelibdir}/*

%changelog
* Tue Oct 16 2018 Terechkov Evgenii <evg@altlinux.org> 0.2.6-alt1
- 0.2.6

* Thu Jul 12 2018 Terechkov Evgenii <evg@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux Sisyphus
- 0.1.0 (226c21a)
