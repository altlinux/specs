%define _unpackaged_files_terminate_build 1

Name: monodevelop
Epoch: 1
Version: 5.10.0.871
Release: alt3

Summary: MonoDevelop is a project to port SharpDevelop to Gtk#
License: LGPLv2.1
Group: Development/Other
Url: https://www.monodevelop.com

ExclusiveArch: %ix86 x86_64

# https://github.com/mono/monodevelop.git
Source: %name-%version.tar
Source2: version.config

# Following data is obtained after running autogen, configure and make
Source3: buildinfo

# Following file is taken from monodevelop-7.6.9.22
Source4: monodevelop.appdata.xml

Source5: nuget-core.tar

# External dependencies (git submodules)
Source10: %name-%version-main-external-cecil.tar
Source11: %name-%version-main-external-debugger-libs.tar
Source12: %name-%version-main-external-fsharpbinding.tar
Source13: %name-%version-main-external-guiunit.tar
Source14: %name-%version-main-external-ikvm.tar
Source15: %name-%version-main-external-libgit2sharp.tar
Source16: %name-%version-main-external-libgit-binary.tar
Source17: %name-%version-main-external-libgit-binary-external-libgit2.tar
Source18: %name-%version-main-external-libgit-binary-external-libssh2.tar
Source19: %name-%version-main-external-mdtestharness.tar
Source20: %name-%version-main-external-mono-addins.tar
Source21: %name-%version-main-external-monomac.tar
Source22: %name-%version-main-external-monomac-maccore.tar
Source23: %name-%version-main-external-mono-tools.tar
Source24: %name-%version-main-external-nrefactory.tar
Source25: %name-%version-main-external-nuget-binary.tar
Source26: %name-%version-main-external-sharpsvn-binary.tar
Source27: %name-%version-main-external-xwt.tar

Patch1: %name-fix-rpm-autoreq.patch
Patch2: %name-disable-nuget-and-git.patch
Patch3: %name-update-rpm-autoreq.patch
Patch5: %name-alt-desktop-translation.patch

# Patches from Fedora
Patch102: %name-nuget-unbundle.patch

# Remove missing dependencies
%filter_from_requires /mono(System\.Web\.DataVisualization).*/d
%filter_from_requires /mono(Microsoft\.VisualStudio\.ImageCatalog).*/d
%filter_from_requires /mono(PresentationCore).*/d

BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-mono >= 2.0.0
BuildRequires: mono-devel-full
BuildRequires: intltool /usr/bin/msgfmt
BuildRequires: desktop-file-utils perl-XML-Parser shared-mime-info
BuildRequires: /proc
BuildRequires: xsp
BuildRequires: autoconf automake cmake
BuildRequires: libgtk-sharp2-devel libgnome-sharp-devel
BuildRequires: libssh2-devel
BuildRequires: mono-addins-devel
BuildRequires: nunit2-devel
BuildRequires: nuget-devel
BuildRequires: newtonsoft-json-devel
BuildRequires: /usr/bin/7z

Requires: mono-core
Requires: mono-web
Requires: mono-devel-full
Requires: pkg-config
Requires: xsp
Requires: mono-addins
Requires: nunit2
Requires: newtonsoft-json

%description
This is MonoDevelop which is intended to be a full-featured
integrated development environment (IDE) for mono and Gtk#.
It was originally a port of SharpDevelop 0.98.

%prep
%setup -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27

%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch5 -p2

%patch102 -p1

cp %SOURCE2 ./

# Prepare build info: add current date to prebuilt file
mkdir -p build/bin
cp %SOURCE3 ./build/bin/buildinfo
LANG=C date '+Build date: %%Y-%%m-%%d %%H:%%M:%%S%%:::z' >> ./build/bin/buildinfo

# unpack nuget packages
tar xf %SOURCE5
mkdir -p packages
pushd packages
for i in ../nuget-core/*.nupkg ; do
	name=$(basename ${i%%.nupkg})
	mkdir $name
	pushd $name
	7z x -y ../$i
	cp ../$i ./
	popd
done

# unzip unpacks filenames with %% sign as is. Convert it. TODO: make a more generic solution when necessary
find . -iname '*%%2B*' | while read file ; do
	mv $file $(echo $file | sed -e 's:%%2B:+:g') ||:
done
popd

find . -type f -print0 | xargs -0 \
    sed -i \
        -e 's:../version.config:version.config:g' \
        -e 's:..\\version.config:version.config:g' \
        %nil

%__subst '/^Encoding=/d;
	s/^Exec=monodevelop$/Exec=monodevelop %%F/;
	s/^Categories=.*$/Categories=Development;IDE;/
	' monodevelop.desktop

%__subst "s|^pkgconfigdir *= \$(prefix)/lib/pkgconfig|pkgconfigdir = %_pkgconfigdir|" \
	Makefile.am

# mono tries to do awk+sed and fails at it for some unknown reason. Workaround it.
cp src/core/MonoDevelop.Core/BuildVariables.cs.in src/core/MonoDevelop.Core/BuildVariables.cs
sed -i \
    -e "s:@PACKAGE_VERSION@:$(cat version.config | grep '^Version=' | sed -e 's|Version=||'):g" \
    -e "s:@PACKAGE_VERSION_LABEL@:$(cat version.config | grep '^Label=' | sed -e 's|Label=||'):g" \
    -e "s:@COMPAT_ADDIN_VERSION@:$(cat version.config | grep '^CompatVersion=' | sed -e 's|CompatVersion=||'):g" \
    -e "s:@BUILD_LANE@:$(cat version.config | grep '^BUILD_LANE=' | sed -e 's|BUILD_LANE=||'):g" \
    -e "s:@FULL_VERSION@:%version:g" \
    src/core/MonoDevelop.Core/BuildVariables.cs

%build
# git may crash monodevelop due to some components missing

NOCONFIGURE=yes sh ./autogen.sh
%configure \
	--disable-update-mimedb \
	--disable-update-desktopdb \
	--disable-subversion \
	--disable-git \
	%nil

pushd external/libgit2sharp/Lib/CustomBuildTasks
xbuild CustomBuildTasks.csproj
mv bin/Debug/* .
popd

%make

%install
%makeinstall_std

install -Dpm644 %SOURCE4 %buildroot%_datadir/appdata/%{name}.appdata.xml

# for some reason, build and installation of version control addons is not skipped
rm -rf %buildroot%_libexecdir/%name/AddIns/VersionControl

# changelog addon depends on version control addon, remove it too
rm -rf %buildroot%_libexecdir/%name/AddIns/ChangeLogAddIn

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/*
%_libexecdir/%name
%_pkgconfigdir/*.pc
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%{name}*.png
%_iconsdir/hicolor/scalable/apps/%{name}*.svg
%_xdgmimedir/packages/*
%_datadir/appdata/%{name}.appdata.xml
%_man1dir/*

%changelog
* Wed Aug 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.10.0.871-alt3
- Rebuilt with new mono.

* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.10.0.871-alt2
- Updated dependencies.

* Tue Apr 27 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.10.0.871-alt1
- Downgraded to version 5.10.0.871 to update mono.
- Applied patches and changes from Fedora.

* Fri Apr 23 2021 Vitaly Lipatov <lav@altlinux.ru> 7.6.9.22-alt4
- NMU: fix 7z unpacking

* Tue Jun 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.9.22-alt3
- Added Russian translation to desktop file (Closes: #36849)

* Tue Oct 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.9.22-alt2
- Fixed work of solution format conversion.

* Tue Oct 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.9.22-alt1
- Updated to upstream version 7.6.9.22.

* Thu Jul 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.5.3.7-alt1
- Updated to upstream version 7.5.3.7.

* Wed Mar 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0.864-alt1
- Updated to stable upstream version 6.3.0.864.

* Wed Sep 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2.44-alt3
- Updated runtime dependencies.

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2.44-alt2
- Rebuilt with support of %%ubt macro.

* Fri Jul 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2.44-alt1
- Updated to stable upstream version 6.1.2.44

* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 2.8.6.4-alt1
- 2.8.6.4

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- build with internal Cecil

* Thu Jun 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Thu Mar 18 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2
- changed License

* Mon Oct 19 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt2
- update buildreq

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Fri Mar 13 2009 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1
- 1.9.2
- updated patches list

* Sun Feb 01 2009 Alexey Shabalin <shaba@altlinux.ru> 1.9.1-alt3.1
- rebuild with mono-2.2 (fix requires new cecil )

* Mon Jan 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt3
- fixed manual deps to be x86_64-friendly

* Sat Jan 03 2009 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt2
- desktop file fixes according to repocop results

* Sun Nov 23 2008 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt1
- 1.9.1
- manual rpm reqs for MonoDevelop.VersionControl.Subversion.dll
- new switch: %%def_(en|dis)able tests - disabled

* Fri Oct 31 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt1.r117558
- 2.0 alpha1, svn version 117558
- main package and core addins. extra addins move to package monodevelop-extra

* Tue Apr 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt2
- use gtksourceview2-sharp

* Fri Mar 28 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Mon Feb 25 2008 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1
- 0.19
- revised patch3 (use system cecil)

* Wed Jan 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.18.1-alt1
- 0.18.1
- use system cecil (patch3)
- cleanup spec
- use gtksourceview1-sharp

* Wed Nov 28 2007 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt0.20071121
- 0.17
- use gtksourceview-2.0 and gtksourceview2-sharp
- disable build database support - fail build with gtksourceview2-sharp
- use firefox instead seamonkey
- add man page mdtool

* Tue Oct 09 2007 Alexey Shabalin <shaba@altlinux.ru> 0.16-alt1
- 0.16
- add seamonkey, libgnomeui to Requires (#13033)

* Sat Sep 08 2007 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15
- fix build for x86_64

* Sat Jul 28 2007 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- Update to 0.14
- source from svn (no full archive in download homepage)

* Sun Mar 25 2007 Ildar Mulyukov <ildar@altlinux.ru> 0.13.1-alt1
- 0.13.1
- new translation ru.po
- disable nemerle AddIn, it's not working right now

* Tue Dec 12 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.12-alt2
- added "enable-feature" switches

* Wed Sep 27 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.12-alt1
- BuildRequires fixes
- new features on

* Wed Jul 19 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.11-alt1
- 0.11
- automatic dependancies calculation (due to rpm-4.0.4-alt66.1)

* Sun May 22 2005 Evgeny Sinelnikov <sin@altlinux.ru> 0.7-alt1
- Update to release

* Mon May 16 2005 Evgeny Sinelnikov <sin@altlinux.ru> 0.6-alt1
- Initial build for ALTLinux.
