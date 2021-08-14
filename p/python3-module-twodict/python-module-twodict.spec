Name: python3-module-twodict
Version: 1.2
Release: alt2

Summary: Simple two way ordered dictionary for Python.

License: Public Domain
Group: Development/Python3
Url: https://github.com/MrS0m30n3/twodict

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3

%description
TwoWayOrderedDict it's a custom dictionary
in which you can get the key:value relationship
but you can also get the value:key relationship.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%python3_sitelibdir/*
%python3_sitelibdir/*.egg-info


%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- build python3 module separately

* Mon Mar 05 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt1
- Initial build for Sisyphus
