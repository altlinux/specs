Name: renpy
Version: 6.12.2
Release: alt1.1.1
Summary: A visual novel engine
Group: Games/Adventure
License: LGPL
Source: %name-%version-source.tar.bz2
Url: http://www.renpy.org/

Patch1: 00_module_setup.patch
Patch2: 01_abspaths.patch
Patch3: 02_traceback.patch
Patch4: 03_checkdir.patch
Patch5: 04_editor.patch

%setup_python_module %name

%define gamedir %_gamesdatadir/%name

Requires: %packagename = %version
# Automatically added by buildreq on Tue Jul 19 2011
# optimized out: fontconfig libGL-devel libGLU-devel libavcodec-devel libavcore-devel libavutil-devel python-base python-devel python-modules python-modules-compiler python-modules-email python-modules-encodings zlib-devel
BuildRequires: ImageMagick-tools libSDL-devel libavformat-devel libfreetype-devel libfribidi-devel libglew-devel libpng-devel libswscale-devel python-module-Cython python-module-pygame-devel time

BuildRequires: rpm-build-fonts

%description
Ren'Py is a visual novel engine that helps you use words, images, and
sounds to tell stories with the computer. These can be both visual
novels and life simulation games. The easy to learn script language
allows you to efficiently write large visual novels, while its Python
scripting is enough for complex simulation games.

Ren'Py is open source and free for commercial use. It supports Windows,
Mac OS X, Linux, and Android.

%package -n %packagename
Summary: Python module for %name, %summary
Group: Development/Python
%description -n %packagename
Python module for %name, %summary

%package tutorial
Summary: Tutorial demo for %name, %summary
Group: Games/Adventure
BuildArch: noarch
Requires: %name = %version
%description tutorial
Tutorial demo for %name, %summary

%package the_question
Summary: Example game for %name, %summary
Group: Games/Adventure
BuildArch: noarch
Requires: %name = %version
%description the_question
Example game for %name, %summary

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

touch $(find . -name \*.pyx)

%ifarch x86_64
sed -i "s/'', 'lib'/'', 'lib64'/g" module/setup.py
%endif

for s in 16 24 32 48 256; do
  convert launcher/logo.png -crop '200x200+0+0!' -resize ${s}x${s} $s.png
  convert tutorial/game/eileen_happy.png -crop '266x266+0+0!' -resize ${s}x${s} tutorial$s.png
  convert the_question/game/sylvie_normal.png -crop '391x391+0+0!' -resize ${s}x${s} the_question$s.png
done

for d in tutorial the_question ""; do
cat > %name-$d.sh <<@@@
#!/bin/sh
%_gamesbindir/%name %gamedir/$d
@@@

cat > %name$d.desktop <<@@@
[Desktop Entry]
Type=Application
Name=Ren'Py${d:+ $d game}
GenericName=Visual novel
Comment=visual novel game ${d:-engine}
Icon=%name${d:+-$d}
Exec=%name${d:+-$d}
Terminal=false
Categories=Game;AdventureGame;
@@@
done

# TODO: Do something with theme setup (now it tries to write at gamedir)

%build
export RENPY_DEPS_INSTALL="%prefix"
cd module
%python_build

%install
mkdir -p %buildroot%gamedir %buildroot%_gamesbindir
cp -a [^A-Zdm]* %buildroot/%gamedir/
chmod +x %buildroot/%gamedir/%name.py

for d in tutorial the_question ""; do
  test -z "$d" || install -m755 -D %name-$d.sh %buildroot%gamedir/%name-$d.sh
  install -D %name$d.desktop %buildroot%_desktopdir/%name${d:+-$d}.desktop
  for s in 256 48 32 24 16; do
    test -r $d$s.png &&
    install -D $d$s.png %buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name${d:+-$d}.png
  done
done

ln -s $(relative %gamedir/%name-tutorial.sh %_gamesbindir/%name-tutorial) \
                                  %buildroot%_gamesbindir/%name-tutorial
ln -s $(relative %gamedir/%name-the_question.sh %_gamesbindir/%name-the_question) \
                                      %buildroot%_gamesbindir/%name-the_question
ln -s $(relative %gamedir/%name.py %_gamesbindir/%name) \
                         %buildroot%_gamesbindir/%name
ln -s $(relative %_defaultdocdir/%name-%version %gamedir/doc) \
                                      %buildroot%gamedir/doc
for F in `find * -name DejaVuSans.ttf -o -name DejaVuSerif.ttf`; do
  ln -sf $(relative %_ttffontsdir/dejavu/$(basename $F) %gamedir/$F) \
                                                %buildroot%gamedir/$F
done

export RENPY_DEPS_INSTALL="%prefix"
cd module
%python_install

%files
%doc doc/*
%gamedir
%exclude %gamedir/tutorial
%exclude %gamedir/the_question
%_gamesbindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*

%files -n %packagename
%python_sitelibdir/%{name}*
%python_sitelibdir/_%{name}*
%python_sitelibdir/pysdlsound

%files tutorial
%_gamesbindir/%name-tutorial
%gamedir/tutorial
%_desktopdir/%name-tutorial.desktop
%_iconsdir/hicolor/*/apps/%name-tutorial.*

%files the_question
%_gamesbindir/%name-the_question
%gamedir/the_question
%_desktopdir/%name-the_question.desktop
%_iconsdir/hicolor/*/apps/%name-the_question.*

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 6.12.2-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 6.12.2-alt1.1
- Rebuild with Python-2.7

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 6.12.2-alt1
- Autobuild version bump to 6.12.2

* Wed Jul 20 2011 Fr. Br. George <george@altlinux.ru> 6.12.1-alt1
- Autobuild version bump to 6.12.1

* Tue Jul 19 2011 Fr. Br. George <george@altlinux.ru> 6.12.0-alt1
- Initial build from scratch

