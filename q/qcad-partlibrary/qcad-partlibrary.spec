%define oname partlibrary
Name: qcad-partlibrary
Version: 2.1.2.8
Release: alt1

Summary: QCad part library
Summary(ru_RU.KOI8-R): Библиотека компонентов для QCad

License: Distributable
Group: Graphics
Url: http://www.ribbonsoft.com/qcad_library.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

%define pldir %_datadir/qcad/partlibrary

Buildarch: noarch
#Source: %name-%version.tar.bz2
Source: http://www.ribbonsoft.com/download.php?file=/archives/partlibrary/%oname-%version-1.tar.bz2
Requires: qcad

%description
The QCad part library is a collection of CAD files that can be used
from the library browser of QCad. These are typically drawings
of small parts that are often used in drawings (such as screws or nuts).

%prep
%setup -q -n %oname-%version-1

%install
mkdir -p %buildroot%pldir/
cp -rf * %buildroot%pldir/

%files
%pldir/

%changelog
* Tue Jul 03 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1.2.8-alt1
- new version 2.1.2.8 (with rpmrb script)
- move to datadir

* Wed Dec 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.1.2-alt1
- first build for ALT Linux Sisyphus
