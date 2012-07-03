Summary: A small wrapper to disable fsync and related functions
Name: libeatmydata
Version: 28
Release: alt2
Group: File tools
License: GPLv3
Url: https://launchpad.net/libeatmydata
Source: https://launchpad.net/libeatmydata/trunk/release-28/+download/libeatmydata-28.tar.gz
Source1: eatmydata
Source2: eatmydata.sh.in
Source3: eatmydata.1

# Automatically added by buildreq on Fri May 25 2012
# optimized out: python-base python-modules
BuildRequires: python-modules-compiler python-modules-email

# buildreq works only on %%build stage
BuildRequires: strace

%description
EatMyData is LD_PRELOAD library that disables all forms of writing data
safely to disk. fsync() becomes a NO-OP, O_SYNC is removed etc. The idea
is to use in testing to get faster test runs where real durability is
not required.

%prep
%setup

%build
%autoreconf
%configure
%make

sed -e 's,@LIBDIR@,%{_libdir},g' < %SOURCE2 > eatmydata.sh

%install
make install DESTDIR=%buildroot

mkdir -p %buildroot{%_bindir,%_datadir/%name,%_man1dir}

cp %SOURCE1 %buildroot%_bindir/
cp eatmydata.sh %buildroot%_datadir/%name/
cp %SOURCE3 %buildroot%_man1dir/

%check
make check

%files
%doc AUTHORS README COPYING
%_bindir/eatmydata
%dir %_datadir/%name
%_datadir/%name/eatmydata.sh
%_man1dir/eatmydata.1*
%_libdir/*.so*

%changelog
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

