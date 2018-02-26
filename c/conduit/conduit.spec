# TODO
# - build extensions for nautilus, eog, totem
# - may be add support opensync (upstream?)
# webkit or xulrunner
%define webengine webkit

%define ver_major 0.3
%def_disable static
%add_python_req_skip hildon
%def_disable nautilus
%def_disable eog
%def_disable totem

Name: conduit
Version: %ver_major.17
Release: alt1.1
BuildArch: noarch

Summary: Synchronization solution for GNOME
License: GPLv2
Group: Communications
Url: http://www.conduit-project.org/
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar

# Use system python-gdata
Patch0: conduit-0.3.10-systemgdata.patch

Requires: python-module-gdata >= 1.1.0
BuildRequires: python-module-gdata >= 1.1.0

BuildPreReq: rpm-build-gnome
BuildRequires: gnome-doc-utils-xslt intltool python-devel python-module-dbus python-module-pygoocanvas python-module-pygtk python-module-vobject python-modules-encodings python-modules-sqlite3
%if %webengine == webkit
BuildRequires: python-module-pywebkitgtk
%add_python_req_skip gtkmozembed
%else
BuildRequires: python-module-pygnome-gtkmozembed
%add_python_req_skip webkit
%endif

BuildRequires: gnome-doc-utils
BuildRequires: glib2-devel

%_python_set_noarch

%description
Conduit is a synchronization solution for GNOME which allows the user
to take their emails, files, bookmarks, and any other type of personal
information and synchronize that data with another computer, an online
service, or even another electronic device.

Conduit manages the synchronization and conversion of data into other
formats. For example, conduit allows you to synchronize your tomboy
notes to a file on a remote computer, synchronize your emails to your
mobile phone, synchronize your bookmarks to delicious, gmail, or even
your own webserver, and more.

%prep
%setup -q 
%patch0 -p1 -b .gdata

# correct start_conduit.py for the changes made above
perl -pi -e 's.\"GnomeVfs\".\"GIO\".' conduit/defs.py.in
%if %webengine == webkit
perl -pi -e 's.\"gtkmozembed\".\"webkit\".' conduit/defs.py.in
%endif

# get rid of any shebangs
for file in `find conduit/{dataproviders,hildonui,modules} -type f -print`; do
  sed -i '/#!/d' $file
done

# dataprovider files install to the wrong directory - fix that
find conduit/{dataproviders,modules} -type f -name Makefile.am | \
  xargs sed -i 's/\$(libdir)/$(pythondir)/'
sed -i 's/@MODULEDIR@/@PYTHONDIR@\/%{name}\/modules/' conduit/defs.py.in

%build
gnome-doc-prepare --copy --force
ACLOCAL="aclocal -I ./m4" %autoreconf
%configure \
%if_enabled nautilus
	--enable-nautilus-extension \
	--with-nautilus-extension-dir=%nautilus_extdir \
%endif
%if_enabled eog
	--enable-eog-plugin \
	--with-eog-plugin-dir=%_libdir/eog/plugins \
%endif
%if_enabled totem
	--enable-totem-plugin \
	--with-totem-plugin-dir=%_libdir/totem/plugins \
%endif
	--disable-scrollkeeper

%make

%install
%make_install install DESTDIR=%buildroot

# conduit wrapper is unneeded because we're using WebKig and not mozembed.
# also conduit wrapper no longer needed with Gecko 1.9/Firefox 3
(cd %buildroot%_bindir && mv conduit.real conduit)


# don't need devel package
rm -f %buildroot%_pkgconfigdir/%name.pc

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/*
%python_sitelibdir/%name
#_prefix/lib/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/dbus-1/services/org.%name.service
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.17-alt1.1
- Rebuild with Python-2.7

* Thu Jan 28 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3.17-alt1
- 0.3.17
- build as noarch

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.16-alt1.1
- Rebuilt with python 2.6

* Thu Aug 27 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.16-alt1
- 0.3.16
- change require python-module-pysqlite2 to python-modules-sqlite3

* Mon Jan 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.15-alt4
- remove obsoleted pre/post macros
- add python-module-pysqlite2 to Requires(#17765)

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.15-alt3
- changed web engine to webkit
- remove noarch

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.15-alt2
- cleanup spec
- fix changelog

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.15-alt1
- 0.3.15
- use gio instead of gnomevfs
- add post/postun scripts
- move modules from /usr/lib/conduit to pythondir/conduit

* Mon Sep 01 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.14-alt1
- 0.3.14
- use system google modules 

* Sun Aug 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.13.1-alt1
- initial build for ALTLinux

