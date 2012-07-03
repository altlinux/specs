Name: pyfa-gtk
Version: 0.8.0
Release: alt4.1

Summary: Python fitting assistant for EVE Online

Packager: Alexey Borovskoy <alb@altlinux.org>

License: %gpl3plus
Group: Games/Other 
BuildArch: noarch
Url: http://pyfa.sourceforge.net/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: python-module-setuptools python-module-pygtk-libglade
BuildRequires: python-modules-sqlite3

Requires: pyfa-common >= 0.8.0-alt4

%add_python_compile_include %_datadir/pyfa

#Костыль. Need fix.
%add_python_req_skip model

%description
pyfa is the Python Fitting Assistant, a standalone application to create
fittings for the EVE-Online SciFi MMORPG.
The layout of pyfa heavily based on EFT, the EVE fitting tool. Although
it is a complete rewrite and replacement for EFT, the fittings are still
compatible with EFT

This is GTK GUI frontend.

%prep
%setup -q

%build

%install

mkdir -p %buildroot%_datadir/pyfa
cp -r gui %buildroot%_datadir/pyfa/
cp *.py %buildroot%_datadir/pyfa/
cp *.ico %buildroot%_datadir/pyfa/
rm -f %buildroot%_datadir/pyfa/setup.py

mkdir -p %buildroot%_docdir/%name-%version
cp README.txt %buildroot%_docdir/%name-%version/README
cp LICENSE.txt %buildroot%_docdir/%name-%version/LICENSE
cp README.ALT %buildroot%_docdir/%name-%version

mkdir -p %buildroot%_bindir
install -m755 pyfa.wrapper %buildroot%_bindir/pyfa

%files
%_datadir/pyfa/*
%_docdir/%name-%version
%_bindir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt4.1
- Rebuild with Python-2.7

* Tue Mar 16 2010 Alexey Borovskoy <alb@altlinux.ru> 0.8.0-alt4
- Git version, commit 5dc7f0cc0261d72cac681c41451c9effd04893f4

* Mon Mar 08 2010 Alexey Borovskoy <alb@altlinux.ru> 0.8.0-alt3
- Git version, commit e1ad82a7ace3b3a211db0c986181f5372613ba4f

* Thu Feb 25 2010 Alexey Borovskoy <alb@altlinux.ru> 0.8.0-alt2
- Git version, commit 351493baf7288d467fa13fe661ef8cab5a297ba7

* Thu Feb 04 2010 Alexey Borovskoy <alb@altlinux.ru> 0.8.0-alt1
- 0.8.0
- Git version, commit 9322e14514ad84416042e69814e777fdc3eec59b

* Sat Jan 16 2010 Alexey Borovskoy <alb@altlinux.ru> 0.7.0-alt3
- Git version, commit 8ad134f0e003bb7db43e8613de1d383da7221ec1 
- Detete pyfa-download-data

* Fri Jan 01 2010 Alexey Borovskoy <alb@altlinux.ru> 0.7.0-alt2
- Fix deleting modules from active fitting
- Git version, commit 885f4d4683901a70dd1a1b10a5e450fa24bf8ee2

* Thu Dec 31 2009 Alexey Borovskoy <alb@altlinux.ru> 0.7.0-alt1
- 0.7.0
- Git version, commit 373156e2e7602f061a0b3bbdff77a3ea05b6bbfb

* Mon Dec 21 2009 Alexey Borovskoy <alb@altlinux.ru> 0.6.1-alt1
- 0.6.1
- Git version, commit 5c61053a625eab39075b3d173c4df57919110921

* Tue Dec 01 2009 Alexey Borovskoy <alb@altlinux.ru> 0.6.0-alt1
- 0.6.0
- Dominion support
- Git version, commit 0e5a951e14b143c1a24c0ffe88e12470a8cc410e

* Mon Nov 30 2009 Alexey Borovskoy <alb@altlinux.ru> 0.5.1-alt2
- Git version, commit 5e5b2c16255632e7501fd9927ea91425c6647518

* Tue Nov 24 2009 Alexey Borovskoy <alb@altlinux.ru> 0.5.1-alt1
- 0.5.1
- Git version, commit 0426d8b04b0b54813cfb06dcff252d04d7805c5f

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.1
- Rebuilt with python 2.6

* Tue Nov 17 2009 Alexey Borovskoy <alb@altlinux.ru> 0.5.0-alt1
- Git version, commit bc7f3671958971642b36c7cec16505654c40cf59

* Sun Nov 15 2009 Alexey Borovskoy <alb@altlinux.ru> 0.4.2-alt1
- Git version, commit a47674a6a41c6ab3646b60cccb8c86a2e7bd8549
