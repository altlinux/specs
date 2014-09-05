# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: fcitx-cloudpinyin
Version: 0.3.0
Release: alt2
Summary: Cloudpinyin module for fcitx
Group: System/Libraries
License: GPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://code.google.com/p/fcitx/
Source0: http://fcitx.googlecode.com/files/%name-%version.tar.xz
Patch0: %name-0.3.0-logging.patch

BuildRequires: ctest cmake fcitx-devel gettext intltool libcurl-devel
Requires: fcitx
Source44: import.info

%description
Cloulpinyin is an based cloud compute input method.

%prep
%setup -n %name-%version
%patch0 -p1 -b .logging

%build
mkdir -pv build
pushd build
%fedora_cmake ..
make %{?_smp_mflags} VERBOSE=1
popd

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
popd

%find_lang %name

%files -f %name.lang
%doc README COPYING
%_datadir/fcitx/configdesc/*.desc
%_datadir/fcitx/addon/*.conf
%_libdir/fcitx/*.so

%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.3.0-alt2
- build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_4
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_2
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_1
- initial fc import

