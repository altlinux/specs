Name: imgv
Version: 3.1.6
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A cross-platform feature rich image viewer
License: GPLv2
Group: Graphics

Url: http://imgv.sourceforge.net/
Source: http://download.sourceforge.net/imgv/imgv-%version-src.tar.gz

BuildArch: noarch

%description
A cross-platform feature rich image viewer. Features include a file browser,
slideshows, zooming, rotating, on-the-fly Exif viewing, histograms, fullscreen
support, wallpaper setting, the ability to view 4 images on the screen at once,
adjustable thumbnail sizes, playlists, view and download images from Web sites,
movie playing, file searching/filtering, multiple directory loading,
transitional effects, image hiding and more.

%prep
%setup

%build

%install
install -d %buildroot{%_bindir,%_datadir/imgv/data}
install *.py %buildroot%_datadir/imgv/

install -m644 data/{imgv.conf,*.jpg,*.png,*.ttf} %buildroot%_datadir/imgv/data/

rm -f %buildroot%_datadir/imgv/setup.py

cat <<EOF >%buildroot%_bindir/imgv
#!/bin/sh
export IMGV_HOME=%_datadir/imgv
python %_datadir/imgv/imgv.py
EOF
chmod 755 %buildroot%_bindir/imgv

# Avoid bytecompile :)
unset RPM_PYTHON

%files
%_bindir/*
%_datadir/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.6-alt1.1
- Rebuild with Python-2.7

* Mon Sep 13 2010 Victor Forsiuk <force@altlinux.org> 3.1.6-alt1
- 3.1.6

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt2.1
- Rebuilt with python 2.6

* Tue Feb 26 2008 Victor Forsyuk <force@altlinux.org> 3.1-alt2
- Fix underinstalling. :)
- This is noarch package!
- Fix wrong Group.

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.1-alt1.1
- Rebuilt with python-2.5.

* Tue Jun 13 2006 Victor Forsyuk <force@altlinux.ru> 3.1-alt1
- Initial build.
