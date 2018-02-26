Name: pinta
Version: 1.1
Release: alt1

Summary: An easy to use drawing and image editing program

Group: Graphics

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License: MIT and CC-BY
Url: http://pinta-project.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://github.com/downloads/PintaProject/Pinta/%name-%version.tar

# Mono only available on these:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ia64 %arm sparcv9 alpha s390x

# Automatically added by buildreq on Sat Feb 25 2012
# optimized out: libavahi-sharp  mono mono-csharp mono-data mono-data-sqlite mono-devel mono-extras mono-mcs mono-mscorlib mono-wcf mono-web mono-winforms mono-winfxcore ndesk-dbus ndesk-dbus-glib perl-Encode pkg-config
# Manually:
BuildRequires: intltool mono-devel mono-addins-devel libgtk-sharp2-devel

Requires: icon-theme-hicolor


%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup
%__subst 's!$(InstallPrefix)/lib/!$(InstallPrefix)/%_lib/!' Pinta/Pinta.csproj
%__subst 's!@prefix@/lib/!%_libdir/!' pinta.in
%__subst 's!$(InstallPrefix)/lib/!$(InstallPrefix)/%_lib/!' Pinta.Install.proj

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc todo.txt readme.md license-mit.txt license-pdn.txt
%_bindir/%name
%_libdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/%name.*
%_man1dir/%{name}*
%_pixmapsdir/%{name}*

%changelog
* Sat Feb 25 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Mon Oct 03 2011 Александр Казанцев <kazancas@mandriva.org> 1.0-1mdv2012.0
+ Revision: 702606
- imported package pinta

