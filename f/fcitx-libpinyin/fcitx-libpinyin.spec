Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat rpm-macros-qt5-webengine
BuildRequires: gcc-c++ qt5-base-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		fcitx-libpinyin
Version:	0.5.4
Release:	alt1_8
Summary:	Libpinyin Wrapper for Fcitx
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Libpinyin
Source0:	http://download.fcitx-im.org/fcitx-libpinyin/%{name}-%{version}_dict.tar.xz

BuildRequires:	gcc
BuildRequires:	libpinyin-devel >= 1.9.91
BuildRequires:	ctest cmake, fcitx-devel, gettext-tools, intltool, libpinyin-devel
BuildRequires:	libpinyin-tools glib2-devel libgio libgio-devel, fcitx
BuildRequires:	qt5-webengine-devel, libdbus-devel
BuildRequires:	fcitx-qt5-devel >= 1.1
Requires:	fcitx
Source44: import.info
ExclusiveArch: %qt5_qtwebengine_arches
# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches

%description
Fcitx-libpinyin is a libpinyin Wrapper for Fcitx.

Libpinyin is a Frontend of the Intelligent Pinyin IME Backend.


%prep
%setup -q -n %{name}-%{version}


%build
%{fedora_v2_cmake}
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%doc --no-dereference COPYING
%{_libdir}/fcitx/%{name}.so
%{_libdir}/fcitx/qt/*.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/imicon/*
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/inputmethod/*-libpinyin.conf
%{_datadir}/fcitx/libpinyin/
%{_datadir}/icons/hicolor/48x48/status/fcitx-*.png

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.5.4-alt1_8
- update to new release by fcimport

* Wed Feb 02 2022 Igor Vlasenko <viy@altlinux.org> 0.5.4-alt1_3
- support for qt5_qtwebengine_arches (closes: #41842)

* Thu Oct 14 2021 Igor Vlasenko <viy@altlinux.org> 0.5.4-alt1_2
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_11
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_5
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_3
- update to new release by fcimport

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2.92-alt2
- build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.92-alt1_2
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.92-alt1_1
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.90-alt1_1
- initial fc import

