%define _unpackaged_files_terminate_build 1

Name:       java-atk-wrapper
Version:    0.44.0
Release:    alt1
Summary:    Java ATK Wrapper

License:    LGPL-3.0-or-later
Group: Development/Other
URL:        https://gitlab.gnome.org/GNOME/java-atk-wrapper
Source:    %name-%version.tar
# this is a fedora-specific file
# needed to explain how to use java-atk-wrapper with different java runtimes
Source1:    README.fedora

Patch0: fix-configure-dash-version.patch

BuildRequires(pre): rpm-macros-java
BuildRequires:	gcc-c++
BuildRequires:	clang
BuildRequires:  libatk-devel libatk-gir-devel
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  gtk-builder-convert libgail-devel libgtk+2-devel
BuildRequires:  xprop
BuildRequires:  libgail3-devel libgtk+3-devel libgtk+3-gir-devel
BuildRequires:  at-spi2-atk-devel
BuildRequires:  libat-spi2-core-devel libat-spi2-core-gir-devel
BuildRequires:  gobject-introspection-devel
BuildRequires: imake libXt-devel pkgconfig(dbus-1) xorg-cf-files
BuildRequires: /proc java-devel-default


Requires:   java
Requires:   xprop
Source44: import.info

%description
Java ATK Wrapper is a implementation of ATK by using JNI technic. It
converts Java Swing events into ATK events, and send these events to
ATK-Bridge.

JAW is part of the Bonobo deprecation project. It will replaces the
former java-access-bridge.
By talking to ATK-Bridge, it keeps itself from being affected by the
change of underlying communication mechanism.

%prep
%setup
%patch0 -p2

%build
%autoreconf
%configure \
--with-jardir=%_jnidir \
--with-propertiesdir=%_datadir/%name
%make

%install
%makeinstall_std

install -m 444 %SOURCE1 README.fedora

%check
%make check


%files
%doc AUTHORS COPYING.LESSER NEWS README README.fedora
%_libdir/libatk-wrapper.so
%_jnidir/%name.jar
%_datadir/%name

%changelog
* Mon Oct 20 2025 Artem Semenov <savoptik@altlinux.org> 0.44.0-alt1
- Updated to new version 0.44.0

* Tue Aug 05 2025 Artem Semenov <savoptik@altlinux.org> 0.42.1-alt1
- Builded new wersion 0.42.1

* Sat Mar 29 2025 Artem Semenov <savoptik@altlinux.org> 0.40.0-alt1
- Build new version 0.40.0

* Tue Aug 16 2022 Igor Vlasenko <viy@altlinux.org> 0.38.0-alt2_6jpp11
- jdk17 support

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 0.38.0-alt1_6jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0.38.0-alt1_4jpp11
- update

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 0.38.0-alt1_1jpp11
- new version

* Tue Nov 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.33.2.1-alt2_0.pre01jpp8
- updated buildrequires

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.33.2.1-alt1_0.pre01jpp8
- new version

* Wed Aug 05 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.33.2-alt6_9jpp8
- drop llvm buildreqs

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt5_9jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt5_8jpp8
- fc29 update

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt4_8jpp8
- java update

* Mon Dec 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt4_7jpp8
- fixed build

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt3_7jpp8
- fc28+ update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt2_7jpp8
- java fc28+ update

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt2_6jpp8
- make -j2 instead of %%make_build -- helps on altair

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt1_6jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt1_3jpp8
- fixed build

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt1_2jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt1_0jpp8
- java 8 mass update

* Wed Jun 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.30.4-alt2_4jpp7
- converted from JPackage by jppimport script

* Wed Apr 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.30.4-alt1_3jpp7
- converted from JPackage by jppimport script

