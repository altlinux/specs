%define sover 1
%define libqoauth libqoauth%sover

Name:          qoauth
Version:       1.0.1
Release:       alt2

Group:         Graphical desktop/KDE
Summary:       Qt-based C++ library for OAuth authorization scheme
License:       GPL
URL:           http://www.kde.org
Packager: Sergey V Turchin <zerg@altlinux.org>

Requires: qca2-ossl

Source0:       %name-%version.tar.bz2

BuildRequires: doxygen gcc-c++ glibc-devel libqca2-devel libqt4-devel

%description 
QOAuth is an attempt to support interaction with OAuth-powered network 
services in a Qt way, i.e. simply, clearly and efficiently. It gives 
the application developer no more than 4 methods, namely:

* requestToken() to obtain an unauthorized Request Token,
* accessToken() to exchange Request Token for the Access Token,
* createParametersString() to construct a request according to OAuth
  authorization scheme,
* inlineParemeters() - to construct a query string basing on given 
  parameters (provided only for convenience).

%package -n %libqoauth
Summary: %name core library
Group: System/Libraries
%description -n %libqoauth
%name core library.

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: %libqoauth = %version-%release
%description  devel
This package contains header files needed if you wish to build applications
based on %{name} .


%prep
%setup -q
#sed -i -e '/^ *docs \\$/d' \
#       -e "s|\(\$\${INSTALL_PREFIX}\)/lib.*|%{_libdir}|" src/src.pro
sed -i -e 's|/lib|/%{_lib}|g' src/pcfile.sh
find -type f -name \*.pro | \
while read f
do
    echo "QMAKE_CXXFLAGS += \$(RPM_OPT_FLAGS)" >> $f
done
qmake-qt4 qoauth.pro

%build
%make_build


%install
%make install INSTALL="install -p" INSTALL_ROOT=%{buildroot}
doxygen Doxyfile

# fix the time stamp
for file in doc/html/*; do
     touch -r Doxyfile $file
done
make check || :


%files -n %libqoauth
%_libdir/libqoauth.so.%sover
%_libdir/libqoauth.so.%sover.*

%files devel
%doc doc/html doc/examples
%_libdir/libqoauth.so
%_includedir/QtOAuth
%_libdir/libqoauth.prl
%_libdir/libqoauth.so
%_pkgconfigdir/qoauth.pc
%_datadir/qt4/mkspecs/features/oauth.prf

%changelog
* Wed Feb 01 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt2
- rebuilt for debuginfo

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Rebuilt for soname set-versions

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt0.M51.1
- built for M51

* Mon Aug 16 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- initial specfile

