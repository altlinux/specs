%def_without tests
%def_with ffmpeg
# waiting ImageMagick >= 7.0
%def_without ImageMagick

Name: vapoursynth
Version: 58
Release: alt1
Summary: Video processing framework with simplicity in mind
License: WTFPL and LGPL-2.1+ and OFL-1.1 and GPL-2.0+ and ISC and MIT
Group: Video
Url: http://www.vapoursynth.com

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: https://github.com/%name/%name/archive/R%version/%name-R%version.tar.gz
Patch: %name-version-info.patch

#ExclusiveArch: %%ix86 x86_64

BuildRequires(pre): rpm-build-python3
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: nasm
BuildRequires: pkgconfig(tesseract)
BuildRequires: pkgconfig(zimg)
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools
BuildRequires: glibc-pthread

%if_with tests
BuildRequires: python3-test
BuildRequires: python3-module-pytest
%endif

%if_with ImageMagick
BuildRequires: pkgconfig(Magick++) >= 7.0
%endif

%if_with ffmpeg
BuildRequires: pkgconfig(libass)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
%endif

%description
VapourSynth is an application for video manipulation. Or a plugin. Or a library.
It is hard to tell because it has a core library written in C++ and a Python
module to allow video scripts to be created.

%package -n lib%name
Summary: VapourSynth core library with a C++ API
Group: System/Libraries

%description -n lib%name
VapourSynth core library with a C++ API.

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

# %%package plugins
# Summary: VapourSynth plugins
# Group: Video

# %%description plugins
# VapourSynth plugins.

%prep
%setup -n %name-R%version
%patch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' setup.py

%build
%add_optflags -L/%_lib -lpthread
%autoreconf
%configure \
    --disable-static \
    --enable-x86-asm \
    --enable-core \
    --enable-vsscript \
    --enable-vspipe \
    --enable-python-module \
    --enable-eedi3 \
%if_with ImageMagick
    --imwri \
%endif
    --enable-miscfilters \
    --enable-morpho \
    --enable-ocr \
    --enable-removegrain \
%if_with ffmpeg
    --enable-subtext \
%endif
    --enable-vinverse \
    --enable-vivtc

%make_build LIBDIR=%_libdir
# %%python3_build

%install
%python3_install
%makeinstall_std
find %buildroot -type f -name "*.la" -delete

# Let RPM pick up docs in the files section
rm -fr %buildroot%_docdir/%name

%if_with tests
%check
python3 -m pytest -v
%endif

%files -n lib%name
%doc ChangeLog COPYING.LESSER README.md
%_libdir/lib%name.so.*
%_libdir/lib%name-script.so.*

%files -n python3-module-%name
%python3_sitelibdir/%name.so
%python3_sitelibdir/VapourSynth-*.egg-info

%files devel
%_includedir/%name/
%_libdir/lib%name.so
%_libdir/lib%name-script.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-script.pc

%files tools
%_bindir/vspipe

# %%files plugins
# %%dir %%_libdir/%%name
# %%_libdir/%%name/lib*.so

%changelog
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
