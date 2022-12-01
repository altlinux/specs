Name: rav1e
Version: 0.6.1
Release: alt1

Summary: The fastest and safest AV1 encoder
License: BSD-2-Clause
Group: Video
Url: https://github.com/xiph/rav1e

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo rust-cargo-c nasm /proc

%package -n librav1e
Summary: rav1e shared library
Group: System/Libraries

%package -n librav1e-devel
Summary: development part of rav1e
Group: Development/C

%define desc \
rav1e is an AV1 video encoder. It is designed to eventually cover all use cases,\
though in its current form it is most suitable for cases where libaom \
(the reference encoder) is too slow.

%description
%desc

%description -n librav1e
%desc
this package contains shared libraries of rav1e

%description -n librav1e-devel
i%desc
this package contains development part of rav1e

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
cargo build --release

%install
export CARGO_HOME=${PWD}/cargo
install -pm0755 -D target/release/rav1e %buildroot%_bindir/rav1e
cargo cinstall --destdir=%buildroot --includedir=%_includedir \
	--libdir=%_libdir --library-type=cdylib

%files
%_bindir/rav1e

%files -n librav1e
%_libdir/lib*.so.*

%files -n librav1e-devel
%_includedir/rav1e
%_libdir/lib*.so
%_pkgconfigdir/*pc

%changelog
* Thu Dec 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.1-alt1
- 0.6.1 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.1-alt1
- 0.5.1 released

* Fri Nov 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- initial
