Name: catfish
Version: 0.3.2
Release: alt2.1
Summary: A handy file search tool

Group: File tools
License: GPLv2+
Url: http://software.twotoasts.de/index.php?/pages/catfish_summary.html
Source0: http://software.twotoasts.de/media/%name/%name-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>
BuildArch: noarch

BuildRequires: gettext
# search engine
Requires: %_bindir/locate
Requires: %_bindir/find
Requires: gnome-icon-theme
Requires: python-module-pygtk-libglade

%define _python_req_method normal

%description
A handy file search tool using different backends which is
configurable via the command line.

This program acts as a frontend for different file search engines.
The interface is intentionally lightweight and simple. But it takes
configuration options from the command line.

# TODO invent something (e. g. %name-<engine> packages)
#package engines
#Summary: Metapackage to install all supported engines
#Group: Applications/File
#License: GPLv2+

#Requires: %name = %version-%release
#Requires:	beagle
#Requires: doodle
#Requires: pinot
#Requires: strigi
#Requires: tracker

#%description engines
#This is a metapackage to install all engines supported by %name.

%prep
%setup -q -n %name-%version
# Fix up permissions...
chmod 0644 po/* [A-Z]* catfish*

%build
# Some configulation changes
#
# msgfmt is fixed.
# Linking is still broken...
sed -i.misc \
	-e '/svg/s|install|install -m 644|' \
	-e '/glade/s|install| install -m 644|' \
	-e 's|install |install -p |' \
	-e 's|pyc|py|' \
	-e 's|^\([ \t]*\)ln |\1: ln |' \
	-e 's|cp -rf|cp -prf|' \
	Makefile.in

sed -i.byte \
	-e 's|pyc|py|' \
	%name.in

sed -i.engine \
	-e 's|Nautilus|nautilus|' \
	%name.py

# This configure accepts only the option --prefix
# and does not accept --libdir= option
./configure --prefix=%prefix

%install

#__make install DESTDIR=%buildroot
%makeinstall DESTDIR=%buildroot

install -D %name.desktop %buildroot/%_desktopdir/%name.desktop

# Remove all unnecessary documentation
rm -rf %buildroot%_datadir/doc/%name

# and.. manually link..
ln -s -f ../icons/hicolor/scalable/apps/%name.svg %buildroot%_datadir/%name/
ln -s -f ../locale/ %buildroot%_datadir/%name/

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING README TODO

%_bindir/%name
%_desktopdir/%name.desktop
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/icons/hicolor/scalable/apps/%name.svg

#files engines
%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 0.3.2-alt2
- Add requirement python-module-pygtk-libglade (closes: 25231)

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.1
- Rebuilt with python 2.6

* Mon Jun 01 2009 Fr. Br. George <george@altlinux.ru> 0.3.2-alt1
- Initial build from FC

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.2-2
- GTK icon cache updating script update

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com>
- Rebuild for Python 2.6

* Tue Oct 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3.2-1
- 0.3.2

* Thu Oct 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-1
- 0.3

* Fri Oct  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.3.c
- Remove beagle dependency for now because beagle is not
  available on ppc64 (although catfish itself is noarch :( )

* Wed Oct  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.2.c
- License update
- Create sub-metapackage to install all supported search engines
- Remove redhat-artwork dependency

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.c
- 0.3c

* Tue May 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.b
- 0.3b

* Wed Apr  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.a
- 0.3a

* Wed Feb 28 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2.2-1
- 0.2.2

* Sun Feb 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2.1-1
- 0.2.1

* Wed Feb 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2stable-1
- 0.2

* Wed Jan 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2d-1
- 0.2d

* Mon Jan 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2c-1
- 0.2c

* Sun Jan 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2b-1
- Upstream rename: search4files -> catfish
- Remove the dependencies for beagle, nautilus,
  replace with redhat-artwork

* Mon Jan  1 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2a-1
- 0.2a

* Sat Dec 23 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Require pyxdg again (fc7)

* Wed Dec 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1e-1
- 0.1e

* Thu Dec 14 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1d-1
- 0.1d
- Disable pyxdg support on devel for now.

* Sat Dec  8 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1c-2
- Fix type typo

* Fri Dec  8 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1c-1
- Initial packaging to import to Fedora Extras.
