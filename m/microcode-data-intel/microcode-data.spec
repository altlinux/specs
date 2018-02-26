Name: microcode-data-intel
Version: 20100914
Release: alt1

Packager: Vicror Forsiuk <force@altlinux.org>

Summary: Microcode definitions for Intel processors
License: INTEL SOFTWARE LICENSE AGREEMENT
Group: System/Kernel and hardware

URL: http://downloadcenter.intel.com/
Source0: http://downloadmirror.intel.com/19342/eng/microcode-%version.tgz

Provides: microcode-data

# This package may be totally useless for some architectures. This is CPU maker
# specific microcode, so by its nature it can not be arch-independent. OTOH,
# being packaged it will be binary identical for all arches, so formally this
# is noarch.
#
# And in order to package this code as a microcode we need to obey microcode
# packaging checks and tag package as noarch.
BuildArch: noarch

%description
The microcode data file for Linux contains the latest microcode definitions for
all Intel processors.

%prep
%setup -c

%build
mv microcode*.dat microcode.dat

%install
install -pDm644 microcode.dat %buildroot/lib/microcode/microcode.dat

%files
%dir /lib/microcode
/lib/microcode/microcode.dat

%changelog
* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 20100914-alt1
- Initial build.
