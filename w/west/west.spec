Name: west
Version: 1.0.0
Release: alt1

Summary: Zephyr RTOS Project meta-tool

License: Apache-2.0
Group: Development/Other
Url: https://github.com/zephyrproject-rtos/west

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python3-module-setuptools rpm-build-python3

%description
West provides a multiple repository management system with features
inspired by Google's Repo tool and Git submodules. West is also
"pluggable": you can write your own west extension commands which
add additional features to west.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-*

%changelog
* Mon Mar 13 2023 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

* Thu Sep 15 2022 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
