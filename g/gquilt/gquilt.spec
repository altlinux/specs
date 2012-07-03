Name: gquilt
Version: 0.22
Release: alt1.1.qa1.1

Summary: PyGTK GUI wrapper for quilt

License: GPL
Group: Development/Other
Url: http://gquilt.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sf.net/%name/%name-%version.tar.bz2
Patch: %name-0.20.patch

BuildArch: noarch

Requires: quilt

# manually removed: eric
# Automatically added by buildreq on Sun Jan 22 2006
BuildRequires: python-base python-modules-compiler python-modules-encodings
BuildRequires: desktop-file-utils

%description
quilt is a tool for managing a series of patches by keeping track
of the changes each patch makes. Patches can be applied, un-applied,
refreshed, etc.

gquilt is a PyGTK GUI wrapper for quilt.

%prep
%setup -q
%patch -p0

%build
make PREFIX=%prefix all gquilt

%install
%makeinstall_std PREFIX=%prefix

# fix broken desktop
sed -i 's/Generic Name/GenericName/g' %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=RevisionControl \
	%buildroot%_desktopdir/gquilt.desktop

#desktop-file-install --vendor fedora --delete-original \
#  --dir %buildroot%_desktopdir \
#  %buildroot%_desktopdir/%name.desktop

%files
%doc ChangeLog
%_bindir/gquilt
%dir %_datadir/gquilt/
%_datadir/gquilt/icons/
%_datadir/gquilt/qbsfe.sh
%_datadir/gquilt/*.py*
#%_datadir/gquilt/*.pyc
#%ghost %_datadir/gquilt/*.pyo
%_desktopdir/*
%_pixmapsdir/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.22-alt1.1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.22-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gquilt
  * postclean-03-private-rpm-macros for the spec file

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1.1
- Rebuilt with python 2.6

* Thu Aug 20 2009 Vitaly Lipatov <lav@altlinux.ru> 0.22-alt1
- new version 0.22 (with rpmrb script)

* Tue Jul 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- new version 0.20 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt1
- new version 0.19 (with rpmrb script)

* Sat Feb 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt1
- fix desktop

* Wed Feb 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt0.1
- new version

* Sun Jan 22 2006 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

