Name: python3-module-orjson
Version: 3.7.7
Release: alt2

Summary: Fast, correct JSON library for Python
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/orjson/

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rpm-build-python3 maturin unzip
BuildRequires: rust-cargo /proc

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
maturin build --no-sdist --release

%install
mkdir -p %buildroot%python3_sitelibdir 
unzip -d %buildroot%python3_sitelibdir target/wheels/*whl

%files
%python3_sitelibdir/orjson
%python3_sitelibdir/orjson-%version.dist-info

%changelog
* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt2
- rebuilt on ppc64le

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt1
- 3.7.7 released
