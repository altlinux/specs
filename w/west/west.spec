Name: west
Version: 1.3.0
Release: alt1

Summary: Zephyr RTOS Project meta-tool

License: Apache-2.0
Group: Development/Other
Url: https://github.com/zephyrproject-rtos/west

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)

%description
West provides a multiple repository management system with features
inspired by Google's Repo tool and Git submodules. West is also
"pluggable": you can write your own west extension commands which
add additional features to west.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-*.dist-info

%changelog
* Mon Nov 25 2024 Vladimir Didenko <cow@altlinux.org> 1.3.0-alt1
- New version

* Mon Nov 27 2023 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- New version

* Thu Jun 22 2023 Vladimir Didenko <cow@altlinux.org> 1.1.0-alt1
- New version

* Mon Mar 13 2023 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

* Thu Sep 15 2022 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
