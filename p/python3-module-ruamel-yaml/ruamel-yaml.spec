Name: python3-module-ruamel-yaml
Version: 0.18.5
Release: alt1

Summary: is a YAML 1.2 loader/dumper package for Python

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ruamel.yaml

# Source-url: %%__pypi_url ruamel.yaml
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= 3.7
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch
%py3_provides ruamel
%add_python3_req_skip _ruamel_yaml

%description
ruamel.yaml is a YAML 1.2 parser/emitter
that supports roundtrip preservation of comments,
seq/map flow style, and map key order.

%prep
%setup

%build
%pyproject_build

%install
export RUAMEL_NO_PIP_INSTALL_CHECK="1"
%pyproject_install

%files
%doc LICENSE CHANGES README.md
%python3_sitelibdir/ruamel
%python3_sitelibdir/ruamel.yaml-%version.dist-info

%changelog
* Tue Jan 30 2024 Alexey Shabalin <shaba@altlinux.org> 0.18.5-alt1
- new version 0.18.5

* Sat Oct 21 2023 Vitaly Lipatov <lav@altlinux.ru> 0.17.40-alt1
- new version 0.17.40 (with rpmrb script)
- switch to pyproject_build
- restored Source-url
- updated description

* Fri Jul 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.17.21-alt2
- Fixed Url (Closes: #43377).

* Thu Jul 21 2022 Grigory Ustinov <grenka@altlinux.org> 0.17.21-alt1
- Build new version.

* Wed Jan 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.15.100-alt2
- Fixed build with python3.10.

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.100-alt1
- 0.15.100 released

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 0.15.57-alt1
- update build requires

* Thu Aug 16 2018 Pavel Vainerman <pv@altlinux.ru> 0.15.57-alt0.1
- new version (0.15.57) with rpmgs script
