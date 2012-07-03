%def_disable static

Name: lash
Version: 0.6.0
Release: alt0.20090725.4

Summary: A session management system for JACK audio systems
Summary(ru_RU.UTF-8): Менеджер сессий для сервера JACK
License: %gpl2plus
Group: Sound
Url: http://www.altlinux.org/SampleSpecs/program

Packager: Timur Batyrshin <erthad@altlinux.org>
Source0: %name-%version.tar.bz2
Patch0: %name-0.6.0-alt-DSO.patch

BuildPreReq: rpm-build-licenses
# Automatically added by buildreq on Tue Aug 04 2009
BuildRequires: gcc-c++ jackit-devel libalsa-devel libdbus-devel libgtk+2-devel libreadline-devel libuuid-devel libxml2-devel swig tetex-core

%description
LASH is a session management system for GNU/Linux audio applications. It allows
you to save and restore audio sessions consisting of multiple interconneced
applications, restoring program state (ie loaded patches) and the connections
between them.

%package doc
Summary: Documentation for LASH
Group: Development/Documentation

%description doc
This package holds documentation for LASH -- a session management system for
GNU/Linux audio applications. LASH allows you to save and restore audio sessions
consisting of multiple interconnected applications, restoring program state (ie
loaded patches) and the connections between them.


%package -n liblash
Summary: Headers for lib%name
Group: System/Libraries

%description -n liblash
Headers for building software that uses lib%name


%package -n liblash-devel
Summary: Headers for lib%name
Group: Development/C
Requires: liblash = %version-%release

%description -n liblash-devel
Headers for building software that uses lib%name


%if_enabled static
%package -n liblash-devel-static
Summary: Static libraries for lib%name
Group: Development/C
Requires: liblash = %version-%release

%description -n liblash-devel-static
Static libs for building statically linked software that uses lib%name
%endif

#%package -n python-module-lash
#Summary: Python wrapper for LASH
#Group: Development/Python
#Requires: liblash = %version-%release

#%description -n python-module-lash
#Python bindings for LASH

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --without-jack-dbus --without-python
%make_build

%install
%makeinstall_std

mkdir -p %buildroot{%_desktopdir,%_infodir}
mkdir -p %buildroot%_docdir/lash-doc/{lash-manual-html-one-page,lash-manual-html-split}
mkdir -p %buildroot%_iconsdir/hicolor/{16x16,24x24,48x48,96x96,scalable}/apps

mv %buildroot%_datadir/lash/icons/lash_16px.png %buildroot%_datadir/icons/hicolor/16x16/apps/lash.png
mv %buildroot%_datadir/lash/icons/lash_24px.png %buildroot%_datadir/icons/hicolor/24x24/apps/lash.png
mv %buildroot%_datadir/lash/icons/lash_48px.png %buildroot%_datadir/icons/hicolor/48x48/apps/lash.png
mv %buildroot%_datadir/lash/icons/lash_96px.png %buildroot%_datadir/icons/hicolor/96x96/apps/lash.png
mv %buildroot%_datadir/lash/icons/lash.svg %buildroot%_datadir/icons/hicolor/scalable/apps/lash.svg

#install -pD -m0644 docs/lash-manual.info %buildroot%_infodir/lash.info

#cp -ar AUTHORS ChangeLog NEWS README TODO %buildroot%_docdir/lash

cp -ar docs/api-proposal.html %buildroot%_docdir/lash-doc/
cp -ar docs/lash-manual-html-split/*.html %buildroot%_docdir/lash-doc/lash-manual-html-split/
cp -ar docs/lash-manual-html-one-page/*.html %buildroot%_docdir/lash-doc/lash-manual-html-one-page/

# install the desktop entry
cat << EOF > %buildroot%_desktopdir/%{name}-panel.desktop
[Desktop Entry]
Name=LASH Panel
Comment=LASH Panel
Icon=lash
Exec=%_bindir/lash_panel
Terminal=false
Type=AudioVideo;Audio;
EOF


%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_datadir/dbus-1/services/org.nongnu.lash.service
%_desktopdir/*
%_datadir/icons/hicolor/16x16/apps/lash.png
%_datadir/icons/hicolor/24x24/apps/lash.png
%_datadir/icons/hicolor/48x48/apps/lash.png
%_datadir/icons/hicolor/96x96/apps/lash.png
%_datadir/icons/hicolor/scalable/apps/lash.svg
%_datadir/lash
#_infodir/*.info*

%files doc
%_docdir/lash-doc/api-proposal.html
%_docdir/lash-doc/lash-manual-html-split
%_docdir/lash-doc/lash-manual-html-one-page

%files -n liblash
%_libdir/*.so.*

%files -n liblash-devel
%_libdir/*.so
%_includedir/lash-1.0
%_pkgconfigdir/*.pc

%if_enabled static
%files -n liblash-devel-static
%_libdir/lib/liblash.a
%endif

#%files -n python-module-lash
#%python_sitelibdir/*lash*.so
#%python_sitelibdir/*lash*.py
#%python_sitelibdir/*lash*.pyc
#%python_sitelibdir/*lash*.pyo

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt0.20090725.4
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt0.20090725.3.1.1
- Rebuild with Python-2.7

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt0.20090725.3.1
- Rebuilt for soname set-versions

* Wed Mar 24 2010 Timur Batyrshin <erthad@altlinux.org> 0.6.0-alt0.20090725.3
- python support removed

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt0.20090725.2
- Rebuilt with python 2.6

* Tue Aug 04 2009 Timur Batyrshin <erthad@altlinux.org> 0.6.0-alt0.20090725.1
- Initial build for sisyphus
