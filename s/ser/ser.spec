# TODO -- chrooted ser
Name: ser
Version: 0.9.4
Release: alt1

Summary: SIP Express Router
License: GPL
Group: System/Servers

Url: ftp://ftp.berlios.de/pub/ser/latest/src/ser-0.9.3_src.tar.gz
Source: ftp://ftp.berlios.de/pub/ser/latest/src/%name-%{version}_src.tar.gz
#Source1: %name.conf
#Source2: %name.init
Packager: Denis Smirnov <mithraen@altlinux.ru>

# Automatically added by buildreq on Sun Oct 22 2006 (-bb)
BuildRequires: flex libexpat-devel libMySQL-devel libradiusclient-ng-devel libxml2-devel mailx python-modules-compiler python-modules-encodings termutils

%description
%summary

%prep
%setup -q

%build
make all \
		exclude_modules= \
		basedir=%buildroot \
		prefix=%prefix \
		cfg-prefix=%buildroot \
		cfg-target=/etc/ser/

%install
%makeinstall \
		basedir=%buildroot \
		prefix=%prefix \
		cfg-prefix=%buildroot \
		cfg-target=/etc/ser/

#mkdir -p %buildroot/etc
#mv %buildroot/usr/etc/ser %buildroot/etc/

%files
%dir /etc/ser
/etc/ser/*
%_sbindir/*
#_initdir/*
%dir %_libdir/ser
%dir %_libdir/ser/modules
%_libdir/ser/modules/*
%_docdir/%name
%_man5dir/*
%_man8dir/*

#post
#post_service %name

#preun
#preun_service %name
%changelog
* Sun Oct 22 2006 Denis Smirnov <mithraen@altlinux.ru> 0.9.4-alt1
- version update
- build some new modules
- doesn't try to start initscript that not packed today

* Thu Oct 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.9.3-alt2
- fix macro (for rebuilding)

* Sat Aug 13 2005 Denis Smirnov <mithraen@altlinux.ru> 0.9.3-alt1
- first build

