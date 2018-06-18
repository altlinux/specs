%define git 04b9d19

Name: vkd3d
Version: 1.0
Release: alt0.1.g%git
Summary: The vkd3d 3D Graphics Library

Group: System/Libraries
License: GPL
Url: https://source.winehq.org/git/vkd3d.git/

Source: %name-%git.tar

BuildRequires: libvulkan-devel spirv-headers libwine-vanilla-devel
BuildRequires: libxcb-devel libxcbutil-devel libxcbutil-keysyms-devel libxcbutil-icccm-devel
BuildRequires: libspirv-tools-devel spirv-tools

%description
Vkd3d is a 3D graphics library built on top of Vulkan. It has an API very
similar, but not identical, to Direct3D 12.

%package -n lib%{name}1
Summary: %{name} libraries
Group: System/Libraries

%description -n lib%{name}1
Vkd3d is a 3D graphics library built on top of Vulkan. It has an API very
similar, but not identical, to Direct3D 12.

%package devel
Summary: %name development package
Group: Development/C
Requires: lib%{name}1 = %EVR

%description devel
Development headers for %name.

%prep
%setup -n %name-%git
%autoreconf
%configure \
  --with-spirv-tools

%build
%make_build

%install
%makeinstall

%files -n lib%{name}1
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jun 18 2018 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt0.1.g04b9d19
- Initial build for ALTLinux.


