Name: flux
Version: 0.200.0
Release: alt1
Summary: Influx data language
Group: Development/Other
License: Apache-2.0 AND MIT AND (Apache-2.0 OR MIT) AND Apache-2.0 WITH LLVM-exception AND CC-BY-3.0 AND CC-BY-SA-4.0 AND (Apache-2.0 OR BSL-1.0) AND BSD-3-Clause AND MPL-2.0 AND Zlib AND X11 AND Unicode-DFS-2016 AND Unicode-TOU
Url: https://github.com/influxdata/flux
Source: %name-%version.tar
Patch0: %name-%version.patch
Patch1: disable-static-library.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%define soname 0

%description
Flux is a lightweight scripting language for querying databases (like InfluxDB)
and working with data. It is part of InfluxDB 1.7 and 2.0, but can be run
independently of those. This repository contains the language definition and an
implementation of the language core.

%package -n libflux%soname
Summary: Influx data language
Group: System/Libraries
Provides: libflux = %EVR

%description -n libflux%soname
Flux is a lightweight scripting language for querying databases (like InfluxDB)
and working with data. It is part of InfluxDB 1.7 and 2.0, but can be run
independently of those. This repository contains the language definition and an
implementation of the language core.

%package -n libflux-devel
Summary: Development libraries and header files for Influx data language
Group: Development/Other
Requires: libflux%soname = %EVR

%description -n libflux-devel
This package contains the header files and libraries for building
programs using Influx data language.

%prep
%setup

%autopatch -p1
patch -p1 <<EOF
--- a/libflux/flux/build.rs
+++ b/libflux/flux/build.rs
@@ -79,5 +79,7 @@ fn main() -> Result<()> {
     let path = dir.join("stdlib.data");
     serialize(Environment::from(imports), fb::build_env, &path)?;

+    println!("cargo:rustc-cdylib-link-arg=-Wl,-soname,libflux.so.%soname");
+
     Ok(())
 }
EOF

%build
pushd libflux/flux
%rust_build
popd

%install
install -D -m 644 libflux/include/influxdata/flux.h %buildroot%_includedir/influxdata/flux.h
install -D -m 755 libflux/target/release/libflux.so %buildroot%_libdir/libflux.so.%soname
ln -sf ./libflux.so.%soname %buildroot%_libdir/libflux.so

cat > flux.pc <<EOF
prefix=%prefix
exec_prefix=%prefix
libdir=%_libdir
includedir=%_includedir

Name: Flux
Version: %version
Description: Library for the InfluxData Flux engine
Libs: -L%_libdir -lflux
Libs.private: -ldl -lpthread
Cflags: -I%_includedir
EOF

install -D -m 644 flux.pc %buildroot%_pkgconfigdir/flux.pc

%check
pushd libflux/flux
%rust_test
popd

%files -n libflux%soname
%_libdir/libflux.so.%soname

%files -n libflux-devel
%doc README.md LICENSE
%_libdir/libflux.so
%_pkgconfigdir/flux.pc
%_includedir/influxdata

%changelog
* Thu Apr 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.200.0-alt1
- 0.199.0 -> 0.200.0

* Sat Dec 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.199.0-alt1
- 0.198.0 -> 0.199.0

* Tue Dec 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.198.0-alt1
- 0.196.1 -> 0.198.0 (git.40a30737)

* Thu May 29 2025 Alexey Shabalin <shaba@altlinux.org> 0.196.1-alt1
- Initial build.

