Name: pinta
Version: 1.7
Release: alt2

Summary: An easy to use drawing and image editing program

Group: Graphics

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License: MIT and CC-BY-2.5
Url: http://pinta-project.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/PintaProject/Pinta/archive/%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-alt-fix-MonoPosix.patch

# Mono only available on these:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ia64 %arm sparcv9 alpha s390x


# Manually:
BuildRequires(pre): rpm-build-mono
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: libgtk-sharp2-devel
BuildRequires: mono-addins-devel
BuildRequires: mono-devel

Requires: icon-theme-hicolor
Requires: mono-addins

# Interfaces of slightly older versions are required, upstream corrects it by modifying 'Requires'
%filter_from_requires /mono\(Mono.Cairo\) = 2.0/d
%filter_from_requires /mono\(Mono.Posix\) = 2.0/d

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup
%patch0 -p1
%__subst 's!$(InstallPrefix)/lib/!$(InstallPrefix)/%_lib/!' Pinta/Pinta.csproj
%__subst 's!@prefix@/lib/!%_libdir/!' pinta.in
%__subst 's!$(InstallPrefix)/lib/!$(InstallPrefix)/%_lib/!' Pinta.Install.proj

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc readme.md license-mit.txt license-pdn.txt
%_bindir/%name
%_libdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/%name.*
%_man1dir/%{name}*
%_pixmapsdir/%{name}*

%changelog
* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7-alt2
- Updated dependencies.

* Wed Dec 16 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7-alt1
- new version 1.7 (close: #39106)
- update BR:

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.6-alt5
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.6-alt4
- NMU: remove %%ubt from release

* Wed May 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6-alt3
- NMU: rebuilt with %%ubt.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6-alt3
- (NMU) rebuilt to regenerate package dependencies.

* Tue Sep 12 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.6-alt2
- rebuild with mono5

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- new version 1.6 (with rpmrb script)

* Wed Jul 31 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- new version 1.4 (with rpmrb script)

* Sat Feb 25 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Mon Oct 03 2011 Александр Казанцев <kazancas@mandriva.org> 1.0-1mdv2012.0
+ Revision: 702606
- imported package pinta

