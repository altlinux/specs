Summary: Non Linear Video Editor using Python and MLT
Name: openshot
Version: 1.4.2
Release: alt3
Source: %name-%version.tar.gz
License: GPLv3
Group: Video
Url: http://www.openshotvideo.com/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Patch: openshot-1.4.2-fix-dialog.patch

Requires: mlt-utils python-module-pygtk-libglade python-module-httplib2

# Automatically added by buildreq on Mon Jan 11 2010
BuildRequires: python-devel rpm-build-python

%description
OpenShot Video Editor is a free, open-source, non-linear video editor, based on Python, GTK, and MLT.
It can edit video and audio files, composite and transition video files, and mix multiple layers of
video and audio together and render the output in many different formats.

%prep
%setup -q
%patch -p1

%build
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --install-lib=%python_sitelibdir

%files
%doc AUTHORS COPYING README
%_bindir/*
%python_sitelibdir/%name
%python_sitelibdir/*.egg-info

%_man1dir/*
%_pixmapsdir/*
#%_miconsdir/*
#%_liconsdir/*
#%_niconsdir/*
%_desktopdir/*
%_datadir/mime/packages/*

%changelog
* Mon Apr 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt3
- Rebuild with Blender

* Mon Mar 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt2
- Add patch openshot-1.4.2-fix-dialog.patch for fix (ALT #25659) thanks serpiph@

* Tue Feb 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt1
- New version (bugfix release)

* Mon Jan 30 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.1-alt1
- New version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty at altlinux.ru> 1.4.0-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.0-alt1
- New version

* Tue May 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.1-alt1
- New version

* Sun Feb 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt1
- New version

* Wed Sep 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.2-alt1
- New version
- Close (ALT #24125)

* Mon Apr 19 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.3-alt1
- New version

* Tue Mar 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.1-alt1
- New version

* Tue Jan 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- Build for ALT
