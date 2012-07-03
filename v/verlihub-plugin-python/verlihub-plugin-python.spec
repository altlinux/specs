%define oname python
Name: verlihub-plugin-python
Version: 1.1
Release: alt2.1.1

Summary: Python Plugin for verlihub

Url: http://www.verlihub-project.org
License: GPL
Group: Development/C

Source: %oname.tar.bz2
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Automatically added by buildreq on Tue Apr 29 2008
BuildRequires: gcc-c++ glibc-devel-static libGeoIP-devel libMySQL-devel libpcre-devel libverlihub-devel python-devel zlib-devel

%description
Python Plugin for Verlihub brings you the ability to run python scripts
in your hub.

%prep
%setup -n %oname
sed -i 's|python2\.5|python%__python_version|g' configure.in

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc README ChangeLog
%_libdir/*.so*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.1
- Rebuilt with python 2.6

* Mon Jul 13 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.1-alt2
- Fix building with gcc4.4

* Tue Apr 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus
