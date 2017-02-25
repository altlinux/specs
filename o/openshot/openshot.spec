%def_disable snapshot
%define ver_major 2.2

Name: openshot
Version: %ver_major.0
Release: alt1

Summary: Non Linear Video Editor using Python and MLT
Group: Video
License: GPLv3
Url: http://www.openshotvideo.com/

%if_disabled snapshot
Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-qt-%version.tar.gz
%else
# bzr branch lp:openshot/2.0
Source: %name-%version.tar.gz
%endif

BuildArch: noarch

Requires: python3-module-%name >= 0.1.3
Requires: blender inkscape

# should be self-satisfied
%add_python3_req_skip classes classes.legacy.openshot.classes images
# should be provided by blender
%add_python3_req_skip bpy.props

%define __python %nil
BuildRequires: rpm-build-python3 python3-devel python3-module-setuptools

%description
OpenShot Video Editor is a free, open-source, non-linear video editor. It
can create and edit videos and movies using many popular video, audio,
and image formats. Create videos for YouTube, Flickr, Vimeo, Metacafe,
Xbox, and many more common formats.

%prep
%setup -D -c -n %name-qt-%version

%build
%python3_build

%install
%python3_install

#%find_lang --with-qt %name OpenShot
#-f OpenShot.lang

%files
%_bindir/*
%python3_sitelibdir_noarch/%{name}_qt/
%python3_sitelibdir_noarch/*.egg-info/
%_pixmapsdir/*
%_desktopdir/*
%_datadir/mime/packages/*
%doc AUTHORS README

%changelog
* Thu Jan 26 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0 (qt5)

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.alpha1.bzr20131031
- Version 1.4.4~alpha1

* Tue Oct 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.3-alt1
- New version

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
