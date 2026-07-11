%define srcname unicode-segmentation-rs
%define modname unicode_segmentation_rs

Name: python3-module-%srcname
Summary: Unicode segmentation and width for Python using Rust
Version: 0.2.4
Release: alt1
License: MIT AND (MIT OR Apache-2.0)
Group: Development/Python3

URL: https://github.com/WeblateOrg/unicode-segmentation-rs
VCS: https://github.com/WeblateOrg/unicode-segmentation-rs

Source: %srcname-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools)
BuildRequires: python3(maturin)
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust 

%description
%summary.

%prep
%setup -n %srcname-%version
%autopatch -p1
%rust_prep

%build
%rust_build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version.dist-info

%changelog
* Sat Jul 11 2026 Anton Midyukov <antohami@altlinux.org> 0.2.4-alt1
- Initial build.
