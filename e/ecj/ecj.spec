BuildRequires: unzip
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Epoch: 1

%global qualifier R-4.19-202103031800

Summary: Eclipse Compiler for Java
Name: ecj
Version: 4.19
Release: alt2_1jpp11
URL: https://www.eclipse.org
License: EPL-2.0

Source0: https://download.eclipse.org/eclipse/downloads/drops4/%{qualifier}/ecjsrc-%{version}.jar
Source1: https://repo1.maven.org/maven2/org/eclipse/jdt/ecj/3.25.0/ecj-3.25.0.pom
# Extracted from https://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/%%{qualifier}/ecj-%%{version}.jar
Source4: MANIFEST.MF
# Java API stubs for newer JDKs to allow us to build on the system default JDK
# Fetched from https://github.com/eclipse/eclipse.jdt.core/blob/R4_18/org.eclipse.jdt.compiler.tool/lib/javax15api.jar
Source5: https://github.com/eclipse/eclipse.jdt.core/blob/R4_18/org.eclipse.jdt.compiler.tool/lib/javax15api.jar

# Always generate debug info when building RPMs (Andrew Haley)
Patch0: %{name}-rpmdebuginfo.patch

# Include java API stubs in build
Patch1: javaAPI.patch

BuildArch: noarch

BuildRequires: ant
BuildRequires: javapackages-local

# Build with Java 11 against bootclasspath of Java 8
BuildRequires: java-11-openjdk-devel
BuildRequires: java-1.8.0-openjdk-devel
Source44: import.info
# Use ECJ for GCJ
# cvs -d:pserver:anonymous@sourceware.org:/cvs/rhug \
# export -D 2013-12-11 eclipse-gcj
# tar cjf ecj-gcj.tar.bz2 eclipse-gcj
Source2: ecj-gcj.tar.bz2
Patch33: ecj-defaultto1.5.patch
Patch55: eclipse-gcj-nodummysymbol.patch
Patch34: ecj-gcj-for-4.6-api.patch

AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%prep
%setup -q -c
%patch0 -p1
%patch1

sed -i -e 's|debuglevel=\"lines,source\"|debug=\"yes\"|g' build.xml

cp %{SOURCE1} pom.xml
mkdir -p scripts/binary/META-INF/
cp %{SOURCE4} scripts/binary/META-INF/MANIFEST.MF
rm ./META-INF/ECLIPSE_.{SF,RSA}

# Aliases
%mvn_alias org.eclipse.jdt:ecj org.eclipse.jdt:core org.eclipse.jdt.core.compiler:ecj \
  org.eclipse.tycho:org.eclipse.jdt.core org.eclipse.tycho:org.eclipse.jdt.compiler.apt

# Make Java API stubs available for other packages
%mvn_artifact "org.eclipse:javax15api:jar:15" %{SOURCE5}
%patch33 -p1

# Use ECJ for GCJ's bytecode compiler
tar jxf %{SOURCE2}
mv eclipse-gcj/org/eclipse/jdt/internal/compiler/batch/GCCMain.java \
  org/eclipse/jdt/internal/compiler/batch/
%patch55 -p1
cat eclipse-gcj/gcc.properties >> \
  org/eclipse/jdt/internal/compiler/batch/messages.properties
rm -rf eclipse-gcj
%patch34 -p1
#patch55 -p1

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Djavaapi=%{SOURCE5}

%install
%mvn_artifact pom.xml ecj.jar
%mvn_install

# Install the ecj wrapper script
%jpackage_script org.eclipse.jdt.internal.compiler.batch.Main '' '' ecj ecj true

# Install manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p ecj.1 $RPM_BUILD_ROOT%{_mandir}/man1/ecj.1

%files -f .mfiles
%doc --no-dereference about.html
%{_bindir}/ecj
%{_mandir}/man1/ecj*

%changelog
* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 1:4.19-alt2_1jpp11
- added BR: unzip

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:4.19-alt1_1jpp11
- new version

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 1:4.16-alt2_4jpp11
- removed compat symlink for gradle

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:4.16-alt1_4jpp11
- new version

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 1:4.14-alt1_3jpp11
- new version

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_2jpp8
- new version

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt1_0.1jpp9
- rebuild with java 9

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt1_0.1jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.7.3a-alt1_1jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.7.1-alt1_1jpp8
- new version

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.2-alt2_3jpp8
- merged eclipse-gcj code && native by glebfm@

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.2-alt1_3jpp8
- new version

* Wed Feb 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:4.5.1-alt2_1jpp8
- Reenabled eclipse-gcj code.
- Updated eclipse-gcj to CVS 2013-12-11.
- Restored native subpackage.

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt1_1jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.2.1-alt1_7jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt5_7jpp6.qa1
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:3.4.2-alt4_7jpp6.qa1
- NMU: rebuilt for debuginfo.

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt4_7jpp6
- removed Req: java-gcj-compat (closes: #23902)

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt3_7jpp6
- BR:java-gcj-compat reduced to fastjar (#23902)

* Sat Feb 20 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt2_7jpp6
- removed poms as it breaks too much builds

* Tue Jan 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt1_7jpp6
- replaces ecj-standalone

