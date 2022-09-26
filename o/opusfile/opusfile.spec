Name: opusfile
Version: 0.12.0.39.0a4c
Release: alt1

Summary: A high-level API for decoding and seeking within .opus files
License: BSD-3-Clause
Group: System/Libraries
Url: https://opus-codec.org/
Vcs: https://gitlab.xiph.org/xiph/opusfile
Source: %name-%version.tar

BuildRequires: doxygen graphviz fonts-ttf-dejavu libogg-devel libopus-devel libssl-devel

%def_disable static

%description
The opusfile and opusurl libraries provide a high-level API for
decoding and seeking within .opus files on disk or over http(s).

%package -n lib%{name}0
Summary: Runtime decoder library for .opus streams
License: BSD-3-Clause
Group: System/Libraries
Provides: lib%name = %version
Obsoletes: lib%name < %version

%description -n lib%{name}0
This package contains %name shared library for .opus streams.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%name-devel
This package contains the header files and documentation needed
to develop applications with %name.

%package -n lib%name-devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: lib%name-devel = %EVR
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version

%description -n lib%name-devel-static
This package contains development libraries required for packaging
statically linked %name-based software.

%package -n libopusurl0
Summary: High-level Opus decoding library, URL support
License: BSD-3-Clause
Group: System/Libraries

%description -n libopusurl0
High-level Opus decoding library, URL support.

%package -n libopusurl-devel
Summary: Development files for opusurl
Group: Development/C
Provides: opusurl-devel = %version
Obsoletes: opusurl-devel < %version

%description -n libopusurl-devel
This package contains the header files and documentation needed
to develop applications with opusurl.

%package -n libopusurl-devel-static
Summary: Static libraries for opusurl
Group: Development/C
Requires: lib%name-devel = %EVR
Provides: opusurl-devel-static = %version
Obsoletes: opusurl-devel-static < %version

%description -n libopusurl-devel-static
This package contains development libraries required for packaging
statically linked libopusurl-based software.

%prep
%setup
cat > package_version <<-'EOF'
	PACKAGE_VERSION=%version
	AUTO_UPDATE=no
EOF

%build
%autoreconf
%configure \
	%{subst_enable static}
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%files -n lib%{name}0
%_libdir/lib%{name}.so.*
%doc AUTHORS COPYING README.md

%files -n lib%name-devel
%_libdir/lib%{name}.so
%_includedir/*
%_pkgconfigdir/%name.pc
%_docdir/%name/

%files -n libopusurl0
%_libdir/libopusurl.so.*

%files -n libopusurl-devel
%_libdir/libopusurl.so
%_pkgconfigdir/opusurl.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a

%files -n libopusurl-devel-static
%_libdir/libopusurl.a
%endif

%changelog
* Mon Sep 26 2022 L.A. Kostis <lakostis@altlinux.ru> 0.12.0.39.0a4c-alt1
- v0.12-3-g4174c26 -> v0.12-39-g0a4cd79.

* Sun Nov 08 2020 Dmitry V. Levin <ldv@altlinux.org> 0.12.0.3.4174-alt2
- Made libopusfile0 Provide+Obsolete libopusfile to facilitate replacement
  of the removed libopusfile package with libopusfile0 (closes: #39223).

* Tue Oct 13 2020 Dmitry V. Levin <ldv@altlinux.org> 0.12.0.3.4174-alt1
- v0.11-5-gd2577d7 -> v0.12-3-g4174c26.
- Renamed subpackages:
  opusfile-devel -> libopusfile-devel,
  opusurl-devel -> libopusurl-devel.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 0.11-alt0.5.gd2577d7
- initial build for ALTLinux.
