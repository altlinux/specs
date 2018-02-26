BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-freeglut
Version:        2.6.0
Release:        alt1_0.2.rc1
Summary:        Fedora MinGW alternative to the OpenGL Utility Toolkit (GLUT)

License:        MIT
Group:          System/Libraries

URL:            http://freeglut.sourceforge.net
Source0:        http://downloads.sourceforge.net/freeglut/freeglut-%{version}-rc1.tar.gz

# Patches from native Fedora package:
# (none)

# Case sensitivity of the header includes.
Patch1000:      freeglut-2.6.0-header-case.patch

# Hack to disable X / enable Windows in the configure.ac file.
Patch1001:      freeglut-2.6.0-disable-X.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 35
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  dos2unix

# Because we patch configure.ac.
BuildRequires:  autoconf automake libtool
Source44: import.info


%description
freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library with an OSI approved free software
license. GLUT was originally written by Mark Kilgard to support the
sample programs in the second edition OpenGL 'RedBook'. Since then,
GLUT has been used in a wide variety of practical applications because
it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing
OpenGL contexts on a wide range of platforms and also read the mouse,
keyboard and joystick functions.

%{_mingw32_description}


%prep
%setup -q -n freeglut-2.6.0

%patch1000 -p1
%patch1001 -p1

autoreconf
libtoolize

dos2unix -k FrequentlyAskedQuestions


%build
%{_mingw32_configure} --disable-static --enable-shared
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install

rm $RPM_BUILD_ROOT%{_mingw32_libdir}/libglut.la


%files
%doc AUTHORS COPYING FrequentlyAskedQuestions NEWS README README.win32 TODO
%{_mingw32_bindir}/libglut-0.dll
%{_mingw32_libdir}/libglut.dll.a
%{_mingw32_includedir}/GL/freeglut.h
%{_mingw32_includedir}/GL/freeglut_ext.h
%{_mingw32_includedir}/GL/freeglut_std.h
%{_mingw32_includedir}/GL/glut.h


%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_0.2.rc1
- initial release by fcimport

