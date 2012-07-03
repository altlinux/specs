Name: avra
Version: 1.3.0
Release: alt1

Summary: AVRA is an assembler for Atmel AVR microcontrollers
License: GPL
Group: Development/C

Url: http://avra.sourceforge.net

Packager: Sergey Alembekov <rt@altlinux.ru>

Source0: %name.tar

BuildRequires: autoconf automake

%description
%summary

%prep
%setup -n %name

%build
cd src
aclocal
autoconf
touch INSTALL NEWS README AUTHORS ChangeLog
automake -a
%configure
%make

%install
cd src
make install  DESTDIR=%buildroot


%files
%_bindir/*


%changelog
* Wed Jan 12 2011 Sergey Alembekov <rt@altlinux.ru> 1.3.0-alt1
- Initial build
~       
