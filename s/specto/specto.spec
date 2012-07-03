%define _python_req_skip "indicate"

Name: specto
Version: 0.4.1
Release: alt1

Summary: A desktop application that will watch configurable events
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://%name.sourceforge.net/

Source: http://%name.googlecode.com/files/%name-%version.tar.gz
Patch: %name-0.4.1-alt-ru.po.patch

BuildArch: noarch

BuildRequires: python-devel rpm-build-python intltool

%description
Specto is a desktop application that watches configurable events (such
as website updates, emails, file and folder changes, system processes,
etc) and then trigger notifications.

Specto can watch a website for updates and notify you when there is
activity (otherwise, Specto will just stay out of the way). This changes
the way you work, because you can be informed of events instead of
having to look out for them.

%define pkgdocdir %_docdir/%name-%version

%prep
%setup -q
%patch

# move docs in proper location
subst 's|share/doc/%name|share/doc/%name-%version|g' setup.py spectlib/util.py

%build
%python_build

%install
%python_install

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/*
%python_sitelibdir/*
%doc %pkgdocdir

%exclude %_datadir/indicators/messages/applications/specto

%changelog
* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.1
- Rebuild with Python-2.7

* Fri Feb 12 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- first build for Sisyphus

