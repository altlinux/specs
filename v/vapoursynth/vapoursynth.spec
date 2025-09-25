%define sonamev 0

%def_with tests
%def_with python_ext

Name: vapoursynth
Version: 72
Release: alt2

Summary: Video processing framework with simplicity in mind

License: WTFPL and LGPL-2.1-or-later and OFL-1.1 and GPL-2.0-or-later
Group: Video
Url: https://www.vapoursynth.com
Vcs: https://github.com/vapoursynth/vapoursynth

Source: https://github.com/%name/%name/archive/R%version/%name-R%version.tar.gz
Patch0: %name-%version-%release.patch
Patch1: %name-version-info.patch
Patch2: %name-72-upstream-cython-31.patch

BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Mon Oct 30 2023
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libgpg-error libstdc++-devel perl pkg-config python3 python3-base python3-dev python3-module-setuptools sh5 xz
BuildRequires: gcc-c++ libzimg-devel python3-module-Cython

%if_with python_ext
BuildRequires: python3-module-wheel
%endif

# python_ext
%if_with tests
BuildRequires: python3-test
BuildRequires: python3-module-pytest
%endif

%description
VapourSynth is an application for video manipulation. Or a plugin. Or a library.
It is hard to tell because it has a core library written in C++ and a Python
module to allow video scripts to be created.

%package -n lib%name%version
Summary: VapourSynth core library with a C++ API
Group: System/Libraries
Provides: lib%name = %version
Obsoletes: lib%name < %version

%description -n lib%name%version
VapourSynth core library with a C++ API.

%package -n lib%name-script%sonamev
Summary: VapourSynth script library with a C++ API
Group: System/Libraries

%description -n lib%name-script%sonamev
VapourSynth script library with a C++ API.

%package -n python3-module-%name
Summary: Python interface for VapourSynth
Group: Development/Python3

%description -n python3-module-%name
Python interface for VapourSynth/VSSCript.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
Development files for %name.

%package tools
Summary: Extra tools for VapourSynth
Group: Video

%description tools
This package contains the vspipe tool for interfacing with VapourSynth.

%prep
%setup -n %name-R%version
%patch0 -p1
%patch1 -p1
%if "%(rpmquery --qf '%%{VERSION}' python3-module-Cython)" < "3.1.0"
%patch2 -p1 -R
%endif

sed -i 's|#!/usr/bin/env python|#!%__python3|' setup.py

%build
%autoreconf
%configure \
    --disable-static \
    --enable-x86-asm \
    --enable-core \
    --enable-vsscript \
    --enable-vspipe \
    --enable-python-module

%make_build LIBDIR=%_libdir

%install
%makeinstall_std

%if_with python_ext
# Python installer does not find -lvapoursynth.
%add_optflags -L./.libs -lvapoursynth
%pyproject_build && %pyproject_install
%endif

find %buildroot -type f -name "*.la" -delete

# Let RPM pick up docs in the files section
rm -fr %buildroot%_docdir/%name

%if_with tests
%check
# Python test does not find -lvapoursynth.
export LD_LIBRARY_PATH=%buildroot%_libdir
%pyproject_run_pytest -v
%endif

%files -n lib%name%version
%doc ChangeLog COPYING.LESSER README.md
%_libdir/lib%name.so.%{version}*

%files -n lib%name-script%sonamev
%_libdir/lib%name-script.so.%{sonamev}*

%files -n python3-module-%name
%python3_sitelibdir/%name.so
%if_with python_ext
%python3_sitelibdir/%name.abi3.so
%python3_sitelibdir/%{pyproject_distinfo %name}/
%endif

%files devel
%_includedir/%name/
%_libdir/lib%name.so
%_libdir/lib%name-script.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-script.pc

%files tools
%_bindir/vspipe

# extensions built against stable API, drop versioned ABI req
%filter_from_requires /%python3_ABI_dep/d

%changelog
* Wed Sep 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 72-alt2
- fixed FTBFS with cython>3.1

* Wed Aug 20 2025 Leontiy Volodin <lvol@altlinux.org> 72-alt1
- New version 72.
- Prevented build error with cython less 3.1.0.
- Updated license tag.

* Fri Apr 18 2025 Stanislav Levin <slev@altlinux.org> 71-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Apr 16 2025 Leontiy Volodin <lvol@altlinux.org> 71-alt1
- New version 71.

* Wed Sep 18 2024 Leontiy Volodin <lvol@altlinux.org> 70-alt1
- New version 70.

* Fri Jul 05 2024 Leontiy Volodin <lvol@altlinux.org> 69-alt1
- New version 69.

* Mon May 13 2024 Leontiy Volodin <lvol@altlinux.org> 68-alt1
- New version 68.

* Mon Mar 11 2024 Leontiy Volodin <lvol@altlinux.org> 66-alt1
- New version 66.

* Mon Oct 30 2023 Leontiy Volodin <lvol@altlinux.org> 65-alt1
- New version 65.
- Cleanup BRs.

* Thu Sep 28 2023 Leontiy Volodin <lvol@altlinux.org> 64-alt1
- New version 64.
- Updated version info patch.
- Enabled tests.

* Wed Jun 28 2023 Leontiy Volodin <lvol@altlinux.org> 63-alt1
- New version 63.

* Wed Apr 12 2023 Leontiy Volodin <lvol@altlinux.org> 62-alt1
- New version 62.

* Tue Nov 22 2022 Leontiy Volodin <lvol@altlinux.org> 61-alt1
- New version (61).

* Fri Sep 16 2022 Leontiy Volodin <lvol@altlinux.org> 60-alt1
- New version (60).

* Mon Jun 06 2022 Leontiy Volodin <lvol@altlinux.org> 59-alt1
- New version (59).
- Subpackages:
  + Rename libvapoursynth to libvapoursynth59.
  + Rename libvapoursynth-script to libvapoursynth-script0.

* Fri Apr 15 2022 Leontiy Volodin <lvol@altlinux.org> 58-alt1
- New version (58).

* Thu Mar 10 2022 Leontiy Volodin <lvol@altlinux.org> 57-alt1
- New version (57).
- Subpackages:
  + Disabled plugins.
  + Enabled tools.
  + Fixed python3 module.

* Wed Jul 28 2021 Leontiy Volodin <lvol@altlinux.org> 54-alt1
- New version (54).

* Thu Apr 22 2021 Leontiy Volodin <lvol@altlinux.org> 53-alt1
- New version (53) with rpmgs script.
- Upstream:
  + Add Python 3.9 support.
  + Apply a few contributes bugfixes.

* Wed Jan 13 2021 Leontiy Volodin <lvol@altlinux.org> 52-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
