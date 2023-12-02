# see alt bug #43049
%global __find_debuginfo_files %nil
# libs.req java problem
%add_findreq_skiplist %_libdir/eclipse-swt/*.so
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 4.25
Epoch:                  1

%global swtdir          eclipse-platform-sources-I20220831-1800
%global eclipse_rel     %{version}
%global eclipse_tag     R-%{eclipse_rel}-202208311800
%global swtsrcdir       eclipse.platform.swt/bundles/org.eclipse.swt
%global eclipse_arch    %{_arch}

Name:           eclipse-swt
Version:        4.25
Release:        alt1_1jpp11.1
Summary:        Eclipse SWT: The Standard Widget Toolkit for GTK+

License:        EPL-2.0
URL:            https://www.eclipse.org/swt/

Source0:        https://download.eclipse.org/eclipse/downloads/drops4/%{eclipse_tag}/eclipse-platform-sources-%{eclipse_rel}.tar.xz
# Copy of the script https://git.eclipse.org/c/linuxtools/org.eclipse.linuxtools.eclipse-build.git/tree/utils/ensure_arch.sh. Need for create secondary arch for s390x
Source1:        ensure_arch.sh

# Avoid the need for a javascript interpreter at build time
Patch0:         eclipse-swt-avoid-javascript-at-build.patch
# Remove eclipse tasks and modify build tasks to generate jar like expected
Patch1:         eclipse-swt-rm-eclipse-tasks-and-customize-build.patch
# Add fedora cflags to build native libs
Patch2:         eclipse-swt-fedora-build-native.patch

ExclusiveArch:  s390x x86_64 aarch64 ppc64le loongarch64

Requires:       java-11-openjdk
Requires:       libwebkit2gtk libwebkit2gtk-gir

BuildRequires:  java-11-openjdk-devel
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  gcc
BuildRequires:  libwebkit2gtk-devel libwebkit2gtk-gir-devel
BuildRequires:  libcairo-devel
BuildRequires:  gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:  libGLU-devel

#Provides:       eclipse-swt = 1:%{version}-%{release}
#Obsoletes:      eclipse-swt <= 1:4.19-3
Source44: import.info

%description
SWT is an open source widget toolkit for Java designed to provide 
efficient, portable access to the user-interface facilities of the 
operating systems on which it is implemented.

%javadoc_package

%prep
%setup -q -n %{swtdir}
%patch0 -p1
%patch1 -p1

# Remove pre-compiled native launchers	
rm -rf rt.equinox.binaries/org.eclipse.equinox.executable/{bin,contributed}/

# Delete pre-built binary artifacts except some test data that cannot be generated
rm -rf rt.equinox.p2/
rm -rf eclipse.jdt.core/org.eclipse.jdt.core.tests.model/
find . ! -path "*/JCL/*" ! -name "rtstubs*.jar" ! -name "javax15api.jar" ! -name "j9stubs.jar" ! -name "annotations.jar" \
-type f -name *.jar -delete
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.so' -delete
find -name '*.dll' -delete
find -name '*.jnilib' -delete

# Patch doesn't support path with spaces, renaming and back to apply patch
mv %{swtsrcdir}/Eclipse\ SWT\ PI %{swtsrcdir}/Eclipse-SWT-PI
%patch2 -p1
mv %{swtsrcdir}/Eclipse-SWT-PI %{swtsrcdir}/Eclipse\ SWT\ PI

# This part generates secondary fragments using primary fragments
%pom_xpath_inject "pom:plugin[pom:artifactId='target-platform-configuration']/pom:configuration/pom:environments" \
  "<environment><os>linux</os><ws>gtk</ws><arch>s390x</arch></environment>" eclipse-platform-parent
rm -rf eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.s390x
rm -rf rt.equinox.framework/bundles/org.eclipse.equinox.launcher.gtk.linux.s390x
for dir in rt.equinox.binaries equinox/bundles eclipse.platform.swt.binaries/bundles ; do
  %{_sourcedir}/ensure_arch.sh "$dir" x86_64 s390x	
done

cp %{swtsrcdir}/Eclipse\ SWT/common/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT/common/version.txt %{swtsrcdir}/
cp %{swtsrcdir}/Eclipse\ SWT\ PI/{common,cairo}/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ OpenGL/glx/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ AWT/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.%{eclipse_arch}/about_files/*.txt %{swtsrcdir}/about_files/

%build

#export JAVA_HOME=%{_jvmdir}/java-11-openjdk

cd %{swtsrcdir}

# Build native part
export SWT_LIB_DEBUG=1
export CFLAGS="${RPM_OPT_FLAGS}"
export LFLAGS="${RPM_LD_FLAGS}"
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -f buildSWT.xml build_local -Dbuild_dir=Eclipse\ SWT\ PI/gtk/library -Dtargets="-gtk3 install" -Dclean= -Dcflags="${RPM_OPT_FLAGS}" -Dlflags="${RPM_LD_FLAGS}"

# Build Java part
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -f buildSWT.xml check_compilation_all_platforms -Drepo.src=../../

# Build Jar file
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -f build.xml

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

#fix so permissions
find %{swtsrcdir}/*.so -name *.so -exec chmod a+x {} \;

install -d 755 %{buildroot}/%{_libdir}/%{name}
cp -a %{swtsrcdir}/*.so %{buildroot}/%{_libdir}/%{name}

%files -f .mfiles
%{_libdir}/%{name}
%doc --no-dereference LICENSE
%doc --no-dereference NOTICE

%changelog
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

