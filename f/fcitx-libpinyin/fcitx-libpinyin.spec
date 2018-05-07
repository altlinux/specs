# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ qt5-base-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		fcitx-libpinyin
Version:	0.5.3
Release:	alt1_3
Summary:	Libpinyin Wrapper for Fcitx
Group:		System/Libraries
License:	GPLv2+
URL:		https://fcitx-im.org/wiki/Libpinyin
Source0:	http://download.fcitx-im.org/fcitx-libpinyin/%{name}-%{version}_dict.tar.xz

BuildRequires:	libpinyin-devel >= 1.9.91
BuildRequires:	ctest cmake, fcitx-devel gettext gettext-tools, intltool, libpinyin-devel
BuildRequires:	libpinyin-tools glib2-devel libgio libgio-devel, fcitx
BuildRequires:	qt5-webengine-devel, libdbus-devel
BuildRequires:	fcitx-qt5-devel >= 1.1
Requires:	fcitx
Source44: import.info
# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches

%description
Fcitx-libpinyin is a libpinyin Wrapper for Fcitx.

Libpinyin is a Frontend of the Intelligent Pinyin IME Backend.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -pv build
pushd build
%{fedora_cmake} ..
make VERBOSE=1 %{?_smp_mflags}
popd

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

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

