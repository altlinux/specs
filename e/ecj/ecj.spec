Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
Obsoletes: ecj-standalone <= 3.4.2-alt4_0jpp6
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Epoch: 1

%global qualifier R-4.5.2-201602121500

Summary: Eclipse Compiler for Java
Name: ecj
Version: 4.5.2
Release: alt1_3jpp8
URL: http://www.eclipse.org
License: EPL

Source0: http://download.eclipse.org/eclipse/downloads/drops4/%{qualifier}/ecjsrc-%{version}.jar
Source1: ecj.sh.in
Source3: https://repo1.maven.org/maven2/org/eclipse/jdt/core/compiler/ecj/%{version}/ecj-%{version}.pom
# Extracted from https://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/%%{qualifier}/ecj-%%{version}.jar
Source4: MANIFEST.MF

# Always generate debug info when building RPMs (Andrew Haley)
Patch0: %{name}-rpmdebuginfo.patch

BuildArch: noarch

BuildRequires: gzip gzip-utils less
BuildRequires: ant
BuildRequires: javapackages-local

Obsoletes: %{name}-native < 1:4.2.1-10
Source44: import.info

AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%prep
%setup -q -c
%patch0 -p1

sed -i -e 's|debuglevel=\"lines,source\"|debug=\"yes\"|g' build.xml
sed -i -e "s/Xlint:none/Xlint:none -encoding cp1252/g" build.xml
sed -i -e 's|1.6|1.7|g' build.xml
sed -i -e 's|import org.eclipse.jdt.core.JavaCore;||g' org/eclipse/jdt/internal/compiler/batch/ClasspathDirectory.java
sed -i -e 's|JavaCore.getOptions()||g' org/eclipse/jdt/internal/compiler/batch/ClasspathDirectory.java

cp %{SOURCE3} pom.xml
mkdir -p scripts/binary/META-INF/
cp %{SOURCE4} scripts/binary/META-INF/MANIFEST.MF

# JDTCompilerAdapter isn't used by the batch compiler
rm -f org/eclipse/jdt/core/JDTCompilerAdapter.java

# No dep on ant needed
%pom_remove_dep org.apache.ant:ant

# Symlinks and aliases
%mvn_file :ecj ecj eclipse-ecj jdtcore
%mvn_alias org.eclipse.jdt.core.compiler:ecj \
  org.eclipse.tycho:org.eclipse.jdt.core org.eclipse.tycho:org.eclipse.jdt.compiler.apt \
  org.eclipse.jetty.orbit:org.eclipse.jdt.core org.eclipse.jetty.orbit:org.eclipse.jdt.compiler.apt \
  org.eclipse.jdt:core

%build
ant 
gzip ecj.1

%install
%mvn_artifact pom.xml ecj.jar
%mvn_install

# Install the ecj wrapper script
install -p -D -m0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/ecj

# Install manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p ecj.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/ecj.1.gz

%files -f .mfiles
%doc about.html
%{_bindir}/ecj
%{_mandir}/man1/ecj*

%changelog
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

