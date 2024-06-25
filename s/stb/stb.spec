%define git 013ac3b
%define snapdate 20240531

# ORIGINAL DESCRIPTION FROM FEDORA PACKAGE
# We choose not to package the "stb_include" library (stb_include.h) because,
# during the package review, it was observed that it follows coding practices
# that make it dangerous to use on untrusted inputs, including but not limited
# to:
#
# - It uses of strcat/strcpy into a fixed-length buffer that is assumed (but
#   not proven) to be large enough for all possible uses
# - It ignores I/O errors (possibly leading to undefined behavior from reading
#   uninitialized memory), and so on.
#
# A substantial rewrite would be required to mitigate these concerns. If a
# request for this library arises, this decision may be revisited, or the
# necessary rewrite may be done and offered upstream. For now, we omit the
# library and expect it will not be missed.
%def_without stb_include

Name: stb
Version: 2.38
Release: alt5.g%git.%snapdate

Summary: single-file libraries for C/C++
License: MIT or ALT-Public-Domain
Group: Development/C++

# see stb.h for the version
Url: http://github.com/nothings/stb
Source: %name-%version.tar

# Fix undefined behavior from array "shape-punning"
# https://github.com/nothings/stb/pull/1194
Patch0: %url/pull/1194.patch

# Fix misleading indentation in stb_divide.h
# https://github.com/nothings/stb/pull/1195
Patch1: %url/pull/1195.patch

# Trivial fix for array-in-structure initialization (missing braces warning)
# https://github.com/nothings/stb/pull/1196
Patch2: %url/pull/1196.patch

# Fix signature of dummy realloc() for STB_VORBIS_NO_CRT
# https://github.com/nothings/stb/pull/1198
Patch3: %url/pull/1198.patch

# Forward declare stbhw__process struct to fix warnings
# https://github.com/nothings/stb/pull/1236
#
# We don’t see these warnings in the "compile tests", but we can reproduce them
# by manually compiling tests/herringbone_map.c; a real user of the
# stb_herringbone_wang_tile library would encounter them; and inspection of the
# patch shows it to be correct.
Patch4: %url/pull/1236.patch

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
Patch5: %url/pull/1454.patch

# Fix integer overflow
# https://github.com/nothings/stb/pull/1530
#
# Fixes:
#
# Integer overflow in stbi__convert_8_to_16
# https://github.com/nothings/stb/issues/1529
Patch7: %url/pull/1530.patch

# Add overflow checks
# https://github.com/nothings/stb/pull/1532
#
# Fixes:
#
# Integer overflow in stbi__load_gif_main
# https://github.com/nothings/stb/issues/1531
Patch8: %url/pull/1532.patch

# Fix int overflow
# https://github.com/nothings/stb/pull/1534
#
# Fixes:
#
# Integer overflow in stbi__jpeg_decode_block
# https://github.com/nothings/stb/pull/1533
Patch9: %url/pull/1534.patch

# Fix wild address read in stbi__gif_load_next
# https://github.com/nothings/stb/pull/1539
#
# Fixes:
#
# Wild address read in stbi__gif_load_next (GHSL-2023-145/CVE-2023-45661)
# https://github.com/nothings/stb/issues/1538
Patch10: %url/pull/1539.patch

# Fix multi-byte read heap buffer overflow in stbi__vertical_flip
# https://github.com/nothings/stb/pull/1541
#
# Fixes:
#
# Multi-byte read heap buffer overflow in stbi__vertical_flip
# (GHSL-2023-146/CVE-2023-45662)
# https://github.com/nothings/stb/issues/1540
Patch11: %url/pull/1541.patch

# Fix disclosure of uninitialized memory in stbi__tga_load
# https://github.com/nothings/stb/pull/1543
#
# Fixes:
#
# Disclosure of uninitialized memory in stbi__tga_load
# (GHSL-2023-147/CVE-2023-45663)
# https://github.com/nothings/stb/issues/1542
Patch12: %url/pull/1543.patch

# Fix double-free in stbi__load_gif_main_outofmem
# https://github.com/nothings/stb/pull/1545
#
# Fixes:
#
# Double-free in stbi__load_gif_main_outofmem (GHSL-2023-148/CVE-2023-45664)
# https://github.com/nothings/stb/issues/1544
#
# Rebased on top of https://github.com/nothings/stb/pull/1539.
Patch13: 0001-Fix-double-free-in-stbi__load_gif_main_outofmem.patch

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
Patch14: 0002-Fix-possible-double-free-or-memory-leak-in-stbi__loa.patch

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
Patch15: 0001-Fix-Null-pointer-dereference-because-of-an-uninitial.patch

# Fix 0 byte write heap buffer overflow in start_decoder
# https://github.com/nothings/stb/pull/1553
#
# Fixes:
#
# 0 byte write heap buffer overflow in start_decoder
# (GHSL-2023-165/CVE-2023-45675)
# https://github.com/nothings/stb/issues/1552
Patch16: %url/pull/1553.patch

Patch17: alt-stb-loongarch64-and-riscv64-support.patch

%global stb_c_lexer_version 0.12
%global stb_connected_components_version 0.96
%global stb_divide_version 0.94
%global stb_ds_version 0.67
%global stb_dxt_version 1.12
%global stb_easy_font_version 1.1
%global stb_herringbone_wang_tile_version 0.7
%global stb_hexwave_version 0.5
%global stb_image_version 2.30
%global stb_image_resize_version 0.97
%global stb_image_resize2_version 2.07
%global stb_image_write_version 1.16
%global stb_include_version 0.2
%global stb_leakcheck_version 0.6
%global stb_perlin_version 0.5
%global stb_rect_pack_version 1.1
%global stb_sprintf_version 1.10
%global stb_textedit_version 1.14
%global stb_tilemap_editor_version 0.42
%global stb_truetype_version 1.26
%global stb_vorbis_version 1.22
%global stb_voxel_render_version 0.89

%define stbdir %_includedir/stb

BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: /usr/bin/convert

%global __find_debuginfo_files %nil

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

# Append to OS build flags rather than overriding them
#
# Instead of hard-coding C++ standard and calling the C compiler, defer to the
# default and call the C++ compiler.
#
# When upstream says CPPFLAGS, they
# mean C++ flags, i.e. CXXFLAGS, not "C PreProcessor Flags" as is common in
# autoconf-influenced projects.
sed -r -i \
    -e 's/([[:alpha:]]+FLAGS[[:blank:]]*)=/\1+=/' \
    -e 's/(\$\(CC\))(.*)-std=[^[:blank:]]+/\$\(CXX\)\2/' \
    -e 's/CPPFLAGS/CXXFLAGS/' tests/Makefile

# Add a dummy main(); how does this one work upstream?! Note that omitting
# parameter names is a C++-ism.
echo 'int main(int, char *[]) { return 0; }' >> tests/test_cpp_compilation.cpp

# Remove any pre-compiled Windows executables
find . -type f -name '*.exe' -print -delete

# Remove some unused parts of the source tree that could contribute different
# (but acceptable) license terms if they were used—just to prove that we do not
# use them.
rm -rvf tests/caveview
find deprecated -type f ! -name 'stb_image_resize.h' -print -delete

%if_disabled stb_include
sed -r -i '/#include[[:blank:]]+"stb_include.h"/d' tests/test_c_compilation.c
%endif

%build
# build only tests
%make_build -C tests

%install
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

# Installing a ".c" file in /usr/include is unconventional, but correct and not
# unprecedented. Any .c file in stb is meant to be #include’d and used as a
# header-only library, just as the ".h" files in the other stb libraries. The
# only difference is the file extension.
install -t '%buildroot%stbdir' -p -m 0644 -D \
    stb_*.h stb_*.c deprecated/stb_image_resize.h
%if_disabled stb_include
rm -vf '%buildroot%stbdir/stb_include.h'
%endif

%check
# The tests in tests/Makefile are largely just "will it compile" tests. There
# are some other files with main routines under tests/, but they have neither
# Makefile targets nor instructions on how to build or run them or what to
# expect them to do. We don’t dig through these sources to try to guess what to
# do with them.

# We can run image_write_test and confirm the output images are valid.
rm -vf output
mkdir -p output
./tests/image_write_test
# We assume that if ImageMagick can read the output images, then they are valid.
for img in wr6x5_flip.bmp wr6x5_flip.jpg wr6x5_flip.tga wr6x5_regular.hdr \
    wr6x5_regular.png wr6x5_flip.hdr wr6x5_flip.png wr6x5_regular.bmp \
    wr6x5_regular.jpg wr6x5_regular.tga
do
  convert "output/${img}" 'output/dummy.bmp'
done

# As a sanity check, verify that all of the subpackage version numbers appear
# in the corresponding headers.
while read -r version header
do
  %{?_disable_stb_include:if [ "${header}" = 'stb_include.h' ]; then continue; fi}
  # The minor version may be zero-padded in the header.
  grep -E "$(
    echo "${version}" |
    sed -r 's/([[:digit:]]+)\.([[:digit:]]+)/\\bv\1\\.0*\2\\b/'
  )" "%buildroot%_includedir/stb/${header}" >/dev/null
done <<'EOF'
%stb_c_lexer_version stb_c_lexer.h
%stb_connected_components_version stb_connected_components.h
%stb_divide_version stb_divide.h
%stb_ds_version stb_ds.h
%stb_dxt_version stb_dxt.h
%stb_easy_font_version stb_easy_font.h
%stb_herringbone_wang_tile_version stb_herringbone_wang_tile.h
%stb_hexwave_version stb_hexwave.h
%stb_image_version stb_image.h
%stb_image_resize_version stb_image_resize.h
%stb_image_resize2_version stb_image_resize2.h
%stb_image_write_version stb_image_write.h
%stb_include_version stb_include.h
%stb_leakcheck_version stb_leakcheck.h
%stb_perlin_version stb_perlin.h
%stb_rect_pack_version stb_rect_pack.h
%stb_sprintf_version stb_sprintf.h
%stb_textedit_version stb_textedit.h
%stb_tilemap_editor_version stb_tilemap_editor.h
%stb_truetype_version stb_truetype.h
%stb_vorbis_version stb_vorbis.c
%stb_voxel_render_version stb_voxel_render.h
EOF

%files -n lib%name-devel
%doc *.md docs/*
%stbdir
%_datadir/pkgconfig/%name.pc

%changelog
* Tue Jun 25 2024 L.A. Kostis <lakostis@altlinux.ru> 2.38-alt5.g013ac3b.20240531
- Rebased to 013ac3beddff3dbffafd5177e7972067cd2b5083:
  stb_resize2 updated to 2.07.
  stb_image updated to 2.30.

* Fri Feb 23 2024 L.A. Kostis <lakostis@altlinux.ru> 2.38-alt4.gae721c5.20240212
- Rebased to ae721c50eaf761660b4f90cc590453cdb0c2acd0.

* Tue Nov 21 2023 Ivan A. Melnikov <iv@altlinux.org> 2.38-alt3.g03f50e3.20231115
- NMU: loongarch64 and riscv64 support

* Sun Nov 19 2023 L.A. Kostis <lakostis@altlinux.ru> 2.38-alt2.g03f50e3.20231115
- Added more tweaks from Fedora:
  + disable stb_include (as it's not safe to use).
  + pack stb_resize (still needed).
  + enable rudimental tests.

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

