Name: bouml
Version: 4.22.2
Release: alt1

Summary: BOUML is a free UML 2 tool box

License: GPLv2+
Group: Development/Other
Url: http://bouml.free.fr

Packager: Yuriy Kashirin <uka@altlinux.ru>

Source: %{name}_%version.tar.gz
Source1: %name-changelog
#Patch0: %name-default-charset.patch
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Thu Nov 06 2008
BuildRequires: gcc-c++ libqt3-devel


%description
BOUML is a free UML 2 tool box (under development) allowing you to
specify and generate code in C++, Java and Idl.

BOUML runs under Unix/Linux/Solaris, MacOS X(Power PC and Intel) and
Windows.

BOUML is very fast and doesn't require much memory to manage several
thousands of classes, see benchmark.

BOUML is extensible, and the external tools named plug-outs can be
written in C++ or Java, using BOUML for their definition as any other
program. The code generators and reverses are ones of the pre-defined
plug-outs included in the BOUML distribution.

%prep
%setup -n %{name}_%version
%patch -p1

bzip2 -ck9 %SOURCE1 > ChangeLog.bz2

%build
export QTDIR=%_qt3dir
export PATH=%_qt3dir/bin:$PATH

%define boumldefs BOUML_LIB=%_libdir/%name BOUML_DIR=%_bindir BOUML_DESKTOP_DIR=%_desktopdir BOUML_ICONS_PREFIX_DIR=%_iconsdir/hicolor

%make_build %boumldefs

%install
%make_install %boumldefs DESTDIR=%buildroot install

%files
%_bindir/*
%_libdir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*
%doc README ChangeLog.bz2

%changelog
* Wed Dec 15 2010 Yuriy Kashirin <uka@altlinux.ru> 4.22.2-alt1
- New version, see ChangeLog for more details
- The previous releases of BOUML cannot read a project saved
  with this version. Obviously this release is able to read the
  projects made by previous releases of BOUML

* Thu Jan 14 2010 Yuriy Kashirin <uka@altlinux.ru> 4.17.1-alt1
- New version, see ChangeLog for more details
  + Added internationalization. Currently languages supported:
    de, es, fr, pt_br
- The previous releases of BOUML cannot read a project saved
  with this version. Obviously this release is able to read the
  projects made by previous releases of BOUML

* Wed Jul 22 2009 Yuriy Kashirin <uka@altlinux.ru> 4.13.1-alt1
- New version, see ChangeLog for more details
- The previous releases of BOUML cannot read a project saved
  with this version. Obviously this release is able to read the
  projects made by previous releases of BOUML

* Tue Dec 23 2008 Yuriy Kashirin <uka@altlinux.ru> 4.9-alt1
- New version
  + new feature: activity partitions (swimlanes)
  + bug fixes
- The previous releases of BOUML cannot read a project saved
  with this version. Obviously this release is able to read the
  projects made by previous releases of BOUML

* Sun Nov 16 2008 Yuriy Kashirin <uka@altlinux.ru> 4.8.2-alt1
- New version, see ChangeLog for more details
- Removed depricated %%update_menus, %%update_menus

* Thu Nov 06 2008 Yuriy Kashirin <uka@altlinux.ru> 4.8.1-alt2
- Updated BuildRequires by buildreq (fixes build in hasher)

* Thu Nov 06 2008 Yuriy Kashirin <uka@altlinux.ru> 4.8.1-alt1
- New version, see ChangeLog for more details
- The previous releases of BOUML cannot read a project saved
  with this version. Obviously this release is able to read the
  projects made by previous releases of BOUML
 

* Thu Aug 28 2008 Yuriy Kashirin <uka@altlinux.ru> 4.5-alt1
- New version, see ChangeLog for more details
- The previous releases of BOUML cannot read a project saved
  with this version. Obviously this release is able to read the
  projects made by previous releases of BOUML

* Thu Aug 28 2008 Yuriy Kashirin <uka@altlinux.ru> 4.4.3-alt1
- New version, see ChangeLog for more details
- Added additional categories to desktop files (fix
  freedesktop-categories repocop test warnings)
- The previous releases of BOUML cannot read a project saved
  with this version. Obviously this release is able to read the
  projects made by previous releases of BOUML


* Tue Mar 11 2008 Yuriy Kashirin <uka@altlinux.ru> 4.2-alt1
- New version
  + Added python support
  + See ChangeLog for more details
- Because the format of the BOUML files is changed, the previous
  releases of BOUML cannot read a project saved with this version

* Wed Jan 09 2008 Yuriy Kashirin <uka@altlinux.ru> 3.4.1-alt1
- New version, see ChangeLog for details
- Because the format of the BOUML files is changed, the previous
  releases of BOUML cannot read a project saved with this version

* Tue Nov 06 2007 Yuriy Kashirin <uka@altlinux.ru> 3.3.1-alt1
- New version
  + Fixed crash when transform a sequence diagram containing
    fragment separator to use flat/overlapping activity bars

* Mon Nov 05 2007 Yuriy Kashirin <uka@altlinux.ru> 3.3-alt1
- New version
  + Sequence diagram: add explicit reflexive return
  + Sequence diagram: add overlapping activity bars
  + Fixed possible crash when replace class instance in a
    sequence or collaboration diagram
  + Minor fixes
- Because the format of the BOUML files is changed, the previous
  releases of BOUML cannot read a project saved with this version

* Wed Oct 10 2007 Yuriy Kashirin <uka@altlinux.ru> 3.0.2-alt1
- New version
  + Since 2.32.1 Bouml crash when you add a non self
    transition, fixed
  + minor fixes
- Fixed more compilation warnings

* Tue Oct 09 2007 Yuriy Kashirin <uka@altlinux.ru> 3.0.1-alt1
- New version
  + fixed crash during a save
  + minor fixes

* Mon Oct 08 2007 Yuriy Kashirin <uka@altlinux.ru> 3.0-alt2
- Fixed more compilation warnings

* Mon Oct 08 2007 Yuriy Kashirin <uka@altlinux.ru> 3.0-alt1
- New version, see ChangeLog for details
  + Add management of PHP 4 and 5
- License: changed GPL -> GPLv2+

* Wed Oct 03 2007 Yuriy Kashirin <uka@altlinux.ru> 2.32.1-alt1
- New version, see ChangeLog for details 
- Fixed compiler warnings
  + invalid use of undefined type for QPtrList<type> class
    instantiation
  + uninitialized variables

* Wed Sep 26 2007 Yuriy Kashirin <uka@altlinux.ru> 2.32-alt1
- New version, see ChangeLog for details
  + In the previous releases the lines are always drawn in the
    diagrams between the center of their extremities. Now it is
    possible to decenter them
  + It is now possible to add state machines and activities
    under use cases and use case views
  + Add management of the multiplicity for the attributes
  + Bug fixes
- Because the format of the BOUML files is changed, the previous
  releases of BOUML cannot read a project saved with this version

* Fri Jul 06 2007 Yuriy Kashirin <uka@altlinux.ru> 2.29-alt1
- New version, see ChangeLog for details
- Because the format of the BOUML files is changed, the previous
  releases of BOUML cannot read a project saved with this version

* Fri May 11 2007 Yuriy Kashirin <uka@altlinux.ru> 2.26-alt1
- New version, see ChangeLog for details

* Thu Apr 26 2007 Yuriy Kashirin <uka@altlinux.ru> 2.24-alt1
- New version, see ChangeLog for details
- Packed ChangeLog obtained from project site

* Tue Apr 17 2007 Yuriy Kashirin <uka@altlinux.ru> 2.23.1-alt1
- New version, see http://bouml.free.fr/historic.html for details
- Build from git

* Tue Apr 03 2007 Yuriy Kashirin <uka@altlinux.ru> 2.22.2-alt1
- New version, see http://bouml.free.fr/historic.html for details
- Use UTF8 charset instead of Latin1 by default

* Tue Mar 27 2007 Yuriy Kashirin <uka@altlinux.ru> 2.22-alt0.2
- Spec cleanup

* Mon Mar 26 2007 Yuriy Kashirin <uka@altlinux.ru> 2.22-alt0.1
- First build for ALT Linux (Sisyphus)

