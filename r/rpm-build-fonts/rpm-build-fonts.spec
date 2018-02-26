Name: rpm-build-fonts
Version: 0.6
Release: alt4

Summary: RPM helper scripts for building font packages

License: GPL
Group: Development/Other
URL: http://www.altlinux.org/Fonts_Policy

# Git repo http://git.altlinux.org/people/{lav,viy}/packages/rpm-build-fonts.git
Source: %name-%version.tar

BuildArch: noarch

# for ttf, type1 fonts indexing
Requires: mkfontscale mkfontdir
# for mkfontscale, mkfontdir to work correctly
Requires: xorg-font-encodings
# for fontconfig.prov
Requires: /usr/bin/fc-query

Requires: rpm-macros-fonts = %version-%release

%description
RPM helper scripts and build environment
for building fonts packages.

See %url for detailed fonts packaging policy.

%package -n rpm-macros-fonts
Summary: RPM helper macros for building font packages

License: GPL
Group: Development/Other

%description -n rpm-macros-fonts
RPM marcos for building fonts packages.
It introduced ttf_fonts_install, type_fonts_install,
bitmap_fonts_install, otf_fonts_install,
post_fonts, postun_fonts macros.

See %url for detailed fonts packaging policy.

%prep
%setup

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/fonts
install -D -m755 fontconfig.prov %buildroot/usr/lib/rpm/fontconfig.prov
install -D -m755 fontconfig.prov.files %buildroot/usr/lib/rpm/fontconfig.prov.files

%files
%doc EXAMPLE.ALT
/usr/lib/rpm/fontconfig.prov
/usr/lib/rpm/fontconfig.prov.files

%files -n rpm-macros-fonts
%_rpmmacrosdir/fonts

%changelog
* Sat May 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt4
- enabled fontlang provides for en,ru,uk,be

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3
- bugfix: enabled fontlang provides for japanese

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2
- bugfix for fontconfig.prov

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- added rpm-macros-fonts subpackage
- added fontconfig.prov

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2
- added req: xorg-font-encodings
  for mkfontscale, mkfontdir to work correctly

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- new font policy: post/un font macros are obsolete

* Wed Mar 30 2011 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt4
- replace xorg-x11-font-utils with mkfontscale, mkfontdir requires

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt3
- small cleanup for rebuild

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- fix URL, cleanup

* Thu Dec 10 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- use quoted file list

* Mon Jul 13 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt2
- add EXAMPLE.ALT doc, rebuild from gear repo

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- add support for new ALT font policy (patch from Valery V. Inozemtsev <shrek@>)

* Sat May 19 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- small fixes

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
