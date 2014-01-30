Name: python-module-pyrad
Version: 2.0
Release: alt1
Summary: RADIUS tools

Group: Development/Python
License: BSD
Url: https://github.com/wichert/pyrad

Source: %name-%version.tar
Patch: %name-%version-alt.patch
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
RADIUS tools

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%doc CHANGES.txt README.rst

%changelog
* Tue Jan 28 2014 Terechkov Evgenii <evg@altlinux.org> 2.0-alt1
- Initial build for ALT Linux Sisyphus
