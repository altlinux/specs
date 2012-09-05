AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global tag 201204190339

Name:      jacoco
Version:   0.5.7
Release:   alt1_0.6jpp7
Summary:   Java Code Coverage for Eclipse 
Group:     System/Libraries
License:   EPL
URL:       http://www.eclemma.org/jacoco/
#http://eclemma.svn.sourceforge.net/viewvc/eclemma/jacoco/tags/v0.5.7/?view=tar
Source0:   eclemma-v0.5.7.tar.gz
Patch0:    removeGroovyScriptingAndCircularDependency.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    eclipse-platform >= 1:4.2.0-0.10
BuildRequires:    eclipse-pde >= 1:4.2.0-0.10
BuildRequires:    tycho
BuildRequires:    maven-shade-plugin >= 1.5
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-dependency-plugin maven-antrun-plugin maven-assembly-plugin maven-clean-plugin maven-compiler-plugin maven-deploy-plugin
BuildRequires:    maven-install-plugin maven-invoker-plugin maven-gpg-plugin maven-jar-plugin maven-javadoc-plugin maven-plugin-plugin
BuildRequires:    maven-release-plugin maven-resources-plugin maven-shade-plugin maven-source-plugin maven-surefire-plugin maven-site-plugin
BuildRequires:    maven-plugin-tools-javadoc
BuildRequires:    dos2unix
Requires:         ant
Requires:         objectweb-asm
Source44: import.info

%description
JaCoCo is a free code coverage library for Java, 
which has been created by the EclEmma team based on the lessons learned 
from using and integration existing libraries over the last five years. 


%package    javadoc
Summary:    Java-docs for %{name}
Group:      Development/Java
Requires:   %{name} = %{version}-%{release}
Requires:   jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package    maven-plugin
Summary:    A Jacoco plugin for maven
Group:      System/Libraries
Requires:   maven
Requires:   objectweb-asm
Requires:   %{name} = %{version}-%{release}

%description maven-plugin
A Jacoco plugin for maven.

%prep
%setup -q -n v%{version}
%patch0 -p3

# make sure upstream hasn't sneaked in any jars we don't know about
JARS=""
for j in `find -name "*.jar"`; do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
   echo "These jars should be deleted and symlinked to system jars: $JARS"
   exit 1
fi

%build
# Note: Tests must be disabled because they introduce circular dependency
# right now.
OPTIONS=" -DrandomNumner=${RANDOM} -Dmaven.test.skip=true  clean install javadoc:aggregate"

# Ensure that all required dependencies are available in a local p2 repo                                
/bin/sh -x %{_eclipse_base}/buildscripts/copy-platform SDK %{_eclipse_base}

eclipse -debug -consolelog -nosplash -verbose -application org.eclipse.equinox.p2.publisher.FeaturesAndBundlesPublisher -me\
tadataRepository file:$PWD/myrepo -artifactRepository file:$PWD/myrepo -source $PWD/SDK -compress -append -publishArtifacts

pushd org.jacoco.build
    mvn-rpmbuild $OPTIONS
popd

dos2unix org.jacoco.doc/docroot/doc/.resources/doc.css 

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}

for f in    org.jacoco.agent \
            org.jacoco.agent.rt \
            org.jacoco.ant \
            org.jacoco.core \
            org.jacoco.report \
            jacoco-maven-plugin
do
    cp $f/target/$f-%{version}.%{tag}.jar %{buildroot}%{_javadir}/%{name}/$f.jar
done;

# Intsall maven stuff.
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 org.jacoco.build/pom.xml %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom
for f in    org.jacoco.agent \
            org.jacoco.agent.rt \
            org.jacoco.ant \
            org.jacoco.core \
            org.jacoco.report \
            jacoco-maven-plugin
do
    install -pm 644 $f/pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}-$f.pom
    %add_maven_depmap JPP.%{name}-$f.pom %{name}/$f.jar
done;

# javadoc 
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rf org.jacoco.build/target/site/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
#agent
%{_javadir}/jacoco/org.jacoco.agent.rt.jar
%{_mavenpomdir}/JPP.%{name}-org.jacoco.agent.rt.pom
#OSGi bundles
%{_javadir}/jacoco/org.jacoco.ant.jar
%{_javadir}/jacoco/org.jacoco.agent.jar
%{_javadir}/jacoco/org.jacoco.core.jar
%{_javadir}/jacoco/org.jacoco.report.jar
%{_mavenpomdir}/JPP.%{name}-org.jacoco.ant.pom
%{_mavenpomdir}/JPP.%{name}-org.jacoco.agent.pom
%{_mavenpomdir}/JPP.%{name}-org.jacoco.core.pom
%{_mavenpomdir}/JPP.%{name}-org.jacoco.report.pom

%doc org.jacoco.doc/docroot/*
%doc org.jacoco.doc/about.html

%files maven-plugin
%{_javadir}/%{name}/jacoco-maven-plugin.jar
%{_mavenpomdir}/JPP.%{name}-jacoco-maven-plugin.pom

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_0.6jpp7
- new version

