Name: fontforge-doc
Version: 20070313
Release: alt1

Summary: FontForge documentation
Summary(ru_RU.KOI8-R): Документация к FontForge

License: GPL
Group: Publishing
Url: http://fontforge.sourceforge.net/

Packager: Pavel Vainerman <pv@altlinux.ru>

Source: http://dl.sf.net/fontforge/fontforge_htdocs-%version.tar.bz2

Conflicts: fontforge < 20061014-alt1

%description
FontForge documentation (html)

%description -l ru_RU.KOI8-R
Документация к FontForge (html)

%prep
%setup -q -c %name

%build

%install
mkdir -p %buildroot%_datadir/fontforge/
tar zxf cidmaps.tgz
mv *.cidmap %buildroot%_datadir/fontforge/

mkdir -p %buildroot%_docdir/fontforge/
cp -r * %buildroot%_docdir/fontforge/
rm -f %buildroot%_docdir/fontforge/cidmaps.tgz

%post

%postun

%files
%_docdir/fontforge/
%_datadir/fontforge/*.cidmap

%changelog
* Sat Mar 17 2007 Pavel Vainerman <pv@altlinux.ru> 20070313-alt1
- new version

* Sat Nov 11 2006 Pavel Vainerman <pv@altlinux.ru> 20061014-alt1
- new version

* Mon Mar 06 2006 Pavel Vainerman <pv@altlinux.ru> 20060114-alt0.1
- new version 20060114.20060114 (with rpmrb script)

* Sun Mar 05 2006 Pavel Vainerman <pv@altlinux.ru> 20050909-alt1
- first build for stand-alone doc package
