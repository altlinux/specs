%set_verify_elf_method relaxed

Name: libvamp
Version: 2.10.0
Release: alt2
Summary: An API for audio analysis and feature extraction plugins

License: BSD
Group: System/Libraries
Url: https://vamp-plugins.org/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://code.soundsoftware.ac.uk/attachments/download/2588/vamp-plugin-sdk-%version.tar.gz
Patch0: %name-2.9.0-libdir.patch
Patch1: %name-2.9.0-examples-Makefile.patch
Patch2: %name-2.10.0-no-static-libs.patch

BuildRequires: gcc-c++
BuildRequires: libsndfile-devel

Provides: vamp-plugin-sdk = %EVR
Obsoletes: vamp-plugin-sdk < %EVR

%description
Vamp is an API for C and C++ plugins that process sampled audio data
to produce descriptive output (measurements or semantic observations).

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name%{?_isa} = %version-%release
Requires: pkg-config
Provides: vamp-plugin-sdk-devel = %EVR
Obsoletes: vamp-plugin-sdk-devel < %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

# %package static
# Summary: Static libraries for %name
# Group:  System/Libraries
# Requires: %name-devel = %version-%release

# %description static
# The %name-static package contains library files for
# developing static applications that use %name.

%prep
%setup -n vamp-plugin-sdk-%version
touch examples/Makefile
%patch0 -p1
%patch1 -p1
%patch2 -p2

subst 's|/lib/vamp|/%_lib/vamp|g' src/vamp-hostsdk/PluginHostAdapter.cpp
subst 's|/lib/|/%_lib/|g' src/vamp-hostsdk/PluginLoader.cpp

%build
%configure
%make_build

%install
# fix libdir
find . -name '*.pc.in' -exec sed -i 's|/lib|/%_lib|' {} ';'
%makeinstall_std LIBDIR=%_libdir

find %buildroot -name '*.la' -exec rm -f {} ';'
make clean -C examples

%files
%doc COPYING README
%_libdir/*.so.*
%_libdir/vamp

%files devel
%doc examples
%_bindir/vamp-*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

# %files static
# %_libdir/*.a

%changelog
* Tue May 09 2023 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt2
- FTBFS: do not build static library.

* Sat Jun 20 2020 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- New version.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt4
- Remove executable files from examples in documentation

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt3
- Rename to libvamp (ALT #38566)

* Sat Mar 28 2020 Artyom Bystrov <arbars@altlinux.org> 2.9.0-alt2
- Replace possibility of creating Makefile for examples into separate patch
- Remove package with static libraries

* Sat Mar 28 2020 Artyom Bystrov <arbars@altlinux.org> 2.9.0-alt1
- Initial build to ALT Sisyphus
