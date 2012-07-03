%define _snap 060722
Name: unsermake
Version: 0.3.2.%_snap
Release: alt0.1.2.1

Summary: An automake replacement by The KDE Team

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: LGPL
Group: Development/Other
Url: http://wiki.kde.org/unsermake

#Source: %name-%version.tar.bz2
# FIXME:
Source: ftp://ftp.pld-linux.org/software/kde/%name-%_snap.tar.bz2
BuildArch: noarch

# Automatically added by buildreq on Mon Aug 01 2005
BuildRequires: python-base python-modules-compiler python-modules-encodings

%description
An automake replacement by The KDE Team.

%prep
%setup -q -n %name-%_snap
#__subst "s|exec python|eval python|g" %name
%build
%__python -c "import compileall; compileall.compile_dir('./')"

%install
install -d %buildroot%_datadir/%name
install %name *.{py,pyc,um} %buildroot%_datadir/%name
%__mkdir_p %buildroot/%_bindir
ln -s %_datadir/%name/%name %buildroot/%_bindir/%name

%files
%_bindir/*
%doc README TODO doc/*.{pdf,obj,sxi,txt}
%dir %_datadir/%name
%_datadir/%name/%name
%_datadir/%name/*.py
%_datadir/%name/*.pyc
%_datadir/%name/*.um


%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2.060722-alt0.1.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2.060722-alt0.1.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.3.2.060722-alt0.1.1
- Rebuilt with python-2.5.

* Sat Jul 22 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.2.060722-alt0.1
- new version from SVN 20060722

* Mon Jun 19 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.2.060619-alt0.1
- new version from SVN 20060619

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.1.5270.0-alt1
- new version from SVN 20050911

* Mon Aug 01 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.1.4319.0-alt0.1
- first build for ALT Linux Sisyphus

