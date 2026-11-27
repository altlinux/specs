%define _unpackaged_files_terminate_build 1
%define libname libimplot
%define sover 1

Name:    implot
Version: 1.1
Release: alt1.1

Summary: Immediate Mode Plotting
License: MIT
Group:   Other
Url:     https://github.com/epezent/implot
VCS:     https://github.com/epezent/implot.git

Source: %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: libimgui-devel

%description
%summary.

%package -n %libname%sover
Summary: Lib files fore %name
Group: System/Libraries
Obsoletes: libimplot0 < %EVR

%description -n %libname%sover
%summary.

%package -n %libname-devel
Summary: Dev files and headers %name
Group: Development/C++
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR
Requires: libimgui-devel
Requires: %libname%sover = %EVR

%description -n %libname-devel
%summary.

%prep
%setup

%build
g++ %optflags -shared -I%_includedir/imgui -fPIC -Wl,--no-undefined -Wl,-soname,lib%name.so.%sover -o lib%name.so.%sover *.cpp -L%_libdir -limgui

%install
install -D -m 644 %name.h %buildroot%_includedir/%name/%name.h
install -D -m 644 %libname.so.%sover %buildroot%_libdir/%libname.so.%sover
ln -s %libname.so.%sover %buildroot%_libdir/%libname.so

%files -n %libname%sover
%_libdir/%libname.so.%sover

%files -n %libname-devel
%_includedir/%name/*
%_libdir/%libname.so

%changelog
* Fri Nov 27 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1.1
- NMU: use libimgui-devel and bump the ImPlot SONAME.

* Mon Oct 26 2026 Artem Semenov <savoptik@altlinux.org> 1.1-alt1
- Builded shared lib.
- NEw version.

* Thu Oct 08 2026 Artem Semenov <savoptik@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
