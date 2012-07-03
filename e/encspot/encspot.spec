Name: encspot
Version: 2.01
Release: alt1

Summary: guesses encoder used to create MP3 file

Group: Sound

License: BSD-like
Url: https://launchpad.net/~francis-russell/+archive/encspot

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sun Mar 25 2012
# optimized out: cmake cmake-modules libstdc++-devel
BuildRequires: ccmake gcc-c++

%description
For a given list of MP3 files, encspot displays technical information
and attempts to determine  which encoder was used to create
them. Encspot also displays the contents of the LAME header (if present).

%prep
%setup

%build
%cmake
cd BUILD
%make_build

%install
install -m644 -D %name.1 %buildroot%_man1dir/%name.1
cd BUILD
%makeinstall_std

%files
%doc LICENSE README
%_bindir/%name
%_man1dir/%{name}*

%changelog
* Sun Mar 25 2012 Vitaly Lipatov <lav@altlinux.ru> 2.01-alt1
- initial build for ALT Linux Sisyphus
