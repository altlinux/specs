Name: xmms-skins
Version: 1.1
Release: alt2
Summary: selected best XMMS skins
License: GPL
Group: Sound
BuildArchitectures: noarch
Source0: Antares_1a.wsz
Source1: detone_blue.zip
Source2: detone_green.zip
Source3: myxmms-default-1.01.tar.gz
Source4: xliquidxmms-default-1.0.6.tar.gz
Source5: yummiyogurtxmms-default-1.tar.gz
Source6: wmp.zip
Obsoletes: xmms-skin-wmp
Provides: xmms-skin-wmp
Requires: xmms
Prefix: %prefix
%description
Skins for xmms. Install this package. Browse with Options/Skin browser.
This package contains a small set of most beautiful skins.

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE0 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE1 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE2 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE3 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE4 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE5 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE6 $RPM_BUILD_ROOT%_datadir/xmms/Skins


cat >README << EOF
This package is a collection of skins for xmms.
Most of them come from http://www.xmms.org
If you would like even more of them you can visit sites like:
  http://www.skinz.org
  http://www.customize.org

If you like skins, please consider installing the package xmms-kjofol-skins
which enable the import of skins for k-jofol.
EOF

%files
%_datadir/xmms/Skins
%doc README

%changelog
* Wed Aug 11 2004 Nick S. Grechukh <gns@altlinux.ru> 1.1-alt2
- packaging policy changed: now this package contains only few skins, which are manually selected. More skins will be available in separate packages.

* Wed Apr 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.1-alt1
- Added few skins.

* Fri Dec 22 2000 Kostya Timoshenko <kt@petr.kz>
- Build for RE

* Thu Aug 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-7mdk
- added Packager tag

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-6mdk
- BM
- macros

* Tue Jun 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-5mdk
- added dependency to unzip
- added 4 of the top skins of http://www.xmms.org

* Mon Apr 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-4mdk
- documentation

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-3mdk
- new groups

* Thu Feb 03 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0.0-2mdk
- split skins into its own rpm spec file; so we can set it to noarch
