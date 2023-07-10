%define modname pypresence

Name: python3-module-%modname
Version: 4.3.0
Release: alt1

Summary: Discord RPC and Rich Presence wrapper library

License: MIT
Group: Development/Python3
Url: https://qwertyquerty.github.io/pypresence/html/index.html
# https://github.com/qwertyquerty/pypresence

Source: %url/archive/%version/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-wheel

%description
%summary.

%prep
%setup -n %modname-%version
# description-file will not be supported in future versions
sed -i 's|description-file|description_file|' setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%files
%doc docs README.md LICENSE CONTRIBUTING.md
%python3_sitelibdir_noarch/%{modname}*

%changelog
* Mon Jul 10 2023 Leontiy Volodin <lvol@altlinux.org> 4.3.0-alt1
- New version 4.3.0.

* Mon Dec 06 2021 Leontiy Volodin <lvol@altlinux.org> 4.2.1-alt1.gite305409
- Initial build for ALT Sisyphus.

