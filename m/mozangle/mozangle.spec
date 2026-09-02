Name: mozangle
Version: 0.5.5
Release: alt1

Summary: Mozilla's fork of Google ANGLE shader translator

License: BSD-3-Clause
Group: Development/C++
URL: https://github.com/servo/mozangle
# Source-url: https://github.com/servo/mozangle.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: gcc-c++
BuildRequires: clang-devel clang

%description
Mozilla's fork of Google ANGLE, repackaged as a Rust crate.
ANGLE is an implementation of OpenGL ES. This package provides
the ANGLE shader translator (GLSL ES compiler) as static libraries.

%package -n libmozangle-devel
Summary: Development files for mozangle (ANGLE shader translator)
Group: Development/C++

%description -n libmozangle-devel
Mozilla's fork of Google ANGLE shader translator.
This package contains static libraries and header files needed
for building applications that use the ANGLE shader translator,
such as the Servo web engine.

%prep
%setup -a1

mkdir -p .cargo
cat <<EOF >> .cargo/config
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release 2>&1

%install
# Install static libraries from cargo build output
OUTDIR=$(find target/release/build/mozangle-*/out -maxdepth 0 -type d | head -1)
install -d %buildroot%_libdir
install -m 0644 $OUTDIR/libangle_common.a %buildroot%_libdir/
install -m 0644 $OUTDIR/libpreprocessor.a %buildroot%_libdir/
install -m 0644 $OUTDIR/libtranslator.a %buildroot%_libdir/
install -m 0644 $OUTDIR/libglslang_glue.a %buildroot%_libdir/

# Install headers
install -d %buildroot%_includedir/mozangle
cp -a gfx/angle/checkout/include/* %buildroot%_includedir/mozangle/

# Install the C glue header (useful for consumers)
install -d %buildroot%_includedir/mozangle/shaders
install -m 0644 src/shaders/glslang-c.cpp %buildroot%_includedir/mozangle/shaders/

%files -n libmozangle-devel
%doc README.md LICENSE
%_libdir/libangle_common.a
%_libdir/libpreprocessor.a
%_libdir/libtranslator.a
%_libdir/libglslang_glue.a
%_includedir/mozangle/

%changelog
* Sat Apr 04 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5.5-alt1
- initial build for ALT Sisyphus

