%def_disable demos
%define major 1

Name: vkd3d
Version: 1.1
Release: alt0.3.gbe4ca96
Summary: The vkd3d 3D Graphics Library

Group: System/Libraries
License: GPL
Url: https://source.winehq.org/git/vkd3d.git/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libvulkan-devel spirv-headers libwine-vanilla-devel
BuildRequires: libspirv-tools-devel spirv-tools
%if_enabled demos
BuildRequires: libxcb-devel libxcbutil-devel libxcbutil-keysyms-devel libxcbutil-icccm-devel
%endif

%description
Vkd3d is a 3D graphics library built on top of Vulkan. It has an API very
similar, but not identical, to Direct3D 12.

%package -n lib%{name}%{major}
Summary: %{name} libraries
Group: System/Libraries

%description -n lib%{name}%{major}
Vkd3d is a 3D graphics library built on top of Vulkan. It has an API very
similar, but not identical, to Direct3D 12.

%package devel
Summary: %name development package
Group: Development/C
Requires: lib%{name}%{major} = %EVR

%description devel
Development headers for %name.

%package demos
Summary: %name demos
Group: Development/C
Requires: lib%{name}%{major} = %EVR

%description demos
%name demos.

%prep
%setup
%patch -p1
%autoreconf
%configure \
  %{subst_enable demos} \
  --with-spirv-tools

%build
%make_build

%install
%makeinstall
%if_enabled demos
mkdir -p %buildroot%_bindir
for f in demos/{gears,triangle}; do
  cp -a "$i" %buildroot%_bindir/%{name}_"$f";
done
%endif

%files -n lib%{name}%{major}
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled demos
%files demos
%_bindir/*
%endif

%changelog
* Sun May 05 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.3.gbe4ca96
- GIT be4ca96.

* Thu Feb 07 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.2.gfd3d661
- GIT fd3d661.

* Mon Dec 03 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.1
- Bump to 1.1 release.
- Disable demos and libxcb (can be enabled one day).

* Mon Jun 18 2018 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt0.1.g04b9d19
- Initial build for ALTLinux.
