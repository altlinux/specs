%define _unpackaged_files_terminate_build 1
%undefine _configure_gettext
%def_without python
%global optflags_lto %optflags_lto -ffat-lto-objects

Name:     libredwg
Version:  0.12.5
Release:  alt2

Summary:  GNU LibreDWG is a free C library to handle DWG files
License:  GPL-3.0
Group:    Graphics
URL:      https://www.gnu.org/software/libredwg/
VCS:      https://github.com/LibreDWG/libredwg

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: jsmn.h

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
# Generate version
echo %version >.tarball-version
echo %version >.version
# Copy header from submodule
install -Dpm0644 %SOURCE1 jsmn/jsmn.h

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
# Remove examples
rm -f %buildroot%_datadir/*.{example,py}

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
* Tue Dec 06 2022 Andrey Cherepanov <cas@altlinux.org> 0.12.5-alt2
- Conflicted with libdxfrw.

* Thu Aug 18 2022 Andrey Cherepanov <cas@altlinux.org> 0.12.5-alt1
- Initial build for Sisyphus.
