# run "sh .gear/update_crates.sh" script before build for srpms

%define _unpackaged_files_terminate_build 1

Name: minify-html
Version: 0.8.0
Release: alt1

Summary: A Rust HTML minifier
License: MIT
Group: Text tools
Url: https://github.com/wilsonzlin/minify-html

ExcludeArch: i586 armh

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc
BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: golang

%package -n python3-module-minify-html
Summary: A Rust HTML minifier
Group: Development/Python

%description
Rust HTML minifier meticulously optimised for speed and effectiveness,
with bindings for other languages.

%description -n python3-module-minify-html
Rust HTML minifier meticulously optimised for speed and effectiveness,
with bindings for other languages.
This package contains Python bindings.

%prep
%setup -a1
ln -snr gen rust/common/
(cd python && python3 ./prepare.py yes)
cat > python/__init__.py << 'E_O_F'
from .minify_html import *

__doc__ = minify_html.__doc__
E_O_F

%build
export CARGO_HOME=${PWD}/cargo
cargo build --manifest-path cli/Cargo.toml --release
cargo build --manifest-path python/Cargo.toml --release
pushd python
cp target/release/libminify_html.so minify_html.so
%python3_build
popd

%install
install -pm0755 -D cli/target/release/minify-html-cli %buildroot%_bindir/minify-html-cli
mkdir -p %buildroot%python3_sitelibdir/minify_html
pushd python
install -pm0644 __init__.py %buildroot%python3_sitelibdir/minify_html
install -pm0644 minify_html.so %buildroot%python3_sitelibdir/minify_html
%python3_install --install-lib=%python3_sitelibdir --single-version-externally-managed
popd

%files
%doc README.md
%_bindir/minify-html-cli

%files -n python3-module-minify-html
%python3_sitelibdir/*

%changelog
* Fri Feb 18 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux
