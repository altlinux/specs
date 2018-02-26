
Name: libmygpo-qt
Version: 1.0.5
Release: alt1
%define sover 1
%define libname %name%sover

Group: System/Libraries
Summary: Qt Library that wraps the gpodder.net Web API
Url: http://wiki.gpodder.org/wiki/Libmygpo-qt
License: LGPLv2.1+

Source: %name-%version.tar
Patch1: alt-fix-pkgconfig.patch

# Automatically added by buildreq on Wed Dec 21 2011 (-bi)
# optimized out: cmake-modules elfutils libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libstdc++-devel openssh-common pkg-config
#BuildRequires: cmake cvs doxygen gcc-c++ git-core graphviz libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 mercurial phonon-devel qjson-devel subversion valgrind
BuildRequires: cmake doxygen gcc-c++ graphviz libqt4-devel phonon-devel qjson-devel
BuildRequires: kde-common-devel

%description
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API (http://wiki.gpodder.org/wiki/Web_Services/API_2)
v1.0 wraps nearly every Request from the gpodder.net API except:
- Simple API Calls Downloading subscription Lists & Uploading subscription Lists
- Retrieving Subscription Changes (you should use "Retrieving Updates for a given Device" instead)

%package -n %libname
License: LGPL-2.1+
Group: Development/C++
Summary: Qt Library that wraps the gpodder.net Web API
Group: Development/C++
%description -n %libname
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API (http://wiki.gpodder.org/wiki/Web_Services/API_2)
v1.0 wraps nearly every Request from the gpodder.net API except:
- Simple API Calls Downloading subscription Lists & Uploading subscription Lists
- Retrieving Subscription Changes (you should use "Retrieving Updates for a given Device" instead)

%package devel
License: LGPL-2.1+
Group: Development/C++
Summary: Qt Library that wraps the gpodder.net Web API
Requires: libqt4-devel >= 4.6.0
%description devel
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API (http://wiki.gpodder.org/wiki/Web_Services/API_2)
v1.0 wraps nearly every Request from the gpodder.net API except:
- Simple API Calls Downloading subscription Lists & Uploading subscription Lists
- Retrieving Subscription Changes (you should use "Retrieving Updates for a given Device" instead)

%prep
%setup -q
%patch1 -p1

%build
libsuffix=
%if "%_lib" == "lib64"
libsuffix="64"
%endif
%Kbuild -DLIB_INSTALL_DIR_SUFFIX="$libsuffix"

%install
%Kinstall


%files -n %libname
%_libdir/libmygpo-qt.so.%sover
%_libdir/libmygpo-qt.so.%sover.*

%files devel
%_includedir/mygpo-qt/
%_libdir/cmake/mygpo-qt/
%_libdir/lib*.so
%_libdir/pkgconfig/lib*.pc


%changelog
* Wed Dec 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- initial build
