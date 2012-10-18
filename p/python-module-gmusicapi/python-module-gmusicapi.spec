%define module_name gmusicapi

Name: python-module-%module_name
Version: 2012.08.31
Release: alt1
Summary: An unofficial api for Google Play Music.
License: BSD
Group: Development/Python
Url: https://github.com/simon-weber/Unofficial-Google-Music-API

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-distribute

%setup_python_module %module_name

%description
gmusicapi is an unofficial api for Google Play Music.
This api is not supported nor endorsed by Google, and could break at any time.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS COPYING changelog
%python_sitelibdir/%module_name
%python_sitelibdir/%module_name-*.egg-info
%exclude %python_sitelibdir/%module_name/test

%changelog
* Thu Oct 18 2012 Alexey Shabalin <shaba@altlinux.ru> 2012.08.31-alt1
- 2012.08.31

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 2012.05.04-alt1
- Initial build for ALT Linux
