Name: pdfsam
Version: 6.0.5
Release: alt1

Summary: PDFsam Basic - split, merge and rotate PDF documents

Group: Publishing
License: AGPL-3.0-or-later AND OFL-1.1
Url: https://pdfsam.org/pdfsam-basic/
ExcludeArch: %ix86
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/torakiki/pdfsam/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: pdfsam.sh
Source2: pdfsam.desktop
Source3: make-runtime-classpath.py

BuildRequires: maven-local rpm-build-java
BuildRequires: /proc java-25-openjdk-devel
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/msgfmt
BuildRequires: mvn(com.soberlemur:soberlemur-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(com.googlecode.gettext-commons:gettext-maven-plugin)
BuildRequires: mvn(org.pdfsam:eventstudio)
BuildRequires: mvn(org.pdfsam:pdfsam-injector)
BuildRequires: mvn(org.sejda:sejda-model)
BuildRequires: mvn(org.sejda:sejda-core)
BuildRequires: mvn(org.sejda:sejda-conversion)
BuildRequires: mvn(org.sejda:sejda-sambox)
BuildRequires: mvn(org.sejda:sejda-commons)
BuildRequires: mvn(org.openjfx:javafx-base)
BuildRequires: mvn(org.openjfx:javafx-controls)
BuildRequires: mvn(org.openjfx:javafx-graphics)
BuildRequires: mvn(org.openjfx:javafx-media)
BuildRequires: mvn(org.kordamp.ikonli:ikonli-bom:pom:)
BuildRequires: mvn(org.kordamp.ikonli:ikonli-javafx)
BuildRequires: mvn(org.kordamp.ikonli:ikonli-unicons-pack)
BuildRequires: mvn(org.kordamp.ikonli:ikonli-boxicons-pack)
BuildRequires: mvn(org.tinylog:tinylog-api)
BuildRequires: mvn(org.tinylog:tinylog-impl)
BuildRequires: mvn(org.tinylog:slf4j-tinylog)
BuildRequires: mvn(org.slf4j:slf4j-api:2)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j:2)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)
BuildRequires: mvn(com.fasterxml.jackson:jackson-bom:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.datatype:jackson-datatype-jsr310)
BuildRequires: mvn(com.fasterxml.jackson.datatype:jackson-datatype-jdk8)

# Java 25 preview classes and the graphical interface require the full JRE.
Requires: jre-25

%description
PDFsam Basic is a free desktop application to split, merge, rotate, extract,
and mix pages from PDF documents. It processes documents locally.

%prep
%setup
%pom_disable_module pdfsam-test
# Keep dependency:build-classpath limited to the packaged runtime graph;
# that goal otherwise resolves unavailable TestFX fixtures before filtering.
for pom in $(find . -name pom.xml); do
    if grep -q '<scope>test</scope>' "$pom"; then
        %pom_xpath_remove "//pom:dependencies/pom:dependency[pom:scope='test']" "$pom"
    fi
done
%pom_remove_plugin :maven-toolchains-plugin
# The system gettext plugin already uses the current Hebrew locale code (he).
%pom_remove_plugin :maven-antrun-plugin pdfsam-i18n
# Native installers and their OS detector are not used by the RPM build.
%pom_xpath_remove 'pom:build/pom:extensions' pdfsam-basic
# ALT installs SLF4J 2 alongside the Maven toolchain's SLF4J 1.7.
%pom_change_dep org.slf4j:slf4j-api org.slf4j:slf4j-api:2
%pom_change_dep org.slf4j:jcl-over-slf4j org.slf4j:jcl-over-slf4j:2
%mvn_file "org.pdfsam:{*}" %name/@1

%build
export JAVA_HOME=%_jvmdir/java-25-openjdk
%mvn_build -f -j -G dependency:build-classpath -- -Dmdep.outputFile=target/runtime-classpath.txt -DincludeScope=runtime

%install
%mvn_install
install -Dm755 %SOURCE1 %buildroot%_bindir/%name
install -Dm644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -Dm644 pdfsam-basic/src/deb/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -d %buildroot%_datadir/%name
python3 %SOURCE3 pdfsam-basic/target/runtime-classpath.txt %buildroot %_javadir/%name %_javadir/openjfx > %buildroot%_datadir/%name/classpath

desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE pdfsam-fonts/src/main/resources/fonts/pdfsam/sans/LICENSE_OFL.txt
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 6.0.5-alt1
- Update to PDFsam Basic 6.0.5 (ALT bug 56168).
- Build with Maven and system Java libraries, Java 25 and JavaFX 25.
- Replace the legacy Enhanced interface with current Basic PDF tools.

* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 2.2.4e-alt2
- Require a full JRE for the graphical interface (ALT bug 56168).

* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 2.2.4e-alt1
- new version (2.2.4e) with rpmgs script

* Thu Jun 23 2016 Vitaly Lipatov <lav@altlinux.ru> 2.2.2e-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 2.2.2e-3
+ Revision: 0c0fd58
- MassBuild#464: Increase release tag
