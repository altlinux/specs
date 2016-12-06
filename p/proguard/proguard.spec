Name: proguard
Summary: Java class file shrinker, optimizer, obfuscator, and preverifier
Version: 5.3.2
Release: alt1
License: GPL
Group: Development/Java
BuildArch: noarch
BuildRequires: ant checkstyle tzdata log4j slf4j rpm-build-java java-devel-default
BuildRequires: /proc
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Url: http://proguard.sourceforge.net/

Patch: %name-%version-%release.patch
Source100: %name.watch
Source101: %name.desktop
Source102: %{name}16.png
Source103: %{name}32.png
Source104: %{name}48.png

Requires: java-headless

%description
Java class file shrinker, optimizer, obfuscator, and preverifier

%package manual
Group: Development/Java
Summary: Manual for %{name}

%description manual
The manual for %{name}.

%package gui
Group: Development/Java
Summary: GUI for %{name}
Requires:       %{name} = %{version}
Requires: java

%description gui
A GUI for %{name}.

%prep
%setup
%patch -p1

# remove all jar and class files, the snippet from Packaging:Java does 
# not work
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

# remove the Class-Path from MANIFESTs
sed -i '/class-path/I d' src/%{name}/gui/MANIFEST.MF
sed -i '/class-path/I d' src/%{name}/retrace/MANIFEST.MF

%build
pushd buildscripts
ant \
	-Djdk.javadoc=%{_javadocdir}/java

%install
mkdir -p %buildroot%_javadir/%{name}/
cp -p lib/%{name}.jar %buildroot%_javadir/%{name}/%{name}.jar
cp -p lib/%{name}gui.jar %buildroot%_javadir/%{name}/%{name}gui.jar
cp -p lib/retrace.jar %buildroot%_javadir/%{name}/retrace.jar

mkdir -p %buildroot%_bindir
%jpackage_script proguard.ProGuard "" "" proguard proguard true
%jpackage_script proguard.gui.ProGuardGUI "" "" proguard proguard-gui true
%jpackage_script proguard.retrace.ReTrace "" "" proguard proguard-retrace true

# proguard-gui
install -m 644 -D %{SOURCE101} %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir}
cp -p %{SOURCE102} %buildroot%_miconsdir/%{name}.png
cp -p %{SOURCE103} %buildroot%_niconsdir/%{name}.png
cp -p %{SOURCE104} %buildroot%_liconsdir/%{name}.png

%files
%doc README
%dir %_javadir/%{name}
%_javadir/%{name}/proguard.jar
%_javadir/%{name}/retrace.jar
%_bindir/proguard
%_bindir/proguard-retrace

%files manual
%doc docs/*

%files gui
%_bindir/%{name}-gui
%_javadir/%{name}/proguardgui.jar
%_desktopdir/%name.desktop
%_miconsdir/%{name}.png
%_niconsdir/%{name}.png
%_liconsdir/%{name}.png

%changelog
* Tue Dec 06 2016 Cronbuild Service <cronbuild@altlinux.org> 5.3.2-alt1
- new version 5.3.2

* Tue Oct 25 2016 Cronbuild Service <cronbuild@altlinux.org> 5.3.1-alt1
- new version 5.3.1

* Sun Sep 25 2016 Cronbuild Service <cronbuild@altlinux.org> 5.3-alt1
- new version 5.3

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt2
- java8 mass update: 
- jar files moved to subdir (required by sbt)
- added manual
- moved gui to subpackage 
- renamed /usr/bin/retrace to proguard-retrace

* Tue Mar 24 2015 Denis Smirnov <mithraen@altlinux.ru> 5.2.1-alt1
- new version 5.2.1

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 5.2-alt1
- new version 5.2

* Thu Oct 30 2014 Cronbuild Service <cronbuild@altlinux.org> 5.1-alt1
- new version 5.1

* Thu Sep 04 2014 Denis Smirnov <mithraen@altlinux.ru> 5.0-alt1
- new version 5.0

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 4.11-alt2
- chackstyle4 is dropped; use chackstyle5.

* Sun Dec 29 2013 Cronbuild Service <cronbuild@altlinux.org> 4.11-alt1
- new version 4.11

* Fri Aug 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.10-alt1
- new version 4.10
- add cronbuild support

* Wed Apr 10 2013 Denis Smirnov <mithraen@altlinux.ru> 4.9-alt1
- 4.9

* Fri Jan 25 2013 Denis Smirnov <mithraen@altlinux.ru> 4.8-alt2
- add Url tag

* Fri Oct 12 2012 Denis Smirnov <mithraen@altlinux.ru> 4.8-alt1
- 4.8

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 4.6-alt1
- 4.6

* Mon Nov 09 2009 Denis Smirnov <mithraen@altlinux.ru> 4.4-alt1
- first build for Sisyphus

