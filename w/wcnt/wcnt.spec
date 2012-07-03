Summary: Wav Composer (Not Toilet), modular audio synthesis sequencer, and sampler
Name: wcnt
Version: 1.26.4
Release: alt1
License: GPL
Group: Sound
Source: %name-src-%version.tar.bz2
Patch: %name-gcc43.patch
Url: http://wcnt.sourceforge.net/
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sat Feb 28 2009
BuildRequires: gcc-c++ libsndfile-devel

%description
wcnt is a command line not-real-time modular audio synthesis,
sequencer, and sampler, written in C++ for Linux i386 based
systems. wcnt reads plain text files written in wcnt's 'near
english synth definition language' and may then produce audio
as 16 bit stereo WAV files.

%package examples
Summary: wcnt - Wav Composer Not Toilet - examples
Group: Sound
Requires: %name = %version
Requires: make

%description examples
wcnt - Wav Composer Not Toilet - examples.

To generate the examples simply call the script wcnt-examples.sh

%prep
%setup -q -n %name-%version
%patch -p1

%build
%make_build
#%__make examples %{?jobs:-j%jobs}

%install
install -dm 755 %buildroot%_bindir
install -m 755 %name \
	%buildroot%_bindir

cat > %name-examples.sh << EOF
#!/bin/bash
if [ ! -d \$HOME/wcnt ]; then
	mkdir -p \$HOME/wcnt
	cd \$HOME/wcnt
	cp -a %_datadir/%name/* .
	make examples
fi
EOF
install -m 755 %name-examples.sh \
	%buildroot%_bindir

install -dm 755 %buildroot%_datadir/%name
cp -a examples \
	%buildroot%_datadir/%name
install Makefile \
	%buildroot%_datadir/%name

%files
%doc ChangeLog COPYING NEWS TODO
%doc help_files
%_bindir/%name

%files examples
%doc INSTALL
%_bindir/%name-examples.sh
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sat Feb 28 2009 Fr. Br. George <george@altlinux.ru> 1.26.4-alt1
- Initial build from openSuSE

* Wed Feb 20 2008 Toni Graffy <toni@links2linux.de> - 1.26.4-0.pm.1
- update to 1.26.4
* Thu Feb 14 2008 Toni Graffy <toni@links2linux.de> - 1.26.3-0.pm.1
- update to 1.26.3
* Sun Feb 10 2008 Toni Graffy <toni@links2linux.de> - 1.26.2-0.pm.1
- initial release 1.26.2
