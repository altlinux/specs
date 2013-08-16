%define SVNDATE 20130809
%define SVNREV 2594

# More subpackages to come once licensing issues are fixed
Name: edk2
Version: 0.1
Release: alt1.svn%SVNREV
Summary: EFI Development Kit II

Source0: %name-%version.tar

License: BSD
Group: Emulators
Url: http://sourceforge.net/apps/mediawiki/tianocore/index.php?title=Edk2-buildtools

BuildRequires: gcc-c++
BuildRequires: python-devel
BuildRequires: libuuid-devel

%description
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.

%package tools
Summary: EFI Development Kit II Tools
Group: Emulators

%description tools
This package provides tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package tools-python
Summary: EFI Development Kit II Tools
Group: Development/Python
BuildArch: noarch

%description tools-python
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.  You do not need to install this package;
you probably want to install edk2-tools only.

%package tools-doc
Summary: Documentation for EFI Development Kit II Tools
Group: Development/Documentation
BuildArch: noarch

%description tools-doc
This package documents the tools that are needed to
build EFI executables and ROMs using the GNU tools.

%prep
%setup -q

%build
# source ./BuildEnv
make

%install
mkdir -p %buildroot%_bindir
install	\
	Source/C/bin/BootSectImage \
	Source/C/bin/EfiLdrImage \
	Source/C/bin/EfiRom \
	Source/C/bin/GenCrc32 \
	Source/C/bin/GenFfs \
	Source/C/bin/GenFv \
	Source/C/bin/GenFw \
	Source/C/bin/GenPage \
	Source/C/bin/GenSec \
	Source/C/bin/GenVtf \
	Source/C/bin/GnuGenBootSector \
	Source/C/bin/LzmaCompress \
	Source/C/bin/Split \
	Source/C/bin/VfrCompile \
	Source/C/bin/VolInfo \
	%buildroot%_bindir

ln -f %buildroot%_bindir/GnuGenBootSector \
	%buildroot%_bindir/GenBootSector

mkdir -p %buildroot%_datadir/%name
cp -R Source/Python %buildroot%_datadir/%name/Python

find %buildroot%_datadir/%name/Python -name "*.pyd" | xargs rm

for i in BPDG GenDepex GenFds GenPatchPcdTable PatchPcdValue TargetTool Trim UPT; do
  echo '#!/bin/sh
PYTHONPATH=%_datadir/%name/Python
export PYTHONPATH
exec python '%_datadir/%name/Python/$i/$i.py' "$@"' > %buildroot%_bindir/$i
  chmod +x %buildroot%_bindir/$i
done

%files tools
%_bindir/BootSectImage
%_bindir/EfiLdrImage
%_bindir/EfiRom
%_bindir/GenBootSector
%_bindir/GenCrc32
%_bindir/GenFfs
%_bindir/GenFv
%_bindir/GenFw
%_bindir/GenPage
%_bindir/GenSec
%_bindir/GenVtf
%_bindir/GnuGenBootSector
%_bindir/LzmaCompress
%_bindir/Split
%_bindir/VfrCompile
%_bindir/VolInfo

#%files tools-python
#%_bindir/BPDG
#%_bindir/GenDepex
#%_bindir/GenFds
#%_bindir/GenPatchPcdTable
#%_bindir/PatchPcdValue
#%_bindir/TargetTool
#%_bindir/Trim
#%_bindir/UPT
#%_datadir/%name/Python/

%files tools-doc
%doc UserManuals/*.rtf

%changelog
* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1.svn2594
- initial build
