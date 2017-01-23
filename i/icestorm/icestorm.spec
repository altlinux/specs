Name: icestorm
Version: 0.0.0.292.gce4e1bc
Release: alt1

Summary: Tools for working with Lattice iCE40 bitstream files
License: ISC
Group: Engineering
Url: http://www.clifford.at/icestorm/

Source: %name-%version.tar

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: libstdc++-devel libusb-compat libusb-compat-devel pkg-config python-base python3
BuildRequires: gcc-c++ libftdi-devel python3-base

%description
Project IceStorm aims at reverse engineering and documenting the bitstream
format of Lattice iCE40 FPGAs and providing simple tools for analyzing and
creating bitstream files. The IceStorm Tools are a couple of small programs for
working with iCE40 bitstream files and our ASCII representation of it. The
complete Open Source iCE40 Flow consists of the IceStorm Tools, Arachne-PNR, and
Yosys.

%prep
%setup

%build
%add_optflags -Wextra
%make_build CC=gcc CXX=g++ CFLAGS="%optflags $(pkg-config --cflags libftdi)" \
    CXXFLAGS='%optflags' LDLIBS="$(pkg-config --libs libftdi) -lm"

%install
%makeinstall_std PREFIX=%prefix
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%_bindir/iceboxdb.py %buildroot%python3_sitelibdir/
ln -rs %buildroot%python3_sitelibdir/iceboxdb.py %buildroot%_bindir/
chmod a+x %buildroot%_bindir/icebox.py

%files
%_bindir/ice*
%_datadir/icebox
%python3_sitelibdir/iceboxdb.py*
%python3_sitelibdir/__pycache__/iceboxdb*

%changelog
* Mon Jan 23 2017 Elvira Khabirova <lineprinter@altlinux.org> 0.0.0.292.gce4e1bc-alt1
- Initial build
