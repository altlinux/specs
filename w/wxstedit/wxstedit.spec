%def_disable static

Name: wxstedit
Version: 1.6.0
Release: alt3.r3169.1
Summary: sample program for the wxWidgets's wxStyledTextCtrl Scintilla wrapper
License: wxWidgets License
Group: Editors
Url: http://wxcode.sourceforge.net/showcomp.php?name=wxStEdit
Packager: Ildar Mulyukov <ildar@altlinux.ru>

# http://svn.code.sf.net/p/wxcode/code/trunk/wxCode/components/stedit/
Source: wxstedit.tar
#.gz
Source1: wxStEdit.desktop

# Automatically added by buildreq on Wed Oct 08 2014
# optimized out: cmake cmake-modules fontconfig libgdk-pixbuf libstdc++-devel libwayland-client libwayland-server libwxGTK-contrib-stc python3-base
BuildRequires: cmake gcc-c++ libwxGTK3.1-devel doxygen

%description
wxStEdit is a library and sample program for the wxWidgets's wxStyledTextCtrl
wrapper around the Scintilla text editor widget. It provides a number of
convenience functions and added capabilities, including the necessary
prefs/styles/language management, menu creation and updating, a splitter,
notebook, and frame component. Additionally it provides a find/replace, editor
settings, and property dialogs. It is designed to be easily integrated into a
larger program and while it tries to manage as much as possible, it's fairly
extensible as well. Individual features and &quot;helper&quot; functionality
can be turned off or overridden if desired. The bottom line, this editor
builds upon the wxStyledTextCtrl by adding all the necessary code to ease the
burden of providing a full featured editor or a set of identically styled
editors in a notebook or frame.

%package -n lib%name
Group: System/Libraries
Summary: a library for the wxWidgets's Scintilla wrapper

%description -n lib%name
wxStEdit is a library and sample program for the wxWidgets's wxStyledTextCtrl
wrapper around the Scintilla text editor widget. It provides a number of
convenience functions and added capabilities, including the necessary
prefs/styles/language management, menu creation and updating, a splitter,
notebook, and frame component. Additionally it provides a find/replace, editor
settings, and property dialogs. It is designed to be easily integrated into a
larger program and while it tries to manage as much as possible, it's fairly
extensible as well. Individual features and &quot;helper&quot; functionality
can be turned off or overridden if desired. The bottom line, this editor
builds upon the wxStyledTextCtrl by adding all the necessary code to ease the
burden of providing a full featured editor or a set of identically styled
editors in a notebook or frame.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files of lib%name
Requires: lib%name = %version-%release

%description -n lib%name-devel
wxStEdit is a library and sample program for the wxWidgets's wxStyledTextCtrl
wrapper around the Scintilla text editor widget.

This package contains files required for compiling and linking
applications with lib%name.

%if_enabled static
%package -n lib%name-devel-static
Group: Development/C++
Summary: Static library of %name
Requires: %name-devel = %version-%release

%description -n lib%name-devel-static
wxStEdit is a library and sample program for the wxWidgets's wxStyledTextCtrl
wrapper around the Scintilla text editor widget.

This package contains the static library required for statically linking
applications with %name.

%endif #enabled static

%prep
%setup -n %name
sed -r -i 's|LIBRARY DESTINATION .*$|LIBRARY DESTINATION %_lib|' \
	CMakeLists.txt

%build
%cmake
%make_build -C BUILD
#%%make_build -C BUILD wxStEdit_doxygen

%install
%makeinstall_std -C BUILD
mkdir -p \
	%buildroot%_bindir/ \
	%buildroot%_desktopdir/ \
	%buildroot%_niconsdir/
install -p -m 755 BUILD/bin/*/* %buildroot%_bindir/
install -p -m 644 %SOURCE1 %buildroot%_desktopdir/
install -p -m 644 art/pencil32.xpm %buildroot%_niconsdir/
pushd %buildroot%_libdir/
ln -s lib%{name}*.so libwxStEditLib.so
popd

%files
%_bindir/*
%_desktopdir/wxStEdit.desktop
%_niconsdir/*
%doc docs/*
#%%eclude %_datadir/{%name,wxStEdit}

%files -n lib%name
%_libdir/lib%{name}*.so
%doc docs/* website

%files -n lib%name-devel
%_includedir/wx/stedit
%_libdir/libwxStEditLib.so

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt3.r3169.1
- Rebuilt with updated libwxGTK3.1

* Mon Oct 27 2014 Ildar Mulyukov <ildar@altlinux.ru> 1.6.0-alt3.r3169
- rebuild with libwxGTK3.1-devel

* Wed Oct 15 2014 Ildar Mulyukov <ildar@altlinux.ru> 1.6.0-alt2.r3169
- rebuild with libwxGTK3.0-devel

* Wed Oct 08 2014 Ildar Mulyukov <ildar@altlinux.ru> 1.6.0-alt1
- new version (SVN)

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.5-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for wxstedit

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1.1
- Rebuilt for soname set-versions

* Wed Jun 16 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.2.5-alt1
- initial build for ALTLinux
