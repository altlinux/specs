Name: qmtcc
Version: 0.0.1
Release: alt4.1

Summary: Qt based graphical frontend to multitran dictionary
License: GPL
Group: System/Internationalization

Url: http://www.altlinux.org
Source0: %name-%{version}alpha1.tar.bz2
Source1: qmtcc.desktop
Patch0: qmtcc-0.0.1-alt-DSO.patch

Requires: multitran-dict
Requires: libmtquery >= 0.0.1-alt3
BuildRequires: libmtquery-devel >= 0.0.1-alt3
BuildRequires: libbtree-devel libfacet-devel libmtsupport-devel

# Automatically added by buildreq on Sat Oct 09 2010
BuildRequires: gcc-c++ libmtquery-devel libqt3-devel

%description
Qt based graphical frontend to multitran dictionary

%prep
%setup -n %name-%{version}alpha1
%patch0 -p2

%build
pushd src
%_libdir/qt3/bin/qmake
%make_build
popd

%install
pushd src
install -Dpm755 %name %buildroot%_bindir/%name
ln -s %name %buildroot%_bindir/multitran
popd
install -Dpm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%doc AUTHORS README
%_bindir/*
%_desktopdir/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt4.1
- Fixed build

* Sat Oct 09 2010 Michael Shigorin <mike@altlinux.org> 0.0.1-alt4
- added desktop file and "multitran" symlink (closes: #8317)
- buildreq

* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt3
- fixed case sensitivity
- fixed xkb binding

* Tue Feb 15 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt2
- avoid running of qmake, 'cause this util cannot work in hasher

* Tue Jan 25 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt1
- initial build
