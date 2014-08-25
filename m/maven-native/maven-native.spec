# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name maven-native
%define version 1.0
%global namedreltag  -alpha-7
%global namedversion %{version}%{?namedreltag}
%global dotreltag    %(echo %{namedreltag} | tr - .)

Name:          maven-native
Version:       1.0
Release:       alt1_0.3.alpha.7jpp7
Summary:       Compile c and c++ source under Maven
Group:         Development/Java
License:       ASL 2.0 and MIT
Url:           http://mojo.codehaus.org/maven-native/
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/natives/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip

BuildRequires: mojo-parent

BuildRequires: mvn(bcel:bcel)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-api)
# replace plexus-container-default 1.0
BuildRequires: mvn(org.codehaus.plexus:plexus-container-default) >= 1.5.5
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)

# test deps
BuildRequires: mvn(aopalliance:aopalliance)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-plugin-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      mvn(org.codehaus.plexus:plexus-container-default) >= 1.5.5
Requires:      mvn(org.codehaus.plexus:plexus-utils)

BuildArch:     noarch
Source44: import.info

%description
Maven Native - compile C and C++ source under Maven
with compilers such as GCC, MSVC, GCJ etc ...

%package components
Group:         Development/Java
Summary:       Maven Native Components
Requires:      %{name} = %{version}-%{release}
Requires:      mvn(commons-lang:commons-lang)
Requires:      mvn(org.codehaus.plexus:plexus-container-default) >= 1.5.5
Requires:      mvn(org.codehaus.plexus:plexus-utils)

%description components
%{summary}.

%package -n native-maven-plugin
Group:         Development/Java
Summary:       Native Maven Plugin
Requires:      %{name} = %{version}-%{release}
Requires:      %{name}-components = %{version}-%{release}
Requires:      mvn(bcel:bcel)
Requires:      mvn(org.apache.maven:maven-artifact)
Requires:      mvn(org.apache.maven:maven-model)
Requires:      mvn(org.apache.maven:maven-plugin-api)
Requires:      mvn(org.apache.maven:maven-compat)
Requires:      mvn(org.apache.maven:maven-core)
Requires:      mvn(org.codehaus.plexus:plexus-archiver)
Requires:      mvn(org.codehaus.plexus:plexus-utils)

%description -n native-maven-plugin
%{summary}.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

for d in LICENSE ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

# use jvm apis
%pom_remove_dep backport-util-concurrent:backport-util-concurrent
%pom_remove_dep backport-util-concurrent:backport-util-concurrent maven-native-api
sed -i "s|edu.emory.mathcs.backport.java.util.concurrent|java.util.concurrent|" \
 maven-native-api/src/main/java/org/codehaus/mojo/natives/compiler/AbstractCompiler.java

sed -i 's|<artifactId>maven-project|<artifactId>maven-compat|' pom.xml
%pom_remove_dep :maven-project native-maven-plugin
%pom_add_dep org.apache.maven:maven-compat native-maven-plugin
%pom_add_dep org.apache.maven:maven-core native-maven-plugin

# missing test deps
%pom_add_dep aopalliance:aopalliance::test native-maven-plugin
%pom_add_dep net.sf.cglib:cglib::test native-maven-plugin

%build

#  junit.framework.AssertionFailedError: Failed to create plexus container.
# native-maven-plugin with maven3 test failures:
# Caused by: java.lang.ClassNotFoundException: org.apache.maven.artifact.repository.Authentication
#  java.lang.VerifyError: (class: org/apache/maven/project/MavenProject, 
# method: getSnapshotArtifactRepository signature: ()Lorg/apache/maven/artifact/repository/ArtifactRepository;)
# Incompatible argument to function
# force org.codehaus.plexus plexus-container-default 1.5.5 apis
mvn-rpmbuild -Dmojo.java.target=1.7 \
 -Dmaven.local.depmap.file="%{_mavendepmapfragdir}/plexus-containers-container-default" \
 -Dmaven.test.failure.ignore=true \
 package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom

mkdir -p %{buildroot}%{_javadir}/%{name}

install -m 644 %{name}-api/target/%{name}-api-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}-api.jar
install -pm 644 %{name}-api/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-api.pom
%add_maven_depmap JPP.%{name}-%{name}-api.pom %{name}/%{name}-api.jar

install -m 644 native-maven-plugin/target/native-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/native-maven-plugin.jar
install -pm 644 native-maven-plugin/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-native-maven-plugin.pom
%add_maven_depmap JPP.%{name}-native-maven-plugin.pom %{name}/native-maven-plugin.jar -f plugin
mv -f %{buildroot}%{_mavendepmapfragdir}/%{name}-plugin %{buildroot}%{_mavendepmapfragdir}/native-maven-plugin

(
cd maven-native-components
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-components.pom
%add_maven_depmap JPP.%{name}-components.pom -f components
for m in bcc \
      generic-c \
      javah \
      manager \
      msvc; do
    install -m 644 %{name}-${m}/target/%{name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
    install -pm 644 %{name}-${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar -f components
done
)

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-api.jar
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-api.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt

%files components
%{_javadir}/%{name}/%{name}-bcc.jar
%{_javadir}/%{name}/%{name}-generic-c.jar
%{_javadir}/%{name}/%{name}-javah.jar
%{_javadir}/%{name}/%{name}-manager.jar
%{_javadir}/%{name}/%{name}-msvc.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-bcc.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-generic-c.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-javah.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-manager.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-msvc.pom
%{_mavenpomdir}/JPP.%{name}-components.pom
%{_mavendepmapfragdir}/%{name}-components
%doc LICENSE.txt

%files -n native-maven-plugin
%{_javadir}/%{name}/native-maven-plugin.jar
%{_mavenpomdir}/JPP.%{name}-native-maven-plugin.pom
%{_mavendepmapfragdir}/native-maven-plugin
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.alpha.7jpp7
- new version

