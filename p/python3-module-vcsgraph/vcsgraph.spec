%define oname vcsgraph

Name:    python3-module-%oname
Version: 0.1.2
Release: alt1

Summary: Graph algorithms for version control systems

Group:   Development/Python3
License: GPL-2.0
URL:     https://pypi.org/project/vcsgraph/
Vcs:     https://pypi.org/project/vcsgraph/

Source0: %oname-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-setuptools_rust python3-module-wheel

%description
vcsgraph is a high-performance graph algorithms library specifically designed
for working with version control system (VCS) data structures. It provides
efficient implementations of common graph operations needed by VCS tools, with
both pure Python and Rust-accelerated implementations for performance-critical
operations.

%prep
%setup -n %oname-%version -a1

%build
mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
strip = "none"
lto= "thin"
debug = "full"
EOF

%pyproject_build

%install
%pyproject_install

%files
%doc *.md COPYING.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu May 21 2026 L.A. Kostis <lakostis@altlinux.ru> 0.1.2-alt1
- Initial build for ALTLinux.

