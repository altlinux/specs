# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libQGLViewer
Version:        2.3.9
Release:        alt2_4
Summary:        Qt based OpenGL generic 3D viewer library

Group:          System/Libraries
License:        GPLv2 with exceptions or GPLv3 with exceptions 
URL:            http://www.libqglviewer.com/index.html
Source0:        http://www.libqglviewer.com/src/%{name}-%{version}.tar.gz

# QGLViewer/VRender/gpc.cpp uses exit(0) to "abort" from a failure of malloc
# Use abort() instead.
Patch0:         libQGLViewer-2.3.1-exit.patch

# libQGLViewer .pro files explicitely remove "-g" from compile flags. Make
# them back.
Patch1:         libQGLViewer-2.3.6-dbg.patch

# Need to include <GL/glu.h> explicitely: <GL/glut.h> is no longer sufficent
Patch2:         libQGLViewer-2.3.9-glu.patch


BuildRequires:  qt4-devel
Source44: import.info
Patch33: libQGLViewer-alt-glu.patch

%description
%{name} is a C++ library based on Qt that eases the creation of OpenGL
3D viewers. It provides some of the typical 3D viewer functionality, such
as the possibility to move the camera using the mouse, which lacks in most
of the other APIs. Other features include mouse manipulated frames,
interpolated keyFrames, object selection, stereo display, screenshot saving
and much more. It can be used by OpenGL beginners as well as to create
complex applications, being fully customizable and easy to extend.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libQGLViewer = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package doc
Summary: API documentation, demos and example programs for %{name}
Group: Documentation
Requires: libQGLViewer = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .exit
%patch1 -p1 -b .dbg
%patch2 -p1 -b .glu

# Fix the encoding of several files, so that they all use utf-8.
for f in doc/*.html doc/examples/*.html \
        examples/contribs/terrain/quadtree.cpp \
        examples/contribs/terrain/viewer.cpp \
        examples/contribs/quarto/piece.cpp \
        examples/contribs/dvonn/dvonnwindowimpl.cpp \
        examples/luxo/luxo.cpp \
        examples/contribs/quarto/jeu.cpp \
        examples/contribs/terrain/terrain.cpp \
        examples/contribs/quarto/rules.txt;
do
  cp -a $f $f.bak
  rm -f $f
  sed -e 's/charset=iso-8859-1/charset=utf-8/' < $f.bak | iconv -f l1 -t utf8 > $f;
  touch -r $f.bak $f
  rm -f $f.bak
done
%patch33 -p2

%build
cd QGLViewer
qmake-qt4 \
          LIB_DIR=%{_libdir} \
          DOC_DIR=%{_defaultdocdir}/%{name}-%{version} \
          INCLUDE_DIR=%{_includedir} \
          TARGET_x=%{name}.so.%{version}
# The TARGET_x variable gives the SONAME. However, qmake behavior is not
# correct when the SONAME is customized: it create wrong symbolic links
# that must be cleaned after the installation.

make %{?_smp_mflags}

cd ../designerPlugin
qmake-qt4 LIB_DIR=../QGLViewer
make %{?_smp_mflags}

%install
cd QGLViewer
make -f Makefile -e INSTALL_ROOT=$RPM_BUILD_ROOT install_target install_include
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer.prl

# Clean symbolic links
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer.so.?.? \
   $RPM_BUILD_ROOT%{_libdir}/libQGLViewer.so.%{version}\\*

cd ../designerPlugin
make -e INSTALL_ROOT=$RPM_BUILD_ROOT install

%files
%doc README LICENCE CHANGELOG GPL_EXCEPTION
%{_libdir}/libQGLViewer.so.%{version}

%files devel
%{_includedir}/QGLViewer/
%{_libdir}/libQGLViewer.so
%{_qt4_plugindir}/designer/libqglviewerplugin.so

%files doc
%doc doc
%doc examples

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt2_4
- update to new fc release

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.9-alt2_1.1
- Fixed build

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt1_1
- initial import by fcimport

