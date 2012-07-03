%define oname pygtkimageview
Name: python-module-%oname
Version: 1.1.0
Release: alt1.1.1.1

Summary: PyGtkImageView is a set of Python bindings for GtkImageView

License: LGPL
Group: Video
Url: http://trac.bjourne.webfactional.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/%oname-%version.tar.gz

# Automatically added by buildreq on Thu Nov 13 2008
BuildRequires: gcc-c++ glibc-devel libgtkimageview-devel python-module-pygtk-devel

%description
PyGtkImageView contains a simple but full-featured image viewer widget
similar to the image viewer panes in gThumb or Eye of GNOME. The main
class in the module is ImageView.

%prep
%setup -q -n %oname-%version

%build
%configure
%make_build

%install
%makeinstall_std

%files
%python_sitelibdir/*
#%_pkgconfigdir/%oname.pc

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.1
- Rebuilt with python 2.6

* Thu Nov 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

