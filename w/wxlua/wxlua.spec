Name: wxlua
Version: 2.8.10.0
Release: alt1.qa3
Summary: Lua IDE with a GUI debugger and binding generator
License: wxWidgets License
Group: Development/Other
Url: http://wxlua.sourceforge.net/
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://downloads.sourceforge.net/wxlua/wxLua-2.8.10.0-src.tar
#.gz
Patch: %name-alt-build.patch

# Automatically added by buildreq on Thu Jun 17 2010
BuildRequires: gcc-c++ libGL-devel libX11-devel liblua5-devel libwxGTK-contrib-stc-devel libwxGTK-devel libwxstedit-devel
#TODO: need wxMediaCtrl for this binding
%def_disable wxbindmedia
BuildRequires: desktop-file-utils

%description
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

Additionally, wxLua can be used in your C++ programs to embed a Lua interpreter with the wxWidgets API.

This package contains Integrated Development Environments (IDE, written in
wxLua) with a GUI debugger, a binding generator and wxWidgets bindings usable
as a module.

%package -n lib%name
Group: System/Libraries
Summary: set of Lua bindings to the C++ wxWidgets cross-platform GUI library

%description -n lib%name
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files of lib%name
Requires: lib%name = %version-%release

%description -n lib%name-devel
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

This package contains files required for compiling and linking
applications with lib%name.

%if_enabled static
%package -n lib%name-devel-static
Group: Development/C++
Summary: Static library of %name
Requires: %name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the static library required for statically linking
applications with %name.

%endif #enabled static

%prep
%setup -n wxLua
%patch -p1

%build
%add_optflags -fpermissive
export CPPFLAGS="%optflags"
autoconf -o configure -I build/autoconf build/autoconf/configure.ac
%configure %{subst_enable static} \
	%{subst_enable wxbindmedia} \

make

%install
%makeinstall
mkdir -p \
	%buildroot%_libdir/lua5/ \
	%buildroot%_iconsdir/hicolor/scalable/apps/
subst 's|width="898.612"$|width="350.80908"|' art/wxlualogo.svg
install -p art/wxlualogo.svg %buildroot%_iconsdir/hicolor/scalable/apps/
mv %buildroot%_libdir/lua/*/*.so %buildroot%_libdir/lua5/
subst 's|\.xpm$||;/^Encoding=/d' %buildroot%_desktopdir/*.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=IDE \
	%buildroot%_desktopdir/wxlua.desktop

%files
%_bindir/%{name}*
%_desktopdir/%{name}*.desktop
%_iconsdir/hicolor/scalable/apps/*
%_datadir/mime/packages/%name.xml
%_datadir/%name
%doc docs/*

%files -n lib%name
%_libdir/*.so.*
%_libdir/lua5/*.so

%files -n lib%name-devel
%_includedir/wx*
%_libdir/*.so

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.10.0-alt1.qa3
- Fixed build with gcc 4.6

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.10.0-alt1.qa2

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.8.10.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for wxlua

* Thu Jun 17 2010 Ildar Mulyukov <ildar@altlinux.ru> 2.8.10.0-alt1
- initial build for ALTLinux
- disabled wxGTK Media binding
