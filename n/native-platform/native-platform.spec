# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name native-platform
%define version 0.3
%global bits 32
%global debug_package %{nil}

%ifarch x86_64 ppc64 s390x sparc64
%global bits 64
%endif
%global namedreltag -rc-2
%global namedversion %{version}%{?namedreltag}

Name:          native-platform
Version:       0.3
Release:       alt1_0.2.rc2jpp7
Summary:       Java bindings for various native APIs
Group:         Development/Java
# contacted the developer for info about license, waiting for an answer...
License:       ASL 2.0
URL:           https://github.com/adammurdoch/native-platform
# git clone git://github.com/adammurdoch/native-platform native-platform-0.3-rc-2
# (cd native-platform-0.3-rc-2/ && git archive --format=tar --prefix=native-platform-0.3-rc-2/ 0.3-rc-2 | xz > ../native-platform-0.3-rc-2-src-git.tar.xz)
Source0:       %{name}-%{namedversion}-src-git.tar.xz
Source1:       http://repo.gradle.org/gradle/libs-releases-local/net/rubygrapefruit/%{name}/%{namedversion}/%{name}-%{namedversion}.pom
Source2:       http://repo.gradle.org/gradle/libs-releases-local/net/rubygrapefruit/%{name}-linux-i386/%{namedversion}/%{name}-linux-i386-%{namedversion}.pom
Source3:       http://repo.gradle.org/gradle/libs-releases-local/net/rubygrapefruit/%{name}-linux-amd64/%{namedversion}/%{name}-linux-amd64-%{namedversion}.pom
Patch0:        %{name}-0.3-rc-2-build.patch


# build tools and deps
BuildRequires: antlr-tool
BuildRequires: apache-commons-cli
BuildRequires: gradle
BuildRequires: groovy
BuildRequires: objectweb-asm

BuildRequires: ncurses-devel

# test deps
BuildRequires: spock-core
# test app deps jopt-simple >= 4.2
BuildRequires: jopt-simple
Source44: import.info


%description
A collection of cross-platform Java APIs
for various native APIs.

These APIs support Java 5 and later. Some
of these APIs overlap with APIs available
in later Java versions.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
find .  -name "*.jar" -delete
find .  -name "*.class" -delete

%patch0 -p1

cp -p %{SOURCE1} pom.xml

%pom_remove_dep net.rubygrapefruit:%{name}-osx-universal pom.xml
%pom_remove_dep net.rubygrapefruit:%{name}-windows-i386 pom.xml
%pom_remove_dep net.rubygrapefruit:%{name}-windows-amd64 pom.xml
%if %{bits} == 64
%pom_remove_dep net.rubygrapefruit:%{name}-linux-i386 pom.xml
%else
%pom_remove_dep net.rubygrapefruit:%{name}-linux-amd64 pom.xml
%endif

chmod 644 readme.md
sed -i 's/\r//' readme.md

%build

# TODO not able to perform tests without gradle maven plugin,
# problems to load in cp some groovy classes
export GRADLE_USER_HOME=$PWD
mkdir -p gradlehome
gradle --debug Jar nativeJar javadoc -g $PWD/gradlehome -b $PWD/build.gradle

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 build/libs/%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# there is something of wrong in rawhide for x64 arch _jnidir point to /usr/lib/java
mkdir -p %{buildroot}%{_jnidir}
%if %{bits} == 64
install -m 644 build/libs/%{name}-linux-amd64-%{namedversion}.jar %{buildroot}%{_jnidir}/%{name}-linux-amd64.jar
install -pm 644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP-%{name}-linux-amd64.pom
%add_maven_depmap JPP-%{name}-linux-amd64.pom %{name}-linux-amd64.jar
%else
install -m 644 build/libs/%{name}-linux-i386-%{namedversion}.jar %{buildroot}%{_jnidir}/%{name}-linux-i386.jar
install -pm 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{name}-linux-i386.pom
%add_maven_depmap JPP-%{name}-linux-i386.pom %{name}-linux-i386.jar
%endif

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/docs/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_jnidir}/%{name}-linux*.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-linux*.pom
%{_mavendepmapfragdir}/%{name}
%doc readme.md LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_0.2.rc2jpp7
- new release

