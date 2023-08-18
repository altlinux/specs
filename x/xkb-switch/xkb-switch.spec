Summary:        Switch your X keyboard layouts from the command line
Name:           xkb-switch
Version:        1.8.5
Release:        alt2
URL:            https://github.com/ierton/xkb-switch
License:        GPL-3.0-or-later
Group:          Graphical desktop/Other

Source:         %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires:  cmake gcc-c++ libX11-devel libxkbfile-devel


%description
xkb-switch is a C++ program that allows to query and change the XKB
layout state. Originally ruby-based code written by J.Broomley.

%prep
%setup -q
#quick fix for libdir
%__subst "s|LIBRARY DESTINATION lib OPTIONAL|LIBRARY DESTINATION %_lib OPTIONAL|" CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_libdir/libxkbswitch.so.1*

%changelog
* Thu Aug 17 2023 Ilya Demyanov <turbid@altlinux.org> 1.8.5-alt2
- Fix licence to GPL-3.0-or-later
- Switch build and install to cmake macros
- Don't install .so without soname
- Change "quick fix" CMakeLists.txt from sed to %%__subst macro and move to %prep

* Tue Feb 21 2023 Ilya Demyanov <turbid@altlinux.org> 1.8.5-alt1
- New version 
- Change licence to GPL-3.0 (upstream)
- Add .so symlinks to %files

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.0-alt1.git.d7c1856a
- New version

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.3.1-alt1.git532d92321
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0-alt1.git97bf2c86f
- Initial build for ALT

