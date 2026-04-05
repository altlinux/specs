%define _unpackaged_files_terminate_build 1

%def_with check

Name: wxformbuilder
Version: 4.2.1
Release: alt1

Summary: wxWidgets GUI Builder
License: GPL-2.0-or-later
Group: 	Development/Other
Url: https://github.com/wxFormBuilder/wxFormBuilder

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: libwxBase3.2-devel
BuildRequires: boost-devel
BuildRequires: pkgconfig(tinyxml2)

%if_with check
BuildRequires: /usr/bin/xvfb-run
%endif

%description
wxFormBuilder is a GUI builder for the wxWidgets framework.
Code generation is supported for C++, Python, Lua and PHP.
Additionally, the import and export of XRC code is possible.
To support additional widgets, custom plugins can be used.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# HACK to make plugins loadable
mv -v %buildroot%_libdir/wxformbuilder/*.so %buildroot%_libdir/
rmdir -v %buildroot%_libdir/wxformbuilder

%check
xvfb-run --server-args="-screen 0, 1280x720x24" -a %buildroot%_bindir/wxformbuilder -v

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/wxformbuilder
%_libdir/*.so
%_datadir/wxformbuilder/
%_datadir/mime/packages/*.xml
%_desktopdir/org.wxformbuilder.wxFormBuilder.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/mimetypes/*.png
%_datadir/metainfo/org.wxformbuilder.wxFormBuilder.metainfo.xml

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 4.2.1-alt1
- Initial build for Sisyphus
