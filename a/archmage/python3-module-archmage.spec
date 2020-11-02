Name:    archmage
Version: 0.4.2.1
Release: alt1

Summary: A reader and decompiler for files in the CHM format
License: GPL-2.0
Group:   Development/Python3
URL:     https://github.com/dottedmag/archmage

Packager: Anton Midyukov <antohami@altlinux.org>

%py3_requires chm

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Mon Nov 02 2020 Anton Midyukov <antohami@altlinux.org> 0.4.2.1-alt1
- Initial build for Sisyphus
