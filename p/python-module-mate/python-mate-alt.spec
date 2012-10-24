# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%filter_from_requires /^python2.[0-9]._mate.$/d
%filter_from_requires /^python2.[0-9]._mate.$/d
%define _libexecdir %_prefix/libexec
%define oldname python-module-mate
%define oldname python-mate
# Last updated for 1.1.0
# The order here corresponds to that in configure.ac,
# for easier comparison.  Please do not alphabetize.
%define pygtk_version                   2.10.3
%define python_corba_version             1.1.0
%define glib_version                    2.6.0
%define gtk_version                     2.6.0
%define libmate_version                 1.1.2
%define libmateui_version               1.1.2
%define libmatecanvas_version           1.1.0
%define mate_vfs_version                1.1.0
%define mate_conf_version               1.1.0
%define libmatecomponent_activation_version       1.1.0
%define libmatecomponent_version        1.1.0
%define libmatecomponentui_version      1.1.0
%define python_version                  2.3.0
%define pygobject_version               2.17.0

### Abstract ###

Name:		python-module-mate
Version:	1.4.0
Release:	alt1_1.1.1.1
License:	LGPLv2+
Group:		Development/Other
Summary:	The sources for the PyMATE Python extension module.
URL:		http://mate-desktop.org
Source:		http://pub.mate-desktop.org/releases/1.4/%{oldname}-%{version}.tar.xz

### Dependencies ###

Requires: pygtk2 >= %{pygtk_version}

### Build Dependencies ###

BuildRequires: python-module-pygtk-devel >= %{pygtk_version}
BuildRequires: python-devel >= %{python_version}
BuildRequires: python-module-corba-devel >= %{python_corba_version}
BuildRequires: libmate-devel >= %{libmate_version}
BuildRequires: libmateui-devel >= %{libmateui_version}
BuildRequires: libmatecomponent-devel >= %{libmatecomponent_version}
BuildRequires: libmatecomponentui-devel >= %{libmatecomponentui_version}
BuildRequires: libavahi-glib-devel
BuildRequires: mate-common
BuildRequires: libdbus-glib-devel
BuildRequires: libdbus-devel
BuildRequires: libssl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libselinux-devel

Obsoletes: 		mate-python2
Provides:  		python-mate

%description
The mate-python package contains the source packages for the Python
bindings for MATE called PyMATE.

PyMATE is an extension module for Python that provides access to the
base MATE libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package -n python-module-mate-mate
Summary: Python bindings for libmate
Group: Development/Other
Requires: python-module-mate = %{version}-%{release}
Requires: python-module-mate-matevfs = %{version}-%{release}
Requires: libmate >= %{libmate_version}
Requires: libmateui >= %{libmateui_version}

Obsoletes: 		mate-python2-mate
Provides:  		python-mate-mate

%description -n python-module-mate-mate
This module contains a wrapper that makes libmate functionality available
from Python.

%package capplet
Summary: Python bindings for MATE Panel applets.
Group: Development/Other
Requires: python-module-mate = %{version}-%{release}

Obsoletes: 		mate-python2-capplet
Provides:  		python-mate-capplet

%description capplet
This module contains a wrapper that allows MATE Control Center
capplets to be in Python.

%package -n python-module-mate-canvas
Summary: Python bindings for the MATE Canvas.
Group: Development/Other
Requires: python-module-mate = %{version}-%{release}
Requires: gtk2 >= %{gtk_version}
Requires: libmatecanvas >= %{libmatecanvas_version}
Requires: pygtk2 >= %{pygtk_version}

Obsoletes: 		mate-python2-canvas
Provides:  		python-mate-canvas

%description -n python-module-mate-canvas
This module contains a wrapper that allows use of the MATE Canvas
in Python.


%package -n python-module-mate-matecomponent
Summary: Python bindings for interacting with matecomponent.
Group: Development/Other
Requires: python-module-mate = %{version}-%{release}
Requires: libmatecomponent-activation >= %{libmatecomponent_activation_version}
Requires: libmatecomponent >= %{libmatecomponent_version}
Requires: libmatecomponentui >= %{libmatecomponentui_version}
Requires: python-module-corba >= %{python_corba_version}

Obsoletes: 		mate-python2-matecomponent
Provides:  		python-mate-matecomponent

%description -n python-module-mate-matecomponent
This module contains a wrapper that allows the creation of matecomponent
components and the embedding of matecomponent components in Python.

%package -n python-module-mate-mateconf
Summary: Python bindings for interacting with MateConf
Group: Development/Other
Requires: python-module-mate = %{version}-%{release}
Requires: mate-conf >= %{mate_conf_version}

Obsoletes: 		mate-python2-mateconf
Provides:  		python-mate-mateconf

%description -n python-module-mate-mateconf
This module contains a wrapper that allows the use of MateConf via Python.

%package -n python-module-mate-matevfs
Summary: Python bindings for interacting with mate-vfs
Group: Development/Other
Requires: python-module-mate = %{version}-%{release}
Requires: mate-vfs >= %{mate_vfs_version}
Requires: libmatecomponent >= %{libmatecomponent_version}

Obsoletes: 		mate-python2-matevfs
Provides:  		python-mate-matevfs

%description -n python-module-mate-matevfs
This module contains a wrapper that allows the use of gnome-vfs via python.

%package -n python-module-mate-devel
Summary: Development files for building add-on libraries
Group: Development/Other
Requires: python-module-mate = %{version}-%{release}

Obsoletes: 		mate-python2-devel
Provides:  		python-mate-devel

%description -n python-module-mate-devel
This package contains files required to build wrappers for MATE add-on
libraries so that they interoperate with mate-python2.

%prep
%setup -q -n %{oldname}-%{version}

NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
#find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;



%files
%doc AUTHORS ChangeLog NEWS
%dir %{python_sitelibdir}/gtk-2.0/mate/
%dir %{_datadir}/pygtk/2.0/defs
%dir %{_datadir}/pygtk/2.0/argtypes
%{_libdir}/mate-vfs-2.0/modules/libpythonmethod.la
%{_libdir}/python2.7/site-packages/gtk-2.0/mate/_mate.la
%{_libdir}/python2.7/site-packages/gtk-2.0/mate/ui.la
%{_libdir}/python2.7/site-packages/gtk-2.0/matecanvas.la
%{_libdir}/python2.7/site-packages/gtk-2.0/matecomponent/_matecomponent.la
%{_libdir}/python2.7/site-packages/gtk-2.0/matecomponent/activation.la
%{_libdir}/python2.7/site-packages/gtk-2.0/matecomponent/ui.la
%{_libdir}/python2.7/site-packages/gtk-2.0/mateconf.la




%files -n python-module-mate-mate
%{python_sitelibdir}/gtk-2.0/mate/__init__.*
%{python_sitelibdir}/gtk-2.0/mate/_mate.so
%{python_sitelibdir}/gtk-2.0/mate/ui.so
%{_datadir}/pygtk/2.0/defs/mate/mate.defs
%{_datadir}/pygtk/2.0/defs/mate/mate-types.defs
%{_datadir}/pygtk/2.0/defs/mate/ui.defs

%files -n python-module-mate-canvas
%dir %{python_sitelibdir}/gtk-2.0/mate/
%{python_sitelibdir}/gtk-2.0/mate/__init__.*
%{python_sitelibdir}/gtk-2.0/mate/canvas.*
%{python_sitelibdir}/gtk-2.0/matecanvas.so
%{_datadir}/pygtk/2.0/defs/mate/canvas.defs
%defattr(644,root,root,755)
%doc examples/canvas/*

%files -n python-module-mate-matecomponent
%dir %{python_sitelibdir}/gtk-2.0/matecomponent/
%{python_sitelibdir}/gtk-2.0/matecomponent/__init__.*
%{python_sitelibdir}/gtk-2.0/matecomponent/*.so
%{_datadir}/pygtk/2.0/defs/matecomponent*.defs
%{_datadir}/pygtk/2.0/argtypes/matecomponent*
%defattr(644,root,root,755)
%doc examples/matecomponent/*


%files -n python-module-mate-mateconf
%{python_sitelibdir}/gtk-2.0/mateconf.so
%{_datadir}/pygtk/2.0/defs/mateconf.defs
%{_datadir}/pygtk/2.0/argtypes/mateconf*
%defattr(644,root,root,755)
%doc examples/mateconf/*

%files -n python-module-mate-matevfs
%{python_sitelibdir}/gtk-2.0/matevfs
%{python_sitelibdir}/gtk-2.0/mate/vfs*
%{_libdir}/mate-vfs-2.0/modules/libpythonmethod.so
%doc %{_datadir}/gtk-doc/html/pymatevfs
%defattr(644,root,root,755)
%doc examples/vfs/*

%files -n python-module-mate-devel
%{_includedir}/mate-python-2.0
%{_libdir}/pkgconfig/mate-python-2.0.pc

%changelog
* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1.1
- Build for Sisyphus

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1
- Build for Sisyphus

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_3
- 20120622 mate snapshot

* Wed May 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3
- converted by srpmconvert script

