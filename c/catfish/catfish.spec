Name: catfish
Version: 1.0.2
Release: alt1
Summary: A handy file search tool

Group: File tools
License: GPLv2+
Url: http://www.twotoasts.de/index.php/catfish/
Source: %name-%version.tar.bz2
BuildArch: noarch

BuildRequires: intltool
# search engine
Requires: %_bindir/locate
Requires: %_bindir/find
# This is dirty icon hack
Requires: gnome-icon-theme-symbolic

#define _python_req_method normal

# Automatically added by buildreq on Thu Oct 10 2013
# optimized out: at-spi2-atk fontconfig gobject-introspection libat-spi2-core libatk-gir libcairo-gobject libgdk-pixbuf libgdk-pixbuf-gir libpango-gir libwayland-client libwayland-cursor libwayland-server python-base python-module-pygobject3 python-modules python-modules-compiler python-modules-email python-modules-logging python-modules-xml
BuildRequires: libgtk+3-gir python-module-PyXML python-module-distribute python-module-zeitgeist2.0

%description
A handy file search tool using different backends which is
configurable via the command line.

This program acts as a frontend for different file search engines.
The interface is intentionally lightweight and simple. But it takes
configuration options from the command line.

%define symicons %_datadir/%name/data/icons/gnome

%prep
%setup -n %name-%version
# This is dirty icon hack
sed -i '/Gtk.IconTheme.get_default/{
p
s@ *=.*@.append_search_path("%symicons")@
}' catfish/CatfishWindow.py

%build
# This configure accepts only the option --prefix
# and does not accept --libdir= option
./configure --prefix=%prefix

%install
%makeinstall DESTDIR=%buildroot
rm -rf %buildroot%_defaultdocdir/%name

install -D %name.desktop %buildroot/%_desktopdir/%name.desktop

# This is dirty icon hack
mkdir -p %buildroot/%symicons && ln -s %_iconsdir/gnome %buildroot/%symicons/hicolor

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING README TODO

%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/icons/hicolor/scalable/apps/%name.svg

#files engines
%changelog
* Wed Apr 16 2014 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Thu Oct 10 2013 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Autobuild version bump to 0.8.2
- Mass upstream version update
- Catch icon_not_found exception again

* Wed May 29 2013 Fr. Br. George <george@altlinux.ru> 0.3.2-alt3
- Catch icon_not_found exception (Closes: 26027)

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
