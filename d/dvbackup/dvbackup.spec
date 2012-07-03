Name: dvbackup
Version: 0.0.4
Release: alt1
Group: Archiving/Backup
Summary: Backup to digital camcoders
Summary(ru_RU.KOI8-R): Архивирование на цифровые видеокамеры
License: GPL
Url:http://dvbackup.sourceforge.net/

Source0: http://heanet.dl.sourceforge.net/sourceforge/dvbackup/dvbackup-0.0.4.tar.bz2
# http://www.s.netic.de/gfiala/dvbackup.html
Source1: http://www.s.netic.de/gfiala/rsbep0.0.5.tar.bz2

Patch0: dvbackup-0.0.5-cvs-20030816.diff.gz
Patch1: dvbackup-0.0.4-alt-build.patch.gz
Patch2: dvbackup-0.0.4-alt-rsbep.diff.gz
Patch3: dvbackup-0.0.4-alt-docs.patch.gz

# for /usr/bin/dvcont and /usr/bin/dvconnect
Requires: libavc1394-utils libdv-utils
# Automatically added by buildreq on Sun Apr 11 2004
BuildRequires: docbook-utils libpopt-devel zlib-devel

%description
Dvbackup allows you to backup files to digital camcoder tapes.

%description -l ru_RU.KOI8-R
Dvbackup позволяет архивировать файлы на ленту цифровых видеокамер.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p0
%__rm -f rsbep0.0.5/{dvr,rsbep,*.o}
%__mv rsbep0.0.5/README README.rsbep
%__mv rsbep0.0.5/README.RS32 README.rsbep.RS32
%__mv rsbep0.0.5/Makefile_plain_C rsbep0.0.5/Makefile

%build
export CC=gcc
export CFLAGS=$RPM_OPT_FLAGS
%make_build includedir=%_includedir
pushd rsbep0.0.5
%make
popd
docbook2man dvbackup.sgml
docbook2man rsbep.sgml

%install
%makeinstall
pushd rsbep0.0.5
%makeinstall
popd
%__install -D -m 644 underrun-pal.dv %buildroot%_datadir/%name/underrun-pal.dv
%__install -D -m 644 underrun-ntsc.dv %buildroot%_datadir/%name/underrun-ntsc.dv
%__install -D -m 644 logo.xcf %buildroot%_datadir/%name/logo.xcf
%__install -D -m 644 minilogo.ppm %buildroot%_datadir/%name/minilogo.ppm
%__install -D -m 644 dvbackup.1 %buildroot%_man1dir/dvbackup.1
%__install -D -m 644 rsbep.1 %buildroot%_man1dir/rsbep.1

%files
%doc AUTHORS ChangeLog ReleaseNotes README.rsbep README.rsbep.RS32 README.ALT dvbackup.html
%_bindir/dvbackup
%_bindir/rsbep
%dir %_datadir/%name
%_datadir/%name/*
%_man1dir/*

%changelog
* Tue Apr 13 2004 Grigory Batalov <bga@altlinux.ru> 0.0.4-alt1
- Updated to CVS version 20030816 (0.0.5?)
- Manpages from Debian imported
- Built for ALT Linux
