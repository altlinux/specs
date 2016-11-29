# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xprop gcc-c++ imake java-devel-default libXt-devel pkgconfig(dbus-1) xorg-cf-files
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global major_version 0.33
%global minor_version 2
%global libver 5.0.0

Name:       java-atk-wrapper
Version:    %{major_version}.%{minor_version}
Release:    alt1_2jpp8
Summary:    Java ATK Wrapper

Group:      Development/Other
License:    LGPLv2+
URL:        http://git.gnome.org/browse/java-atk-wrapper
Source0:    http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
# this is a fedora-specific file
# needed to explain how to use java-atk-wrapper with different java runtimes
Source1:    README.fedora
Patch1:		removeNotExistingManifestInclusion.patch

BuildRequires:  java-devel

BuildRequires: libatk-devel libatk-gir-devel
BuildRequires: GConf libGConf-devel libGConf-gir-devel
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires:  xorg-utils
BuildRequires: gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:  at-spi2-atk-devel
BuildRequires: libat-spi2-core-devel libat-spi2-core-gir-devel


Requires:   java
Requires:   xorg-utils
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
%setup -q
%patch1
# Source contains a pre-built AtkWrapper.java with incorrect path to xprop (should 
# be in /usr/bin/ not /opt/X11/bin/). The real source file is AtkWrapper.java.in, 
# so explicitly remove the pre-built file before building.
rm wrapper/org/GNOME/Accessibility/AtkWrapper.java

%build
%configure
make -j2
cp %{SOURCE1} .

%install
# java-atk-wrapper's make install is broken by design
# it installs to the current JDK_HOME. We want to install it to a central
# location and then allow all/any JRE's/JDK's to use it.
# make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_libdir}/%{name}

mv wrapper/java-atk-wrapper.jar %{buildroot}%{_libdir}/%{name}/
mv jni/src/.libs/libatk-wrapper.so.%{libver} %{buildroot}%{_libdir}/%{name}/
ln -s %{_libdir}/%{name}/libatk-wrapper.so.%{libver} \
    %{buildroot}%{_libdir}/%{name}/libatk-wrapper.so.0


%files
%doc AUTHORS
%doc COPYING.LESSER
%doc NEWS
%doc README
%doc README.fedora
%{_libdir}/%{name}/


%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt1_2jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.33.2-alt1_0jpp8
- java 8 mass update

* Wed Jun 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.30.4-alt2_4jpp7
- converted from JPackage by jppimport script

* Wed Apr 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.30.4-alt1_3jpp7
- converted from JPackage by jppimport script

