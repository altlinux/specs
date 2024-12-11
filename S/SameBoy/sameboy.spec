%define _unpackaged_files_terminate_build 1
%global __find_debuginfo_files %nil
%global lower_name sameboy

%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/%lower_name

Name: SameBoy
Version: 0.16.6
Release: alt1.1
Summary: Game Boy and Game Boy Color emulator written in C  
License:  MIT
Group: Games/Other
Url: https://github.com/LIJI32/SameBoy

Source: %name-%version.tar

BuildRequires: libSDL2-devel
BuildRequires: pkgconfig(protobuf)
BuildRequires: rgbds
BuildRequires: desktop-file-utils
BuildRequires: libgio-devel
BuildRequires: libgdk-pixbuf-devel

%description
This is a patched version of the SameBoy Game Boy emulator that can emit traces
in the bap-frames format, primarily to be used in combination with rz-tracetest
for testing gb (sm83) lifting.

%prep
%setup
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' Makefile
%endif

%build
export CFLAGS="%optflags"
%make_build sdl FREEDESKTOP=1 CONF=release PREFIX=%_prefix

%install
%makeinstall_std FREEDESKTOP=1 CONF=release PREFIX=%_prefix
# Fix duplicate license install
rm -f %buildroot%_datadir/%lower_name/LICENSE

%files
%doc README.md
%_bindir/%lower_name
%_bindir/%lower_name-thumbnailer
%_datadir/%lower_name/
%_datadir/icons/hicolor/*/apps/*
%_datadir/icons/hicolor/*/mimetypes/*
%_datadir/applications/%lower_name.desktop
%_datadir/mime/%lower_name.xml
%_datadir/thumbnailers/%lower_name.thumbnailer


%changelog
* Wed Dec 11 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.16.6-alt1.1
- Fixed build for Elbrus

* Thu Jul 25 2024 Pavel Shilov <zerospirit@altlinux.org> 0.16.6-alt1
- Initial build for Sisyphus
