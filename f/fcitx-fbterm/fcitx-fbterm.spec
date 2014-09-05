# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: fcitx-fbterm
Version: 0.2.0
Release: alt2
Summary: Fbterm Support for Fcitx
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: System/Libraries
License: GPLv2+
Url: http://code.google.com/p/fcitx/
Source0: http://fcitx.googlecode.com/files/%name-%version.tar.xz

BuildRequires: ctest cmake fcitx-devel gettext intltool libxml2-devel
BuildRequires: libdbus-glib-devel
Requires: fcitx
Source44: import.info

%description
Fcitx-fbterm is a Wrapper for Fcitx in fbterm,
a fast Framebuffer based terminal emulator.

%prep
%setup -n %name-%version

%build
mkdir -pv build
pushd build
%fedora_cmake ..
make %{?_smp_mflags} VERBOSE=1

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%files
%doc AUTHORS README COPYING
%_bindir/%name
%_bindir/%name-helper

%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2.0-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_4
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_3
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_2
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_1
- initial fc import

