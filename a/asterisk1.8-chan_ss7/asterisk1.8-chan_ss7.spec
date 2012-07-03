%define ast_version %{get_version asterisk1.8-devel}

Name: asterisk1.8-chan_ss7
Summary: SS7 channel module for Asterisk
Version: 2.1.0
Release: alt8
License: GPL
Group: System/Servers
Url: http://www.netfors.com/download

%define modules_dir %_libdir/asterisk/%ast_version/modules

Source: %name-%version.tar

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: asterisk1.8 = %ast_version

BuildRequires(pre): asterisk1.8-devel

# Automatically added by buildreq on Mon Sep 14 2009
BuildRequires: asterisk1.8-devel dahdi-linux-headers

%description
%summary

%prep
%setup

%build
export INCLUDE=-I%_includedir/asterisk-%ast_version
%make_build chan_ss7.so

%install
install -D -m 0640 chan_ss7.so %buildroot%modules_dir/chan_ss7.so

%files
%doc ss7.conf* README NEWS ASTERISK_VARIABLES
%attr(0440,root,_asterisk) %modules_dir/chan_ss7.so

%changelog
* Sat May 05 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt8
- Asterisk update

* Thu Feb 09 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt7
- Asterisk update

* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt6
- Asterisk update

* Sat Dec 17 2011 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt5
- Asterisk update

* Wed Oct 26 2011 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt4
- Asterisk update

* Wed Oct 05 2011 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt3
- Asterisk update

* Sat Sep 24 2011 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt2
- 2.1.0
