Summary: A disassembly framework
Name: capstone
Version: 3.0.4
Release: alt1
License: BSD
Group: Development/Tools
Url: http://capstone-engine.org/
Source: %name-%version-%release.tar
Packager: Nikita Ermakov <arei@altlinux.org>

BuildRequires: /proc java-devel-default jna python-devel python3-module-yieldfrom

%description
An ultimate disassembly framework for binary analysis and reversing.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/C
%description devel
An ultimate disassembly framework for binary analysis and reversing.
This package contains libraries and headers for developing.

%package -n python-module-%name
Summary: Python bindings for %name
Requires: %name = %version-%release
Group: Development/Python
BuildArch: noarch
%description -n python-module-%name
An ultimate disassembly framework for binary analysis and reversing.
This package contains python bindings for %name.

%package -n python3-module-%name
Summary: Python 3 bindings for %name
Requires: %name = %version-%release
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-%name
An ultimate disassembly framework for binary analysis and reversing.
This package contains python 3 bindings for %name.

%package java
Summary: Java bindings for %name
Requires: %name = %version-%release
Group: Development/Java
BuildArch: noarch
%description java
An ultimate disassembly framework for binary analysis and reversing.
This package contains java bindings for %name.

%prep
%setup

%build
DESTDIR=%buildroot CFLAGS="%optflags" LIBDIRARCH=%_lib INCDIR="%_includedir" %make_build

# fix the pkgconfig file
sed -i 's;%buildroot;;' capstone.pc
# remove static libs entry from the pkgconfig file
sed -i 's;archive.*;;' capstone.pc

# python bindings
pushd bindings/python
%python_build
%python3_build
popd

# java bindings
pushd bindings/java
make CFLAGS="%optflags"
popd

%install
DESTDIR=%buildroot LIBDIRARCH=%_lib INCDIR=%_includedir make install
rm -f %buildroot/%_libdir/libcapstone.a

# python bindings
pushd bindings/python
%python_install
%python3_install
popd

# java bindings
install -D -p -m 0644 bindings/java/%name.jar %buildroot/%_javadir/%name.jar

%check
LD_LIBRARY_PATH="%buildroot%_libdir" make check

%files
%doc LICENSE.TXT LICENSE_LLVM.TXT
%doc README ChangeLog
%_libdir/*.so*

%files devel
%_includedir/*
%_libdir/pkgconfig/*

%files -n python-module-%name
%python_sitelibdir_noarch/*egg-info
%python_sitelibdir_noarch/%name

%files -n python3-module-%name
%python3_sitelibdir_noarch/*egg-info
%python3_sitelibdir_noarch/%name

%files java
%_javadir/

%changelog
* Fri Jun 29 2018 Nikita Ermakov <arei@altlinux.org> 3.0.4-alt1
- Initial build for ALT Linux Sisyphus.
