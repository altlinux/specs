Name: python-module-twodict
Version: 1.2
Release: alt1

%setup_python_module twodict

Summary: Simple two way ordered dictionary for Python.
License: Public Domain
Group: Development/Python

Url: https://github.com/MrS0m30n3/twodict
Packager: Andrey Bychkov <mrdrew@altlinux.org>
BuildArch: noarch

Source: twodict-%version.tgz

BuildPreReq: %py_dependencies setuptools

%description
TwoWayOrderedDict it's a custom dictionary in which you can get the key:value relationship but you can also get the value:key relationship.

%prep
%setup -n twodict-%version

%build
%python_build

%install
%python_install

%files
%doc LICENSE
%python_sitelibdir/*
%python_sitelibdir/*.egg-info


%changelog
* Mon Mar 05 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt1
- Initial build for Sisyphus
