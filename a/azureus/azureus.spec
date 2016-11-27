# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
Obsoletes: vuse < 4.2.0.3
Conflicts: vuse < 4.2.0.3
Requires: java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global		_newname Vuze

Name:		azureus
Version:	5.7.1.0
Release:	alt1_2jpp8
Summary:	A BitTorrent Client
Group:		Networking/WWW

#Exception for using Eclipse SWT
#http://wiki.vuze.com/w/Vuze_License
License:	GPLv2 with exceptions

URL:		http://azureus.sourceforge.net

Source0:	http://downloads.sourceforge.net/azureus/%{_newname}_5710_source.zip

Source2:	Azureus.desktop
Source3:	azureus.applications

#ant build script from Azureus-4.3.0.6
Source4:	build.xml

Patch0:		azureus-remove-manifest-classpath.patch
Patch1:		azureus-no-shared-plugins.patch
Patch2:	azureus-SecureMessageServiceClientHelper-bcprov.patch

Patch4:	azureus-4.0.0.4-stupid-invalid-characters.diff

Patch5:	azureus-4.2.0.4-java5.patch

Patch6:	azureus-4.8.1.2-no-bundled-apache-commons.patch

Patch7: azureus-5.2.0.0-startupScript.patch

Patch8: azureus-5.2-no-bundled-json.patch
Patch9: azureus-5.3.0.0-no-bundled-bouncycastle
Patch10: azureus-5.4.0.0-fix_compile.patch
Patch11: vuze-5.3.0.0-disable-updaters.patch

BuildRequires:	ant jpackage-utils >= 1.5 xml-commons-apis
BuildRequires:	apache-commons-cli log4j12
BuildRequires:	apache-commons-lang
BuildRequires:	bouncycastle >= 1.33
BuildRequires:	json_simple
BuildRequires:	eclipse-swt >= 3.5
BuildRequires:	junit
Requires:	apache-commons-cli log4j12
Requires:	apache-commons-lang
Requires:	eclipse-swt >= 3.5
Requires:	 bouncycastle >= 1.33
Requires:	 java >= 1.6.0
Requires:	json_simple
BuildRequires:	 java-devel >= 1.6.0
BuildRequires:	 desktop-file-utils
Requires(post):	 desktop-file-utils
Requires(postun):	desktop-file-utils

Provides:	vuze = %{version}-%{release}

BuildArch:	noarch
Source44: import.info


%description 
Azureus (now %{_newname}) implements the BitTorrent protocol using java
and comes bundled with many invaluable features for both beginners and
advanced users.

%prep
%setup -q -c

cp %{SOURCE4} .

%patch0 -p1 -b .remove-manifest-classpath
%patch1 -p1 -b .no-shared-plugins

%patch2 -p1 -b .nobcprov

rm org/gudy/azureus2/ui/swt/osx/CarbonUIEnhancer.java
rm org/gudy/azureus2/ui/swt/osx/Start.java
rm org/gudy/azureus2/ui/swt/win32/Win32UIEnhancer.java

%patch4  -p1 -b stupid-invalid-characters

%patch5 -p1 -b .java5

%patch6 -p1 -b .no-bundled-apache-commons

%patch7 -p1 -b .startupScript

%patch8 -p1 -b .no-bundled-json
%patch9 -p1 -b .no-bundled-bouncycastle
%patch10 -p1 -b .5.4.0.0_fix_compile
%patch11 -p1 -b .disable_updaters

#hacks to org.eclipse.swt.widgets.Tree2 don't compile.
rm -fR org/eclipse

# Convert line endings...
sed -i 's/\r//' ChangeLog.txt
chmod 644 *.txt

#remove bundled libs
rm -fR org/apache
rm -fR org/bouncycastle
rm -fR org/json
#rm -fR org/pf

%build
mkdir -p build/libs
build-jar-repository -p build/libs bcprov apache-commons-cli log4j12-1.2.17 \
  junit apache-commons-lang json_simple

ln -s %_jnidir/swt.jar build/libs

ant jar

%install
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/azureus/plugins
install -pm 644 dist/Azureus2.jar $RPM_BUILD_ROOT%{_datadir}/azureus/Azureus2.jar

install -p -D -m 0755 org/gudy/azureus2/platform/unix/startupScript $RPM_BUILD_ROOT%{_bindir}/azureus

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -m 644 org/gudy/azureus2/ui/icons/a32.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/azureus.png
install -m 644 org/gudy/azureus2/ui/icons/a16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/azureus.png
install -m 644 org/gudy/azureus2/ui/icons/a32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/azureus.png
install -m 644 org/gudy/azureus2/ui/icons/a64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/azureus.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/application-registry
install -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/application-registry
# alt adaptation
sed -i s,JAVA_HOME=/usr/lib/jvm/java-openjdk,JAVA_HOME=/usr/lib/jvm/java,g %buildroot%_bindir/%name
sed -i 's,uname -i,uname -m,' %buildroot%_bindir/%name

%files
%doc ChangeLog.txt
%doc GPL.txt
%{_datadir}/applications/*
%{_datadir}/application-registry/*
%{_datadir}/pixmaps/azureus.png
%{_datadir}/icons/hicolor/16x16/apps/azureus.png
%{_datadir}/icons/hicolor/32x32/apps/azureus.png
%{_datadir}/icons/hicolor/64x64/apps/azureus.png
%{_bindir}/azureus
%{_datadir}/azureus

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 5.7.1.0-alt1_2jpp8
- new version

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 5.7.0.0-alt2_3jpp8
- %%_jnidir set to /usr/lib/java

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 5.7.0.0-alt2_2jpp8
- added java requires

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.7.0.0-alt1_2jpp8
- java8 mass update

* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 5.2.0.0-alt1_2jpp7
- update

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 5.0.0.0-alt1_2jpp7
- update to new release by jppimport

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 4.9.0.0-alt1_1jpp7
- update to new release by jppimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 4.8.1.2-alt1_2jpp7
- update to new release by jppimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.8.1.2-alt1_1jpp7
- update to new release by jppimport

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 4.8.0.0-alt1_1jpp7
- update to new release by jppimport

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 4.7.1.2-alt1_2jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.7.0.2-alt1_1jpp7
- update to new release by jppimport

* Tue Oct 18 2011 Igor Vlasenko <viy@altlinux.ru> 4.7.0.0-alt1_2jpp6
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 4.6.0.4-alt2_4jpp6
- update to new release by jppimport

* Sun Jul 10 2011 Igor Vlasenko <viy@altlinux.ru> 4.6.0.4-alt2_2jpp6
- added conflict with vuse till real maintainer appear

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 4.6.0.4-alt1_2jpp6
- import by jppimport

