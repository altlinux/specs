Name: renderdoc
Version: 1.31
Release: alt1

Summary: A frame-capture based graphics debugger
License: MIT
Group: Development/Debuggers

Url: https://%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

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
%add_optflags -Wno-error=odr -Wno-error=lto-type-mismatch -Wno-error=stringop-overread -Wno-error=alloc-size-larger-than=
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
* Thu Mar 21 2024 Nazarov Denis <nenderus@altlinux.org> 1.31-alt1
- Initial build for ALT Linux
