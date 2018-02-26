Name:		libglui
Version:	2.36
Release:	alt1
Summary:	GL User Interface Library
Group:		System/Libraries
URL:		http://glui.sourceforge.net/
Source:		glui-%version.tgz
Patch:		glui.makefile.patch
License:	ZLIB

# Automatically added by buildreq on Fri Jul 02 2010
BuildRequires: gcc-c++ libGLUT-devel libXext-devel libXi-devel libXmu-devel

%description
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.

%package devel
Summary: GLUI User Interface Library Development Files
Group: System/Libraries
Requires: %name = %version

%description devel
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes the header files and library.

%package devel-static
Summary: GLUI User Interface Library Development Files
Group: System/Libraries
Requires: %name-devel = %version

%description devel-static
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes static library.

%package demos
Summary: GLUI Demos
Group: Graphics

%description demos
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes some binaries built with GLUI.

%prep
%setup -n glui-%version
%patch -p0

%build
cd src
%make_build

%install
install -D src/lib/%name.a %buildroot%_libdir/%name.a
install -D src/lib/%name.so %buildroot%_libdir/%name.so.0
mkdir -p %buildroot%_libexecdir/%name
install -s src/bin/* %buildroot%_libexecdir/%name/
install -D src/include/GL/glui.h %buildroot%_includedir/GL/glui.h
ln -s %name.so.0 %buildroot%_libdir/%name.so

%files
%doc src/readme.txt
%_libdir/*.so.0

%files devel
%doc src/doc
%_libdir/*.so
%_includedir/GL/glui.h

%files devel-static
%_libdir/*.a

%files demos
%doc src/example
%_libexecdir/%name/*

%changelog
* Sat Jul 03 2010 Fr. Br. George <george@altlinux.ru> 2.36-alt1
- Initial build for ALT

