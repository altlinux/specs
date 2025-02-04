%define nameD shazamio_core
 
Name:    python3-module-shazamio-core
Version: 1.1.1
Release: alt1

Summary: shazamio-core
License: MIT
Group:   Development/Python3
Url:     https://pypi.org/project/shazamio-core/
VCS:     https://github.com/shazamio/shazamio-core

Source0: %name-%version.tar
Source1: vendor.tar
 
BuildRequires(pre): rpm-build-rust rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: libalsa-devel python3-module-maturin
BuildRequires: /proc

%add_python3_path %python3_sitelibdir/%nameD/

%description
%summary

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

tar -xf %SOURCE1 -C %_builddir/%name-%version/

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md LICENSE
%python3_sitelibdir/%nameD/
# %python3_sitelibdir/%{pyproject_distinfo %nameD}
%python3_sitelibdir/shazamio_core-1.1.0.dist-info/

%changelog
* Tue Feb 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.1.1-alt1
- Update to version 1.1.1

* Thu Jan 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus
