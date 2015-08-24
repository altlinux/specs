Name: wikipediafs
Version: 0.4
Release: alt1

Summary: View and edit Wikipedia articles as files

Packager: Paul Wolneykien <manowar@altlinux.ru>

Group: System/Kernel and hardware
License: GPLv2
Url: http://wikipediafs.sourceforge.net/

# Source-url: http://prdownloads.sourceforge.net/wikipediafs/%version/wikipediafs-%version.tar.gz
Source: %name-%version.tar

%py_package_requires fuse >= 0.2

BuildPreReq: python-devel rpm-build-python python-module-fuse
BuildArch: noarch

%description
WikipediaFS is a mountable Linux virtual file system that allows to
read and write articles from and to Wikipedia (or any Mediawiki-based
site) as files.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS COPYING README
%python_sitelibdir/%name/
%python_sitelibdir/%name-*.egg-info
%_bindir/mount.%name
%_man1dir/mount.%name.*

%changelog
* Tue Aug 25 2015 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new version (0.4) with rpmgs script

* Tue Aug 25 2015 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt2
- cleanup spec

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Tue Dec 29 2009 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt1
- Initial build for ALTLinux
