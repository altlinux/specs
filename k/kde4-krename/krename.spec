%define origname krename

Summary: A powerfull batch renamer for KDE4
Name: kde4-%origname
Version: 4.0.7
Release: alt1.1
License: GPL
Url: http://www.krename.net
Group: File tools
Packager: Aeliya Grevnyov <gray_graff@altlinux.org>

Source: %origname.tar.bz2

BuildRequires(pre): kde-common-devel
BuildRequires: gcc-c++ kde4libs-devel libtag-devel libexiv2-devel
BuildRequires: libpodofo-devel

%description
Krename is a very powerful batch file renamer for KDE4 which can rename a list
of files based on a set of expressions. It can copy/move the files to another
directory or simply rename the input files. Krename supports many conversion
operations, including conversion of a filename to lowercase or to uppercase,
conversion of the first letter of every word to uppercase, adding numbers to
filenames, finding and replacing parts of the filename, and many more.
It can also change access and modification dates, permissions, and file ownership.

%prep
%setup -q -n %origname

%build
%K4build

%install
%K4install
#%%add_findpackage_path %_kde4_bindir
#mkdir %buildroot/%_K4i18n
#%%__mv %buildroot/usr/share/locale/* %buildroot/%_K4i18n/
%K4find_lang %origname --with-kde

%files -f %origname.lang
%_K4bindir/%origname
%_K4xdg_apps/*.desktop
%_K4iconsdir/*/*/apps/*.png
%_K4srv/*

%changelog
* Thu Nov 03 2011 Michael Shigorin <mike@altlinux.org> 4.0.7-alt1.1
- NMU: rebuilt with libexiv2.so.11

* Wed Apr 13 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 4.0.7-alt1
- 4.0.7
- move to standart place

* Tue Dec 07 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 3.9.3-alt4
- Fix build

* Wed Jun 02 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 3.9.3-alt3
- Rebuild with new libexiv2

* Wed Jan 13 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 3.9.3-alt2
- Built with new libexiv2

* Fri Sep 11 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 3.9.3-alt1
- Initial build for Sisyphus (ALT #19699)
