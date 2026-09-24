Name: slf4j2
Version: 2.0.18
Release: alt1
Summary: Simple Logging Facade for Java, version 2

License: MIT and Apache-2.0
Group: Development/Java
Url: https://www.slf4j.org/
# Source-url: https://github.com/qos-ch/slf4j/archive/refs/tags/v_%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch
ExcludeArch: %ix86
BuildRequires(pre): rpm-build-java
BuildRequires: java-21-openjdk-devel javapackages-local

%description
The SLF4J version 2 API and Commons Logging bridge, installed alongside
SLF4J 1.x using versioned Maven coordinates.

%prep
%setup
cp jcl-over-slf4j/LICENSE.txt LICENSE-JCL.txt
# Standalone POMs retain runtime dependencies without the upstream build parent.
for module in slf4j-api jcl-over-slf4j; do
    %pom_remove_parent "$module"
    %pom_xpath_inject pom:project '<groupId>org.slf4j</groupId><version>%version</version>' "$module"
    %pom_xpath_remove pom:build "$module"
done
%pom_remove_dep org.slf4j:slf4j-jdk14 jcl-over-slf4j
%pom_change_dep org.slf4j:slf4j-api org.slf4j:slf4j-api:2 jcl-over-slf4j
# Do not provide unversioned Maven artifacts already supplied by SLF4J 1.x.
%mvn_compat_version org.slf4j:* 2
%mvn_file 'org.slf4j:{*}' %name/@1

%build
export JAVA_HOME=%_jvmdir/java-21-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
for module in slf4j-api jcl-over-slf4j; do
    mkdir -p "$module/target/classes" "$module/target/java9"
    find "$module/src/main/java" -name '*.java' > "$module/target/sources"
    javac --release 8 -encoding UTF-8 -cp slf4j-api/target/classes \
        -d "$module/target/classes" @"$module/target/sources"
    if [ -d "$module/src/main/resources" ]; then
        cp -a "$module/src/main/resources/." "$module/target/classes/"
    fi
    mkdir -p "$module/target/classes/META-INF"
    cp "$module/LICENSE.txt" "$module/target/classes/META-INF/LICENSE.txt"
    case "$module" in
        slf4j-api) module_name=org.slf4j ;;
        jcl-over-slf4j) module_name=org.apache.commons.logging ;;
    esac
    javac --release 9 --module-path slf4j-api/target/slf4j-api.jar \
        --patch-module "$module_name=$module/target/classes" \
        -d "$module/target/java9" "$module/src/main/java9/module-info.java"
    jar --create --file "$module/target/$module.jar" \
        -C "$module/target/classes" . --release 9 -C "$module/target/java9" .
    %mvn_artifact "$module/pom.xml" "$module/target/$module.jar"
done

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt LICENSE-JCL.txt README.md

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 2.0.18-alt1
- Initial build of parallel SLF4J 2 API and Commons Logging bridge.
