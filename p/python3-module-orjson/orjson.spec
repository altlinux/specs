Name: python3-module-orjson
Version: 3.8.1
Release: alt1

Summary: Fast, correct JSON library for Python
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/orjson/

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc unzip
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(maturin)

%description
%summary

%prep
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%build
export CARGO_HOME=${PWD}/cargo
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/orjson
%python3_sitelibdir/orjson-%version.dist-info

%changelog
* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.1-alt1
- 3.8.1 released

* Wed Aug 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt3
- rebuilt as pyproject

* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt2
- rebuilt on ppc64le

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt1
- 3.7.7 released
