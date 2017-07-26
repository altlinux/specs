# vim: set ft=spec: -*- rpm-spec -*-

%def_disable tests

Name: monodevelop
Version: 6.1.2.44
Release: alt1

Summary: MonoDevelop is a project to port SharpDevelop to Gtk#
License: LGPLv2.1
Group: Development/Other
Url: http://www.monodevelop.com/

Source: %name-%version.tar
Source1: external.tar.bz2
Source2: version.config
Source3: buildinfo
Source4: nuget-core.tar
Source5: nuget-external-fsharpbinding.tar
Source6: nuget-external-libgit2sharp.tar
Patch0: %name-%version-%release.patch

# Remove missing dependencies
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | sed "/mono\(System\.Web\.DataVisualization\).*/d"'

BuildPreReq: rpm-build-mono >= 2.0.0
BuildPreReq: mono-core >= 5.0.0.0
BuildPreReq: mono-devel >= 5.0.0.0
BuildPreReq: mono-monodoc-devel >= 1.0

BuildRequires: intltool mono-core mono-web-devel mono-winforms
BuildRequires: desktop-file-utils mono-nunit perl-XML-Parser shared-mime-info intltool
BuildRequires: zip
BuildRequires: /proc
BuildRequires: xsp
BuildRequires: autoconf automake cmake
BuildRequires: fsharp libgtk-sharp2-devel libgnome-sharp-devel
BuildRequires: libssh2-devel unzip
BuildRequires: referenceassemblies-pcl

Requires: mono-core
Requires: mono-web
Requires: pkg-config
Requires: xsp
Requires: mono-devel
Requires: mono-nunit
Requires: git
Requires: fsharp
Requires: referenceassemblies-pcl

%description
This is MonoDevelop which is intended to be a full-featured
integrated development environment (IDE) for mono and Gtk#.
It was originally a port of SharpDevelop 0.98.

%prep
%setup -q -n %name-%version
%patch0 -p1

tar xjf %SOURCE1
cp %SOURCE2 ./

# Prepare build info: add current date to prebuilt file
mkdir -p build/bin
cp %SOURCE3 ./build/bin/buildinfo
LANG=C date '+Build date: %%Y-%%m-%%d %%H:%%M:%%S%%:::z' >> ./build/bin/buildinfo

# unpack nuget packages
tar xf %SOURCE4
mkdir -p packages
pushd packages
for i in ../nuget-core/*.nupkg ; do
    name=$(basename ${i%%.nupkg})
    mkdir $name
    pushd $name
    unzip ../$i
    popd
done
popd

tar xf %SOURCE5
mkdir -p external/fsharpbinding/packages
pushd external/fsharpbinding/packages
for i in ../../../nuget-external-fsharpbinding/*.version.txt ; do
    name=$(basename ${i%%.version.txt})
    version=$(cat $i)
    dir=$(dirname $i)
    mkdir $name
    pushd $name
    unzip ../$dir/${name}.${version}.nupkg
    popd
done
popd

tar xf %SOURCE6
mkdir -p external/libgit2sharp/packages
pushd external/libgit2sharp/packages
for i in ../../../nuget-external-libgit2sharp/*.nupkg ; do
    name=$(basename ${i%%.nupkg})
    mkdir $name
    pushd $name
    unzip ../$i
    popd
done
popd

find . -type f -print0 | xargs -0 \
    sed -i \
        -e 's:../version.config:version.config:g' \
        -e 's:..\\version.config:version.config:g'

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
    src/core/MonoDevelop.Core/BuildVariables.cs

%build
NOCONFIGURE=yes sh ./autogen.sh
%configure  \
	    --disable-update-mimedb --disable-update-desktopdb \
        --enable-subversion \
        --enable-git \
        --enable-monoextensions \
	    %{subst_enable tests}

%make

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/*
%_prefix/lib/%name
%_pkgconfigdir/*.pc
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%{name}*.png
%_iconsdir/hicolor/scalable/apps/%{name}*.svg
%_datadir/mime/packages/*
%_man1dir/*

%changelog
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
