%define _unpackaged_files_terminate_build 1

Name: dsd-fme
Version: 2024
Release: alt1
Summary: Digital Speech Decoder - Florida Man Edition
License: MIT
Group: Editors
Url: https://github.com/lwvmobile/dsd-fme

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: mbelib-devel
BuildRequires: libsndfile-devel
BuildRequires: libncursesw-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libpcre2-devel
BuildRequires: rtl-sdr-devel
BuildRequires: itpp-devel
BuildRequires: libcodec2-devel

%description
DSD-FME is an evolution of the original DSD project from 'DSD Author'
using the base code of szechyjs, some code and ideas from LouisErigHerve,
Boatbod OP25 and Osmocom OP25, along with other snippets of code, information,
and inspirations from other projects including DSDcc, SDRTRunk, MMDVMHost, LFSR,
OK-DMRlib, and EZPWD-Reed-Solomon, Eric Cottrell, SP5WWP and others.
Finally, this is all brought together with original code to extend the
fuctionality and add new features including NCurses Terminal and Menu system,
Pulse Audio, TCP Direct Link Audio, RIGCTL, Trunking Features, LRRP/GPS Mapping,
P25 Phase 2, EDACS, YSF, M17, OP25 Capture Bin compatability, etc.

%prep
%setup

%build
export CFLAGS="%optflags"
%cmake \
    -DCMAKE_MODULE_PATH=%_libdir/cmake
%cmake_build

%install 
%cmake_install 

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Jul 15 2024 Pavel Shilov <zerospirit@altlinux.org> 2024-alt1
- initial build for Sisyphus
