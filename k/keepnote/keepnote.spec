Name: keepnote
Version: 0.7.8
Release: alt2

Summary: KeepNote is a note taking application
License: GPLv2
Group: Office

Url: http://keepnote.org
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-pygtk python-module-pygtk-libglade
BuildRequires: libgtk+2-devel python-modules-sqlite3
# optional
BuildRequires: python-module-pygnome-extras-devel

Requires: python-modules-sqlite3 python-module-pygtk-libglade

%description
KeepNote is a note taking application. With KeepNote, you can store your
class notes, TODO lists, research notes, journal entries, paper
outlines, etc in a simple notebook hierarchy with rich-text formatting,
images, and more. Using full-text search, you can retrieve any note for
later reference.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc CHANGES COPYING INSTALL LICENSE README README.translations.txt
%_bindir/*
%python_sitelibdir/%name/
%_liconsdir/*
%_desktopdir/%name.desktop


%changelog
* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.8-alt2
- Added necessary requirements

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.8-alt1
- Version 0.7.8

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt0.1.1
- Rebuild with Python-2.7

* Thu Feb 17 2011 Alexey Morsov <swi@altlinux.ru> 0.7-alt0.1
- initial build


