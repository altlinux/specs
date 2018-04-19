Name: anki2
Version: 2.0.50
Release: alt1
Summary: Flashcard program for using space repetition learning

Group: Games/Educational
License: GPLv3+ and MIT
Url: https://apps.ankiweb.net/
Source0: %name-%version.tar

Conflicts: anki < %version-%release

# Automatically added by buildreq on Wed Apr 18 2018 (-bb)
# optimized out: fontconfig libqt4-core libqt4-xml perl python-base python-modules python3 python3-base python3-module-mpl_toolkits python3-module-zope rpm-build-python3 shared-mime-info xz
BuildRequires: desktop-file-utils kdelibs libicu56 python-module-PyQt4 python3-module-yieldfrom rpm-build-gir selinux-policy xdg-utils

#BuildRequires: python-module-setuptools 
#BuildRequires: python-modules-sqlite3 python-module-SQLAlchemy
#BuildRequires: desktop-file-utils python-module-simplejson
#BuildRequires: python-module-pyaudio

BuildArch: noarch

Requires: python-modules-sqlite3 python-module-matplotlib-qt4

%description
Anki is a program designed to help you remember facts (such as words
and phrases in a foreign language) as easily, quickly and efficiently
as possible. Anki is based on a theory called spaced repetition.

%prep
%setup
%build
#pushd lib%name
#python setup.py build
#popd
tools/build_ui.sh
#python setup.py build

%install

mkdir -p %buildroot%_man1dir %buildroot/usr/share/applications
mkdir -p %buildroot/usr/local/bin %buildroot%_bindir

%make_install DESTDIR=%buildroot install
rm -f %buildroot/usr/share/anki/thirdparty/*/*.so
mv %buildroot/usr/local/bin/anki %buildroot%_bindir/anki

#pushd lib%name
#python setup.py install -O1 --skip-build --root %buildroot
#popd

#python setup.py install -O1 --skip-build --root %buildroot

install -d %buildroot%_desktopdir
desktop-file-install --remove-category=KDE --dir %buildroot%_desktopdir anki.desktop

install -d %buildroot%_datadir/pixmaps
install -m 644 designer/icons/anki.png %buildroot%_datadir/pixmaps/

%find_lang %name

%files -f %name.lang
# libankiqt
#%python_sitelibdir/ankiqt

# libanki
#%python_sitelibdir/anki

#%python_sitelibdir/*egg-info
%_bindir/anki
%_desktopdir/anki.desktop
%_datadir/pixmaps/anki.png
%_datadir/anki
%_man1dir/anki.*

%doc README* LICENSE LICENSE.logo

%changelog
* Tue Apr 17 2018 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt1
- first build for Sisyphus

