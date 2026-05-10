Name: renderdoc
Version: 1.44
Release: alt1

Summary: A frame-capture based graphics debugger
License: MIT
Group: Development/Debuggers

Url: https://%name.org/
Vcs: https://github.com/baldurk/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: %ix86

# https://github.com/baldurk/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: https://github.com/baldurk/swig/archive/renderdoc-modified-7/swig-renderdoc-modified-7.zip

BuildRequires: cmake
BuildRequires: libpcre-devel
BuildRequires: perl-parent
BuildRequires: python3-dev
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel

%description
RenderDoc is a frame-capture based graphics debugger, currently
available for Vulkan, D3D11, D3D12, OpenGL, and OpenGL ES development.

%package devel
Summary: Development files for %{name}
Group: Development/C++
Requires: %name = %EVR

%description devel
RenderDoc is a frame-capture based graphics debugger, currently
available for Vulkan, D3D11, D3D12, OpenGL, and OpenGL ES development.

%prep
%setup

%build
%add_optflags -Wno-error=odr -Wno-error=lto-type-mismatch -Wno-error=stringop-overread -Wno-error=alloc-size-larger-than= -Wno-error=stringop-overflow -I%_includedir/pcre
%cmake \
	-DQMAKE_QT5_COMMAND:STRING=qmake-qt5 \
	-DVULKAN_LAYER_FOLDER:PATH=%_datadir/vulkan/implicit_layer.d \
	-DRENDERDOC_SWIG_PACKAGE:STRING=%SOURCE1 \
	-Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.md README.md
%doc %_datadir/doc/%name
%_bindir/q%name
%_bindir/%{name}cmd
%_desktopdir/%name.desktop
%_libdir/lib%name.so
%_datadir/thumbnailers/%name.thumbnailer
%_iconsdir/hicolor/*/mimetypes/application-x-renderdoc-capture.*
%_datadir/mime/packages/renderdoc-capture.xml
%_pixmapsdir/%name-icon-*.xpm
%_datadir/vulkan/implicit_layer.d/%{name}_capture.json
%_datadir/menu/renderdoc

%files devel
%_includedir/renderdoc_app.h

%changelog
* Sun May 10 2026 Nazarov Denis <nenderus@altlinux.org> 1.44-alt1
- New version 1.44.

* Sun Mar 01 2026 Nazarov Denis <nenderus@altlinux.org> 1.43-alt1
- New version 1.43.

* Fri Dec 19 2025 Nazarov Denis <nenderus@altlinux.org> 1.42-alt1
- New version 1.42.

* Wed Nov 05 2025 Nazarov Denis <nenderus@altlinux.org> 1.41-alt1
- New version 1.41.

* Sun Sep 07 2025 Nazarov Denis <nenderus@altlinux.org> 1.40-alt1
- New version 1.40.

* Tue Jul 01 2025 Nazarov Denis <nenderus@altlinux.org> 1.39-alt1
- New version 1.39.

* Fri May 02 2025 Nazarov Denis <nenderus@altlinux.org> 1.38-alt1
- New version 1.38.

* Sun Mar 23 2025 Nazarov Denis <nenderus@altlinux.org> 1.37-alt1
- New version 1.37.

* Fri Dec 20 2024 Nazarov Denis <nenderus@altlinux.org> 1.36-alt1
- New version 1.36.

* Wed Nov 06 2024 Nazarov Denis <nenderus@altlinux.org> 1.35-alt1
- New version 1.35.

* Thu Mar 21 2024 Nazarov Denis <nenderus@altlinux.org> 1.31-alt1
- Initial build for ALT Linux
