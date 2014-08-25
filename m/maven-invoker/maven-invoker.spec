Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-invoker
Version:        2.1.1
Release:        alt2_6jpp7
Summary:        Fires a maven build in a clean environment
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-invoker/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         %{name}-MSHARED-278.patch
Patch1:         %{name}-MSHARED-279.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-shared
Requires:       jpackage-utils
Requires:       maven-shared
Requires:       plexus-containers-component-annotations
Requires:       plexus-utils

Obsoletes:      maven-shared-invoker < %{version}-%{release}
Provides:       maven-shared-invoker = %{version}-%{release}
Source44: import.info

%description
This API is concerned with firing a Maven build in a new JVM. It accomplishes
its task by building up a conventional Maven command line from options given in
the current request, along with those global options specified in the invoker
itself. Once it has the command line, the invoker will execute it, and capture
the resulting exit code or any exception thrown to signal a failure to execute.
Input/output control can be specified using an InputStream and up to two
InvocationOutputHandlers.

This is a replacement package for maven-shared-invoker

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild package javadoc:aggregate -Dmaven.test.failure.ignore

%install
# JAR
install -Ddm 755 %{buildroot}/%{_javadir}
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM
install -Ddm 755 %{buildroot}/%{_mavenpomdir}
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# JavaDoc
install -Ddm 755 %{buildroot}/%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}


%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_6jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_0jpp7
- hold obsoletes

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_6jpp7
- new version

