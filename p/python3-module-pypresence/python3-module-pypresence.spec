%define modname pypresence

Name: python3-module-%modname
Version: 4.2.1
Release: alt1.gite305409

Summary: Discord RPC and Rich Presence wrapper library

License: BSD-3-Clause and MIT
Group: Development/Python3
Url: https://qwertyquerty.github.io/pypresence/html/index.html
# https://github.com/qwertyquerty/pypresence
# e305409a628e1966cc08bffaffd644bd39a360c7

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
* Mon Dec 06 2021 Leontiy Volodin <lvol@altlinux.org> 4.2.1-alt1.gite305409
- Initial build for ALT Sisyphus.

