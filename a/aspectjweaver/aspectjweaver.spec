BuildRequires: /proc
BuildRequires: jpackage-compat
Name:       aspectjweaver 
Version:    1.6.12
Release:    alt2_5jpp7
Summary:    Java byte-code weaving library
Group:      Development/Java
License:    EPL
URL:        http://eclipse.org/aspectj/

# wget -nd http://www.eclipse.org/downloads/download.php?file=/tools/aspectj/aspectj-1.6.12-src.jar
# jar xf aspectj-1.6.12-src.jar aspectjweaver1.6.12-src.jar
Source0:    aspectjweaver1.6.12-src.jar
# This build.xml file was adapted from the Ubuntu package. The src jar has no build scripts.
Source1:    aspectjweaver-build.xml
Source2:    http://repo1.maven.org/maven2/org/aspectj/aspectjweaver/1.6.12/aspectjweaver-1.6.12.pom
Patch0:     aspectjweaver-build-fixes.patch

BuildRequires:   jpackage-utils
BuildRequires:   ant
BuildRequires:   objectweb-asm
BuildRequires:   apache-commons-logging
Requires:        objectweb-asm
BuildArch:       noarch
Source44: import.info
Obsoletes: aspectj < 1.5.5

%description
The AspectJ Weaver supports byte-code weaving for aspect-oriented
programming (AOP) in java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{summary}.


%prep
%setup -q -c
%patch0 -p1
cp %{SOURCE1} build.xml
# JRockit is not open source, so we cannot build against it
rm org/aspectj/weaver/loadtime/JRockitAgent.java

%build
LANG=en_US.ISO8859-1 CLASSPATH=$( build-classpath objectweb-asm/asm commons-logging ) ant
ant javadoc

%install
install -d -m 0755 ${RPM_BUILD_ROOT}/%{_javadir}
install -m 0644 build/%{name}.jar ${RPM_BUILD_ROOT}/%{_javadir}/%{name}.jar

install -d -m 0755 ${RPM_BUILD_ROOT}/%{_mavenpomdir}
install -m 0644 %{SOURCE2} ${RPM_BUILD_ROOT}/%{_mavenpomdir}/JPP-%{name}.pom

install -d -m 0755 ${RPM_BUILD_ROOT}/%{_javadocdir}
cp -rp javadoc ${RPM_BUILD_ROOT}/%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/*

%changelog
* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt2_5jpp7
- added Obsoletes for aspectj

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt1_5jpp7
- new release

