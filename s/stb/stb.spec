%define git 03f50e3
%define snapdate 20231115

Name: stb
Version: 2.38
Release: alt1.g%{git}.%{snapdate}

Summary: single-file libraries for C/C++
License: MIT or ALT-Public-Domain
Group: Development/C++

# see stb.h for the version
Url: http://github.com/nothings/stb
Source: %name-%version.tar

# Fix undefined behavior from array “shape-punning”
# https://github.com/nothings/stb/pull/1194
Patch0:          %{url}/pull/1194.patch

# Fix misleading indentation in stb_divide.h
# https://github.com/nothings/stb/pull/1195
Patch1:          %{url}/pull/1195.patch

# Trivial fix for array-in-structure initialization (missing braces warning)
# https://github.com/nothings/stb/pull/1196
Patch2:          %{url}/pull/1196.patch

# Fix signature of dummy realloc() for STB_VORBIS_NO_CRT
# https://github.com/nothings/stb/pull/1198
Patch3:          %{url}/pull/1198.patch

# Forward declare stbhw__process struct to fix warnings
# https://github.com/nothings/stb/pull/1236
#
# We don’t see these warnings in the “compile tests”, but we can reproduce them
# by manually compiling tests/herringbone_map.c; a real user of the
# stb_herringbone_wang_tile library would encounter them; and inspection of the
# patch shows it to be correct.
Patch4:          %{url}/pull/1236.patch

# Fixes null pointer dereference in https://github.com/nothings/stb/issues/1452
# https://github.com/nothings/stb/pull/1454
#
# Fixes:
#
# NULL pointer dereference in the stb_image.h
# https://github.com/nothings/stb/issues/1452
# NULL pointer derefence in PIC loading (CVE-2023-43898)
# https://github.com/nothings/stb/issues/1521
# Null pointer dereference in stbi__convert_format (GHSL-2023-149)
# https://github.com/nothings/stb/issues/1546
#
# An alternative and equivalent patch is:
#
# Fix Null pointer dereference in stbi__convert_format
# https://github.com/nothings/stb/pull/1547
Patch5:          %{url}/pull/1454.patch

# Fixed asan error on tiny input images
# https://github.com/nothings/stb/pull/1561
#
# Fixes:
#
# stb_image_resize2.h: Address Sanitizer error
# https://github.com/nothings/stb/issues/1526
Patch6:          %{url}/pull/1561.patch

# Fix integer overflow
# https://github.com/nothings/stb/pull/1530
#
# Fixes:
#
# Integer overflow in stbi__convert_8_to_16
# https://github.com/nothings/stb/issues/1529
Patch7:          %{url}/pull/1530.patch

# Add overflow checks
# https://github.com/nothings/stb/pull/1532
#
# Fixes:
#
# Integer overflow in stbi__load_gif_main
# https://github.com/nothings/stb/issues/1531
Patch8:          %{url}/pull/1532.patch

# Fix int overflow
# https://github.com/nothings/stb/pull/1534
#
# Fixes:
#
# Integer overflow in stbi__jpeg_decode_block
# https://github.com/nothings/stb/pull/1533
Patch9:          %{url}/pull/1534.patch

# Fix wild address read in stbi__gif_load_next
# https://github.com/nothings/stb/pull/1539
#
# Fixes:
#
# Wild address read in stbi__gif_load_next (GHSL-2023-145/CVE-2023-45661)
# https://github.com/nothings/stb/issues/1538
Patch10:          %{url}/pull/1539.patch

# Fix multi-byte read heap buffer overflow in stbi__vertical_flip
# https://github.com/nothings/stb/pull/1541
#
# Fixes:
#
# Multi-byte read heap buffer overflow in stbi__vertical_flip
# (GHSL-2023-146/CVE-2023-45662)
# https://github.com/nothings/stb/issues/1540
Patch11:          %{url}/pull/1541.patch

# Fix disclosure of uninitialized memory in stbi__tga_load
# https://github.com/nothings/stb/pull/1543
#
# Fixes:
#
# Disclosure of uninitialized memory in stbi__tga_load
# (GHSL-2023-147/CVE-2023-45663)
# https://github.com/nothings/stb/issues/1542
Patch12:          %{url}/pull/1543.patch

# Fix double-free in stbi__load_gif_main_outofmem
# https://github.com/nothings/stb/pull/1545
#
# Fixes:
#
# Double-free in stbi__load_gif_main_outofmem (GHSL-2023-148/CVE-2023-45664)
# https://github.com/nothings/stb/issues/1544
#
# Rebased on top of https://github.com/nothings/stb/pull/1539.
Patch13:          0001-Fix-double-free-in-stbi__load_gif_main_outofmem.patch

# Fix possible double-free or memory leak in stbi__load_gif_main
# https://github.com/nothings/stb/pull/1549
#
# Fixes:
#
# Possible double-free or memory leak in stbi__load_gif_main
# (GHSL-2023-150/CVE-2023-45666)
# https://github.com/nothings/stb/issues/1548
#
# Rebased on top of https://github.com/nothings/stb/pull/1539 and
# https://github.com/nothings/stb/pull/1545.
Patch14:          0002-Fix-possible-double-free-or-memory-leak-in-stbi__loa.patch

# Fix Null pointer dereference because of an uninitialized variable
# https://github.com/nothings/stb/pull/1551
#
# Fixes:
#
# Null pointer dereference because of an uninitialized variable
# (GHSL-2023-151/CVE-2023-45667)
# https://github.com/nothings/stb/issues/1550
#
# Rebased on top of https://github.com/nothings/stb/pull/1541.
Patch15:          0001-Fix-Null-pointer-dereference-because-of-an-uninitial.patch

# Fix 0 byte write heap buffer overflow in start_decoder
# https://github.com/nothings/stb/pull/1553
#
# Fixes:
#
# 0 byte write heap buffer overflow in start_decoder
# (GHSL-2023-165/CVE-2023-45675)
# https://github.com/nothings/stb/issues/1552
Patch16:          %{url}/pull/1553.patch

%define stbdir %_includedir/stb

%description
Noteworthy:
* image loader: stb_image.h
* image writer: stb_image_write.h
* image resizer: stb_image_resize.h
* font text rasterizer: stb_truetype.h
* typesafe containers: stb_ds.h

%package -n lib%name-devel
Summary: single-file libraries for C/C++
Group: Development/C++
BuildArch: noarch

%description -n lib%name-devel
Header files for STB library.

Noteworthy:
* image loader: stb_image.h
* image writer: stb_image_write.h
* image resizer: stb_image_resize.h
* font text rasterizer: stb_truetype.h
* typesafe containers: stb_ds.h

%prep
%setup
%autopatch -p1

%build

%install
mv stb_vorbis.c stb_vorbis.h
mkdir -p %buildroot%stbdir
install -pm644 *.h %buildroot%stbdir
# Install stb.pc file
mkdir -p %buildroot%_datadir/pkgconfig
cat > %buildroot%_datadir/pkgconfig/%name.pc << END.
prefix=/usr
includedir=\${prefix}/include/stb

Name: %name
Version: %version
Description: Single-file libraries for C/C++
Cflags: -I\${includedir}
END.

%files -n lib%name-devel
%doc *.md docs/*
%stbdir/*
%_datadir/pkgconfig/%name.pc

%changelog
* Sun Nov 19 2023 L.A. Kostis <lakostis@altlinux.ru> 2.38-alt1.g03f50e3.20231115
- Rebased to 03f50e343d796e492e6579a11143a085429d7f5d.
- Added patches from Fedora up to stb-2.28^20231011gitbeebb24-12.fc40:
- Fixes CVE-2023-43898 GHSL-2023-149 GHSL-2023-145/CVE-2023-45661
  GHSL-2023-146/CVE-2023-45662 GHSL-2023-147/CVE-2023-45663
  GHSL-2023-148/CVE-2023-45664 GHSL-2023-150/CVE-2023-45666
  GHSL-2023-151/CVE-2023-45667 GHSL-2023-165/CVE-2023-45675

* Wed May 11 2022 Andrey Cherepanov <cas@altlinux.org> 2.37-alt1.1
- NMU: added stb.pc file

* Tue Jan 12 2021 Michael Shigorin <mike@altlinux.org> 2.37-alt1
- initial package (for TetrisGL)

