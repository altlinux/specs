BuildRequires: desktop-file-utils
Name: gtknetcat
Version: 0.1
Release: alt2.qa1.1

Summary: GtkNetCat is a GUI frontend for the old UNIX command nc (netcat).
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz
BuildArch: noarch

Requires: python-module-%name = %version-%release

# Automatically added by buildreq on Fri Jul 18 2008
BuildRequires: intltool python-devel glib2-devel

%description
GtkNetCat is a GUI frontend for the old UNIX command nc (netcat).
This tool can be used to transfer files to another computer via direct wired connection.

%package -n python-module-%name
Summary: Python module of GtkNetCat
Group: Development/Python
BuildArch: noarch
%_python_set_noarch

%description -n python-module-%name
GtkNetCat is a GUI frontend for the old UNIX command nc (netcat).
This tool can be used to transfer files to another computer via direct wired connection.

This package contains python module of GtkNetCat.

%prep
%setup

%build
intltoolize --force
aclocal
automake -fca
autoconf
%configure

%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=FileTransfer \
	%buildroot%_desktopdir/gtknetcat.desktop

%files -f %name.lang
%doc ChangeLog INSTALL README
%_bindir/*
%_desktopdir/*
%_libexecdir/*.py
%_datadir/%name

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.qa1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.1-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gtknetcat

* Thu Mar 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Exatracted python module into separate package

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1.1
- Rebuilt with python 2.6

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for gtknetcat

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
