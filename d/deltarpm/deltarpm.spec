Name: deltarpm
Version: 3.3
Release: alt0.1

Summary: Tools to Create and Apply deltarpms

Url: ftp://ftp.suse.com/pub/projects/deltarpm/
License: BSD
Group: System/Configuration/Packaging

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.suse.com/pub/projects/deltarpm/%name-%version.tar.bz2
Patch: %name.patch

# Automatically added by buildreq on Thu Feb 16 2006 (-bi)
BuildRequires: bzlib-devel perl-libnet

%description
This package contains tools to create and apply deltarpms. A deltarpm
contains the difference between an old and a new version of an RPM,
which makes it possible to recreate the new RPM from the deltarpm and
the old one. You do not need to have a copy of the old RPM, because
deltarpms can also work with installed RPMs.

Note: %name contains rsyncable version of zlib

%prep
%setup -q
%patch

%build
make CFLAGS="$RPM_OPT_FLAGS -I%_includedir/rpm" prefix="%prefix" rpmdumpheader="%_libdir/rpm/rpmdumpheader"

%install
#mkdir -p %buildroot%_libdir/rpm
make DESTDIR=%buildroot prefix="%prefix" mandir="%_mandir" rpmdumpheader="%_libdir/rpm/rpmdumpheader" install

%files
%doc README LICENSE.BSD
%_bindir/*
%_man8dir/*
#%_libdir/rpm/rpmdumpheader

%changelog
* Thu Feb 16 2006 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt0.1
- initial build for ALT Linux Sisyphus
- note: %name contains rsyncable version of zlib
