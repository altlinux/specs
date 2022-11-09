Name: python3-module-watchfiles
Version: 0.18.1
Release: alt1

Summary: Simple, modern file watching and code reload in python.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/watchifiles/

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc
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
sed -ri '/^version/ s,"[^"]+","%version",' Cargo.toml

%build
export CARGO_HOME=${PWD}/cargo
%pyproject_build

%install
%pyproject_install

%files
%_bindir/watchfiles
%python3_sitelibdir/watchfiles
%python3_sitelibdir/watchfiles-%version.dist-info

%changelog
* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.1-alt1
- 0.18.1 released

* Wed Aug 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.1-alt1
- 0.16.1 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- initial
