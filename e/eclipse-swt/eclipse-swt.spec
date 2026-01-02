# see alt bug #43049
%global __find_debuginfo_files %nil
# libs.req java problem
%add_findreq_skiplist %_libdir/eclipse-swt/*.so
%define swtsrcdir bundles/org.eclipse.swt

Name:    eclipse-swt
Version: 4.29
Release: alt1
Epoch:   1
Summary: Eclipse SWT: The Standard Widget Toolkit for GTK+

License: EPL-2.0
Group: Development/Java
URL: https://www.eclipse.org/swt/

Source0: %name-%version.tar
Source1: classpath.xls

# Avoid the need for a javascript interpreter at build time
Patch0: eclipse-swt-avoid-javascript-at-build.patch
# Remove eclipse tasks and modify build tasks to generate jar like expected
Patch1: eclipse-swt-rm-eclipse-tasks-and-customize-build.patch
# Add fedora cflags to build native libs
Patch2: eclipse-swt-fedora-build-native.patch

ExclusiveArch:  x86_64 aarch64 ppc64le loongarch64

Requires: java-21-openjdk
Requires: libwebkit2gtk4.1-gir

BuildRequires(pre): /proc rpm-build-java
BuildRequires(pre): maven-local
BuildRequires: gcc-c++
BuildRequires: java-21-openjdk-devel
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
%patch0 -p1
%patch1 -p1
	
# Patch doesn't support path with spaces, renaming and back to apply patch
mv %{swtsrcdir}/Eclipse\ SWT\ PI %{swtsrcdir}/Eclipse-SWT-PI
%patch2 -p1
mv %{swtsrcdir}/Eclipse-SWT-PI %{swtsrcdir}/Eclipse\ SWT\ PI

install -Dpm0644 %SOURCE1 %{swtsrcdir}/tasks/classpath.xls
	
# This part generates secondary fragments using primary fragments
%pom_xpath_inject "pom:profiles/pom:profile[pom:id='unix']/pom:build/pom:plugins/pom:plugin[pom:artifactId='target-platform-configuration']/pom:configuration/pom:environments" \
  "<environment><os>linux</os><ws>gtk</ws><arch>s390x</arch></environment>" .
 
cp %{swtsrcdir}/Eclipse\ SWT/common/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT/common/version.txt %{swtsrcdir}/
cp %{swtsrcdir}/Eclipse\ SWT\ PI/{common,cairo}/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ OpenGL/glx/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ AWT/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/

%build
cd %swtsrcdir
 
# Build native part
export SWT_LIB_DEBUG=1
export CFLAGS="${RPM_OPT_FLAGS} -std=gnu17 -Wno-error=deprecated-declarations"
export LFLAGS="${RPM_LD_FLAGS}"
ant -f buildSWT.xml build_local -Dbuild_dir=Eclipse\ SWT\ PI/gtk/library -Dtargets="-gtk3 install" -Dclean= -Dcflags="${RPM_OPT_FLAGS}" -Dlflags="${RPM_LD_FLAGS}"
 
# Build Java part
ant -f buildSWT.xml check_compilation_all_platforms -Drepo.src=../../
 
# Build Jar file
ant -f build.xml

%install
# Generate addition Maven metadata
rm -rf .xmvn/ .xmvn-reactor
 
# Install Maven metadata for SWT
JAR=%{swtsrcdir}/org.eclipse.swt_*.jar
VER=$(echo $JAR | sed -e "s/.*_\(.*\)\.jar/\1/")
%mvn_artifact "org.eclipse.swt:org.eclipse.swt:jar:$VER" %{swtsrcdir}/org.eclipse.swt_*.jar
%mvn_alias "org.eclipse.swt:org.eclipse.swt" "org.eclipse.swt:swt"
%mvn_file "org.eclipse.swt:org.eclipse.swt" swt
 
%mvn_install -J %{swtsrcdir}/docs/api/
 
# fix so permissions
find %{swtsrcdir}/*.so -name *.so -exec chmod a+x {} \;
 
install -d 755 %buildroot/%_libdir/%name
cp -a %swtsrcdir/*.so %buildroot/%_libdir/%name

%files -f .mfiles
%_libdir/%name
%doc --no-dereference LICENSE
%doc --no-dereference NOTICE

%changelog
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

