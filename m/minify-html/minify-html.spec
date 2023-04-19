%define _unpackaged_files_terminate_build 1

Name: minify-html
Version: 0.10.8
Release: alt1

Summary: A Rust HTML minifier
License: MIT
Group: Text tools
Url: https://github.com/wilsonzlin/minify-html

# x32 systems not supported
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
%ifdef bootstrap
# collect dependencies for the project
cargo vendor alt/crates --manifest-path cli/Cargo.toml --sync python/main/Cargo.toml
tar cf %SOURCE1 alt/crates
%else
tar xf %SOURCE1
%endif

cat > python/main/__init__.py << 'E_O_F'
from .minify_html import *

__doc__ = minify_html.__doc__
E_O_F

%build
export CARGO_HOME=${PWD}/cargo
cargo build --manifest-path cli/Cargo.toml --release
cargo build --manifest-path python/main/Cargo.toml --release
pushd python/main
cp target/release/libminify_html.so minify_html.so
%python3_build
popd

%install
install -pm0755 -D cli/target/release/minify-html-cli %buildroot%_bindir/minify-html-cli
mkdir -p %buildroot%python3_sitelibdir/minify_html
pushd python/main
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
* Wed Apr 19 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 0.10.8-alt1
- New version v0.10.8

* Tue Sep 20 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 0.10.0-alt1
- New version v0.10.0
  + Remove update_crates.sh for build the vendor dependencies
  + Move .spec in the "alt" directory

* Fri Feb 18 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux

# Local Variables:
# compile-command: "share_network=1 gear-hsh --commit --mountpoints=/proc --build-args=\'--define \"bootstrap 1\"\'"
# End:
