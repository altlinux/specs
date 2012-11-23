
Name: accerciser
Version: 3.6.2
Release: alt1

Summary: An interactive Python tool for querying accessibility information
Url: http://live.gnome.org/Accerciser
License: %bsd

Group: Accessibility
Packager: Michael Pozhidaev <msp@altlinux.ru>

# Automatically added by buildreq on Sun Sep 28 2008
BuildRequires: GConf docbook-dtds gnome-doc-utils-xslt perl-XML-Parser python-devel

BuildRequires: rpm-build-licenses rpm-build-gnome gnome-doc-utils libGConf-devel
BuildPreReq: intltool yelp yelp-tools libgio-devel libgtk+3-devel gconf-editor
BuildPreReq: python-module-pygobject3-devel libat-spi2-core-devel

BuildArch: noarch
Source: %name-%version.tar.gz
Source1: accerciser.schemas
Patch: accerciser-3.6.2-alt-config.patch

Requires: python-module-%name = %version-%release

%description
An interactive Python accessibility explorer.

%add_python_req_skip gtksourceview

%package -n python-module-%name
Summary: Python module for accerciser
Group: Development/Python
BuildArch: noarch
%_python_set_noarch

%description -n python-module-%name
An interactive Python accessibility explorer.

This package contains Python module for accerciser.

%prep
%setup
%patch -p2

%build
%autoreconf
%configure \
	--disable-scrollkeeper \
	--without-pyreqs \
	--with-help-dir=%gnome_helpdir/%name \
	--enable-schemas-compile=yes
%make_build

%install
%makeinstall_std

install -d %buildroot%gconf_schemasdir
install -p -m644 %SOURCE1 %buildroot%gconf_schemasdir/

%find_lang --with-gnome %name

%post
%gconf2_install accerciser

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall accerciser
fi

%files -f %name.lang
%doc AUTHORS README COPYING NEWS ChangeLog
%_bindir/*
%_datadir/%name
%_datadir/applications/*
%_man1dir/*
%gnome_helpdir/%name
%gconf_schemasdir/*
%_datadir/icons/hicolor/16x16/apps/%name.png
%_datadir/icons/hicolor/22x22/apps/%name.png
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/48x48/apps/accerciser.png
%_datadir/icons/hicolor/scalable/apps/accerciser.svg
#_omfdir/%name
%_datadir/locale/*/*/accerciser*
%_datadir/glib-2.0/schemas/*.xml

%files -n python-module-%name
%python_sitelibdir/%name/

%changelog
* Fri Nov 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Version 3.6.2 (ALT #28019)

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt1
- Version 1.9.3

* Thu Mar 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3
- Extracted python module into separate package

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.1
- Rebuilt with python 2.6

* Wed Oct 15 2008 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt2
- Fixed gconf schema installation

* Sun Sep 28 2008 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt1
- ALT Linux package

* Thu Apr 12 2007 Peter Parente <parente@cs.unc.edu>
- Added gconf schema install, uninstall, and files

* Mon Apr 02 2007 Peter Parente <parente@cs.unc.edu>
- Added without-pyreqs flag to avoid checking for modules at rpmbuild time
- Added locales to files section

* Wed Feb 22 2007 Peter Parente <parente@cs.unc.edu>
- First release
