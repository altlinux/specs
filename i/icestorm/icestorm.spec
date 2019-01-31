Name: icestorm
Version: 0.0.0.618.gf029975
Release: alt2

Summary: Tools for working with Lattice iCE40 bitstream files
License: ISC
Group: Engineering
Url: http://www.clifford.at/icestorm/

Source: %name-%version.tar

# Automatically added by buildreq on Tue Jun 19 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel libusb-devel pkg-config python-base python3-base
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libftdi1-devel python3
Requires: %name = %version-%release

%description
Project IceStorm aims at reverse engineering and documenting the bitstream
format of Lattice iCE40 FPGAs and providing simple tools for analyzing and
creating bitstream files. The IceStorm Tools are a couple of small programs for
working with iCE40 bitstream files and our ASCII representation of it. The
complete Open Source iCE40 Flow consists of the IceStorm Tools, Arachne-PNR, and
Yosys.

%package -n %name-chipdb
Summary: Tools for working with Lattice iCE40 bitstream files - chipdb files
Group: Engineering
BuildArch: noarch

%description -n %name-chipdb
Project IceStorm aims at reverse engineering and documenting the bitstream
format of Lattice iCE40 FPGAs and providing simple tools for analyzing and
creating bitstream files.
This package contains chipdb files.

%prep
%setup

%build
%add_optflags -Wextra
%make_build CC=gcc CXX=g++ CFLAGS="%optflags $(pkg-config --cflags libftdi1)" \
    CXXFLAGS='%optflags' LDLIBS="$(pkg-config --libs libftdi1) -lm"

%install
%makeinstall_std PREFIX=%prefix
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%_bindir/iceboxdb.py %buildroot%python3_sitelibdir/
ln -rs %buildroot%python3_sitelibdir/iceboxdb.py %buildroot%_bindir/
chmod a+x %buildroot%_bindir/icebox.py

%files
%_bindir/ice*
%python3_sitelibdir/iceboxdb.py*
%python3_sitelibdir/__pycache__/iceboxdb*

%files -n %name-chipdb
%_datadir/icebox

%changelog
* Thu Jan 31 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.0.618.gf029975-alt2
- NMU: Updated build dependencies.

* Tue Jun 19 2018 Elvira Khabirova <lineprinter@altlinux.org> 0.0.0.618.gf029975-alt1
- New version
- Move noarch chipdb files to a separate package

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.0.357.g3c42bdb-alt2
- Switched to libftdi1.

* Mon Jul 17 2017 Elvira Khabirova <lineprinter@altlinux.org> 0.0.0.357.g3c42bdb-alt1
- New version

* Mon Jan 23 2017 Elvira Khabirova <lineprinter@altlinux.org> 0.0.0.292.gce4e1bc-alt1
- Initial build
