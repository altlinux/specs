%define ast_version %{get_version asterisk1.6.2-devel}
%define modules_dir %_libdir/asterisk/%ast_version/modules

Name: asterisk1.6.2-chan_datacard
Summary: Channel driver for Asterisk to use Huawei 3G modem series.
Version: 0.53
Release: alt23
License: GPL
Group: System/Libraries

Source: %name-%version.tar

# Automatically added by buildreq on Sat Oct 03 2009
BuildRequires(pre): asterisk1.6.2-devel

Requires: usb_modeswitch
Requires: asterisk1.6.2 = %ast_version

%description
%summary

%prep
%setup
rm -f chan_conv.o
make clean

%build
%make_build OPTFLAGS="-I /usr/include/asterisk-%ast_version" LIBS="-l pthread"

%install
mkdir -p %buildroot%modules_dir/
cp *.so %buildroot%modules_dir/
mkdir -p %buildroot%_docdir/%name

%files
%modules_dir/*.so
%doc LICENSE.txt README.txt TODO.txt datacard.conf

%changelog
* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt23
- Asterisk update

* Fri Jul 15 2011 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt22
- Asterisk update

* Thu Feb 17 2011 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt21
- Asterisk update

* Wed Feb 09 2011 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt20
- Asterisk update

* Fri Jan 21 2011 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt19
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt18
- Asterisk update

* Mon Dec 20 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt17
- Asterisk update

* Sun Dec 12 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt16
- Asterisk update

* Sat Nov 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt15
- Asterisk update

* Fri Nov 12 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt14
- Asterisk update

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt13
- Asterisk update

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt12
- Asterisk update

* Fri Sep 03 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt11
- Asterisk update

* Wed Aug 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt10
- Asterisk update

* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt9
- Asterisk update

* Sat Jul 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt8
- Asterisk update

* Sat Jul 17 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt7
- Asterisk update

* Wed May 05 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt6
- fix build

* Wed May 05 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt5
- Asterisk update

* Sun Apr 25 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt4
- add requires to usb_modeswitch

* Sun Apr 25 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt3
- rename to asterisk1.6.2-chan_datacard

* Sat Apr 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt2
- cleanups
- build for Sisyphus

* Fri Apr 09 2010 Alex Radetsky <rad@rad.kiev.ua>
- Initial RPM package
