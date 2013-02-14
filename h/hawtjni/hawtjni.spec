Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             hawtjni
Version:          1.5
Release:          alt2_5jpp7
Summary:          Code generator that produces the JNI code
Group:            Development/Java
License:          ASL 2.0 and EPL and BSD
URL:              http://hawtjni.fusesource.org/

# git clone git://github.com/fusesource/hawtjni.git
# cd hawtjni && git archive --format=tar --prefix=hawtjni-1.5/ hawtjni-project-1.5 | xz > hawtjni-1.5.tar.xz
Source0:          %{name}-%{version}.tar.xz
Patch0:           0001-Fix-shading-and-remove-unneeded-modules.patch
Patch1:           0002-Fix-xbean-compatibility.patch
Patch2:           0003-Remove-plexus-maven-plugin-dependency.patch
Patch3:           0004-Remove-eclipse-plugin.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-idea-plugin
BuildRequires:    maven-plugin-plugin
BuildRequires:    maven-surefire-report-plugin
BuildRequires:    maven-project-info-reports-plugin
BuildRequires:    maven-plugin-jxr
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    plexus-containers-component-metadata
BuildRequires:    log4j
BuildRequires:    junit4
BuildRequires:    fusesource-pom
BuildRequires:    xbean

Requires:         jpackage-utils
Requires:         xbean
Requires:         apache-commons-cli
Requires:         objectweb-asm
Source44: import.info

%description
HawtJNI is a code generator that produces the JNI code needed to
implement java native methods. It is based on the jnigen code generator
that is part of the SWT Tools project which is used to generate all the
JNI code which powers the eclipse platform.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%package -n maven-%{name}-plugin
Summary:          Use HawtJNI from a maven plugin
Group:            Development/Java
Requires:         maven
Requires:         plexus-utils
Requires:         plexus-interpolation
Requires:         maven-archiver
Requires:         plexus-archiver
Requires:         plexus-io
Requires:         hawtjni = %{?epoch:%epoch:}%{version}-%{release}

%description -n maven-%{name}-plugin
This package allows to use HawtJNI from a maven plugin.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
# JAR
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}-generator/target/%{name}-generator-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-generator.jar
cp -p %{name}-runtime/target/%{name}-runtime-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-runtime.jar
cp -p maven-%{name}-plugin/target/maven-%{name}-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/maven-%{name}-plugin.jar

# JAVADOC
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-pom.pom
install -pm 644 %{name}-generator/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-generator.pom
install -pm 644 %{name}-runtime/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-runtime.pom
install -pm 644 maven-%{name}-plugin/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-maven-%{name}-plugin.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-pom.pom
%add_maven_depmap JPP-%{name}-generator.pom %{name}-generator.jar
%add_maven_depmap JPP-%{name}-runtime.pom %{name}-runtime.jar
%add_maven_depmap JPP-maven-%{name}-plugin.pom maven-%{name}-plugin.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc readme.md license.txt changelog.md
%exclude %{_mavenpomdir}/JPP-maven-%{name}-plugin.pom
%exclude %{_javadir}/maven-%{name}-plugin.jar

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%files -n maven-%{name}-plugin
%{_mavenpomdir}/JPP-maven-%{name}-plugin.pom
%{_javadir}/maven-%{name}-plugin.jar

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_5jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_5jpp7
- fc update

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_4jpp7
- new fc release

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp6
- fixed build:
  + changed objectweb-asm version in hawtjni-asm.patch to 3.3.1
  + added hawtjni-pom-alt.patch to fix shading

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp6
- new version

