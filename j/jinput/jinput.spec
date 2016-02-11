# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jinput
Version:        2.0.7
Release:        alt2_5.20140526svnjpp8
Summary:        Java Game Controller API

Group:          Development/Java
License:        BSD
URL:            http://java.net/projects/jinput
# Upstream only provides subversion checkout or nightly build.
# Also, some (non-Linux) plugin code is non-free.  As long as we are deleting
# non-free plugins, we also delete plugins for non-Linux operating systems.
# Create the source tarball as follows:
# svn export -r 253 https://svn.java.net/svn/jinput~svn/trunk jinput-2.0.7
# rm -rf jinput-2.0.7/plugins/{OSX,windows,wintab}
# tar cJf jinput-2.0.7.tar.xz jinput-2.0.7
Source0:        %{name}-%{version}.tar.xz
# Fedora-specific patch: will not be sent upstream.  Remove build.xml rules
# for building non-free plugin code.
Patch0:         001_jinput_build.patch
# Fedora-specific patch: will not be sent upstream.  Do not strip the native
# library.
Patch1:         002_jinput_dontstripso.patch
# Fedora-specific patch: will not be sent upstream.  Load the shared library
# from the Fedora-mandated location.
Patch2:         003_jinput_usesystemload.patch
# Patch from https://java.net/jira/browse/JINPUT-44 to not access usage bits,
# which are not supported in current Linux kernels
Patch3:         004_jinput_usagebits.patch
# Patch from https://java.net/jira/browse/JINPUT-51 to fix a resource leak
Patch4:         005_jinput_leak.patch
# Patch to be sent upstream to migrate to Java 5 (Java generics)
Patch5:         006_jinput_java5.patch
# Patch to be sent upstream to adapt to a change in headers in Linux 4.5
Patch6:         007_jinput_linux_4.5.patch

BuildRequires:  ant
BuildRequires:  java-javadoc >= 1:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  jutils
BuildRequires:  jutils-javadoc

Requires:       jpackage-utils
Requires:       jutils
Source44: import.info

%description
jinput is an implementation of an API for game controller discovery and
polled input.  It is part of a suite of open-source technologies
initiated by the Game Technology Group at Sun Microsystems with the
intention of making the development of high performance games in Java a
reality.  The API itself is pure Java and presents a platform-neutral,
completely portable model of controller discovery and polling.  It can
handle arbitrary controllers and returns both human and machine
understandable descriptions of the inputs available.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}
Requires:       jutils-javadoc
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6

# Don't use prebuilt jars
rm -f lib/*.jar
build-jar-repository -s -p lib jutils

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix the version string in the POMs
for fil in jinput.pom jinput-platform.pom; do
  sed -i.orig 's/@VERSION@/%{version}/' $fil
  fixtimestamp $fil
done

# Fix the version string in net.java.games.input.Version
%global buildnum %(cut -d. -f1 <<< %{release})
sed -i.orig 's/@API_VERSION@/%{version}/;s/@BUILD_NUMBER@/%{buildnum}/' \
    coreAPI/src/java/net/java/games/input/Version.java
fixtimestamp coreAPI/src/java/net/java/games/input/Version.java

# Use Fedora's CFLAGS and LDFLAGS
sed -i "s|-O2 -Wall|$RPM_OPT_FLAGS|;s|-shared|& $RPM_LD_FLAGS|" \
    plugins/linux/src/native/build.xml

# Prevent jutils.jar from being included in jinput.jar
sed -i '\@zipfileset.*/>@d' build.xml

%build
# Get the latest definitions from <linux/input-event-codes.h>
ant -f plugins/linux/src/native/build.xml createNativeDefinitions.java

# Build
ant dist

# The ant target to build javadocs has several problems.  It looks for the
# jutils jar in the wrong place.  It doesn't link to the jutils javadocs.
# It creates distinct sets of javadoc pages for the coreAPI and for the
# plugins, where we would like all of the pages to be in a single javadoc
# package.  We can solve all but the last with a bit of judicious hacking in
# the appropriate build.xml files, but that last point is difficult to address
# without resulting in broken links from the plugin pages to the coreAPI pages.
# Therefore, we throw up our hands in despair and do this instead:
javadoc -d javadoc -classpath lib/jutils.jar:dist/jinput.jar -package \
  -sourcepath plugins/awt/src:plugins/linux/src/java:coreAPI/src/java \
  -link file://%{_javadocdir}/jutils -link file://%{_javadocdir}/java \
  -source 1.6 net.java.games.input

%install
# jar
install -Dp -m 644 dist/%{name}.jar $RPM_BUILD_ROOT%{_jnidir}/%{name}.jar

# jni
install -Dp -m 755 dist/libjinput* \
    $RPM_BUILD_ROOT%{_libdir}/%{name}/libjinput.so
ln -s ../../..%{_jnidir}/%{name}.jar $RPM_BUILD_ROOT%{_libdir}/%{name}/

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 jinput-platform.pom  \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-platform.pom
install -pm 644 jinput.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap
%add_maven_depmap JPP-%{name}-platform.pom 

%check
# Do not rebuild; just run the test
sed -i 's/"versiontest" depends="init,all"/"versiontest"/' build.xml
ant versiontest

%files -f .mfiles
%doc README.txt 
%{_libdir}/%{name}/

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_5.20140526svnjpp8
- %%_jnidir set to /usr/lib/java

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1_5.20140526svnjpp8
- java8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_6.20130309svnjpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_2.20110801svnjpp7
- initial build

