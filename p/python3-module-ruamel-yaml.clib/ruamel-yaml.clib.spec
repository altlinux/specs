Name:     python3-module-ruamel-yaml.clib
Version:  0.2.12
Release:  alt1

Summary:  C version of reader, parser and emitter for ruamel.yaml derived from libyaml

License:  MIT
Group:    Development/Python3
URL:      https://pypi.org/project/ruamel.yaml.clib
VCS:      https://github.com/ruamel/yaml.clib

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
This package was split of from ruamel.yaml, so that ruamel.yaml can be build
as a universal wheel. Apart from the C code seldom changing, and taking
a long time to compile for all platforms, this allows installation of the .so
on Linux systems under /usr/lib64/pythonX.Y (without a .pth file or
a ruamel directory) and the Python code for ruamel.yaml under /usr/lib/pythonX.Y.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/_ruamel_yaml.*.so
%python3_sitelibdir/ruamel.yaml.clib-%version.dist-info

%changelog
* Mon Oct 21 2024 Grigory Ustinov <grenka@altlinux.org> 0.2.12-alt1
- Automatically updated to 0.2.12.

* Tue Oct 10 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.8-alt1
- Automatically updated to 0.2.8.

* Fri Mar 03 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.7-alt1
- Automatically updated to 0.2.7.

* Fri Jul 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.2.6-alt1
- Initial build for Sisyphus.
