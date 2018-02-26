%def_disable static

Name: wxstedit
Version: 1.2.5
Release: alt1.1.qa1
Summary: sample program for the wxWidgets's wxStyledTextCtrl Scintilla wrapper
License: wxWidgets License
Group: Editors
Url: http://wxcode.sourceforge.net/showcomp.php?name=wxStEdit
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: https://sourceforge.net/projects/wxcode/files/Components/wxStEdit/wxstedit-1.2.5.tar
#.gz
Source1: %name.desktop

# Automatically added by buildreq on Wed Jun 16 2010
BuildRequires: gcc-c++ libwxGTK-contrib-stc-devel libwxGTK-devel
BuildRequires: desktop-file-utils

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
wxstedit is a collection library providing GObject-based interfaces and classes
for commonly used data structures.

This package contains the static library required for statically linking
applications with %name.

%endif #enabled static

%prep
%setup -n %name

%build
ln -s setup0.h include/wx/stedit/setup.h
%configure %{subst_enable static}
# broken parallel build
#make_build
%make

%install
%makeinstall
mkdir -p \
	%buildroot%_bindir/ \
	%buildroot%_desktopdir/ \
	%buildroot%_niconsdir/
install -p samples/stedit/%name %buildroot%_bindir/
install -p %SOURCE1 %buildroot%_desktopdir/
install -p art/pencil32.xpm %buildroot%_niconsdir/
# FIXME: i guess this is right
ln -s setup0.h %buildroot%_includedir/wx/stedit/setup.h
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Utility \
	%buildroot%_desktopdir/wxstedit.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_niconsdir/*

%files -n lib%name
%_libdir/*.so.*
%doc docs/* website

%files -n lib%name-devel
%_includedir/wx/stedit
%_libdir/*.so

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.5-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for wxstedit

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1.1
- Rebuilt for soname set-versions

* Wed Jun 16 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.2.5-alt1
- initial build for ALTLinux
