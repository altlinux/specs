%define swt_bundle_version 3.132.0
%define major_version   4
%define minor_version   38
# see alt bug #43049
%define __find_debuginfo_files %nil
# libs.req java problem
%add_findreq_skiplist %_libdir/eclipse-swt/*.so
%define swtsrcdir bundles/org.eclipse.swt

Name:    eclipse-swt
Version: 4.38
Release: alt1
Epoch:   1
Summary: Eclipse SWT: The Standard Widget Toolkit for GTK+

License: EPL-2.0
Group: Development/Java
URL: https://www.eclipse.org/swt/

Source0: %name-%version.tar
Source1: classpath.xls

Patch0: eclipse-swt-fedora-build-native.patch

ExclusiveArch:  x86_64 aarch64 ppc64le loongarch64

Requires: java-25-openjdk
Requires: libwebkit2gtk4.1-gir

BuildRequires(pre): /proc rpm-build-java
BuildRequires(pre): maven-local
BuildRequires: gcc-c++
BuildRequires: java-25-openjdk-devel
BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: libwebkit2gtk4.1-devel
BuildRequires: libwebkit2gtk4.1-gir-devel
BuildRequires: libcairo-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgtk+3-gir-devel
BuildRequires: libGLU-devel

%description
SWT is an open source widget toolkit for Java designed to provide
efficient, portable access to the user-interface facilities of the
operating systems on which it is implemented.

%javadoc_package

%prep
%setup
# Patch doesn't support path with spaces, renaming and back to apply patch
mv %{swtsrcdir}/Eclipse\ SWT\ PI %{swtsrcdir}/Eclipse-SWT-PI
%patch0 -p1
mv %{swtsrcdir}/Eclipse-SWT-PI %{swtsrcdir}/Eclipse\ SWT\ PI
 
# This part generates secondary fragments using primary fragments
%pom_xpath_inject "pom:profiles/pom:profile[pom:id='unix']/pom:build/pom:plugins/pom:plugin[pom:artifactId='target-platform-configuration']/pom:configuration/pom:environments" \
  "<environment><os>linux</os><ws>gtk</ws><arch>s390x</arch></environment>" .
# Prepare native build
cp %{swtsrcdir}/Eclipse\ SWT/common/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT/common/version.txt %{swtsrcdir}/
cp %{swtsrcdir}/Eclipse\ SWT\ PI/{common,cairo}/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ OpenGL/glx/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ AWT/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
# Prepare java build
mkdir -p bundles/org.eclipse.swt/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT/{common,gtk,cairo,emulated/bidi,emulated/coolbar,emulated/taskbar}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Accessibility/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ AWT/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Browser/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Custom\ Widgets/common/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Drag\ and\ Drop/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ OpenGL/{common,gtk,glx}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ PI/{common,gtk,cairo}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Printing/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ Program/{common,gtk}/org/* %{swtsrcdir}/src/main/java/org
cp -r %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/org/* %{swtsrcdir}/src/main/java/org
# Prepare maven build for fedora
%pom_remove_parent
%pom_remove_plugin org.eclipse.tycho:
%pom_remove_plugin org.eclipse.tycho: bundles/org.eclipse.swt
%pom_remove_plugin org.eclipse.tycho: local-build/local-build-parent
%pom_disable_module binaries
%pom_disable_module examples/org.eclipse.swt.examples
%pom_disable_module examples/org.eclipse.swt.examples.browser.demos
%pom_disable_module examples/org.eclipse.swt.examples.launcher
%pom_disable_module examples/org.eclipse.swt.examples.ole.win32
%pom_disable_module examples/org.eclipse.swt.examples.views
%pom_disable_module tests/org.eclipse.swt.tests
rm .mvn/extensions.xml
 
%pom_xpath_replace "//pom:packaging" "<packaging>jar</packaging>" bundles/org.eclipse.swt
%pom_xpath_inject "//pom:artifactId[text()='eclipse.platform.swt']/.." "<version>%{major_version}.%{minor_version}.0</version>"
 
%pom_add_plugin :maven-compiler-plugin bundles/org.eclipse.swt
%pom_xpath_inject "//pom:plugin[pom:artifactId='maven-compiler-plugin']" \
"<configuration>
    <source>25</source>
    <target>25</target>
    <compilerArgs>
		<arg>-classpath</arg>
		<arg>\${project.build.outputDirectory}</arg>
	</compilerArgs>
</configuration>" bundles/org.eclipse.swt
# Remove -SNAPSHOT in version
%pom_xpath_set "//pom:project/pom:version" "%{major_version}.%{minor_version}.0" pom.xml
%pom_xpath_set "//pom:project/pom:version" "%{swt_bundle_version}" bundles/org.eclipse.swt/pom.xml
%pom_xpath_set "//pom:parent/pom:version" "%{major_version}.%{minor_version}.0" bundles/org.eclipse.swt/pom.xml
%pom_xpath_set "//pom:parent/pom:version" "%{major_version}.%{minor_version}.0" local-build/local-build-parent/pom.xml

%build
cd %{swtsrcdir}
 
# Build native part
export SWT_LIB_DEBUG=1
export SWT_JAVA_HOME=/usr/lib/jvm/java-25-openjdk
export CFLAGS="${RPM_OPT_FLAGS} -std=gnu17 -Wno-deprecated-declarations"
export LFLAGS="${RPM_LD_FLAGS}"
cd Eclipse\ SWT\ PI/gtk/library/
sh build.sh -gtk3
 
# Build Java part
cd ../../..
%mvn_build

%install
# Generate addition Maven metadata
rm -rf .xmvn/ .xmvn-reactor
 
# Install Maven metadata for SWT
JAR="$(ls -1 %{swtsrcdir}/target/org.eclipse.swt-*.jar | head -n1)"
VER="$(basename "$JAR" | sed -E 's/^org\.eclipse\.swt-([0-9][0-9.]*(-SNAPSHOT)?)\.jar/\1/')"
%mvn_artifact "org.eclipse.swt:org.eclipse.swt:jar:$VER" "$JAR"
%mvn_alias "org.eclipse.swt:org.eclipse.swt" "org.eclipse.swt:swt"
%mvn_file "org.eclipse.swt:org.eclipse.swt" swt
 
%mvn_install -J %{swtsrcdir}/target/xmvn-apidocs
 
# fix so permissions
find %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/*.so -name *.so -exec chmod a+x {} \;
 
install -d 755 %{buildroot}/%{_libdir}/%{name}
cp -a %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/*.so %{buildroot}/%{_libdir}/%{name}

%files -f .mfiles
%_libdir/%name
%doc --no-dereference LICENSE
%doc --no-dereference NOTICE

%changelog
* Mon Feb 23 2026 Andrey Cherepanov <cas@altlinux.org> 1:4.38-alt1
- New version.

* Fri Jan 02 2026 Andrey Cherepanov <cas@altlinux.org> 1:4.29-alt1
- New version.

* Sat Dec 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:4.25-alt1_1jpp11.1
- NMU: build for LoongArch.

* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 1:4.25-alt1_1jpp11
- update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:4.23-alt1_1jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:4.21-alt1_1jpp11
- new version

* Tue Jul 02 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.9.0-alt0.2jpp
- updated requires thanks to arei@

* Sun Jun 30 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.9.0-alt0.1jpp
- updated to 4.9.0; added armv7hl and ppc64le

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.7.3-alt0.1jpp
- updated to 4.7.3

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt0.2jpp
- added aarch64

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt0.1jpp
- bootstrap pack of jars

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.2jpp
- install to %%_jnidir

* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

