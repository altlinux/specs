%define _unpackaged_files_terminate_build 1
%define dotnetver 8.0

Name: osu-lazer
Version: 2026.401.0
Release: alt1

Summary: Rhythm is just a *click* away!
License: MIT
Group: Games/Arcade
Url: https://osu.ppy.sh/
Vcs: https://github.com/ppy/osu.git
ExclusiveArch: %_dotnet_archlist

Source: %name-%version.tar
Source1: vendor.tar
Source2: NuGet.Config
Source3: osu-lazer.desktop

Requires: dotnet-%dotnetver

BuildRequires(pre): rpm-macros-dotnet
BuildRequires: dotnet-sdk-%dotnetver
BuildRequires: /proc
BuildRequires: patchelf

%description
A free-to-win rhythm game. Rhythm is just a click away!

This is the future - and final - iteration of the osu! game client which
marks the beginning of an open era! Currently known by and released under
the release codename "lazer". As in sharper than cutting-edge.

%prep
%setup -a1
%autopatch -p1

%build
export DOTNET_CLI_TELEMETRY_OPTOUT="true"

dotnet restore osu.Desktop \
	--configfile %SOURCE2 \
	--packages vendor \
	--ignore-failed-sources \
	--use-current-runtime

dotnet publish osu.Desktop \
	--packages vendor \
	--no-restore \
	--use-current-runtime \
	--no-self-contained \
	--configuration Release \
	--output output \
	/property:Version="%version"

%install
mkdir -pv %buildroot%_libdir
cp -rv output %buildroot%_libdir/osu-lazer

pushd %buildroot%_libdir/osu-lazer/
while read -r file; do
	if ! file "$file" | grep -q ' ELF '; then
		continue
	fi
	patchelf --set-rpath %_libdir/osu-lazer/ "$file"
done < <(find . -type f -name '*.so.*' -or -name '*.so')
popd

mkdir -pv %buildroot%_bindir
ln -srvf %_libdir/osu-lazer/osu! %buildroot%_bindir/osu-lazer

install -pDm644 %SOURCE3 %buildroot%_desktopdir/osu-lazer.desktop
echo 'Icon=%_libdir/osu-lazer/lazer.ico' >> %buildroot%_desktopdir/osu-lazer.desktop

%files
%_bindir/osu-lazer
%_libdir/osu-lazer/
%_desktopdir/osu-lazer.desktop

%changelog
* Wed Apr 01 2026 Ajrat Makhmutov <rauty@altlinux.org> 2026.401.0-alt1
- New version.

* Mon Jan 19 2026 Ajrat Makhmutov <rauty@altlinux.org> 2026.119.0-alt1
- New version.

* Tue Dec 09 2025 Ajrat Makhmutov <rauty@altlinux.org> 2025.1209.0-alt1
- New version.

* Sat Dec 06 2025 Ajrat Makhmutov <rauty@altlinux.org> 2025.1205.0-alt1
- New version.

* Sun Nov 02 2025 Ajrat Makhmutov <rauty@altlinux.org> 2025.1029.1-alt1
- New version.

* Sun Sep 14 2025 Ajrat Makhmutov <rauty@altlinux.org> 2025.912.0-alt1
- First build for ALT (thx ancieg@ for the review).
