Name: anki
Version: 1.2.8
Release: alt2
Summary: Flashcard program for using space repetition learning

Group: Games/Educational
License: GPLv3+ and MIT
Url: http://ankisrs.net/
Source0: %name-%version.tgz

Patch0: %name-1.2.8-noupdate.patch

BuildRequires: python-module-setuptools python-module-PyQt4-devel
BuildRequires: python-modules-sqlite3 python-module-SQLAlchemy
BuildRequires: desktop-file-utils python-module-simplejson

BuildArch: noarch

Requires: python-modules-sqlite3 python-module-matplotlib-qt4

%description
Anki is a program designed to help you remember facts (such as words
and phrases in a foreign language) as easily, quickly and efficiently
as possible. Anki is based on a theory called spaced repetition.

%prep
%setup
%patch0 -p1 -b .noupdate
%build
pushd lib%name
python setup.py build
popd
tools/build_ui.sh
python setup.py build

%install
pushd lib%name
python setup.py install -O1 --skip-build --root %buildroot
popd

python setup.py install -O1 --skip-build --root %buildroot

install -d %buildroot%_desktopdir
desktop-file-install --remove-category=KDE --dir %buildroot%_desktopdir %name.desktop

install -d %buildroot%_datadir/pixmaps
install -m 644 icons/%name.png %buildroot%_datadir/pixmaps/

%find_lang %name

%files -f %name.lang
# libankiqt
%python_sitelibdir/ankiqt

# libanki
%python_sitelibdir/%name

%python_sitelibdir/*egg-info
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/pixmaps/%name.png

%doc COPYING CREDITS README*

%changelog
* Wed May  9 2012 Terechkov Evgenii <evg@altlinux.org> 1.2.8-alt2
- Fix ALT#27312

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8-alt1.1
- Rebuild with Python-2.7

* Sun May 29 2011 Terechkov Evgenii <evg@altlinux.org> 1.2.8-alt1
- 1.2.8 (ALT #25680)

* Wed Dec  1 2010 Terechkov Evgenii <evg@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Jun 28 2010 Terechkov Evgenii <evg@altlinux.ru> 0.9.9.8.6-alt2
- Buildreqs updated
- Requires added to fix installing

* Mon Feb 22 2010 Evgenii Terechkov <evg@altlinux.ru> 0.9.9.8.6-alt1
- Initial build for ALT Linux Sisyphus (thanks to Fedora for initial spec)
