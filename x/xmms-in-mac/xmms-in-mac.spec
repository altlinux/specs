Name: xmms-in-mac
Version: 0.3.1
Release: alt3

Summary: an input plugin for xmms to play Monkey's Audio files (APE)
Group: Sound
License: Free for personal and educational use, see documentation

Url: http://xmms-mad.sourceforge.net
Source0: xmms-in-mac-%version.tar.bz2
Source1: XMMS_MAC-ALTLinux-permission.eml
Patch0: xmms-in-mac-0.3.1-alt-new_automake.patch
Patch1: xmms-in-mac-0.3.1-alt-gcc44.patch
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

Provides: xmms-mac = %version-%release
Requires: xmms

# Automatically added by buildreq on Mon May 25 2009
BuildRequires: gcc-c++ libmac-devel libxmms-devel

BuildRequires: libxmms-devel pkg-config

%define permission_file %_defaultdocdir/%name-%version/XMMS_MAC-ALTLinux-permission.eml
%define license_file %_docdir/%name-%version/COPYING

Summary(ru_RU.UTF-8): входной плагин xmms для проигрывания файлов Monkey's Audio (APE)

%description
%name is an input plugin for xmms to play Monkey's Audio files (APE)

MAC plugin for xmms can be used freely for personal, educational
and non-commercial purposes (so as Monkey's Audio codec itself).
Commercial usage requires prior written permission from the
plugin author.

See %license_file before usage.
Author's written permission can be found in %permission_file

%description -l ru_RU.UTF-8
%name - это входной плагин xmms для проигрывания файлов Monkey's Audio (APE)

Плагин MAC для xmms может свободно использоваться в персональных, образовательных
и некоммерческих целях (так же как и сам кодек Monkey's Audio).
Коммерческое использование требует письменного согласия автора плагина.

Ознакомьтесь с %license_file перед использованием
Письменное согласие автора на распространение плагина в составе ALTLinux
находится в файле %permission_file

%define _xmms_input_plugin_dir %(xmms-config --input-plugin-dir)

%prep
%setup
install %SOURCE1 .
%patch0 -p1
%patch1 -p1

%build
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install
rm -f %buildroot%_libdir/xmms/*/*.la

%files
%_xmms_input_plugin_dir/*.so*
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO XMMS_MAC-ALTLinux-permission.eml

%changelog
* Wed May 27 2009 Michael Shigorin <mike@altlinux.org> 0.3.1-alt3
- fixed macro abuse
- cleanup *.la

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 0.3.1-alt2
- NMU: fixed FTBFS by exchanging extra autocrap for a patch

* Fri Jun 23 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3.1-alt1
- Resurrected from orphaned
- 0.3.1
- Dropped libxmms_mac-0.2.1-no_version.patch
- Patch libxmms_mac-0.2.1-new_automake.patch rediffed and renamed to
  xmms-in-mac-0.3.1-alt-new_automake.patch
- Set Packager tag

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.1-alt2.1
- Rebuilt with libstdc++.so.6.

* Fri Jul  9 2004 Alexey Morozov <morozov@altlinux.org> 0.2.1-alt2
- First 'official' build
- Added e-mail w/ written permission from SuperMMX <supermmx@163.com>

* Sun Jun 13 2004 Alexey Morozov <morozov@altlinux.org> 0.2.1-alt1
- Initial build for ALT Linux (based on xmms-in-mad-0.5.7-alt1)
