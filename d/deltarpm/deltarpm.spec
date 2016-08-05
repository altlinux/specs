Name: deltarpm
Version: 3.6.1
Release: alt1

Summary: Tools to Create and Apply deltarpms

Url: ftp://ftp.suse.com/pub/projects/deltarpm/
License: BSD
Group: System/Configuration/Packaging

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/rpm-software-management/deltarpm/archive/%version.tar.gz
Source: %name-%version.tar
#Source: ftp://ftp.suse.com/pub/projects/deltarpm/%name-%version.tar
Patch: %name.patch

# Automatically added by buildreq on Sat Aug 03 2013 (-bi)
# optimized out: elfutils python-base python-devel python-module-distribute python-module-zope python-modules python3-base
BuildRequires: bzlib-devel liblzma-devel perl-libnet python-module-mwlib

%description
This package contains tools to create and apply deltarpms. A deltarpm
contains the difference between an old and a new version of an RPM,
which makes it possible to recreate the new RPM from the deltarpm and
the old one. You do not need to have a copy of the old RPM, because
deltarpms can also work with installed RPMs.

Note: %name contains rsyncable version of zlib

%prep
%setup
%patch -p2

%build
make CFLAGS="$RPM_OPT_FLAGS -I%_includedir/rpm" prefix="%prefix" rpmdumpheader="%_libdir/rpm/rpmdumpheader"

%install
#mkdir -p %buildroot%_libdir/rpm
%makeinstall_std prefix="%prefix" mandir="%_mandir" rpmdumpheader="%_libdir/rpm/rpmdumpheader"

%files
%doc README LICENSE.BSD
%_bindir/*
%_man8dir/*
#%_libdir/rpm/rpmdumpheader

%changelog
* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 3.6.1-alt1
- new version (3.6.1) with rpmgs script

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 3.6-alt1
- new version 3.6 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.3-alt0.1.qa1
- NMU: rebuilt for debuginfo.

* Thu Feb 16 2006 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt0.1
- initial build for ALT Linux Sisyphus
- note: %name contains rsyncable version of zlib
