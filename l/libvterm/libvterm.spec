Name: libvterm
Version: 0.3.1
Release: alt1
Epoch: 1

Summary: an abstract C99 library which implements a VT220 or xterm-like terminal emulator

License: MIT
Group: System/Libraries
Url: http://www.leonerd.org.uk/code/libvterm/

Source: %name-%version.tar
Source1: %name.watch

%package devel
Summary: Development files needed for %name
Group: Development/C

%package tools
Summary: %name tools
Group: Terminals

%define common_descr \
An abstract C99 library which implements a VT220 or xterm-like terminal\
emulator. It doesn't use any particular graphics toolkit or output system,\
instead it invokes callback function pointers that its embedding program should\
provide it to draw on its behalf. It avoids calling malloc() during normal\
running state, allowing it to be used in embedded kernel situations.

%description
%common_descr

%description devel
%common_descr

This package contains development files needed for %name.

%description tools
%common_descr

This package contains %name tools.

%prep
%setup

%build
%make_build PREFIX=%_prefix LIBDIR=%_libdir CFLAGS="%optflags"

%install
%makeinstall_std  PREFIX=%_prefix LIBDIR=%_libdir
rm -- %buildroot%_libdir/%name.a

%check
make test

%files
%doc LICENSE
%_libdir/%name.so.*

%files devel
%_includedir/*.h
%_libdir/%name.so
%_pkgconfigdir/vterm.pc

%files tools
%_bindir/*

%changelog
* Mon Feb 06 2023 Vladimir Didenko <cow@altlinux.org> 1:0.3.1-alt1
- Updated to 0.3.1.

* Wed Oct 05 2022 Vladimir Didenko <cow@altlinux.org> 1:0.3.0-alt1
- Updated to 0.3.0.

* Fri Jan 15 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:0.1.4-alt1
- Updated to 0.1.4.

* Sun May 03 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:0.1.3-alt1
- Updated to 0.1.3.
- Fixed watch file.

* Wed Sep 18 2019 Vladimir Didenko <cow@altlinux.org> 1:0.1.1-alt1
- Updated to 0.1.1

* Thu Sep 12 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0+bzr726-alt2
- Fixes CVE-2018-20786.

* Thu Apr 25 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0+bzr726-alt1
- Updated to 0+bzr726 snapshot.

* Tue Jul 10 2018 Vladimir Didenko <cow@altlinux.org> 0+bzr681-alt2
- rebuild for aarch architecture.

* Wed May 03 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0+bzr681-alt1
- Initial build for Sisyphus.
