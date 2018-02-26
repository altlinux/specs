Name: mppenc
Version: 1.16
Release: alt0.1

Summary: The latest StreamVersion7 encoder

License: LGPL
Group: Sound
Url: http://www.musepack.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://files.musepack.net/source/%name-%version.tar.bz2

# Automatically added by buildreq on Thu Dec 28 2006
BuildRequires: cpack

%description
Musepack is an audio compression format with a strong emphasis on high
quality. It's not lossless, but it is designed for transparency, so
that you won't be able to hear differences between the original wave
file and the much smaller MPC file.

It is based on the MPEG-1 Layer-2 / MP2 algorithms, but since 1997 it
has rapidly developed and vastly improved and is now at an advanced
stage in which it contains heavily optimized and patentless code.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX:=%buildroot%prefix

%install
make install

%files
%doc Changelog
%_bindir/%name

%changelog
* Thu Dec 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt0.1
- initial build for ALT Linux Sisyphus
