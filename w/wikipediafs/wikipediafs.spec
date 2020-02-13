Name: wikipediafs
Version: 0.4
Release: alt2

Summary: View and edit Wikipedia articles as files
License: GPLv2
Group: System/Kernel and hardware
Url: http://wikipediafs.sourceforge.net/

Packager: Paul Wolneykien <manowar@altlinux.ru>
BuildArch: noarch

# Source-url: http://prdownloads.sourceforge.net/wikipediafs/%version/wikipediafs-%version.tar.gz
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-fuse

Requires: python3-module-fuse >= 0.2


%description
WikipediaFS is a mountable Linux virtual file system that allows to
read and write articles from and to Wikipedia (or any Mediawiki-based
site) as files.

%prep
%setup
%patch0 -p2

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS COPYING README
%_man1dir/mount.%name.*
%_bindir/mount.%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-*.egg-info


%changelog
* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt2
- Porting on python3.

* Tue Aug 25 2015 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new version (0.4) with rpmgs script

* Tue Aug 25 2015 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt2
- cleanup spec

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Tue Dec 29 2009 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt1
- Initial build for ALTLinux
