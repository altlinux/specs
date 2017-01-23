Name: arachne-pnr
Version: 0.0.0.187.e97e35c
Release: alt1

Summary: Place and route tool for iCE40 family FPGAs
License: %mit
Group: Engineering
Url: https://github.com/cseed/arachne-pnr

Source: %name-%version.tar
Patch: use-explicit-git-hash.patch

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Tue Jan 24 2017
# optimized out: libstdc++-devel python-base python3 python3-base
BuildRequires: gcc-c++ icestorm yosys valgrind python-modules

%description
Arachne-pnr implements the place and route step of the hardware compilation
process for FPGAs. It accepts as input a technology-mapped netlist in BLIF
format, as output by the Yosys synthesis suite for example. It currently
targets the Lattice Semiconductor iCE40 family of FPGAs. Its output is a
textual bitstream representation for assembly by the IceStorm icepack
command. The output of icepack is a binary bitstream which can be uploaded to a
harware device.
Together, Yosys, arachne-pnr and IceStorm provide an fully open-source
Verilog-to-bistream tool chain for iCE40 1K and 8K FPGA development.

%prep
%setup
%patch -p1

%build
%make_build PREFIX=%prefix OPTDEBUGFLAGS='%optflags'

%install
%makeinstall_std PREFIX=%prefix CXX=false

%check
sed -i 's/shasum/sha1sum/g' tests/simple/run-test.sh
make simpletest ICEBOX=%_datadir/icebox

%files
%_bindir/%name
%_datadir/%name

%changelog
* Mon Jan 23 2017 Elvira Khabirova <lineprinter@altlinux.org> 0.0.0.187.e97e35c-alt1
- Initial build
