%define dotnet_version 10.0
%define xdg_name com.github.PintaProject.Pinta

%def_with prebuild

Name: pinta
Version: 3.1.2
Release: alt2

Summary: An easy to use drawing and image editing program

Group: Graphics

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License: MIT and CC-BY-3.0
Url: http://pinta-project.com/

# Source-url: https://github.com/PintaProject/Pinta/releases/download/%version/%name-%version.tar.gz
Source: %name-%version.tar
%if_with prebuild
Source1: packages.tar
%endif

ExclusiveArch: %dotnet_arches

BuildRequires(pre): rpm-macros-dotnet
BuildRequires: /proc
BuildRequires: autoconf-archive
BuildRequires: dotnet-sdk-%dotnet_version
BuildRequires: intltool
BuildRequires: libadwaita-devel

Requires: dotnet-%dotnet_version
Requires: libadwaita >= 1.7
Requires: libgtk4 >= 4.18

# replace Adwaita symbolic icons (ALT bug 59342)
BuildRequires: xapp-symbolic-icons
Requires: xapp-symbolic-icons

%description
Pinta is a free, open-source program for drawing and image editing.
It combines intuitive tools with powerful features, making it easy to create,
enhance, and manipulate images. Whether you're sketching or retouching photos,
Pinta keeps things simple without sacrificing functionality.

%prep
%setup %{?_with_prebuild:-a1}
%__subst 's!PINTA_BUILD_OPTS =!PINTA_BUILD_OPTS = --source ./packages!' Makefile.am
%__subst 's!lib_dir?.Name == "lib"!lib_dir?.Name == "%_lib"!' Pinta.Core/Managers/SystemManager.cs

# change Tmds.DBus version because version 0.22.0 has vulnerability
# https://github.com/advisories/GHSA-xrw6-gwf8-vvr9
%__subst 's!Include="Tmds.DBus" Version="0.22.0"!Include="Tmds.DBus" Version="0.93.0"!' Directory.Packages.props

# replace Adwaita symbolic icons (ALT bug 59342)
xsi-replace-adwaita-symbolic --fix Pinta.Resources

%build
%if_without prebuild
# no certificates: https://bugzilla.altlinux.org/53633
export DOTNET_NUGET_SIGNATURE_VERIFICATION=false
dotnet restore Pinta/Pinta.csproj \
	-p:TargetFramework=net%dotnet_version \
	--packages ./packages
%endif

export DOTNET_CLI_TELEMETRY_OPTOUT=true
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
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/*/*
%_man1dir/%{name}*
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Wed Jun 03 2026 Alexander Kovalev <alexvk@altlinux.org> 3.1.2-alt2
- replace Adwaita symbolic icons (ALT #59342)

* Sun May 24 2026 Alexander Kovalev <alexvk@altlinux.org> 3.1.2-alt1
- new version 3.1.2
- build with .NET 10
- build with Tmds.DBus version 0.93.0 (fixes: CVE-2026-39959)
- cleanup spec

* Tue Feb 03 2026 Alexander Kovalev <alexvk@altlinux.org> 3.1.1-alt2
- add requires: libadwaita, libgtk4

* Sat Jan 17 2026 Alexander Kovalev <alexvk@altlinux.org> 3.1.1-alt1
- new version 3.1.1

* Fri Oct 10 2025 Alexander Kovalev <alexvk@altlinux.org> 3.0.4-alt1
- new version 3.0.4

* Thu Oct 02 2025 Alexander Kovalev <alexvk@altlinux.org> 3.0.3-alt1
- new version 3.0.3
- build with .NET 9

* Mon Jul 18 2022 Anton Midyukov <antohami@altlinux.org> 1.7-alt3
- add aarch64 in ExclusiveArch

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
