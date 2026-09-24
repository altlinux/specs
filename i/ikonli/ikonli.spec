Name: ikonli
Version: 12.4.0
Release: alt1
Summary: JavaFX icon library with Unicons and Boxicons

License: Apache-2.0 AND MIT
Group: Development/Java
URL: https://github.com/kordamp/ikonli
# Source-url: https://github.com/kordamp/ikonli/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
ExcludeArch: %ix86
Patch: ikonli-desktop.patch
Source1: ikonli-core.pom
Source2: ikonli-javafx.pom
Source3: ikonli-unicons-pack.pom
Source4: ikonli-boxicons-pack.pom
Source5: ikonli-bom.pom
# Unicons 20201106 was published under Apache-2.0, before the later relicensing.
# https://raw.githubusercontent.com/Iconscout/unicons/9233c03f87fd9869517c6a61135334ebada07abe/LICENSE
Source6: LICENSE-unicons
Source7: LICENSE-boxicons
Source8: ikonli-smoke.java
BuildRequires: java-25-openjdk-devel maven-local
BuildRequires: openjfx

%description
Ikonli provides JavaFX controls for scalable icon fonts. This package includes
the core library, JavaFX integration and the Unicons and Boxicons font packs.

%prep
%setup
%patch -p1
# Desktop runtime uses ServiceLoader; OSGi and Graal build-time annotations
# are replaced by explicit service descriptors in the desktop patch.
rm core/ikonli-core/src/main/java/org/kordamp/ikonli/OSGiIkonResolver.java
cp %SOURCE1 core/ikonli-core/pom.xml
cp %SOURCE2 core/ikonli-javafx/pom.xml
cp %SOURCE3 icon-packs/ikonli-unicons-pack/pom.xml
cp %SOURCE4 icon-packs/ikonli-boxicons-pack/pom.xml
cp %SOURCE5 bom.pom
cp %SOURCE6 %SOURCE7 .
%pom_add_dep org.openjfx:javafx-controls:25.0.4 core/ikonli-javafx

%build
export JAVA_HOME=%_jvmdir/java-25-openjdk
export PATH=$JAVA_HOME/bin:$PATH
classpath=$(find %_javadir/openjfx -name '*.jar' -printf '%%p:' )
for module in core/ikonli-core core/ikonli-javafx icon-packs/ikonli-unicons-pack icon-packs/ikonli-boxicons-pack; do
    name=$(basename $module)
    mkdir -p $module/target/classes
    find $module/src/main/java -name '*.java' ! -name module-info.java > $module/target/sources
    javac --release 25 -encoding UTF-8 -cp "$classpath" -d $module/target/classes @$module/target/sources
    if [ -d $module/src/main/resources ]; then cp -a $module/src/main/resources/. $module/target/classes/; fi
    module_name=$(sed -n 's/^module \([^ ]*\) {.*/\1/p' $module/src/main/java/module-info.java)
    printf 'Automatic-Module-Name: %%s\n' "$module_name" > $module/target/MANIFEST.MF
    jar cfm $module/target/$name.jar $module/target/MANIFEST.MF -C $module/target/classes .
    %mvn_artifact $module/pom.xml $module/target/$name.jar
    classpath="$classpath:$module/target/classes"
done
%mvn_artifact -Dtype=pom bom.pom
%mvn_file ":{*}" %name/@1

%check
export JAVA_HOME=%_jvmdir/java-25-openjdk
classpath=.
for module in core/ikonli-core core/ikonli-javafx icon-packs/ikonli-unicons-pack icon-packs/ikonli-boxicons-pack; do
    classpath="$classpath:$module/target/$(basename $module).jar"
done
$JAVA_HOME/bin/javac -cp "$classpath" -d . %SOURCE8
$JAVA_HOME/bin/java -cp "$classpath" IkonliSmoke

%install
%mvn_install

%files -f .mfiles
%doc LICENSE LICENSE-unicons LICENSE-boxicons README.adoc

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 12.4.0-alt1
- Initial build of the JavaFX icon runtime with Unicons and Boxicons.

