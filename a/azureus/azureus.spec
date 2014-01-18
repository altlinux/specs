# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Conflicts: vuse < 4.2.0.3
BuildRequires: /proc
BuildRequires: jpackage-compat
%global		_newname Vuze

Name:		azureus
Version:	5.2.0.0
Release:	alt1_2jpp7
Summary:	A BitTorrent Client
Group:		Networking/WWW
License:	GPLv2+
URL:		http://azureus.sourceforge.net

Source0:	http://downloads.sourceforge.net/azureus/%{_newname}_5200_source.zip

Source2:	Azureus.desktop
Source3:	azureus.applications

#ant build script from Azureus-4.3.0.6
Source4:	build.xml

Patch0:		azureus-cache-size.patch
Patch1:		azureus-remove-manifest-classpath.patch
Patch2:		azureus-no-shared-plugins.patch
Patch3:	azureus-SecureMessageServiceClientHelper-bcprov.patch

Patch4:	azureus-4.0.0.4-boo-osx.diff

Patch6:	azureus-4.0.0.4-stupid-invalid-characters.diff

Patch7:	azureus-4.2.0.4-java5.patch

Patch9:	azureus-4.8.1.2-no-bundled-apache-commons.patch

Patch10: azureus-5.2.0.0-startupScript.patch

BuildRequires:	ant jpackage-utils >= 1.5 xml-commons-apis
BuildRequires:	apache-commons-cli log4j
BuildRequires:	apache-commons-lang
BuildRequires:	bouncycastle >= 1.33-3
BuildRequires:	eclipse-swt >= 3.5
BuildRequires:	junit
Requires:	apache-commons-cli log4j
Requires:	eclipse-swt >= 3.5
Requires:	 bouncycastle >= 1.33-3
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

%patch0 -p0 -b .cache-size
%patch1 -p1 -b .remove-manifest-classpath
%patch2 -p1 -b .no-shared-plugins

%patch3 -p1 -b .nobcprov


rm org/gudy/azureus2/ui/swt/osx/CarbonUIEnhancer.java
rm org/gudy/azureus2/ui/swt/osx/Start.java
rm org/gudy/azureus2/ui/swt/win32/Win32UIEnhancer.java
%patch4 -p1 -b .boo-osx

%patch6  -p1 -b stupid-invalid-characters

%patch7 -p1 -b .java5

%patch9 -p1 -b .no-bundled-apache-commons

%patch10 -p1 -b .startupScript

#hacks to org.eclipse.swt.widgets.Tree2 don't compile.
rm -fR org/eclipse

# Convert line endings...
sed -i 's/\r//' ChangeLog.txt
chmod 644 *.txt

#remove bundled libs
rm -fR org/apache

%build
mkdir -p build/libs
build-jar-repository -p build/libs bcprov apache-commons-cli log4j \
  junit apache-commons-lang

#ppc seems to have eclipse-swt.ppc64 installed so libdir can't be used
if [ -e /usr/lib/eclipse/swt.jar ];then
  ln -s /usr/lib/eclipse/swt.jar build/libs
else
  ln -s /usr/lib64/eclipse/swt.jar build/libs
fi

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

%post
touch %{_datadir}/icons/hicolor

%postun
touch %{_datadir}/icons/hicolor

%files
%doc ChangeLog.txt GPL.txt
%{_datadir}/applications/*
%{_datadir}/application-registry/*
%{_datadir}/pixmaps/azureus.png
%{_datadir}/icons/hicolor/16x16/apps/azureus.png
%{_datadir}/icons/hicolor/32x32/apps/azureus.png
%{_datadir}/icons/hicolor/64x64/apps/azureus.png
%{_bindir}/azureus
%{_datadir}/azureus

%changelog
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

