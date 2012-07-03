
Name: ebook-tools
Version: 0.2.1
Release: alt3

Group: Publishing
Summary: Tools for accessing and converting various ebook file formats
Url: http://sourceforge.net/projects/ebook-tools
License: MIT

Source0: %name-%version.tar
Patch1: ebook-tools-0.2.1-fix-lib.patch

# Automatically added by buildreq on Mon Aug 31 2009 (-bi)
#BuildRequires: cmake doxygen gcc-c++ ghostscript-utils graphviz latex2html libxml2-devel libzip-devel xml-utils
BuildRequires: cmake doxygen gcc-c++ ghostscript-utils graphviz latex2html libxml2-devel libzip-devel xml-utils
BuildRequires: kde-common-devel

%description
Tools for accessing and converting various ebook file formats

%package -n libepub
Summary: KDE 4 library
Group: System/Libraries
%description -n libepub
%name library.

%package devel
Summary: Devel stuff for %name
Group: Development/C++
Requires: libepub = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name


%prep
%setup -q
%patch1 -p1


%build
%define libzip_flags %(pkg-config --cflags libzip)
%add_optflags %libzip_flags
%Kcmake \
    -DLIB_INSTALL_DIR=%_libdir \
    -DLIBZIP_INCLUDE_DIR:PATH=%_includedir/libzip
%Kmake


%install
%Kinstall


%files
%_bindir/einfo
%_bindir/lit2epub

%files -n libepub
%_libdir/libepub.so.*

%files devel
%_includedir/*.h
%_libdir/lib*.so

%changelog
* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt3
- fix to build

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt2
- fix to build

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt1
- new version

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- initial specfile
