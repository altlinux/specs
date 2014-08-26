# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
Obsoletes: ecj-standalone <= 3.4.2-alt4_0jpp6
BuildRequires: /proc
BuildRequires: jpackage-compat
Epoch: 1

%global qualifier 201209141800

%define with_gcjbootstrap %{!?_with_gcjbootstrap:0}%{?_with_gcjbootstrap:1}
%define without_gcjbootstrap %{?_with_gcjbootstrap:0}%{!?_with_gcjbootstrap:1}

Summary: Eclipse Compiler for Java
Name: ecj
Version: 4.2.1
Release: alt1_7jpp7
URL: http://www.eclipse.org
License: EPL
Group: Development/Java
Source0: http://download.eclipse.org/eclipse/downloads/drops4/R-%{version}-%{qualifier}/%{name}src-%{version}.jar
Source1: ecj.sh.in
# Use ECJ for GCJ
# cvs -d:pserver:anonymous@sourceware.org:/cvs/rhug \
# export -D 2009-09-28 eclipse-gcj
# tar cjf ecj-gcj.tar.bz2 eclipse-gcj
Source2: %{name}-gcj.tar.bz2
#Patched from http://repo2.maven.org/maven2/org/eclipse/jdt/core/3.3.0-v_771/core-3.3.0-v_771.pom 
# No dependencies are needed for ecj, dependencies are for using of jdt.core which makes no sense outside of eclipse
Source3: core-3.3.0-v_771.pom
Source4: ecj.1
# Always generate debug info when building RPMs (Andrew Haley)
Patch0: %{name}-rpmdebuginfo.patch
Patch1: %{name}-defaultto1.5.patch
Patch2: %{name}-generatedebuginfo.patch
# Patches Source2 for compatibility with newer ecj
Patch3: eclipse-gcj-compat4.2.1.patch
# build.xml fails to include a necessary .props file in the built ecj.jar
Patch4: %{name}-include-props.patch
Patch5: eclipse-gcj-nodummysymbol.patch

BuildRequires: gcc-java >= 4.0.0
BuildRequires: /usr/bin/aot-compile-rpm
BuildRequires: java-gcj-compat
BuildRequires: gzip

%if ! %{with_gcjbootstrap}
BuildRequires: ant
%endif

Provides: eclipse-ecj = %{epoch}:%{version}-%{release}
Obsoletes: eclipse-ecj < 1:3.4.2-4
Source44: import.info

AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%package native
Summary:	Native(gcj) bits for %{name}
Group:		Development/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires: libgcj >= 4.0.0
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat

%description native
AOT compiled ecj to speed up when running under GCJ.


%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

cp %{SOURCE3} pom.xml
# Use ECJ for GCJ's bytecode compiler
tar jxf %{SOURCE2}
mv eclipse-gcj/org/eclipse/jdt/internal/compiler/batch/GCCMain.java \
  org/eclipse/jdt/internal/compiler/batch/
%patch3 -p1
%patch5 -p1
cat eclipse-gcj/gcc.properties >> \
  org/eclipse/jdt/internal/compiler/batch/messages.properties
rm -rf eclipse-gcj

# Remove bits of JDT Core we don't want to build
rm -r org/eclipse/jdt/internal/compiler/tool
rm -r org/eclipse/jdt/internal/compiler/apt
rm -f org/eclipse/jdt/core/BuildJarIndex.java

# JDTCompilerAdapter isn't used by the batch compiler
rm -f org/eclipse/jdt/core/JDTCompilerAdapter.java
cp %{SOURCE4} ecj.1

%build
%if %{with_gcjbootstrap}
  for f in `find -name '*.java' | cut -c 3- | LC_ALL=C sort`; do
    gcj -Wno-deprecated -C $f
  done

  find -name '*.class' -or -name '*.properties' -or -name '*.rsc' |\
    xargs fastjar cf %{name}-%{version}.jar
%else
   ant
%endif
gzip ecj.1

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -a *.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}.jar eclipse-%{name}.jar
ln -s %{name}.jar jdtcore.jar
popd

# Install the ecj wrapper script
install -p -D -m0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/ecj
sed --in-place "s:@JAVADIR@:%{_javadir}:" $RPM_BUILD_ROOT%{_bindir}/ecj

# Install manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p ecj.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/ecj.1.gz

aot-compile-rpm

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap -a "org.eclipse.tycho:org.eclipse.jdt.core,org.eclipse.jdt.core.compiler:ecj" JPP-%{name}.pom %{name}.jar

%files
%doc about.html
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_javadir}/eclipse-%{name}.jar
%{_javadir}/jdtcore.jar
%{_mandir}/man1/ecj.1*

%files native
%{_libdir}/gcj/%{name}

%changelog
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

