%define modulename furo

Name:     python3-module-%modulename
Version:  2021.03.20.beta31
Release:  alt1

Summary:  A clean customizable documentation theme for Sphinx
License:  MIT
Group:    Development/Python3
Url:      https://github.com/pradyunsg/furo

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
%summary

%prep
%setup
%patch -p1
version_no_eta=$(echo %version | sed 's/eta//')
sed -i "s/\(version='\)[^']*\('\)/\1$version_no_eta\2/" setup.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 2021.03.20.beta31-alt1
- Initial build for Sisyphus.
