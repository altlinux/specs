Name: pyrenamer
Version: 0.6.0
Release: alt2.1

Summary: Mass rename files for the GNOME desktop
Group: File tools
License: GPLv2
Url: http://www.infinicode.org/code/pyrenamer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch: noarch
Source: http://www.infinicode.org/code/pyrenamer/files/pyrenamer-0.6.0.tar.gz

BuildRequires(pre): rpm-build-python rpm-build-gnome
BuildPreReq: python-devel python-module-pygtk-devel python-module-eyeD3
BuildPreReq: GConf libGConf-devel intltool

Requires: python-module-%name = %version-%release

%description
With pyRenamer you can change the name of several files at the same time
easily.

- You can use patterns to rename files.
- You can use search & replace to rename files.
- You can use common substitutions.
- You can manually rename selected files.
- You can rename images using their metadata.
- You can rename music using its metadata.

It is written using PyGTK for the GNOME desktop, altought it will work
in any PyGTK enabled environment (KDE, XFCE, even Windows), and it's
licensed under the GPL.

%package -n python-module-%name
Summary: Python module of pyRenamer
Group: Development/Python
BuildArch: noarch
%_python_set_noarch

%description -n python-module-%name
With pyRenamer you can change the name of several files at the same time
easily.

This package contains python module of pyRenamer.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

install -d %buildroot%_liconsdir
ln -s %_datadir/%name/%name.svg %buildroot%_liconsdir

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/*.py
%_bindir/*
%_datadir/applications/*
%_datadir/%name
%_liconsdir/*.svg
%_man1dir/*
%gconf_schemasdir/*

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Fixed desktop file

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus (ALT #23841)

