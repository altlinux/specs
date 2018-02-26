Name: foobnix
Version: 0.2.3.1
Release: alt1.qa1.1

Summary: Music player written in Python, GTK+
License: GPLv3
Group: Sound

Url: http://www.foobnix.com
Packager: Alexey Morsov <swi@altlinux.ru>
BuildArch: noarch

Requires: python-module-keybinder

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools
BuildRequires: desktop-file-utils

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
%setup

%build
pushd src
%python_build

%install
pushd src
python setup.py install --root=%{buildroot}
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Audio \
	--add-category=Player \
	%buildroot%_desktopdir/foobnix.desktop

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

