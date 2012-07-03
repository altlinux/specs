Name: python-module-gdchart2
Version: 0.beta1
Release: alt1.1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Python OO interface to GDChart
License: BSD
Group: Development/Python

Url: http://packages.debian.org/source/pygdchart2
Source: http://ftp.de.debian.org/debian/pool/main/p/pygdchart2/pygdchart2_%version.orig.tar.gz

# Automatically added by buildreq on Mon Feb 01 2010
BuildRequires: libfreetype-devel libgd2-devel libgdchart-devel libjpeg-devel libpng-devel python-devel

%description
Object-oriented Python interface to the nice 2d and 3d graphics library GDChart.

%prep
%setup -n pygdchart2alpha2

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.beta1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.beta1-alt1.1
- Rebuild with Python-2.7

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 0.beta1-alt1
- Initial build.