Name: PsychoPy
Version: 1.78.01
Release: alt1
Summary: Psychophysics toolkit for Python
Url: http://www.psychopy.org
Source: %name-%version.zip
Group: Sciences/Other
License: GPLv3+
BuildArch: noarch

%setup_python_module psychopy
%add_python_req_skip AppKit Quartz pyHook
# TODO device-specific:
## https://github.com/labjack/LabJackPython
## https://github.com/cedrus-opensource/pyxid
## pylink ?
%add_python_req_skip pylabjack pylink

# optimized out: dvipng fontconfig libgdk-pixbuf libwayland-client libwayland-server python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-beaker python-module-dateutil python-module-distribute python-module-docutils python-module-genshi python-module-html5lib python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-mako python-module-matplotlib python-module-mpmath python-module-nose python-module-nss python-module-numpy python-module-numpy-testing python-module-protobuf python-module-py python-module-pyExcelerator python-module-pyglet python-module-pytz python-module-simplejson python-module-sympy python-module-whoosh python-module-xlwt python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-tkinter python-modules-unittest t1lib tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended
BuildRequires: ImageMagick-tools ctags openssl python-module-OpenGL python-module-imaging python-module-pygame python-module-scipy python-module-sphinx python-module-wx python-modules-json time unzip

BuildRequires: python2.7(setuptools) texlive-latex-recommended

# This cannot be found
Requires: python-module-imaging python-module-pygame

%description
PsychoPy uses OpenGL and Python to create a toolkit for running
psychology/neuroscience/psychophysics experiments

%package -n %packagename
Group: Development/Python
Summary: Supplemental python module for %name, psychophysics toolkit

%description -n %packagename
Supplemental python module for %name.
PsychoPy uses OpenGL and Python to create a toolkit for running
psychology/neuroscience/psychophysics experiments

%prep
%setup

for N in 16 32 48 64 128 192 256; do
	convert psychopy/app/Resources/psychopy.png $N.png
done

cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Version=1.0
Name=%name
GenericName=Psychophysics toolkit
Comment=%Psychophysics toolkit for Python
Exec=psychopyApp.py
Icon=%name
Terminal=false
Categories=Science;Humanities;
@@@

%build
%python_build
PYTHONPATH=`pwd`/build/lib sphinx-build docs/source HTML

%install
%python_install
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for N in *.png; do
	S=${N%%.*}
	install -D $N %buildroot%_iconsdir/hicolor/${S}x${S}/%name.png
done

%files
# TODO check if this must reside at specific place
%doc HTML
%_bindir/*
%_iconsdir/hicolor/*/*
%_desktopdir/*

%files -n %packagename
%python_sitelibdir_noarch/%modulename
%python_sitelibdir_noarch/%name-*

%changelog
* Wed Sep 11 2013 Fr. Br. George <george@altlinux.ru> 1.78.01-alt1
- Autobuild version bump to 1.78.01
- Add desktop file
- Generate documentation

* Wed Sep 11 2013 Fr. Br. George <george@altlinux.ru> 1.78.00-alt1
- Initial build for ALT

