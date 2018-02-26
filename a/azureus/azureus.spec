# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Conflicts: vuse < 4.2.0.3
BuildRequires: /proc
BuildRequires: jpackage-compat
%global		_newname Vuze

Name:		azureus
Version:	4.7.0.2
Release:	alt1_1jpp7
Summary:	A BitTorrent Client
Group:		Development/Java
License:	GPLv2+
URL:		http://azureus.sourceforge.net

Source0:	http://downloads.sourceforge.net/azureus/%{_newname}_4702_source.zip

Source1:	azureus.script
Source2:	Azureus.desktop
Source3:	azureus.applications

#ant build script from Azureus-4.3.0.6
Source4:	build.xml

Patch2:		azureus-cache-size.patch
Patch3:		azureus-remove-manifest-classpath.patch
Patch9:		azureus-no-shared-plugins.patch
Patch12:	azureus-no-updates-PluginInitializer.patch
Patch13:	azureus-no-updates-PluginInterfaceImpl.patch
Patch14:	azureus-no-update-manager-AzureusCoreImpl.patch
Patch15:	azureus-no-update-manager-CorePatchChecker.patch
Patch16:	azureus-no-update-manager-CoreUpdateChecker.patch
Patch19:	azureus-no-update-manager-PluginUpdatePlugin.patch
Patch20:	azureus-no-update-manager-SWTUpdateChecker.patch
Patch22:	azureus-no-update-manager-UpdateMonitor.patch
Patch27:	azureus-SecureMessageServiceClientHelper-bcprov.patch
Patch28:	azureus-configuration.patch

Patch50:	azureus-4.0.0.4-boo-windows.diff
Patch51:	azureus-4.0.0.4-boo-osx.diff
Patch53:	azureus-4.0.0.4-boo-updating-w32.diff
Patch54:	azureus-4.0.0.4-screw-win32utils.diff

Patch56:	azureus-4.0.0.4-silly-java-tricks-are-for-kids.diff
Patch57:	azureus-4.0.0.4-stupid-invalid-characters.diff

Patch58:	azureus-4.2.0.4-java5.patch


BuildRequires:	ant jpackage-utils >= 1.5 xml-commons-apis
BuildRequires:	jakarta-commons-cli log4j
BuildRequires:	bouncycastle >= 1.33-3
BuildRequires:	eclipse-swt >= 3.5
BuildRequires:	junit
Requires:	jakarta-commons-cli log4j
Requires:	eclipse-swt >= 3.5
Requires:	 bouncycastle >= 1.33-3
BuildRequires:	 desktop-file-utils
Requires(post):	 desktop-file-utils
Requires(postun):	desktop-file-utils
BuildArch:	noarch
Source44: import.info


%description 
Azureus (now %{_newname}) implements the BitTorrent protocol using java
and comes bundled with many invaluable features for both beginners and
advanced users.

%prep
%setup -q -c

cp %{SOURCE4} .

%patch2 -p0 -b .cache-size
%patch3 -p1 -b .remove-manifest-classpath
%patch9 -p0 -b .no-shared-plugins
#%patch12 -p1 -b .no-updates-PluginInitializer
#%patch13 -p1 -b .no-updates-PluginInterfaceImpl
#%patch14 -p1 -b .no-update-manager-AzureusCoreImpl
#%patch15 -p1 -b .no-update-manager-CorePatchChecker
#%patch16 -p1 -b .no-update-manager-CoreUpdateChecker
#%patch19 -p1 -b .no-update-manager-PluginUpdatePlugin
#%patch20 -p1 -b .no-update-manager-SWTUpdateChecker
#%patch22 -p1 -b .no-update-manager-UpdateMonitor
%patch27 -p1 -b .nobcprov
#%patch28 -p0 -b .configuration 

#rm com/aelitis/azureus/core/update -rf
#find ./ -name osx | xargs rm -r
#find ./ -name macosx | xargs rm -r
#find ./ -name win32 | xargs rm -r
#find ./ -name Win32\* | xargs rm -r
# Remove test code

rm org/gudy/azureus2/platform/macosx/access/cocoa/CocoaJavaBridge.java
rm org/gudy/azureus2/platform/macosx/PlatformManagerImpl.java
rm org/gudy/azureus2/platform/win32/PlatformManagerImpl.java
rm org/gudy/azureus2/platform/macosx/access/jnilib/OSXAccess.java
rm org/gudy/azureus2/platform/win32/access/AEWin32Access.java
rm org/gudy/azureus2/platform/win32/access/impl/AEWin32AccessInterface.java
rm org/gudy/azureus2/platform/win32/access/impl/AEWin32AccessImpl.java
rm org/gudy/azureus2/platform/macosx/NativeInvocationBridge.java
rm org/gudy/azureus2/platform/macosx/PListEditor.java
rm org/gudy/azureus2/platform/win32/access/AEWin32AccessException.java
rm org/gudy/azureus2/platform/win32/access/AEWin32AccessListener.java
rm org/gudy/azureus2/platform/win32/access/AEWin32Manager.java
rm org/gudy/azureus2/platform/win32/access/impl/AEWin32AccessCallback.java
rm org/gudy/azureus2/platform/win32/access/impl/AEWin32AccessExceptionImpl.java
rm org/gudy/azureus2/platform/win32/PlatformManagerUpdateChecker.java
%patch50 -p1 -b .boo-windows

rm org/gudy/azureus2/ui/swt/osx/CarbonUIEnhancer.java
rm org/gudy/azureus2/ui/swt/osx/Start.java
rm org/gudy/azureus2/ui/swt/win32/Win32UIEnhancer.java
%patch51 -p1 -b .boo-osx
%patch53 -p1 -b .boo-updating-w32
#%patch54 -b .screw-win32utils

%patch56 -p1 -b .silly-java-tricks-are-for-kids
%patch57  -p1 -b stupid-invalid-characters

%patch58 -p1 -b .java5

#hacks to org.eclipse.swt.widgets.Tree2 don't compile.
rm -fR org/eclipse


#sed -i -e \
#  "s|sun.security.action.GetPropertyAction|gnu.java.security.action.GetPropertyAction|" \
#  org/gudy/azureus2/core3/internat/MessageText.java

# Convert line endings...
sed -i 's/\r//' ChangeLog.txt
chmod 644 *.txt


%build
mkdir -p build/libs
build-jar-repository -p build/libs bcprov apache-commons-cli log4j \
  junit

#ppc seems to have eclipse-swt.ppc64 installed so libdir can't be used
if [ -e /usr/lib/eclipse/swt.jar ];then
  ln -s /usr/lib/eclipse/swt.jar build/libs
else
  ln -s /usr/lib64/eclipse/swt.jar build/libs
fi

ant jar

#mkdir -p plugins/azplugins
#pushd plugins
#pushd azplugins
#unzip -q %{SOURCE5}
#rm -f *.jar `find ./ -name \*class`
#find ./ -name \*java | xargs javac -cp %{_libdir}/eclipse/swt.jar:../..:.
#find ./ -name \*java | xargs rm
#jar cvf azplugins_2.1.6.jar .
#popd
#popd

#unzip -q %{SOURCE6}
#pushd plugins
#pushd bdcc
#unzip *.jar
#rm -f *.jar `find ./ -name \*class`
#find ./ -name \*java | xargs javac -cp %{_libdir}/eclipse/swt.jar:../..:.
#find ./ -name \*java | xargs rm
#jar cvf bdcc_2.2.2.jar .
#popd
#popd

%install

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/azureus/plugins
install -pm 644 dist/Azureus2.jar $RPM_BUILD_ROOT%{_datadir}/azureus/Azureus2.jar
# TODO: fix launcher to be multilib-safe
install -p -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/azureus

#install -dm 755 $RPM_BUILD_ROOT%{_datadir}/azureus/plugins/azplugins
#install -pm 644 plugins/azplugins/azplugins_2.1.6.jar $RPM_BUILD_ROOT%{_datadir}/azureus/plugins/azplugins/azplugins_2.1.6.jar
#install -pm 644 plugins/azplugins/plugin.properties $RPM_BUILD_ROOT%{_datadir}/azureus/plugins/azplugins/plugin.properties

#install -dm 755 $RPM_BUILD_ROOT%{_datadir}/azureus/plugins/bdcc
#install -pm 644 plugins/bdcc/bdcc_2.2.2.jar $RPM_BUILD_ROOT%{_datadir}/azureus/plugins/bdcc/bdcc_2.2.2.jar
#install -pm 644 plugins/bdcc/plugin.properties $RPM_BUILD_ROOT%{_datadir}/azureus/plugins/bdcc/plugin.properties

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -m 644 org/gudy/azureus2/ui/icons/a32.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/azureus.png
install -m 644 org/gudy/azureus2/ui/icons/a16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/azureus.png
install -m 644 org/gudy/azureus2/ui/icons/a32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/azureus.png
install -m 644 org/gudy/azureus2/ui/icons/a64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/azureus.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor fedora					\
		     --dir ${RPM_BUILD_ROOT}%{_datadir}/applications	\
		     --add-category X-Fedora				\
	%{SOURCE2}

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

