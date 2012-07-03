
Name: ninja
Version: 20111127
Release: alt1
License: Apache License
Group: Sound
Summary: Ninja is a small build system closest in spirit to Make
URL: https://github.com/martine/ninja
Packager: Michael Pozhidaev <msp@altlinux.ru>

Source0: %name-%version.tar

# Automatically added by buildreq on Sun Nov 27 2011
# optimized out: libstdc++-devel python-base python-modules
BuildRequires: gcc-c++ python-module-distribute

%description
Ninja is yet another build system. It takes as input the
interdependencies of files (typically source code and output
executables) and orchestrates building them, quickly.  Ninja joins a
sea of other build systems. Its distinguishing goal is to be fast.

%prep
%setup -q
%build
./bootstrap.sh

%install
%__install -pD -m755 %name %buildroot%_bindir/%name
%__install -d -m755 %buildroot%_datadir/%name
%__cp -r misc/. %buildroot%_datadir/%name

%files
%doc COPYING doc/* HACKING README
%_bindir/*
%_datadir/%name

%changelog
* Sun Nov 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20111127-alt1
- Initial release for ALT Linux

