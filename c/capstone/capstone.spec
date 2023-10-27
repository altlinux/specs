%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects

Summary: Capstone disassembly/disassembler framework
Name: capstone
Version: 4.0.2
Release: alt4.1
License: BSD-3-Clause
Group: Development/Tools
Url: http://capstone-engine.org/
Vcs: https://github.com/capstone-engine/capstone

Source: %name-%version-%release.tar
Patch1: Allow-to-override-PYTHON-23-in-Makefiles.patch
Patch2: remove-distutils-for-python-3.12.patch

Requires: lib%name = %EVR

BuildRequires(pre): rpm-macros-java
BuildRequires(pre): rpm-macros-python3
BuildRequires: java-devel-default
BuildRequires: jna
BuildRequires: /proc
BuildRequires: python-devel
BuildRequires: rpm-build-python3

%description
Capstone is a disassembly framework with the target of becoming the ultimate
disasm engine for binary analysis and reversing in the security community.

%package -n lib%name
Summary: Capstone shared library
Group: System/Libraries
Obsoletes: capstone < %EVR
%description -n lib%name
An ultimate disassembly framework for binary analysis and reversing.

%package -n libcapstone-devel
Summary: Development files for %name
Provides: capstone-devel = %EVR
Obsoletes: capstone-devel < %EVR
Requires: lib%name = %EVR
Group: Development/C
%description -n libcapstone-devel
An ultimate disassembly framework for binary analysis and reversing.
This package contains libraries and headers for developing.

%package -n python3-module-%name
Summary: Python3 bindings for %name
Requires: lib%name = %EVR
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
%autopatch -p1

%build
unset MAKEFLAGS
export PYTHON2="%__python"
export PYTHON3="%__python3"
# ln is required to build cstool dynamically
ln -s libcapstone.so libcapstone.so.${RPM_PACKAGE_VERSION%%%%.*}
DESTDIR=%buildroot CFLAGS="%optflags" LIBDIRARCH=%_lib INCDIR="%_includedir" %make_build V=1

# fix the pkgconfig file
sed -i 's;%buildroot;;' capstone.pc
# remove static libs entry from the pkgconfig file
sed -i 's;archive.*;;' capstone.pc
# remove temporary fuzzallcorp test from 'check:' in Makefile
sed -E -i 's;^(check:.*)fuzzallcorp;\1;g' Makefile

# python bindings
pushd bindings/python
%python3_build
popd

# java bindings
pushd bindings/java
make CFLAGS="%optflags"
popd

%install
DESTDIR=%buildroot LIBDIRARCH=%_lib INCDIR=%_includedir make install V=1
rm -f %buildroot%_libdir/libcapstone.a

# python bindings
pushd bindings/python
%python3_install --install-lib %python3_sitelibdir
popd

# java bindings
install -D -p -m 0644 bindings/java/%name.jar %buildroot%_javadir/%name.jar

%check
export LD_LIBRARY_PATH=%buildroot%_libdir PATH=%buildroot%_bindir:$PATH
make check

ldd %buildroot%_bindir/cstool | grep -F %_libdir/libcapstone.so.
cstool -v
cstool -d x64 90

%files
%doc cstool/README LICENSE.TXT
%_bindir/cstool

%files -n lib%name
%_libdir/*.so.*

%files -n libcapstone-devel
%doc LICENSE*.TXT README ChangeLog
%_includedir/capstone
%_libdir/pkgconfig/%name.pc
%_libdir/*.so

%files -n python3-module-%name
%python3_sitelibdir/*egg-info
%python3_sitelibdir/%name

%files java
%_javadir/*.jar

%changelog
* Fri Oct 27 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt4.1
- NMU: dropped dependency on distutils.

* Tue Aug 08 2023 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt4
- NMU: remove unused BR: python3-module-yieldfrom

* Wed Aug 10 2022 Vitaly Chikunov <vt@altlinux.org> 4.0.2-alt3
- Update spec, package cstool, create separate libcapstone package, fix
  packaging shared library in -devel, do not package python2 module.

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
