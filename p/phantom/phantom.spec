Name: phantom
Version: 0.14.0
Release: alt2

Summary: I/O engine with some modules
License: LGPL-2.1
Group: Networking/WWW

Url: https://github.com/yandex-load/phantom

Source: %name-%version.tar
Patch0: make-R.diff

BuildRequires: libssl-devel gcc5-c++ binutils-devel

ExclusiveArch: x86_64

%description
I/O engine with some modules

%package ssl
Summary: %name ssl subpackage
Group: Networking/WWW
Requires: %name = %version-%release

%description ssl
This package contains ssl support module for %name

%prep
%setup
%patch0 -p1

%build
%make_build

%install
mkdir -p %buildroot%_bindir %buildroot%_prefix/lib/%name
install -pm755 bin/%name %buildroot%_bindir

pushd lib/%name
for i in *.so;do
install -pm644 $i %buildroot%_prefix/lib/%name
done
popd

%files
%_bindir/%name
%_prefix/lib/%name/*.so
%exclude %_prefix/lib/%name/mod_ssl.so
%exclude %_prefix/lib/%name/mod_io_stream_transport_ssl.so
%exclude %_prefix/lib/%name/mod_io_benchmark_method_stream_transport_ssl.so
%doc README* AUTHORS examples

%files ssl
%_prefix/lib/%name/mod_ssl.so
%_prefix/lib/%name/mod_io_stream_transport_ssl.so
%_prefix/lib/%name/mod_io_benchmark_method_stream_transport_ssl.so

%changelog
* Mon Jul  3 2017 Terechkov Evgenii <evg@altlinux.org> 0.14.0-alt2
- Build only for x86_64 for now (see https://github.com/yandex-load/phantom/issues/7)

* Tue Jun 20 2017 Terechkov Evgenii <evg@altlinux.org> 0.14.0-alt1
- 0.14.0~pre65
