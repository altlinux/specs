Name:     libyui
Version:  4.6.2
Release:  alt2
Summary:  GUI abstraction library
Group:    System/Libraries

License:  LGPL-2.1-only OR LGPL-3.0-only
URL:      https://github.com/libyui/libyui
Source:   %{name}-%{version}.tar
Patch: %name-%version.patch

BuildRequires(pre):  rpm-macros-cmake

BuildRequires(pre):  rpm-macros-ruby
BuildRequires(pre):  rpm-macros-python3

BuildRequires:  rpm-build-cmake
BuildRequires:  ctest
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  libncurses++-devel
BuildRequires:  libncursesw-devel
BuildRequires:  libtool
BuildRequires:  ruby-stdlibs
BuildRequires:  perl-devel
BuildRequires:  swig
BuildRequires:  fontconfig-devel


BuildRequires:  pkgconfig(ruby)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libpng)

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)

BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(ncurses)

%global so_version 16
%global bin_name %{name}%{so_version}


%description
This is the user interface engine that provides the abstraction
from graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).

Originally developed for YaST, libyui can now be used
independently of YaST for generic (C++) applications.

libyui has very few dependencies.


#--------------------------------------------------------
# libyui (so-versioned)

%package -n %{bin_name}
Summary:  GUI abstraction library
Group:    System/Libraries

%description -n %{bin_name}
This is the user interface engine that provides the abstraction
from graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).

Originally developed for YaST, libyui can now be used
independently of YaST for generic (C++) applications.

libyui has very few dependencies.


#--------------------------------------------------------
# libyui-devel

%package devel
Summary:      libYUI, YaST2 User Interface Engine - header files
Group:        Development/C++
Requires:     %{bin_name} = %{version}-%{release}
Requires:     boost-devel

%description devel
This is the development package for libyui user interface engine that provides
the abstraction from graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).


#--------------------------------------------------------
# libyui-qt

%package qt%{so_version}
Summary:        Libyui - Qt (graphical) user interface
Group:          System/Libraries
Requires:       libqt5-x11extras
Provides:       %{name}-qt = %{version}-%{release}

%description qt%{so_version}
This package contains the Qt (graphical) user interface component for libyui.


#--------------------------------------------------------
# libyui-qt-devel

%package qt-devel
Summary:        Libyui - Qt (graphical) user interface header files
Group:          Development/KDE and QT
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-qt = %{version}-%{release}

%description qt-devel
This package contains the header files for the Qt based user interface
component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-qt.


#--------------------------------------------------------
# libyui-qt-graph

%package qt-graph%{so_version}
Summary:        Libyui - Qt graph component for libyui.
Group:          System/Libraries
BuildRequires:  graphviz-devel
Requires:       libqt5-x11extras
Requires:       %{name}-qt = %{version}-%{release}
Provides:       %{name}-qt-graph = %{version}-%{release}


%description qt-graph%{so_version}
This package contains the Qt graph component for libyui.

This is a special widget to visualize graphs such as the
storage device hierarchy (disks, partitions, subvolumes
etc.).  and similar graphviz-generated graphs.


#--------------------------------------------------------
# libyui-qt-graph-devel

%package qt-graph-devel
Summary:        Libyui - Qt (graphical) user interface header files
Group:          Development/KDE and QT
Requires:       %{name}-qt-devel = %{version}-%{release}
Requires:       %{name}-qt-graph = %{version}-%{release}

%description qt-graph-devel
This package contains the header files for the Qt based user interface
component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-qt.


#--------------------------------------------------------
# libyui-ncurses

%package ncurses%{so_version}
Summary:        Libyui - NCurses (text based) user interface
Group:          System/Libraries
Provides:       %{name}-ncurses = %{version}-%{release}

%description ncurses%{so_version}
This package contains the NCurses (text based) user interface component for
libyui.


#--------------------------------------------------------
# libyui-ncurses-devel

%package ncurses-devel
Summary:        Libyui - Header fles for the NCurses (text based) user interface
Group:          Development/Other
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-ncurses = %{version}-%{release}

%description ncurses-devel
This package contains the header files for the NCurses (text based) user
interface component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-ncurses.


#--------------------------------------------------------
# libyui-ncurses-tools

%package ncurses-tools
Summary:        Libyui - tools for the NCurses (text based) user interface
Group:          System/Libraries
Requires:       screen
BuildArch:      noarch

%description ncurses-tools
This package contains tools for the NCurses (text based) user interface
component for libyui:

libyui-terminal - useful for testing on headless machines


#--------------------------------------------------------
# ruby-yui

%package -n ruby-yui
Summary:        Ruby bindings for libyui
Group:          Development/Ruby

%description -n ruby-yui
This package provides Ruby language bindings to access functions of libyui, the
YaST User Interface engine that provides the abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).


#--------------------------------------------------------
# python3-module-yui

%package -n python3-module-yui
Summary:        Python 3 bindings for libyui
Group:          Development/Python


%description -n python3-module-yui
This package provides Python 3 language bindings to access functions of libyui,
the YaST User Interface engine that provides the abstraction from graphical
user interfaces (Qt, Gtk) and text based user interfaces (ncurses).


#--------------------------------------------------------
# perl-yui

%package -n perl-yui
Summary:        Perl bindings for libyui
Group:          Development/Perl

%description -n perl-yui
This package provides Perl language bindings to access functions of libyui, the
YaST User Interface engine that provides the abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).


#--------------------------------------------------------

%prep
%setup
%patch -p1

# Upstream's testing-targets expect compiled libs at .../build/src, not .../src
# So, we need to redefine builddir
%define _cmake__builddir build

%build
for pkgname in libyui libyui-qt libyui-qt-graph libyui-ncurses libyui-bindings; do
  pushd $pkgname

  %cmake \
    -DWERROR=FALSE \
    -DBUILD_EXAMPLES=OFF \
    -DWITH_MONO=OFF \
    -DPYTHON_EXECUTABLE=%{__python3} \
    -DPYTHON_INCLUDE_DIR=%{__python3_includedir} \
    -DPYTHON_SITEDIR=%{python3_sitelibdir} \
    -DPYTHON_LIB_DIR=%{python3_libdir} \
    -DBUILD_RUBY_GEM=NO \
    -DRuby_VENDORLIB_DIR=%{ruby_vendorlibdir} \
    DRUBY_VENDOR_ARCH_DIR=%{python3_sitelibdir}
  
  %cmake_build

  popd
done

    
%install
install -m0755 -d %{buildroot}%{_libdir}/yui

for pkgname in libyui libyui-qt libyui-qt-graph libyui-ncurses libyui-bindings; do
  pushd $pkgname
  %cmake_install
  popd
done


%check
for pkgname in libyui libyui-ncurses; do
  pushd $pkgname
  %ctest -V
  popd
done


#--------------------------------------------------------
# libyui (so-versioned)

%files -n %{bin_name}
%doc COPYING*
%{_libdir}/%{name}.so.%{so_version}*

#--------------------------------------------------------
# libyui-devel

%files devel
%dir %{_datadir}/%{name}
%dir %{_includedir}/yui
%{_libdir}/%{name}.so
%{_includedir}/yui/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/buildtools

#--------------------------------------------------------
# libyui-qt

%files qt%{so_version}
%doc COPYING*
%dir %{_libdir}/yui
%{_libdir}/yui/%{name}-qt.so.%{so_version}*

#--------------------------------------------------------
# libyui-qt-devel

%files qt-devel
%{_libdir}/yui/%{name}-qt.so
%{_includedir}/yui/qt
%{_libdir}/pkgconfig/%{name}-qt.pc

#--------------------------------------------------------
# libyui-qt-graph

%files qt-graph%{so_version}
%doc COPYING*
%dir %{_libdir}/yui
%{_libdir}/yui/%{name}-qt-graph.so.%{so_version}*

#--------------------------------------------------------
# libyui-qt-graph-devel

%files qt-graph-devel
%{_libdir}/yui/%{name}-qt-graph.so
%{_includedir}/yui/qt-graph

#--------------------------------------------------------
# libyui-ncurses

%files ncurses%{so_version}
%doc COPYING*
%dir %{_libdir}/yui
%{_libdir}/yui/%{name}-ncurses.so.%{so_version}*

#--------------------------------------------------------
# libyui-ncurses-devel

%files ncurses-devel
%{_libdir}/yui/%{name}-ncurses.so
%{_includedir}/yui/ncurses
%{_libdir}/pkgconfig/%{name}-ncurses.pc

#--------------------------------------------------------
# libyui-ncurses-tools

%files ncurses-tools
%{_bindir}/%{name}-terminal

#--------------------------------------------------------
# ruby-yui

%files -n ruby-yui
%doc libyui-bindings/swig/ruby/examples/*.rb
%{ruby_vendorarchdir}/*
%{ruby_vendorlibdir}/*

#--------------------------------------------------------
# python3-module-yui

%files -n python3-module-yui
%doc libyui-bindings/swig/python/examples/*.py
%{python3_sitelibdir}/*

#--------------------------------------------------------
# perl-yui

%files -n perl-yui
%doc libyui-bindings/swig/perl/examples/*.pl
%{perl_vendorarch}/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 13 2025 Sergey Konev <darisishe@altlinux.org> 4.6.2-alt2
- Fixed build with CMake 4.0.0

* Mon Mar 03 2025 Sergey Konev <darisishe@altlinux.org> 4.6.2-alt1
- Initial package (re-packaged after deletion in 2017)


