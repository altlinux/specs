# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jinput
Version:        2.0.6
Release:        alt1_2.20110801svnjpp7
Summary:        Java Game Controller API

Group:          Development/Java
License:        BSD
URL:            http://java.net/projects/jinput
# Upstream only provides subversion checkout or nightly build.
# Also, some (non-Linux) plugin code is non-free.  As long as we are deleting
# non-free plugins, we also delete plugins for non-Linux operating systems.
# Create the source tarball as follows:
# svn export -r 247 https://svn.java.net/svn/jinput~svn/trunk jinput-2.0.6
# rm -rf jinput-2.0.6/plugins/{OSX,windows,wintab}
# tar cJf jinput-2.0.6.tar.xz jinput-2.0.6
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
# Patch from http://java.net/jira/browse/JINPUT-44 to not access usage bits,
# which are not supported in current Linux kernels
Patch3:         004_jinput_usagebits.patch

BuildRequires:  ant
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
Requires:       %{name} = %{version}-%{release}
Requires:       jutils-javadoc
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

# Don't use prebuilt jars
rm -f lib/*.jar
build-jar-repository -s -p lib jutils

# Fix the version string in the POMs
sed -i 's/@VERSION@/%{version}/' jinput.pom jinput-platform.pom

# Use Fedora's CFLAGS
sed -i "s/-O2 -Wall/$RPM_OPT_FLAGS/" plugins/linux/src/native/build.xml

%build
# Get the latest definitions from <linux/input.h>
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
  -link %{_javadocdir}/jutils net.java.games.input

%install
# jar
install -Dp -m 644 dist/%{name}.jar \
    $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}.jar

# jni
install -Dp -m 755 dist/libjinput* \
    $RPM_BUILD_ROOT%{_libdir}/%{name}/libjinput.so

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 jinput-platform.pom  \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-platform.pom
install -pm 644 jinput.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# added by hand
mkdir -p %buildroot%_javadir/
ln -s $(relative %_libdir/%{name}/%{name}.jar %_javadir/) %buildroot%_javadir/%{name}.jar
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-platform.pom 

%check
ant versiontest

%files
%doc README.txt 
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_libdir}/%{name}
%_javadir/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_2.20110801svnjpp7
- initial build

