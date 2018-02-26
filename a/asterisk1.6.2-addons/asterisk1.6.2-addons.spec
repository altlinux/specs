%define ast_version %{get_version asterisk1.6.2-devel}

Name: asterisk1.6.2-addons
Summary: Asterisk addons
Version: 1.6.2.3
Release: alt3
License: GPL
Group: System/Servers
Url: http://www.asterisk.org/

%define modules_dir %_libdir/asterisk/%ast_version/modules

Source: %name-%version.tar

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: asterisk1.6.2 = %ast_version

BuildRequires(pre): asterisk1.6.2-devel

# Automatically added by buildreq on Sun Oct 24 2010 (-bb)
BuildRequires: asterisk1.6.2-devel gcc-c++ libbluez-devel libmysqlclient-devel libncurses-devel libnewt-devel

%description
%summary

%prep
%setup

%build
export CFLAGS=-I%_includedir/asterisk-%ast_version
export ASTCFLAGS=-I%_includedir/asterisk-%ast_version
./configure
%make_build

%install
export DESTDIR=%buildroot
export MODULE_DIR=%modules_dir
export ASTDATADIR=/var/lib/asterisk
mkdir -p %buildroot/"${ASTDATADIR}/documentation"
mkdir -p %buildroot%modules_dir

%make_install install

mv %buildroot/usr/lib/asterisk/modules/*.so %buildroot%modules_dir/

%files
/var/lib/asterisk/documentation/addons-en_US.xml
%attr(0440,root,_asterisk) %modules_dir/res_config_mysql.so
%attr(0440,root,_asterisk) %modules_dir/app_addon_sql_mysql.so
%attr(0440,root,_asterisk) %modules_dir/cdr_addon_mysql.so
%attr(0440,root,_asterisk) %modules_dir/app_saycountpl.so
%attr(0440,root,_asterisk) %modules_dir/chan_ooh323.so
%attr(0440,root,_asterisk) %modules_dir/format_mp3.so
%attr(0440,root,_asterisk) %modules_dir/chan_mobile.so

%changelog
* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.3-alt3
- Asterisk update

* Fri Jul 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.3-alt2
- Asterisk update

* Thu Feb 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.3-alt1
- 1.6.2.3

* Wed Feb 09 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.2-alt6
- Asterisk update

* Fri Jan 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.2-alt5
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.2-alt4
- Asterisk update

* Mon Dec 20 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.2-alt3
- Asterisk update

* Sun Dec 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.2-alt2
- Asterisk update

* Sat Nov 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.2-alt1
- 1.6.2.2

* Sat Nov 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt16
- Asterisk update

* Fri Nov 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt15
- Asterisk update

* Fri Nov 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt14
- Asterisk update

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt13
- fix build

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt12
- Asterisk update

* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt11
- rebuild with new libmysqlclient

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt10
- Asterisk update

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt9
- Asterisk update

* Fri Sep 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt8
- Asterisk update

* Wed Aug 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt7
- Asterisk update

* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt5
- Asterisk update

* Sat Jul 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt4
- Asterisk update

* Sat Jul 17 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt3
- Asterisk update

* Wed May 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt2
- Asterisk update

* Sat Apr 17 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.1-alt1
- 1.6.2.1

* Sun Mar 28 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt9
- Asterisk update

* Wed Mar 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt8
- fix build

* Wed Mar 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt7
- use get_version for Asterisk version instead of hardcode to spec

* Fri Feb 26 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt6
- Asterisk update

* Fri Feb 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt5
- Asterisk update

* Sat Feb 06 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt4
- fix summary 

* Fri Feb 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt3
- Asterisk update

* Fri Feb 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt2
- Asterisk update

* Wed Jan 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt1.1
- rebuild with new asterisk

* Sat Dec 26 2009 Denis Smirnov <mithraen@altlinux.ru> 1.6.2.0-alt1
- first build for Sisyphus
