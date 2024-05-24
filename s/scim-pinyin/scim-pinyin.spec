# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: scim-pinyin
Version: 0.5.92
Release: alt2.qa1
Summary: Smart Pinyin IMEngine for Smart Common Input Method platform
Packager: Ilya Mashkin <oddity@altlinux.ru>
License: GPLv2
Group: System/Libraries
Url: https://github.com/scim-im/scim-pinyin
Source0: http://dl.sourceforge.net/scim/%name-%version.tar.gz

BuildRequires: scim-devel gtk2-devel gettext gettext-devel autoconf automake libtool
Requires: scim
Obsoletes: iiimf-le-chinput <= 0.3, miniChinput <= 0.0.3
Patch2: scim-pinyin-showallkeys.patch
# Patch3:         scim-pinyin-helper.patch
# Patch4:         scim-pinyin-0.5.91-13.bz200702.patch
# Patch5:         scim-pinyin-help-translate.patch
Patch6: scim-pinyin-0.5.91-save-in-temp.patch
Patch7: scim-pinyin-0.5.91-fix-load.patch
Patch8: scim-pinyin-0.5.91-fix-ms-shuangpin.patch
Source44: import.info
#Patch9:         scim-pinyin-0.5.91-gcc43.patch

%description
Simplified Chinese Smart Pinyin IMEngine for SCIM.

%prep
%setup
%patch2 -p1 -b .2-showallkeys
# %patch3 -p1 -b .3-helperi
# %patch4 -p1 -b .4-bz200702
# %patch5 -p1 -b .5-translate
%patch6 -p1 -b .6-savetmp
%patch7 -p1 -b .6-fix-load
%patch8 -p1 -b .8-fix-ms-shuangpin
#%patch9 -p1 -b .9-gcc43

%build
./bootstrap
%configure --disable-static
make -C po update-gmo
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm $RPM_BUILD_ROOT%_libdir/scim-1.0/*/{IMEngine,SetupUI}/*.la
rm -f $RPM_BUILD_ROOT%_libdir/scim-1.0/*/Helper/*.la

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README
%_libdir/scim-1.0/*/IMEngine/pinyin.so
%_libdir/scim-1.0/*/SetupUI/pinyin-imengine-setup.so
# %_libdir/scim-1.0/*/Helper/pinyin-imengine-helper.so
%_datadir/scim/pinyin
%_datadir/scim/icons/smart-pinyin.png

%changelog
* Sat Oct 17 2015 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.5.92-alt2.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.5.92-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.92-alt1_4
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.92-alt1_3
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.92-alt1_2
- initial fc import

