%brp_strip_none %_bindir/*
%brp_strip_none %browser_plugins_path/*
%set_verify_elf_method textrel=relaxed
%def_enable include_x86_64

Name: adobe-flash-player
%define bin_name mozilla-plugin-adobe-flash
%define ver_fake 11
%define ver_ix86 11.2.202.336
%define ver_x86_64 11.2.202.336
Release: alt10
Serial: 2

%define ver_real %ver_fake
%ifarch x86_64
%define ver_real %ver_x86_64
%endif
%ifarch %ix86
%define ver_real %ver_ix86
%endif
Version: %ver_fake

Group: Networking/WWW
Summary: Adobe Flash Player
URL: http://www.adobe.com/products/flashplayer/
License: Commercial

ExclusiveArch: %ix86 x86_64
BuildRequires: rpm-macros-browser-plugins libXt libgtk+2-devel fontconfig desktop-file-utils

Source: LICENSE
Source2: adobe_flash_player_eula.desktop.in
#
Source10: flash_player-x86_64-%ver_x86_64.tar
Source11: flash_player-x86-%ver_ix86.tar

%description
Adobe Flash Player %version (Macromedia Flash)
Fully Supported: Mozilla 1.0+, Netscape 7.x, Firefox 0.8+
Partially Supported: Opera, Konqueror 3.x

See the end user license in
  %_docdir/%name-%version/LICENSE.txt
See the distribution license in
  http://www.adobe.com/licensing/distribution/license/

%package -n %bin_name
Version: %ver_real
Group: Networking/WWW
Summary: Adobe Flash Player
Requires: libcurl /usr/bin/xdg-open
Provides: flash-plugin = %version-%release
Obsoletes: flash-plugin < %version-%release
Provides: mozilla-plugin-macromedia-flash = %version-%release
Obsoletes: mozilla-plugin-macromedia-flash < %version-%release
%description -n %bin_name
Adobe Flash Player %version (Macromedia Flash)
Fully Supported: Mozilla 1.0+, Netscape 7.x, Firefox 0.8+
Partially Supported: Opera, Konqueror 3.x

See the end user license in
  %_docdir/%name-%version/LICENSE.txt
See the distribution license in
  http://www.adobe.com/licensing/distribution/license/

%package fake
Version: %ver_fake
Group: Networking/WWW
Summary: fake
%description fake
fake


%prep
%setup -Tqcn install_flash_player_10_linux
%ifarch x86_64
%if_enabled include_x86_64
tar xfv %SOURCE10
%endif
%else
tar xfv %SOURCE11
%endif
install -m 0644 %SOURCE0 LICENSE.txt


%build

%install
mkdir -p -m 0755 %buildroot/%browser_plugins_path
%ifarch x86_64
%if_enabled include_x86_64
install -m 0644 libflashplayer.so %buildroot/%browser_plugins_path
%endif
%else
install -m 0644 libflashplayer.so %buildroot/%browser_plugins_path
%endif

# install flash-player-properties
mkdir -p %buildroot/{%_bindir,%_desktopdir,%_miconsdir,%_niconsdir,%_liconsdir}
install -m0755 ./%_bindir/flash-player-properties %buildroot/%_bindir/
desktop-file-install -m 0644 --dir %buildroot/%_desktopdir \
    --add-category=X-PersonalSettings \
    --remove-key=NotShowIn \
    ./%_desktopdir/flash-player-properties.desktop
for icondir in %_miconsdir %_niconsdir %_liconsdir
do
    install -m 0644 ./$icondir/flash-player-properties.png %buildroot/$icondir/
done


# menu
mkdir -p -m0755 %buildroot/%_desktopdir
cat %SOURCE2 | sed 's|%%PATH%%|%{_docdir}/%{bin_name}-%{ver_real}/LICENSE.txt|' > adobe_flash_player_eula.desktop
install -m0644 adobe_flash_player_eula.desktop %buildroot/%_desktopdir/

%ifarch x86_64
%if_disabled include_x86_64
%post -n %bin_name
echo "At this moment you must install manually nspluginwrapper and i586-%name (see bugs 23876 23877 23878 23903)"
%endif
%endif

%files -n %bin_name
%_bindir/flash-player-properties
%_desktopdir/flash-player-properties.desktop
%_iconsdir/hicolor/*/apps/flash-player-properties.*
#
%ifarch x86_64
%if_enabled include_x86_64
%doc LICENSE*
%browser_plugins_path/*
%_desktopdir/adobe_flash_player_eula.desktop
%endif
%else
%doc LICENSE*
%browser_plugins_path/*
%_desktopdir/adobe_flash_player_eula.desktop
%endif

%changelog
* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt10
- security fixes:
  CVE-2012-2034, CVE-2012-2035, CVE-2012-2036, CVE-2012-2037,
  CVE-2012-2038, CVE-2012-2039, CVE-2012-2040

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt9
- 11.2.202.335 (x86,x86-64)
  CVE-2012-0779

* Mon Apr 02 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt8
- 11.2.202.228 (x86,x86-64)

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt7
- CVE-2012-0768, CVE-2012-0769

* Thu Feb 16 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt5.M60P.1
- built for M60P

* Thu Feb 16 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt6
- 11.1.102.62 (x86,x86-64)
- security fixes:
  CVE-2012-0751, CVE-2012-0752, CVE-2012-0753, CVE-2012-0754,
  CVE-2012-0755, CVE-2012-0756, CVE-2012-0767

* Thu Dec 01 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt4.M60P.1
- built for M60P

* Thu Dec 01 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt5
- update license text

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt3.M60P.1
- built for M60P

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt4
- 11.1.102.55 (x86,x86-64)
- security fixes:
  CVE-2011-2445, CVE-2011-2450, CVE-2011-2451, CVE-2011-2452,
  CVE-2011-2453, CVE-2011-2454, CVE-2011-2455, CVE-2011-2456,
  CVE-2011-2457, CVE-2011-2458, CVE-2011-2459, CVE-2011-2460

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt2.M60P.1
- built for M60P

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt3
- 11.0.1.152 (x86,x86-64)

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt2
- use brp_strip_none instead of set_strip_method

* Mon Sep 26 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt1
- 11.0.1.129 (x86,x86-64)

* Fri Aug 26 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt13
- new version 11.0.1.98(x86)

* Fri Aug 12 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt11.M51.1
- built for M51

* Thu Aug 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt12
- new version 10.3.183.5(x86), 11.0.1.98(x86-64)
- security fixes:
  CVE-2011-2130, CVE-2011-2134, CVE-2011-2135, CVE-2011-2136,
  CVE-2011-2137, CVE-2011-2138, CVE-2011-2139, CVE-2011-2140,
  CVE-2011-2414, CVE-2011-2415, CVE-2011-2416, CVE-2011-2417,
  CVE-2011-2425

* Thu Jul 14 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt11
- new beta 11.0.1.60 (64-bit only)

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt9.M51.1
- built for M51

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt10
- new version 10.3.181.22 (32-bit only)

* Sun May 29 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt9
- fix path to LICENSE.txt

* Fri May 20 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt8
- fix desktop-file premissions

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt6.M51.1
- build for M51

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt7
- package flash-player-properties

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt6
- new version 10.3.181.14(x86-32)
- only 32-bit security fixes:
  CVE-2011-0579, CVE-2011-0618, CVE-2011-0619, CVE-2011-0620,
  CVE-2011-0621, CVE-2011-0622, CVE-2011-0623, CVE-2011-0624,
  CVE-2011-0625, CVE-2011-0626, CVE-2011-0627

* Mon Apr 18 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt4.M51.1
- build for M51

* Mon Apr 18 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt5
- new version 10.2.159.1(x86-32)

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt3.M51.1
- build for M51

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt4
- fix build requires

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt2.M51.1
- build for M51

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt3
- new version 10.2.153.1(x86-32)

* Tue Feb 15 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt1.M51.1
- build for M51

* Mon Feb 14 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt2
- new version 10.2.152.27(x86-32)

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 1:10-alt0.M51.1
- built for M51

* Fri Dec 03 2010 Sergey V Turchin <zerg@altlinux.org> 1:10-alt1
- new version
- package different versions for ix86(10.1.102.65) and x86_64(10.3.162.29)

* Thu Sep 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.23-alt0.M51.1
- built for M51

* Thu Sep 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.23-alt1
- CVE-2010-2884

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.22-alt0.M51.1
- built for M51

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.22-alt1
- 10.2.161.22 beta
- package 64-bit version too

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt3
- fix conflicts with i586-%name

* Wed Aug 18 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt2
- don't package 64-bit version

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt0.M51.1
- built for M51

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt1
- only 32-bit new version
- CVE-2010-0209 CVE-2010-2188 CVE-2010-2213 CVE-2010-2214 CVE-2010-2215
  CVE-2010-2216

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.53.64-alt0.M51.1
- built for M51

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.53.64-alt1
- only 32-bit new version (ALT#17168)
- only 32-bit fixes CVE-2008-4546 CVE-2009-3793 CVE-2010-1297 CVE-2010-2160
  CVE-2010-2161 CVE-2010-2162 CVE-2010-2163 CVE-2010-2164 CVE-2010-2165
  CVE-2010-2166 CVE-2010-2167 CVE-2010-2169 CVE-2010-2170 CVE-2010-2171
  CVE-2010-2172 CVE-2010-2173 CVE-2010-2174 CVE-2010-2175 CVE-2010-2176
  CVE-2010-2177 CVE-2010-2178 CVE-2010-2179 CVE-2010-2180 CVE-2010-2181
  CVE-2010-2182 CVE-2010-2183 CVE-2010-2184 CVE-2010-2185 CVE-2010-2186
  CVE-2010-2187 CVE-2010-2188 CVE-2010-2189

* Wed Feb 17 2010 Sergey V Turchin <zerg@altlinux.org> 10.0.45.2-alt0.M51.1
- built for M51

* Wed Feb 17 2010 Sergey V Turchin <zerg@altlinux.org> 10.0.45.2-alt1
- new version
- fix requires

* Wed Dec 09 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.42.34-alt0.M51.1
- built for M51

* Wed Dec 09 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.42.34-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt4
- fix requires

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt3
- don't use old netscape plugins placement

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt2
- move to more accessible place

* Tue Aug 11 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt1
- new version

* Thu Jun 25 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.22.87-alt2
- add x86_64 version

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 10.0.22.87-alt0.M41.1
- built for M41

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 10.0.22.87-alt1
- security update (SA34012)

* Fri Dec 19 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.15.3-alt1
- new version
- remove deprecated macroses from specfile

* Fri Oct 31 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.12.36-alt2
- add libcurl to requires

* Wed Oct 15 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.12.36-alt1
- new version

* Thu Apr 10 2008 Sergey V Turchin <zerg at altlinux dot org> 9.0.124.0-alt2
- fix src tarball file permissions

* Wed Dec 05 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.115.0-alt1
- new version

* Fri Aug 17 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt3
- fix path to license in desktop-file

* Thu Jul 12 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt2
- add Categories parameter to desktop-file

* Thu Jul 12 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt1
- new version

* Mon Jan 22 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.31.0-alt2
- fix license && package description

* Fri Jan 19 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.31.0-alt1
- release 9.0.31.0

* Thu Oct 26 2006 Sergey V Turchin <zerg at altlinux dot org> 9.0.21.55-alt0.1.beta
- new beta version

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 7.0.63-alt1
- new version

* Wed Dec 28 2005 Sergey V Turchin <zerg at altlinux dot org> 7.0.61-alt1
- new version

* Thu Jan 06 2005 Alexey Gladkov <legion@altlinux.ru> 7.0.25-alt1.1
- browser-plugins-npapi support added;

* Fri May 28 2004 Sergey V Turchin <zerg at altlinux dot org> 7.0.25-alt1
- new version

* Thu May 27 2004 Sergey V Turchin <zerg at altlinux dot org> 6.0.81-alt2
- fix menu section

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 6.0.81-alt1
- new version
- add menufile to show license

* Fri Aug 01 2003 Sergey V Turchin <zerg at altlinux dot org> 6.0.79-alt1
- new version

* Tue Feb 11 2003 Sergey V Turchin <zerg@altlinux.ru> 6.0.69-alt1
- initial spec
