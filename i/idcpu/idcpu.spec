Summary: CPU identification utility
Name: idcpu
Version: 1.0
Release: alt1
Group: System/Configuration/Hardware
License: GPL
URL: vovaprog.narod.ru

Source: %name-%version.tar.bz2

%description
This is CPU identification utility.

%description -l ru_RU.KOI8-R
Информация о процессоре

%prep
%setup -q

%make_build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/idcpu
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1/
install idcpu $RPM_BUILD_ROOT/usr/bin/idcpu
install CHANGES COPYING README $RPM_BUILD_ROOT/usr/share/doc/idcpu
install idcpu.1.gz $RPM_BUILD_ROOT/usr/share/man/man1

%files
/usr/bin/idcpu
%_man1dir/*
%{_docdir}/idcpu/*

%changelog
* Wed May 24 2006 Dmitri Kuzishchin <dim@altlinux.ru> 1.0-alt1
- first build
