Name: archmage
Version: 0.3.1
Release: alt1

Summary: Extensible reader/decompiler of files in CHM format

Group: Text tools
License: GPL
Url: http://archmage.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/dottedmag/archmage/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

# for conversion to text
#Requires: elinks

BuildRequires: rpm-build-compat >= 1.2

# Automatically added by buildreq on Sun Oct 05 2008
BuildRequires: python-devel python-module-setuptools

Requires: python-module-pychm

%description
arCHMage - extensible reader/decompiler of files in CHM format
(Microsoft HTML help, also known as Compiled HTML).
arCHMage is based on chmlib by Jed Wing and is written on python.

%prep
%setup
echo "%version" >RELEASE-VERSION

%build
%python_build

%install
%python_install
# remove apache integration
rm -f %buildroot%python_sitelibdir/archmod/mod_chm.py*
install -D -m644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc AUTHORS NEWS README.md
#dir %_sysconfdir/archmage/
#config(noreplace) %_sysconfdir/archmage/arch.conf
%_bindir/archmage
%python_sitelibdir/archmod/
%python_sitelibdir/archmage-*egg-info
#_datadir/archmage/
%_man1dir/archmage*

%changelog
* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version 0.3.1 (with rpmrb script)
- conf. file /etc/archmage/arch.conf is not supported anymore

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt1
- new version 0.2.4 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.9-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1.1
- Rebuilt with python 2.6

* Sun Oct 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.9-alt1
- initial build for ALT Linux Sisyphus

* Thu Jan  3 2008 Patrice Dumas <pertusus@free.fr> 0.1.9-2
- ship egg

* Fri Aug  3 2007 Patrice Dumas <pertusus@free.fr> 0.1.9-1
- update to 0.1.9

* Thu Jan 18 2007 Patrice Dumas <pertusus@free.fr> 0.0.8-1
- update to 0.0.8

* Tue Dec 12 2006 Patrice Dumas <pertusus@free.fr> 0.0.7-4
- add BuildRequires python-devel

* Sat Dec  9 2006 Patrice Dumas <pertusus@free.fr> 0.0.7-3
- rebuild for python 2.5

* Tue Sep 12 2006 Patrice Dumas <pertusus@free.fr> 0.0.7-2
- .pyo files added. Bug #205369
- BuildRequires:  python and not python-devel since it is noarch

* Mon Mar 20 2006 Patrice Dumas <pertusus@free.fr> 0.0.7-1
- initial release
