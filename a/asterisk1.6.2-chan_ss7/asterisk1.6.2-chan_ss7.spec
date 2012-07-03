%define ast_version %{get_version asterisk1.6.2-devel}

Name: asterisk1.6.2-chan_ss7
Summary: SS7 channel module for Asterisk
Version: 2.0.0
Release: alt4
License: GPL
Group: System/Servers
Url: http://www.netfors.com/download

%define modules_dir %_libdir/asterisk/%ast_version/modules

Source: %name-%version.tar

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: asterisk1.6.2 = %ast_version

BuildRequires(pre): asterisk1.6.2-devel

# Automatically added by buildreq on Mon Sep 14 2009
BuildRequires: asterisk1.6.2-devel dahdi-linux-headers

%description
%summary

%prep
%setup

%build
export INCLUDE=-I/usr/include/asterisk-%ast_version
%make_build chan_ss7.so

%install
install -D -m 0640 chan_ss7.so %buildroot%modules_dir/chan_ss7.so

%files
%doc ss7.conf* README NEWS ASTERISK_VARIABLES
%attr(0440,root,_asterisk) %modules_dir/chan_ss7.so

%changelog
* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 2.0.0-alt4
- Asterisk update

* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 2.0.0-alt3
- Asterisk update

* Fri Jul 15 2011 Denis Smirnov <mithraen@altlinux.ru> 2.0.0-alt2
- Asterisk update

* Fri Feb 18 2011 Denis Smirnov <mithraen@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Thu Feb 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt25
- Asterisk update

* Wed Feb 09 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt24
- Asterisk update

* Fri Jan 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt23
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt22
- Asterisk update

* Mon Dec 20 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt21
- Asterisk update

* Sun Dec 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt20
- Asterisk update

* Sat Nov 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt19
- Asterisk update

* Fri Nov 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt18
- Asterisk update

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt17
- Asterisk update

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt16
- Asterisk update

* Fri Sep 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt15
- Asterisk update

* Wed Aug 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt14
- Asterisk update

* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt13
- Asterisk update

* Sat Jul 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt12
- Asterisk update

* Sat Jul 17 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt11
- Asterisk update

* Wed May 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt10
- Asterisk update

* Sun Mar 28 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt9
- Asterisk update

* Wed Mar 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt8
- fix build

* Wed Mar 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt7
- use get_version for Asterisk version instead of hardcode to spec

* Fri Feb 26 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt6
- Asterisk update

* Fri Feb 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt5
- Asterisk update

* Fri Feb 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt4
- Asterisk update

* Fri Feb 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt3
- Asterisk update

* Fri Feb 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt2
- Asterisk update

* Wed Jan 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt1.1
- rebuild with new Asterisk

* Sat Dec 19 2009 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Tue Sep 15 2009 Denis Smirnov <mithraen@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Mon Sep 14 2009 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt1
- first build for Sisyphus
