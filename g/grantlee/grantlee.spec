
Name: grantlee
Version: 0.2.0
Release: alt1

Group: System/Libraries
Summary: Qt string template engine based on the Django template system
Url: http://www.gitorious.org/grantlee/pages/Home
License: LGPLv2+

Source: %name-%version.tar.gz

# Automatically added by buildreq on Wed Sep 07 2011 (-bi)
# optimized out: cmake-modules elfutils fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libstdc++-devel python-base ruby
#BuildRequires: cmake doxygen fonts-type1-dmtr40in fonts-type1-urw gcc-c++ graphviz libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel rpm-build-ruby
BuildRequires: cmake doxygen gcc-c++ graphviz libqt4-devel kde-common-devel

%description
Grantlee is a plug-in based String Template system written
using the Qt framework. The goals of the project are to make it easier for
application developers to separate the structure of documents from the
data they contain, opening the door for theming.

The syntax is intended to follow the syntax of the Django template system,
and the design of Django is reused in Grantlee.
Django is covered by a BSD style license.

Part of the design of both is that application developers can extend
the syntax by implementing their own tags and filters. For details of
how to do that, see the API documentation.

For template authors, different applications using Grantlee will present
the same interface and core syntax for creating new themes. For details of
how to write templates, see the documentation.

%package -n lib%name
Summary: Qt string template engine based on the Django template system
Group: System/Libraries
%description -n lib%name
Grantlee is a plug-in based String Template system written
using the Qt framework. The goals of the project are to make it easier for
application developers to separate the structure of documents from the
data they contain, opening the door for theming.

The syntax is intended to follow the syntax of the Django template system,
and the design of Django is reused in Grantlee.
Django is covered by a BSD style license.

Part of the design of both is that application developers can extend
the syntax by implementing their own tags and filters. For details of
how to do that, see the API documentation.

For template authors, different applications using Grantlee will present
the same interface and core syntax for creating new themes. For details of
how to write templates, see the documentation.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package apidocs
Group: Development/Documentation
Summary: Grantlee API documentation
Requires: kde-common
BuildArch: noarch
%description apidocs
This package includes the Grantlee API documentation in HTML
format for easy browsing.

%prep
%setup -q

%build
%Kbuild \
  -DCMAKE_BUILD_TYPE=release

pushd BUILD*
%make docs
popd

%install
%Kinstall
mkdir -p %buildroot%_docdir/HTML/en/grantlee-apidocs
cp -prf BUILD*/apidox/* %buildroot%_docdir/HTML/en/grantlee-apidocs

%files -n lib%name
%doc AUTHORS CHANGELOG README GOALS
%_libdir/libgrantlee_core.so.*
%_libdir/libgrantlee_gui.so.*
%_libdir/grantlee/

%files devel
%_includedir/grantlee/
%_includedir/grantlee_*.h
%_libdir/libgrantlee_*.so
%dir %_libdir/cmake
%_libdir/cmake/grantlee/

%files apidocs
%_docdir/HTML/en/grantlee-apidocs/

%changelog
* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- 0.2.0 release (ALT#27236)

* Wed Sep 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt0.0.M60P.1
- built for M60P

* Wed Sep 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt0.1
- initial build of 0.2.0-rc1
