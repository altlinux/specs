%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects

Summary: A disassembly framework
Name: capstone
Version: 4.0.2
Release: alt2
License: BSD
Group: Development/Tools
Url: http://capstone-engine.org/
Source: %name-%version-%release.tar
Patch1: Allow-to-override-PYTHON-23-in-Makefiles.patch
Packager: Nikita Ermakov <arei@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: /proc java-devel-default jna python-devel python3-module-yieldfrom

%description
An ultimate disassembly framework for binary analysis and reversing.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/C
%description devel
An ultimate disassembly framework for binary analysis and reversing.
This package contains libraries and headers for developing.

%package -n python-module-%name
Summary: Python bindings for %name
Requires: %name = %EVR
Group: Development/Python
%description -n python-module-%name
An ultimate disassembly framework for binary analysis and reversing.
This package contains python bindings for %name.

%package -n python3-module-%name
Summary: Python 3 bindings for %name
Requires: %name = %EVR
Group: Development/Python3
%description -n python3-module-%name
An ultimate disassembly framework for binary analysis and reversing.
This package contains python 3 bindings for %name.

%package java
Summary: Java bindings for %name
Requires: %name = %EVR
Group: Development/Java
BuildArch: noarch
%description java
An ultimate disassembly framework for binary analysis and reversing.
This package contains java bindings for %name.

%prep
%setup
%patch1 -p1

%build
export PYTHON2="%__python"
export PYTHON3="%__python3"
DESTDIR=%buildroot CFLAGS="%optflags" LIBDIRARCH=%_lib INCDIR="%_includedir" %make_build

# fix the pkgconfig file
sed -i 's;%buildroot;;' capstone.pc
# remove static libs entry from the pkgconfig file
sed -i 's;archive.*;;' capstone.pc
# remove temporary fuzzallcorp test from 'check:' in Makefile
sed -E -i 's;^(check:.*)fuzzallcorp;\1;g' Makefile

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
%python_install --install-lib %python_sitelibdir
%python3_install --install-lib %python3_sitelibdir
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
%python_sitelibdir/*egg-info
%python_sitelibdir/%name

%files -n python3-module-%name
%python3_sitelibdir/*egg-info
%python3_sitelibdir/%name

%files java
%_javadir/

%changelog
* Thu Sep 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.2-alt2
- Fixed build with LTO.

* Fri May 29 2020 Nikita Ermakov <arei@altlinux.org> 4.0.2-alt1
- Updated to 4.0.2.

* Wed Feb 05 2020 Stanislav Levin <slev@altlinux.org> 4.0.1-alt2
- Fixed FTBS.

* Fri Feb 1 2019 Nikita Ermakov <arei@altlinux.org> 4.0.1-alt1
- Updated to 4.0.1.

* Thu Jan 31 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.5-alt2
- NMU: Updated build dependencies.

* Mon Nov 12 2018 Nikita Ermakov <arei@altlinux.org> 3.0.5-alt1
- Updated to 3.0.5.
- Python bindings are architecture dependent now.

* Fri Jun 29 2018 Nikita Ermakov <arei@altlinux.org> 3.0.4-alt1
- Initial build for ALT Linux Sisyphus.
