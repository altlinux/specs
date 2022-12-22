Name:    pascalabcnet
Version: 3.8.3.3214
Release: alt1

Summary: PascalABC.NET programming language  
License: LGPL-3.0
Group:   Development/Other
Url:     http://pascalabc.net/
# VCS: https://github.com/pascalabcnet/pascalabcnet

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: PascalABCNETLinux.desktop
Source2: icons.tar
Source3: PascalABCNETLinux.appdata.xml

ExcludeArch: ppc64le

BuildRequires(pre): rpm-build-mono
BuildRequires: mono-devel
BuildRequires: mono-locale-extras

Requires: mono-devel
Requires: mono-locale-extras

%filter_from_requires /mono(\(PresentationCore\|PresentationFramework\))/d

%description
PascalABC.NET is a Pascal programming language that implements classic Pascal,
most Delphi language features, as well as a number of their own extensions. It
is implemented on the .NET Framework platform and contains all the modern
language features: classes, operator overloading, interfaces, exception
handling, generic classes and routines, garbage collection, lambda expressions,
parallel programming tools.

%prep
%setup
# Use xbuild insead of msbuild
subst 's/msbuild/xbuild/;/^if/,$d' _RebuildReleaseAndRunTests.sh
# Remove proprietary part
rm -rf bin/PT4
# Remove all binaries
find . -name \*.exe -delete
# TODO remove bundled libraries
#find . -name \*.dll -delete
rm -f bin/*.dll
tar xf %SOURCE2

%build
# Build compiler
sh -x _RebuildReleaseAndRunTests.sh
# Build IDE
MONO_IOMAP=case xbuild /p:Configuration=release PascalABCNETLinux.sln

%install
# Install executables and modules
mkdir -p %buildroot%_libexecdir/%name/{Lib,LibSource,Lng,Highlighting,Samples/Graphics}
cp -a bin/*.{exe,dll,chm,config} %buildroot%_libexecdir/%name
cp -a bin/template.pct %buildroot%_libexecdir/%name
cp -a bin/Highlighting/PascalABCNET.xshd %buildroot%_libexecdir/%name/Highlighting
cp -a bin/Lib/*.pcu %buildroot%_libexecdir/%name/Lib
cp -a bin/Lng/* %buildroot%_libexecdir/%name/Lng

# Install sources 
cp -a bin/Lib/*.pas %buildroot%_libexecdir/%name/LibSource

# Install samples
cp -a InstallerSamples/!MainFeatures %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/!Tutorial  %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/!РусскиеИсполнители %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/Algorithms %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/Applications %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/Games %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/LanguageFeatures %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/LINQ %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/NETLibraries %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/Other %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/StandardUnits %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/WhatsNew %buildroot%_libexecdir/%name/Samples
cp -a InstallerSamples/Graphics/GraphABC %buildroot%_libexecdir/%name/Samples/Graphics

# Install executable wrappers
mkdir -p %buildroot%_bindir

# Executable wrappers
cat > %buildroot%_bindir/pabcnetc << ENDF
#!/bin/bash
export MONO_IOMAP=all
mono %_libexecdir/pascalabcnet/pabcnetc.exe \$@
ENDF
chmod +x %buildroot%_bindir/pabcnetc

cat > %buildroot%_bindir/pabcnetcclear << ENDF
#!/bin/bash
export MONO_IOMAP=all
mono %_libexecdir/pascalabcnet/pabcnetcclear.exe \$@
ENDF
chmod +x %buildroot%_bindir/pabcnetcclear

cat > %buildroot%_bindir/PascalABCNETLinux << ENDF
#!/bin/bash
export MONO_IOMAP=all
export MONO_REGISTRY_PATH=\$HOME/PABCWork.NET
export MONO_HELP_VIEWER=kchmviewer
[ -d "\$MONO_REGISTRY_PATH" ] || mkdir -p "\$MONO_REGISTRY_PATH"
mono %_libexecdir/pascalabcnet/PascalABCNETLinux.exe "\$@"
ENDF
chmod +x %buildroot%_bindir/PascalABCNETLinux

# Install desktop file and icons
install -Dpm0644 %SOURCE1 %buildroot%_desktopdir/PascalABCNETLinux.desktop
pushd icons
for icon in *.png; do
	size="${icon#pascalabcnet-}"
	size="${size%.png}"
	install -Dpm0644 $icon %buildroot%_iconsdir/hicolor/${size}x${size}/apps/pascalabcnet.png
done
popd

# Install appdata.xml
install -Dpm 0644 %SOURCE3 %buildroot%_datadir/metainfo/PascalABCNETLinux.appdata.xml

%files
%doc README.md doc/*
%_bindir/*
%_libexecdir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/pascalabcnet.png
%_datadir/metainfo/*.appdata.xml

%changelog
* Wed Dec 21 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3214-alt1
- New version.

* Tue Dec 06 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3211-alt1
- New version.
- Fixed force popup menu by tooltip (ALT #43948).

* Sun Nov 20 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3205-alt1.git88d903bb
- New version (ALT #44328).

* Tue Nov 15 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3204-alt1.git5c1df570
- New version.
- Built all modules.
- Used install scheme from upstream (_GenerateLinuxVersion.bat).

* Tue Nov 08 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3199-alt1.git75237b4c
- New version.
- Packaged appdata.xml file for appstream-data.

* Fri Oct 28 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3197-alt1
- New version (closes: 43942, 43943, 43944, 43945, 43946).

* Fri Sep 30 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3177-alt1.gitd7d6d24d
- New version.
- Package IDE.

* Mon Aug 29 2022 Andrey Cherepanov <cas@altlinux.org> 3.8.3.3159-alt1
- New version.
- Built graphical library GraphABCLinux.
- Moved binaries and libraries to %_libexecdir/%name.
- Packaged examples.

* Thu Nov 25 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2964-alt2
- Requires mono-devel for compilation.

* Sat Aug 21 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2964-alt1
- New version.
- Runtime requires mono-locale-extras.
- Patches were applied by upstream.

* Sat Aug 07 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt3
- Do not use black background to compiler banner (#211).
- Remove tests run during build process.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt2
- Use rpm-build-mono.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt1
- Initial build in Sisyphus.
