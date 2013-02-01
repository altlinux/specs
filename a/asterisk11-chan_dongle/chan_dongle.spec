%define ast_version 11.2.1
%define modules_dir %_libdir/asterisk/%ast_version/modules

Name: asterisk11-chan_dongle
Summary: Channel driver for Asterisk to use Huawei 3G modem series.
Version: 1.1
Release: alt5
License: GPL
Group: System/Libraries
Url: http://code.google.com/p/asterisk-chan-dongle/

Source: %name-%version.tar

# Automatically added by buildreq on Sat Oct 03 2009
BuildRequires(pre): asterisk11-devel

Requires: usb_modeswitch
Requires: asterisk11 = %ast_version

%description
%summary

%prep
%setup

%build
export CFLAGS="-I /usr/include/asterisk-%ast_version"
aclocal
autoconf
automake -a ||:
%configure \
    --with-asterisk=/usr/include/asterisk-%ast_version
%make_build OPTFLAGS="-I /usr/include/asterisk-%ast_version" LIBS="-l pthread"

%install
mkdir -p %buildroot%modules_dir/
cp *.so %buildroot%modules_dir/
mkdir -p %buildroot%_docdir/%name

%files
%modules_dir/*.so
%doc LICENSE.txt README.txt TODO.txt INSTALL BUGS etc

%changelog
* Fri Feb 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt5
- Asterisk update

* Wed Jan 30 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt4
- add Url tag

* Mon Jan 21 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt3
- Asterisk update

* Wed Jan 09 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt2
- Asterisk update

* Wed Jan 09 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt1
- first build for Sisyphus
