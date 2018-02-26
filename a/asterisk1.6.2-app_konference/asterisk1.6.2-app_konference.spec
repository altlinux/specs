%define ast_version %{get_version asterisk1.6.2-devel}

Name: asterisk1.6.2-app_konference
Summary: Conference module for Asterisk
Version: 1.5
Release: alt10
License: GPL
Group: System/Servers
Url: http://sourceforge.net/projects/appkonference

%define modules_dir %_libdir/asterisk/%ast_version/modules

Source: %name-%version.tar

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: asterisk1.6.2 = %ast_version

BuildRequires(pre): asterisk1.6.2-devel

# Automatically added by buildreq on Sat Dec 26 2009 (-bb)
BuildRequires: asterisk1.6.2-devel

%description
%summary

%prep
%setup
sed -i "s!/usr/lib/asterisk/modules!%modules_dir!g" konference/Makefile

%build
pushd konference
export ASTERISK_INCLUDE_DIR=/usr/include/asterisk-%ast_version
%make_build

%install
pushd konference
export DESTDIR=%buildroot
export MODULE_DIR=%modules_dir
export ASTDATADIR=%buildroot/var/lib/asterisk
mkdir -p "${ASTDATADIR}/documentation"
mkdir -p %buildroot%modules_dir

%make_install INSTALL_MODULES_DIR=%buildroot%modules_dir install

%files
%doc asterikast konference/*.txt konference/README
%attr(0440,root,_asterisk) %modules_dir/app_konference.so

%changelog
* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt10
- Asterisk update

* Fri Jul 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt9
- Asterisk update

* Thu Feb 17 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt8
- Asterisk update

* Wed Feb 09 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt7
- Asterisk update

* Fri Jan 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt6
- Asterisk update

* Sat Jan 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt5
- Asterisk update

* Mon Dec 20 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt4
- Asterisk update

* Sun Dec 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt3
- Asterisk update

* Sat Nov 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt2
- Asterisk update

* Fri Nov 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt1
- 1.5

* Fri Nov 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt6
- Asterisk update

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt5
- Asterisk update

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt4
- Asterisk update

* Fri Sep 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt3
- Asterisk update

* Wed Aug 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt2
- Asterisk update

* Mon Jul 26 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt1
- 1.4
- enable G.722 support

* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt13
- Asterisk update

* Sat Jul 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt12
- Asterisk update

* Sat Jul 17 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt11
- Asterisk update

* Wed May 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt10
- Asterisk update

* Wed Mar 31 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt9
- fix summary/description (thanks to misha@)

* Sun Mar 28 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt8
- Asterisk update

* Wed Mar 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt7
- fix build

* Wed Mar 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt6
- use get_version for Asterisk version instead of hardcode to spec

* Fri Feb 26 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt5
- Asterisk update

* Fri Feb 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt4
- Asterisk update

* Fri Feb 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt3
- Asterisk update

* Fri Feb 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt2
- Asterisk update

* Wed Jan 27 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt1
- 1.3

* Wed Jan 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt1.1
- rebuild with new Asterisk

* Sat Dec 26 2009 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt1
- first build for Sisyphus
