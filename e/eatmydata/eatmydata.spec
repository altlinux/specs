%define oname libeatmydata
%set_automake_version 1.11

Summary: A small wrapper to disable fsync and related functions
Name: eatmydata
Version: 105
Release: alt1
Group: File tools
License: GPLv3
Url: https://launchpad.net/libeatmydata
Source: https://launchpad.net/libeatmydata/trunk/release-%version/+download/libeatmydata-%version.tar.gz

Source3: eatmydata.1

Patch0: libeatmydata-82-alt-fix-packaging.patch

# Automatically added by buildreq on Fri May 25 2012
# optimized out: python-base python-modules
BuildRequires: python-modules-compiler python-modules-email

# buildreq works only on %%build stage
BuildRequires: strace

Provides: %oname = %version-%release
Obsoletes: %oname < %version-%release

%description
EatMyData is LD_PRELOAD library that disables all forms of writing data
safely to disk. fsync() becomes a NO-OP, O_SYNC is removed etc. The idea
is to use in testing to get faster test runs where real durability is
not required.

%prep
%setup -n %oname-%version
%patch0 -p2

%build
%autoreconf
%configure
%make

%install
make install DESTDIR=%buildroot

mkdir -p %buildroot%_man1dir

cp %SOURCE3 %buildroot%_man1dir/

%__subst "s|.*dpkg-architecture.*||" %buildroot%_bindir/%name
%__subst "s|^shlib=.*|shlib=%_datadir/%oname/eatmydata.sh|" %buildroot%_bindir/%name

%check
make check

%files
%doc AUTHORS README COPYING ChangeLog
%_bindir/eatmydata
%dir %_datadir/%oname
%_datadir/%oname/eatmydata.sh
%_man1dir/eatmydata.1*
%_libdir/*.so*

%changelog
* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 105-alt1
- new version 105 (with rpmrb script)

* Mon Nov 18 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 82-alt2
- Fix BFS (use old automake 1.11).

* Wed Jul 31 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 82-alt1
- new version (ALT#29248)

* Fri May 25 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 28-alt2
- move library to %%_libdir
- fix debian script
- use check stage

* Wed Apr 11 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 28-alt1
- New version
- Drop libdir patch

* Wed Apr 11 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 26-alt1
- Initial build using MDV and Debian scripts

* Sun Feb 06 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 26-1mdv2011.0
+ Revision: 636355
- added patch to use correct libdir
- imported package eatmydata
