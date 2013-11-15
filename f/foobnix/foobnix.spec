%define branch 2.6.10

Name: foobnix
Version: %{branch}q
Release: alt1

Summary: Music player written in Python, GTK+
License: GPLv3
Group: Sound

Url: http://www.foobnix.com
Packager: Alexey Morsov <swi@altlinux.ru>
BuildArch: noarch

Requires: python-module-keybinder

Source: %{name}_%{version}.tar.gz

Patch0: foobnix_2.6.10-MO_DIR.diff

BuildPreReq: %py_dependencies setuptools

# Automatically added by buildreq on Fri Nov 15 2013 (-bi)
# optimized out: python-base python-devel python-modules python-modules-encodings
BuildRequires: desktop-file-utils python-module-distribute rpm-build-gir

%description
Music player written in Python, GTK+
Support:
 - Library of multiple choice directories with music
 - Support all formats of gstreamer
 - Scrobbler music on last.fm
 - Display lyrics
 - Support for CUE (also wv, iso.wv) is the best under Linux (zavlab)
 - Video Playback
 - Find any audio information Vkontakte and her audition

More (see at %url )

%prep
%setup -n %name
%patch0 -p1

%build
%python_build

%install
python setup.py install --root=%{buildroot}

%files
%_bindir/%name
%_datadir/%name
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_pixmapsdir/*
%_man1dir/*
%_desktopdir/*
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info

%changelog
* Fri Nov 15 2013 Motsyo Gennadi <drool@altlinux.ru> 2.6.10q-alt1
- 2.6.10q

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3.1-alt1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.3.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for foobnix

* Thu Jan 06 2011 Alexey Morsov <swi@altlinux.ru> 0.2.3.1-alt1
- git from 2010-01-06

* Thu Dec 30 2010 Alexey Morsov <swi@altlinux.ru> 0.2.3-alt1
- initial build for Sisyphus

