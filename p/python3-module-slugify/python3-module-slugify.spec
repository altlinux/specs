%define  modulename slugify

Name:    python3-module-%modulename
Version: 1.2.4
Release: alt1

Summary: Returns unicode slugs
License: MIT
Group:   Development/Python3
URL:     https://github.com/un33k/python-slugify

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
A Python slugify application that handles unicode.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install
mv %buildroot/%_bindir/slugify{,3}

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%_bindir/slugify3

%changelog
* Thu Feb 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.4-alt1
- Separate build for Sisyphus
