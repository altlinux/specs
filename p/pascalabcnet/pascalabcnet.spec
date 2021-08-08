Name:    pascalabcnet
Version: 3.8.0.2951
Release: alt3

Summary: PascalABC.NET programming language  
License: LGPL-3.0
Group:   Development/Other
Url:     http://pascalabc.net/
# VCS: https://github.com/pascalabcnet/pascalabcnet

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: 0001-Exit-build-shell-script-on-first-subcommand-failed.patch
Patch2: 0002-Do-not-change-background-color-of-console-output.patch

ExcludeArch: ppc64le

BuildRequires(pre): rpm-build-mono
BuildRequires: mono-devel
BuildRequires: mono-locale-extras

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
%patch1 -p1
%patch2 -p1
# Use xbuild insead of msbuild
subst 's/msbuild/xbuild/;/^if/,$d' _RebuildReleaseAndRunTests.sh
# Remove proprietary part
rm -rf bin/PT4
# Remove all binaries
find . -name \*.exe -delete
# TODO remove bundled libraries
#find . -name \*.dll -delete

%build
sh -x _RebuildReleaseAndRunTests.sh

%install
mkdir -p %buildroot%_libdir/%name
cp -a bin/* %buildroot%_libdir/%name
mkdir -p %buildroot%_bindir
# Executable wrappers
cat > %buildroot%_bindir/pabcnetc << ENDF
#!/bin/bash
export MONO_IOMAP=all
mono %_libdir/pascalabcnet/pabcnetc.exe \$@
ENDF
chmod +x %buildroot%_bindir/pabcnetc
cat > %buildroot%_bindir/pabcnetcclear << ENDF
#!/bin/bash
export MONO_IOMAP=all
mono %_libdir/pascalabcnet/pabcnetcclear.exe \$@
ENDF
chmod +x %buildroot%_bindir/pabcnetcclear

%files
%doc README.md
%_bindir/*
%_libdir/%name

%changelog
* Sat Aug 07 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt3
- Do not use black background to compiler banner (#211).
- Remove tests run during build process.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt2
- Use rpm-build-mono.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0.2951-alt1
- Initial build in Sisyphus.
