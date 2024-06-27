%define _unpackaged_files_terminate_build 1
%undefine _configure_gettext
%def_without python
%global optflags_lto %optflags_lto -ffat-lto-objects

Name:     libredwg
Version:  0.13.3.7265
Release:  alt1

Summary:  GNU LibreDWG is a free C library to handle DWG files
License:  GPL-3.0
Group:    Graphics
URL:      https://www.gnu.org/software/libredwg/
VCS:      https://github.com/LibreDWG/libredwg

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: jsmn.h
Patch0: 0001-Add-missing-#define__GNU_SOURCE.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: doxygen
BuildRequires: jq
BuildRequires: makeinfo
BuildRequires: python3-dev
%if_with python
BuildRequires: swig
%endif

Conflicts: libdxfrw

%description
GNU LibreDWG is a free C library to handle DWG files. It aims to be a free
replacement for the OpenDWG libraries. DWG is the native file format of
AutoCAD.

%package -n lib%name
Summary: Libraries of LibreDWG
Group: System/Libraries

%description -n lib%name
%{summary}.

%package devel
Summary: Development files for LibreDWG
Group: Development/C

%description devel
%{summary}.

%prep
%setup
%patch0 -p1
# Generate version
echo %version >.tarball-version
echo %version >.version
# Copy header from submodule
install -Dpm0644 %SOURCE1 jsmn/jsmn.h

%build
%add_optflags -Wno-error=use-after-free
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
# Remove examples
rm -f %buildroot%_datadir/*.{example,py}
rm -rf %buildroot%_datadir/%name

%files
%doc AUTHORS NEWS README TODO CONTRIBUTING
%_bindir/*
%_man1dir/*.1*

%files -n lib%name
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%name.pc
%_infodir/*.info*
%_man5dir/*.5*

%changelog
* Thu Jun 27 2024 Andrey Cherepanov <cas@altlinux.org> 0.13.3.7265-alt1
- New version.

* Sat May 18 2024 Andrey Cherepanov <cas@altlinux.org> 0.13.3.7257-alt1
- New version.

* Mon Apr 15 2024 Andrey Cherepanov <cas@altlinux.org> 0.13.3.7227-alt1
- New version.

* Wed Sep 20 2023 Artyom Bystrov <arbars@altlinux.org> 0.12.5.5953-alt2
- Fix build (missing #define _GNU_SOURCE)

* Fri Jul 21 2023 Andrey Cherepanov <cas@altlinux.org> 0.12.5.5953-alt1
- New version.

* Wed Jul 19 2023 Andrey Cherepanov <cas@altlinux.org> 0.12.5.5922-alt1
- New version.

* Mon Jun 26 2023 Andrey Cherepanov <cas@altlinux.org> 0.12.5.5862-alt1
- New version.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 0.12.5.5813-alt1
- New version.

* Tue Dec 06 2022 Andrey Cherepanov <cas@altlinux.org> 0.12.5-alt2
- Conflicted with libdxfrw.

* Thu Aug 18 2022 Andrey Cherepanov <cas@altlinux.org> 0.12.5-alt1
- Initial build for Sisyphus.
