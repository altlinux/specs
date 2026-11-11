%define _unpackaged_files_terminate_build 1

Name: wine-access
Version: 2026.10.31
Release: alt2

Summary: Wine accessibility helper for screen readers

License: LGPL-2.1-or-later
Group: Accessibility
Url: https://git.stormux.org/storm/wine-access
VCS: https://git.stormux.org/storm/wine-access

Source: %name-%version.tar

# 32- and 64-bit x86 Windows hook DLLs (upstream packages it for x86_64 only)
ExclusiveArch: x86_64

# Orca extension and Cthulhu look for /usr/libexec/wine-access/wine-access.exe
%define helperdir %_prefix/libexec/%name

# winebuild leaves the .CRT$X* sections of a Winelib module unallocated but exports
# their symbols __xi_a..__xt_z: eu-strip of the debuginfo extraction moves the
# sections out and the symbols become undefined (girar: bad_elf_symbols);
# binutils strip keeps them (see %%install)
%add_debuginfo_skiplist %helperdir/wine-access.exe.so

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(xcb)
BuildRequires: wine-devel wine-devel-tools

# the winegcc launcher runs wine from PATH
Requires: /usr/bin/wine

%description
wine-access is a standalone Wine-hosted accessibility helper
for screen readers that implement its Wine D-Bus protocol:
it provides MSAA, NVDA Controller and Tolk compatibility for
Windows applications running under Wine.

Stock Orca does not implement the required Wine methods; the
Orca user extension in %_datadir/%name/orca adds them and starts
the helper for Orca (see %_datadir/%name/orca/README.md).

%prep
%setup

%build
# the native PE hook DLLs are built by winegcc in PE mode:
# there is no mingw-w64 cross compiler in the repository
mkdir -p build-tools
cat > build-tools/winegcc32 <<'EOF'
#!/bin/sh
exec %_bindir/winegcc -b i686-w64-mingw32 "$@"
EOF
cat > build-tools/winegcc64 <<'EOF'
#!/bin/sh
exec %_bindir/winegcc -b x86_64-w64-mingw32 "$@"
EOF
chmod 755 build-tools/winegcc32 build-tools/winegcc64
# Winelib linker rejects LTO objects
%cmake -DCMAKE_TOOLCHAIN_FILE=%_builddir/%name-%version/winelib-toolchain.cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS:STRING="-O2 -g -fno-lto" \
  -DCMAKE_CXX_FLAGS:STRING="-O2 -g -fno-lto" \
  -DMINGW32_C_COMPILER=%_builddir/%name-%version/build-tools/winegcc32 \
  -DMINGW_C_COMPILER=%_builddir/%name-%version/build-tools/winegcc64 \
  -DWINE_ACCESS_INSTALL_DIR:PATH=%helperdir \
  -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
strip --strip-debug %buildroot%helperdir/wine-access.exe.so
mkdir -p %buildroot%_datadir/%name/orca/wine_access
install -m644 orca/wine_access/*.py %buildroot%_datadir/%name/orca/wine_access/
install -m644 orca/README.md %buildroot%_datadir/%name/orca/

%files
%doc README.md
%helperdir/
%_datadir/%name/

%changelog
* Mon Nov 09 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.10.31-alt2
- Keep Requires: /usr/bin/wine; BuildRequires are not runtime dependencies.
- Build the native PE hook DLLs with winegcc (no mingw-w64 in Sisyphus):
  removed BuildRequires: rpm-build-mingw64, added BuildRequires: wine-devel
- Use pkgconfig(gio-2.0), pkgconfig(xcb) instead of libgio-devel,
  libxcb-devel in BuildRequires
- Removed BuildRequires: ctest (the tests need a Wine display driver)
- Install the helper to /usr/libexec/wine-access, where Orca and Cthulhu
  look for it; add Requires: /usr/bin/wine for its launcher
- Fix License (LGPL-2.1-or-later), Group, package files
- Pack the Orca extension

* Thu Nov 05 2026 Artem Semenov <savoptik@altlinux.org> 2026.10.31-alt1
- Initial build fore Sisyphus.

