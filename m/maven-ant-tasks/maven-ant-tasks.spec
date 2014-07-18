Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-ant-tasks
Version:        2.1.3
Release:        alt1_4jpp7
Summary:        Allow Maven artifact handling features to be used from within an Ant build

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/ant-tasks/index.html
#The ant-tasks-in-ant-run-plugin test needs a dependency on ant-launcher
#http://jira.codehaus.org/browse/MANTTASKS-208
Source0:        http://www.apache.org/dist/maven/source/maven-ant-tasks-%{version}-src.zip
Source1:        %{name}.depmap
#Fix up ant groupId
Patch0:         maven-ant-tasks-2.1.1-ant-groupId.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant >= 1.8.0
BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-error-diagnostics
BuildRequires:  objectweb-asm
BuildRequires:  plexus-interpolation

Requires:       jpackage-utils
Requires:       ant >= 1.8.0
Requires:       maven
Requires:       maven-error-diagnostics
Source44: import.info

%description
Maven Ant Tasks allow several of Maven's artifact handling features to be
used from within an Ant build. These include:

* Dependency management - including transitive dependencies, scope recognition
  and SNAPSHOT handling
* Artifact deployment - deployment to a Maven repository (file integrated,
  other with extensions)
* POM processing - for reading and writing a Maven 2 pom.xml file


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1 -b .ant-groupId
#Need to tell maven invoker to run in jpp mode, write test.properties files
for f in src/it/*/invoker.properties
do
   tp=${f/invoker/test}
   cat >> $tp <<EOF
maven2.jpp.mode=1
EOF
done


%build
# Skip tests because they fail with maven 3, see upstream bug:
# http://jira.codehaus.org/browse/MANTTASKS-165
mvn-rpmbuild \
   -Dmaven.local.depmap.file="%{SOURCE1}" \
   -Dmaven.test.skip=true \
   install javadoc:javadoc


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/original-%{name}-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp target/site/apidocs \
       $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc DEPENDENCIES LICENSE NOTICE README.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}


%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_4jpp7
- update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

