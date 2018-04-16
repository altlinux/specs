Name: pinta
Version: 1.6
Release: alt3

Summary: An easy to use drawing and image editing program

Group: Graphics

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License: MIT and CC-BY
Url: http://pinta-project.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/PintaProject/Pinta/archive/%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-alt-fix-MonoPosix.patch

# Mono only available on these:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ia64 %arm sparcv9 alpha s390x


# Manually:
BuildRequires(pre): rpm-build-mono
BuildRequires: glib2-devel intltool monodevelop libgtk-sharp2-devel

Requires: icon-theme-hicolor

# Interfaces of slightly older versions are required, upstream corrects it by modifying 'Requires'
%define __find_provides sh -c '/usr/lib/rpm/find-provides | sort | uniq'
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | \
	sed -e "/mono\(Mono.Cairo\) = 2.0/d" | \
	sed -e "/mono\(Mono.Posix\) = 2.0/d"'

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

