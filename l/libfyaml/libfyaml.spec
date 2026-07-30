%define sover 0
%define libfyaml libfyaml%sover
Name:    libfyaml
Version: 0.9.6
Release: alt2

Summary: Fully feature complete YAML parser and emitter
License: MIT
Group:   System/Libraries
Url:     https://github.com/pantoniou/libfyaml

Source: %name-%version.tar
Patch1: 0001-Fix-32-bit-build-by-removing-stray-parameter-to-fy_s.patch
Patch2: 0002-vlsize-Handle-decoding-when-size_t-sizeof-uint64_t.patch

%description
Fully feature complete YAML parser and emitter, supporting the latest YAML spec and passing the full YAML testsuite.

%package devel
Summary: Develpment files for %name
Group: Development/C
%description devel
Development files for %name.

%package utils
Summary: Utils for %name
Group: Development/C
%description utils
Utils for %name.

%package -n %libfyaml
Summary: Fully feature complete YAML parser and emitter
Group: System/Libraries
%description -n %libfyaml
Fully feature complete YAML parser and emitter, supporting the latest YAML spec and passing the full YAML testsuite.

%prep
%setup
%autopatch -p1
%autoreconf

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files utils
%_bindir/fy-*
%_man1dir/fy-*

%files -n %libfyaml
%doc *.md
%_libdir/libfyaml.so.%sover
%_libdir/libfyaml.so.*

%files devel
%_libdir/lib*.so
%_includedir/libfyaml*
%_libdir/pkgconfig/%name.pc
%_man3dir/libfy*

%changelog
* Thu Jul 30 2026 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt2
- using tarball packageing scheme
- apply shared libs policy

* Sun Jul 05 2026 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus.
