# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		fcitx-chewing
Version:	0.2.3
Release:	alt1_1
Summary:	Chewing Wrapper for Fcitx
Group:		System/Libraries
License:	GPLv2+
URL:		https://fcitx-im.org/wiki/Chewing
Source0:	http://download.fcitx-im.org/fcitx-chewing/%{name}-%{version}.tar.xz

BuildRequires:	ctest cmake, fcitx-devel gettext gettext-tools, intltool, libchewing-devel
Requires:	fcitx, fcitx-data
Source44: import.info

%description
Fcitx-chewing is a Chewing Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese 
Phonetic IME.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -pv build
pushd build
%{fedora_cmake} ..
%make_build VERBOSE=1

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README COPYING
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/chewing.conf
%{_datadir}/fcitx/imicon/*.png
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/skin/classic/chewing.png
%{_datadir}/fcitx/skin/dark/chewing.png
%{_datadir}/fcitx/skin/default/chewing.png
%{_datadir}/icons/hicolor/48x48/apps/fcitx-chewing.png

%changelog
* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_1
- update to new version by fcimport

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.1.3-alt2
- build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_3
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_2
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_1
- initial fc import

