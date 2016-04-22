Name: PsychoPy
Version: 1.83.04
Release: alt1
Summary: Psychophysics toolkit for Python
Url: http://www.psychopy.org
Source: %name-%version.zip
Group: Sciences/Other
License: GPLv3+
BuildArch: noarch

%setup_python_module psychopy
%add_python_req_skip AppKit Quartz pyHook CoreFoundation objc
# TODO device-specific:
## https://github.com/labjack/LabJackPython
## https://github.com/cedrus-opensource/pyxid
## pylink ?
## textgrid is internal module
%add_python_req_skip pylabjack pylink textgrid
%add_python_req_skip moviepy

# optimized out: dvipng fontconfig libgdk-pixbuf libwayland-client libwayland-server python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-beaker python-module-dateutil python-module-distribute python-module-docutils python-module-genshi python-module-html5lib python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-mako python-module-matplotlib python-module-mpmath python-module-nose python-module-nss python-module-numpy python-module-numpy-testing python-module-protobuf python-module-py python-module-pyExcelerator python-module-pyglet python-module-pytz python-module-simplejson python-module-sympy python-module-whoosh python-module-xlwt python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-tkinter python-modules-unittest t1lib tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended
BuildRequires: ImageMagick-tools ctags openssl python-module-OpenGL python-module-imaging python-module-pygame python-module-scipy python-module-sphinx python-module-wx3.0 python-modules-json time unzip xvfb-run

BuildRequires: python2.7(setuptools) texlive-latex-recommended

%description
PsychoPy uses OpenGL and Python to create a toolkit for running
psychology/neuroscience/psychophysics experiments

%package -n %packagename
Group: Development/Python
Summary: Supplemental python module for %name, psychophysics toolkit

# This cannot be found or properly selected
Requires: python-module-imaging python-module-pygame python-module-wx3.0

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
Comment=Psychophysics toolkit for Python
Exec=psychopyApp.py
Icon=%name
Terminal=false
Categories=Science;Humanities;
@@@

%build
%python_build
#PYTHONPATH=`pwd`/build/lib xvfb-run sphinx-build docs/source HTML

%install
%python_install
ln -s psychopyApp.py %buildroot%_bindir/%name
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for N in *.png; do
	S=${N%%.*}
	install -D $N %buildroot%_iconsdir/hicolor/${S}x${S}/%name.png
done

%files
# TODO check if this must reside at specific place
#%doc HTML
%_bindir/*
%_iconsdir/hicolor/*/*
%_desktopdir/*

%files -n %packagename
%python_sitelibdir_noarch/*
%exclude %python_sitelibdir_noarch/*/tests
%exclude %python_sitelibdir_noarch/*/demos

%changelog
* Thu Apr 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.83.04-alt1
- 1.83.04
- built with wx3.0

* Mon Feb 16 2015 Fr. Br. George <george@altlinux.ru> 1.82.01-alt1
- Autobuild version bump to 1.82.01
- Eliminate wxpython2.8

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 1.82.00-alt1
- Autobuild version bump to 1.82.00

* Wed Oct 29 2014 Fr. Br. George <george@altlinux.ru> 1.81.01-alt1
- Autobuild version bump to 1.81.01
- Wipe Mac requirements

* Thu Oct 23 2014 Fr. Br. George <george@altlinux.ru> 1.81.00-alt1
- Autobuild version bump to 1.81.00
- Add xvfb-run for fake X11

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 1.80.07-alt1
- Autobuild version bump to 1.80.07

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 1.80.04-alt1
- Autobuild version bump to 1.80.04

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1.80.01-alt1
- Autobuild version bump to 1.80.01
- Fix requierments

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 1.79.01-alt1
- Autobuild version bump to 1.79.01

* Wed Sep 11 2013 Fr. Br. George <george@altlinux.ru> 1.78.01-alt1
- Autobuild version bump to 1.78.01
- Add desktop file
- Generate documentation

* Wed Sep 11 2013 Fr. Br. George <george@altlinux.ru> 1.78.00-alt1
- Initial build for ALT

