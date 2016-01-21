%define ast_version 11.20.0
%define modules_dir %_libdir/asterisk/%ast_version/modules

Name: asterisk11-chan_dongle
Summary: Channel driver for Asterisk to use Huawei 3G modem series.
Version: 1.1
Release: alt26
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
* Fri Jan 15 2016 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt26
- Asterisk update

* Sat Apr 11 2015 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt25
- Asterisk update

* Wed Apr 08 2015 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt24
- Asterisk update

* Sat Feb 07 2015 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt23
- Asterisk update

* Sat Jan 31 2015 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt22
- Asterisk update

* Tue Dec 16 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt21
- Asterisk update

* Thu Dec 11 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt20
- Asterisk update

* Thu Nov 27 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt19
- Asterisk update

* Thu Sep 25 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt18
- Asterisk update

* Sat Sep 20 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt17
- Asterisk update

* Wed Aug 20 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt16
- Asterisk update

* Sat Jul 12 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt15
- Asterisk update

* Mon Jun 23 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt14
- Asterisk update

* Sat Jun 07 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt13
- Asterisk update

* Sat Apr 26 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt12
- Asterisk update

* Tue Mar 11 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt11
- Asterisk update

* Wed Jan 15 2014 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt10
- Asterisk update

* Sun Sep 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt9
- Asterisk update

* Thu Aug 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt8
- Asterisk update

* Sun May 19 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt7
- Asterisk update

* Wed Apr 10 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt6
- Asterisk update

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
