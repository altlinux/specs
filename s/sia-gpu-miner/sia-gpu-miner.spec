Name: sia-gpu-miner
Version: 1.1.0
Release: alt1

Summary: A GPU Miner for Sia

License: MIT
Group: File tools
Url: https://github.com/NebulousLabs/Sia-GPU-Miner

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/NebulousLabs/Sia-GPU-Miner/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: ocl-icd-devel opencl-headers libcurl-devel

Requires: opencl-filesystem

%description
A GPU miner designed for mining siacoins.
This miner runs in a command prompt and prints your hashrate
along side the number of blocks you've mined.

Most cards will see greatly increased hashrates
by increasing the value of 'I' (default is 16, optimal is typically 20-25).

See https://wiki.tiker.net/OpenCLHowTo

%prep
%setup

%build
%make_build

%install
install -Dpm0755 %name %buildroot%_bindir/%name
install -Dpm0644 %name.cl %buildroot%_datadir/%name/%name.cl

%files
%doc README.md
%_bindir/%name
%_datadir/%name/%name.cl

%changelog
* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus
