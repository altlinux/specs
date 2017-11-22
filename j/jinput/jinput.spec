Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Upstream is not in the habit of releasing tarballs.  We pull from git.
%global gitdate         20170607
%global gittag          294629a312eed88be8558a8cebc23da87772ffcd
%global shorttag        %(cut -b -7 <<< %{gittag})

Name:           jinput
Version:        2.0.7
Release:        alt2_11.20170607git.294629ajpp8
Summary:        Java Game Controller API

License:        BSD
URL:            https://github.com/jinput/jinput
Source0:        https://github.com/jinput/jinput/tarball/%{gittag}/%{name}-%{name}-%{shorttag}.tar.gz
# Fedora-specific patch: will not be sent upstream.  Remove build.xml rules
# for building non-free plugin code.
Patch0:         001_jinput_build.patch
# Fedora-specific patch: will not be sent upstream.  Do not strip the native
# library.
Patch1:         002_jinput_dontstripso.patch
# Fedora-specific patch: will not be sent upstream.  Load the shared library
# from the Fedora-mandated location.
Patch2:         003_jinput_usesystemload.patch
# Patch from https://java.net/jira/browse/JINPUT-51 to fix a resource leak
Patch4:         005_jinput_leak.patch
# Patch to be sent upstream to migrate to Java 5 (Java generics)
Patch5:         006_jinput_java5.patch
# Patch to be sent upstream to adapt to a change in headers in Linux 4.5
Patch6:         007_jinput_linux_4.5.patch

BuildRequires:  ant
BuildRequires:  gcc-common
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  java-javadoc >= 1:1.6.0
BuildRequires:  javapackages-local
BuildRequires:  jpackage-utils
BuildRequires:  jutils
BuildRequires:  jutils-javadoc
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
Group: Development/Java
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jutils-javadoc
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{shorttag}
%patch0
%patch1
%patch2
%patch4 -p1
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

# We cannot resolve this self-dependency properly, so just remove it
%pom_remove_dep net.java.jinput:jinput-platform jinput.pom

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
%mvn_artifact %{name}-platform.pom
%mvn_artifact %{name}.pom dist/%{name}.jar
%mvn_install -J javadoc/

# jni
install -Dp -m 755 dist/libjinput* \
    $RPM_BUILD_ROOT%{_libdir}/%{name}/libjinput.so
ln -s ../../..%{_jnidir}/%{name}/%{name}.jar $RPM_BUILD_ROOT%{_libdir}/%{name}/

%check
# Do not rebuild; just run the test
sed -e 's/"versiontest" depends="init,all"/"versiontest"/' \
    -e 's/"runtest" depends="dist"/"runtest"/' \
    -i build.xml
ant versiontest

%files -f .mfiles
%doc README.md
%{_libdir}/%{name}/

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_11.20170607git.294629ajpp8
- new fc release

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_10.20170607git.294629ajpp8
- fc update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_7.20160519git.b813d55jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_6.20160519git.b813d55jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_5.20140526svnjpp8
- %%_jnidir set to /usr/lib/java

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1_5.20140526svnjpp8
- java8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_6.20130309svnjpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_2.20110801svnjpp7
- initial build

