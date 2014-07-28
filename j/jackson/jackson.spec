# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: jackson
Version: 1.9.4
Release: alt2_6jpp7
Summary: Jackson Java JSON-processor

Group: Development/Java
License: ASL 2.0 or LGPLv2
URL: http://jackson.codehaus.org

Source0: http://jackson.codehaus.org/1.9.4/jackson-src-1.9.4.tar.gz

# Build plain jar files instead of OSGi bundles in order to avoid depending on
# BND:
Patch0: %{name}-build-plain-jars-instead-of-osgi-bundles.patch

# Don't require a repackaged version of ASM:
Patch1: %{name}-dont-require-repackaged-asm.patch

# Don't bundle the ASM classes:
Patch2: %{name}-dont-bundle-asm.patch

BuildArch: noarch

Requires: jpackage-utils
Requires: joda-time >= 1.6.2
Requires: stax2-api >= 3.1.1
Requires: jsr-311 >= 1.1.1
Requires: objectweb-asm >= 3.3

BuildRequires: jpackage-utils
BuildRequires: ant >= 1.8.2
BuildRequires: joda-time >= 1.6.2
BuildRequires: stax2-api >= 3.1.1
BuildRequires: jsr-311 >= 1.1.1
BuildRequires: objectweb-asm >= 3.3
BuildRequires: cglib >= 2.2
BuildRequires: groovy >= 1.8.5
Source44: import.info


%description
JSON processor (JSON parser + JSON generator) written in Java. Beyond basic
JSON reading/writing (parsing, generating), it also offers full node-based Tree
Model, as well as full OJM (Object/Json Mapper) data binding functionality.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Remove all the binary jar files, as the packaging policies
# forbids using them:
find . -type f -name '*.jar' -exec rm {} \;

# Remove some tests to avoid additional dependencies:
rm src/test/org/codehaus/jackson/map/interop/TestHibernate.java
rm src/perf/perf/TestJsonPerf.java
rm src/test/org/codehaus/jackson/map/interop/TestGoogleCollections.java

# Make symbolic links to the jar files expected by the ant build
# scripts:
ln -s $(build-classpath joda-time) lib/ext/joda-time.jar
ln -s $(build-classpath stax2-api) lib/xml/sta2-api.jar
ln -s $(build-classpath jsr-311) lib/jaxrs/jsr-311.jar
ln -s $(build-classpath objectweb-asm/asm) lib/ext/asm/asm.jar
ln -s $(build-classpath objectweb-asm/asm) lib/repackaged/jackson-asm.jar
ln -s $(build-classpath cglib) lib/ext/cglib/cglib-nodep.jar
ln -s $(build-classpath groovy) lib/ext/groovy/groovy.jar
ln -s $(build-classpath junit) lib/junit/junit.jar


%build
ant dist


%install

# Create the directories for the jar and pom files:
mkdir -p %{buildroot}%{_javadir}/jackson
install -d -m 755 %{buildroot}%{_mavenpomdir}

# For each jar file install it and its pom:
jars='
jackson-core-asl
jackson-mapper-asl
jackson-xc
jackson-smile
jackson-mrbean
jackson-jaxrs
'
for jar in ${jars}
do
  cp -p dist/${jar}-%{version}.jar %{buildroot}%{_javadir}/jackson/${jar}.jar
  install -pm 644 dist/${jar}-%{version}.pom %{buildroot}/%{_mavenpomdir}/JPP.jackson-${jar}.pom
  %add_maven_depmap JPP.jackson-${jar}.pom jackson/${jar}.jar
done

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}/.


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}/*
%doc README.txt
%doc release-notes


%files javadoc
%{_javadocdir}/%{name}
%doc README.txt
%doc release-notes


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt1_5jpp7
- new version

