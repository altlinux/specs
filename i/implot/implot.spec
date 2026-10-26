%define _unpackaged_files_terminate_build 1
%define libname libimplot
%define sover 0

Name:    implot
Version: 1.1
Release: alt1

Summary: Immediate Mode Plotting
License: MIT
Group:   Other
Url:     https://github.com/epezent/implot
VCS:     https://github.com/epezent/implot.git

Source: %name-%version.tar
Source1: imgui-1.91.6-alt1.tar

BuildRequires: gcc-c++
BuildRequires: imgui-devel

%description
%summary.

%package -n %libname%sover
Summary: Lib files fore %name
Group: System/Libraries

%description -n %libname%sover
%summary.

%package -n %libname-devel
Summary: Dev files and headers %name
Group: Development/C++
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n %libname-devel
%summary.

%prep
%setup

# imgui-devel installs only headers, so the core .cpp files are not on the build host.
# Extract them from Sisyphus's imgui src.rpm (declared as Source1).
mkdir -p %_builddir/imgui-src 
pushd %_builddir/imgui-src
tar xf %SOURCE1
popd
for f in imgui.cpp imgui_demo.cpp imgui_draw.cpp imgui_tables.cpp imgui_widgets.cpp; do
  cp %_builddir/imgui-src/imgui-1.91.6-alt1/imgui/$f .
done


%build
g++ %optflags -shared -I%_includedir/imgui -fPIC -Wl,-soname,lib%name.so.0 -o lib%name.so.0 *.cpp

%install
install -D -m 644 %name.h %buildroot%_includedir/%name/%name.h
install -D -m 644 %libname.so.0 %buildroot%_libdir/%libname.so.0
ln -s %_libdir/%libname.so.0 %buildroot%_libdir/%libname.so

%files -n %libname%sover
%_libdir/%libname.so.%sover

%files -n %libname-devel
%_includedir/%name/*
%_libdir/%libname.so

%changelog
* Mon Oct 26 2026 Artem Semenov <savoptik@altlinux.org> 1.1-alt1
- Builded shared lib.
- NEw version.

* Thu Oct 08 2026 Artem Semenov <savoptik@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
