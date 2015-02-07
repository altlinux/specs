%def_without qt5

Name:    appstream
Version: 0.8.0
Release: alt1
Summary: Utilities to generate, maintain and access the AppStream Xapian database 

# lib LGPLv2+, tools GPLv2+
License: GPLv2+ and LGPLv2+
Group:   System/Configuration/Packaging
URL:     http://www.freedesktop.org/wiki/Distributions/AppStream/Software
Source0: appstream-%{version}.tar
# VCS: https://github.com/ximion/appstream

Patch:   appstream-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: gobject-introspection-devel
BuildRequires: libxml2-devel
#BuildRequires: packagekit-glib2
%if_with qt5
BuildRequires: qt5-base-devel
%endif
BuildRequires: qt4-devel
BuildRequires: libyaml-devel
BuildRequires: libxapian-devel
BuildRequires: xmlto
BuildRequires: ctest

#Requires: appstream-data

%description
AppStream-Core makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%package devel
Summary:  Development files for %{name}
Group:	  Development/C
Requires: %name = %version-%release

%description devel
%{summary}.

%package qt
Summary: Qt bindings for %{name}
Group:	  System/Libraries
Requires: %name = %version-%release

%description qt
%{summary}.

%package qt-devel
Summary:  Development files for %{name}-qt bindings
Group:	  Development/KDE and QT
Requires: %name-qt = %version-%release

%description qt-devel
%{summary}.

%if_with qt5
%package qt5
Summary: Qt bindings for %{name}
Group:	  System/Libraries
Requires: %name = %version-%release

%description qt5
%{summary}.

%package qt5-devel
Summary:  Development files for %{name}-qt5 bindings
Group:	  Development/KDE and QT
Requires: %name-qt5 = %version-%release

%description qt5-devel
%{summary}.
%endif

%prep
%setup
%patch -p1

%build
%cmake \
  -DQT:BOOL=ON -DAPPSTREAM_QT_VERSION:STRING="4"\
  -DTESTS:BOOL=ON \
  -DVAPI:BOOL=OFF
%cmake_build

%if_with qt5
%cmake_insource \
  -DQT:BOOL=ON -DAPPSTREAM_QT_VERSION:STRING="5"\
  -DTESTS:BOOL=ON \
  -DVAPI:BOOL=OFF
%make_build
%endif


%install
%if_with qt5
# TODO build bindings for qt5 in separate directory
%makeinstall_std -C BUILD-qt5
%endif
%makeinstall_std -C BUILD

mkdir -p %{buildroot}%{_datadir}/app-info/{icons,xmls}
mkdir -p %{buildroot}/var/cache/app-info/{icons,xapian,xmls}
touch %{buildroot}/var/cache/app-info/cache.watch

%find_lang appstream

%check
#LDFLAGS=-Lsrc make test -C BUILD ARGS="--output-on-failure --timeout 300"

# TODO %%posttrans
#%%{_bindir}/appstream-index refresh --force >& /dev/null ||:

%files -f appstream.lang
%doc AUTHORS LICENSE.GPLv2 LICENSE.LGPLv2.1
%config(noreplace) %_sysconfdir/appstream.conf
%_bindir/appstream-index
%_bindir/appstream-validate
%_libdir/girepository-1.0/AppStream-0.8.typelib
%_libdir/libappstream.so.*
%dir %_datadir/app-info/
%dir %_datadir/app-info/icons
%dir %_datadir/app-info/xmls
%_datadir/app-info/categories.xml
%ghost %_cachedir/app-info/cache.watch
%dir %_cachedir/app-info
%dir %_cachedir/app-info/icons
%dir %_cachedir/app-info/xapian
%dir %_cachedir/app-info/xmls
%doc %_man1dir/appstream-index.1*
%doc %_man1dir/appstream-validate.1*

%files devel
%_includedir/AppStream/
%_libdir/libappstream.so
%_libdir/pkgconfig/appstream.pc
%_datadir/gir-1.0/AppStream-0.8.gir

%files qt
%_libdir/libAppstreamQt.so.0*

%files qt-devel
%_includedir/AppstreamQt/
%_libdir/cmake/AppstreamQt/
%_libdir/libAppstreamQt.so

%if_with qt5
# TODO: content for %%name-qt5
%endif

%changelog
* Sat Feb 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version

* Sun Jan 25 2015 Andrey Cherepanov <cas@altlinux.org> 0.7.6-alt1
- New version

* Mon Dec 15 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.5-alt1
- New version

* Tue Oct 28 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Import from Fedora
- Disable tests
