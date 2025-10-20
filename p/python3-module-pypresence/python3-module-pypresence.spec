%define modname pypresence

Name: python3-module-%modname
Version: 4.6.1
Release: alt1

Summary: Discord RPC and Rich Presence wrapper library

License: MIT
Group: Development/Python3
Url: https://qwertyquerty.github.io/pypresence/html/index.html
VCS: https://github.com/qwertyquerty/pypresence

# Source-url: %url/archive/%version/%modname-%version.tar.gz
Source: %modname-%version.tar
Patch: %modname-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-wheel

%description
%summary.

%prep
%setup -n %modname-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc docs README.md LICENSE CONTRIBUTING.md
%python3_sitelibdir_noarch/%{modname}*

%changelog
* Mon Oct 20 2025 Leontiy Volodin <lvol@altlinux.org> 4.6.1-alt1
- New version 4.6.1.

* Thu Oct 16 2025 Leontiy Volodin <lvol@altlinux.org> 4.6.0-alt1
- New version 4.6.0.

* Mon Oct 13 2025 Leontiy Volodin <lvol@altlinux.org> 4.5.2-alt1
- New version 4.5.2.
- Added VCS tag.

* Mon Jul 10 2023 Leontiy Volodin <lvol@altlinux.org> 4.3.0-alt1
- New version 4.3.0.

* Mon Dec 06 2021 Leontiy Volodin <lvol@altlinux.org> 4.2.1-alt1.gite305409
- Initial build for ALT Sisyphus.

