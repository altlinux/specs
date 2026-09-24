Name: tinylog
Version: 2.7.0
Release: alt1
Summary: Lightweight Java logging framework

License: Apache-2.0
Group: Development/Java
URL: https://github.com/tinylog-org/tinylog
# Source-url: https://github.com/tinylog-org/tinylog/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch
ExcludeArch: %ix86
Source1: tinylog-smoke.java
Patch: tinylog-desktop.patch
BuildRequires: java-21-openjdk-devel maven-local
BuildRequires: mvn(org.slf4j:slf4j-api:2)
BuildRequires: mvn(org.codehaus.mojo:animal-sniffer-annotations)

%description
Java tinylog library.

%prep
%setup
%patch -p1
# Android-only adapters are not part of the desktop runtime.
rm tinylog-api/src/main/java/org/tinylog/runtime/{AndroidRuntime,LegacyJavaRuntime}.java
rm tinylog-impl/src/main/java/org/tinylog/writers/LogcatWriter.java
sed -i '/org.tinylog.writers.LogcatWriter/d' tinylog-impl/src/main/resources/META-INF/services/org.tinylog.writers.Writer
# Flatten the three runtime POMs, retaining their actual runtime dependencies.
%pom_remove_parent tinylog-api
%pom_remove_parent tinylog-impl
%pom_remove_parent slf4j-tinylog
for module in tinylog-api tinylog-impl slf4j-tinylog; do
    %pom_xpath_set pom:packaging jar $module
    %pom_xpath_inject pom:project '<groupId>org.tinylog</groupId><version>%version</version>' $module
    %pom_xpath_remove pom:build $module
    %pom_xpath_remove pom:dependencies $module
done
%pom_add_dep org.tinylog:tinylog-api:%version tinylog-impl
%pom_add_dep org.tinylog:tinylog-api:%version slf4j-tinylog
%pom_add_dep org.slf4j:slf4j-api:2 slf4j-tinylog

%build
export JAVA_HOME=%_jvmdir/java-21-openjdk
export PATH=$JAVA_HOME/bin:$PATH
classpath=$(build-classpath slf4j2/slf4j-api-2 animal-sniffer-annotations)
for module in tinylog-api tinylog-impl slf4j-tinylog; do
    mkdir -p $module/target/classes
    find $module/src/main/java -name '*.java' > $module/target/sources
    javac --release 21 -encoding UTF-8 -cp "$classpath" -d $module/target/classes @$module/target/sources
    cp -a $module/src/main/resources/. $module/target/classes/
    printf 'Automatic-Module-Name: %%s\n' "$(case $module in tinylog-api) echo org.tinylog.api;; tinylog-impl) echo org.tinylog.impl;; *) echo org.tinylog.api.slf4j;; esac)" > $module/target/MANIFEST.MF
    jar cfm $module/target/$module.jar $module/target/MANIFEST.MF -C $module/target/classes .
    %mvn_artifact $module/pom.xml $module/target/$module.jar
    classpath="$classpath:$module/target/classes"
done
%mvn_file ":{*}" %name/@1

%check
export JAVA_HOME=%_jvmdir/java-21-openjdk
classpath=$(build-classpath slf4j2/slf4j-api-2)
for module in tinylog-api tinylog-impl slf4j-tinylog; do
    classpath="$classpath:$module/target/$module.jar"
done
$JAVA_HOME/bin/javac -cp "$classpath" -d . %SOURCE1
$JAVA_HOME/bin/java -cp ".:$classpath" TinylogSmoke > smoke.log 2>&1
grep -q tinylog-native-smoke smoke.log
grep -q tinylog-slf4j-smoke smoke.log

%install
%mvn_install

%files -f .mfiles
%doc readme.md
%doc license.txt

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- Initial build of the desktop logging API, implementation and SLF4J adapter.

