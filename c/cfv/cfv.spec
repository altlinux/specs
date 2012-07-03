Name: cfv
Version: 1.18.2
Release: alt1.1.1

Summary: Test and create .sfv, .csv and md5sum files

License: GPL
Url: http://cfv.sourceforge.net/
Group: File tools

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2
BuildArch: noarch

BuildPreReq: python >= %__python_version

# need only for internal test
# removed: BitTorrent
# Automatically added by buildreq on Fri Jan 11 2008
BuildRequires: python-module-imaging python-modules-compiler python-modules-encodings
%ifarch %ix86
BuildRequires: python-module-psyco
%endif

%description
cfv is a utility to both test and create .sfv, .csv and md5sum files.
These files are commonly used to ensure the correct retrieval or
storage of data.

%prep
%setup -q

%build
#echo "Last time I get 'tests finished:  ok: 1699  failed: 18'"
#cd test
#%__python test.py

%install
%makeinstall_std prefix=%_prefix mandir=%_mandir

%files
%doc Changelog README
%_bindir/*
%_man1dir/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.18.2-alt1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18.2-alt1.1
- Rebuilt with python 2.6

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.18.2-alt1
- new version 1.18.2 (with rpmrb script)
- disable internal test

* Fri Jan 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1.18.1-alt1
- remove require (find-requires is excellent!)
- use make install instead just copying ones
- enable internal test build package

* Sat Dec 31 2005 Vitaly Lipatov <lav@altlinux.ru> 1.18.1-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

