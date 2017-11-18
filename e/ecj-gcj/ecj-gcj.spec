%def_with gcj
%def_without native
BuildRequires: /proc
BuildRequires: jpackage-1.7.0-compat ant1.9
BuildRequires: rpm-build-java

#global qualifier R-4.5.1-201509040015
%global qualifier R-4.4-201406061215

%define oldname ecj
Group: Development/Java
Summary: Eclipse Compiler for Java
Name: ecj-gcj
Version: 4.4.0
#Version: 4.5.1
Release: alt1_1jpp6
URL: http://www.eclipse.org
License: EPL

Source0: http://download.eclipse.org/eclipse/downloads/drops4/%{qualifier}/ecjsrc-4.4.jar
Source1: %{name}.sh.in
# Use ECJ for GCJ
# cvs -d:pserver:anonymous@sourceware.org:/cvs/rhug \
# export -D 2013-12-11 eclipse-gcj
# tar cjf ecj-gcj.tar.bz2 eclipse-gcj
Source2: %{oldname}-gcj.tar.bz2
Source3: https://repo1.maven.org/maven2/org/eclipse/jdt/core/compiler/ecj/%{version}/ecj-%{version}.pom
# Extracted from https://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/%{qualifier}/ecj-%{version}.jar
Source4: MANIFEST.MF

# Always generate debug info when building RPMs (Andrew Haley)
Patch0: %{oldname}-rpmdebuginfo.patch
# build.xml fails to include a necessary .props file in the built ecj.jar
Patch1: %{oldname}-include-props.patch
Patch2: %{oldname}-defaultto1.5.patch
Patch5: eclipse-gcj-nodummysymbol.patch

BuildRequires: gzip

Source44: import.info

AutoReq: yes, noosgi
AutoProv: yes, noosgi
%if_with gcj
BuildRequires: gcc-java >= 4.0.0
BuildRequires: /usr/bin/aot-compile-rpm
%if_with native
BuildArch: noarch
%endif
%else
BuildArch: noarch
%endif

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%if_with gcj
%if_with native
%package native
Summary:       Native(gcj) bits for %{name}
Group:         Development/Java
Requires:      %{name} = %EVR
Requires: libgcj >= 4.0.0
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat

%description native
AOT compiled ecj to speed up when running under GCJ.
%endif
%endif

%prep
%setup -q -c
%patch0 -p1
%patch1 -b .sav
%patch2 -p1

sed -i -e 's|debuglevel=\"lines,source\"|debug=\"yes\"|g' build.xml
sed -i -e "s/Xlint:none/Xlint:none -encoding cp1252/g" build.xml
#sed -i -e 's|1.6|1.7|g' build.xml
#sed -i -e 's|import org.eclipse.jdt.core.JavaCore;||g' org/eclipse/jdt/internal/compiler/batch/ClasspathDirectory.java
#sed -i -e 's|JavaCore.getOptions()||g' org/eclipse/jdt/internal/compiler/batch/ClasspathDirectory.java

%if 1
sed -i -e 's|source=\"1.6\"|source=\"1.5\"|g' build.xml
sed -i -e 's|target=\"1.6\"|target=\"1.5\"|g' build.xml
%endif

cp %{SOURCE3} pom.xml
# Use ECJ for GCJ's bytecode compiler
tar jxf %{SOURCE2}
mv eclipse-gcj/org/eclipse/jdt/internal/compiler/batch/GCCMain.java \
  org/eclipse/jdt/internal/compiler/batch/
%patch5 -p1
cat eclipse-gcj/gcc.properties >> \
  org/eclipse/jdt/internal/compiler/batch/messages.properties
rm -rf eclipse-gcj

mkdir -p scripts/binary/META-INF/
cp %{SOURCE4} scripts/binary/META-INF/MANIFEST.MF

# Remove bits of JDT Core we don't want to build
rm -r org/eclipse/jdt/internal/compiler/tool
rm -r org/eclipse/jdt/internal/compiler/apt
rm -f org/eclipse/jdt/core/BuildJarIndex.java

# JDTCompilerAdapter isn't used by the batch compiler
rm -f org/eclipse/jdt/core/JDTCompilerAdapter.java

%build
ant1.9 
gzip ecj.1

%install
mkdir -p %{buildroot}%{_javadir}
install -m0644 %{oldname}.jar %{buildroot}%{_javadir}/%{name}.jar

# Install the ecj wrapper script
install -p -D -m0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# Install manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p ecj.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz

aot-compile-rpm

%files
%doc about.html
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%if_with gcj
%if_with native
%files native
%endif
%{_libdir}/gcj/%{name}
%endif

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.4.0-alt1_1jpp6
- compat package for gcj
