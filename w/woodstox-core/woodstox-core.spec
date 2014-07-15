BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name woodstox
%global core_name %{base_name}-core
%global stax2_ver  3.1.1

Name:             %{core_name}
Version:          4.1.2
Release:          alt2_3jpp7
Summary:          High-performance XML processor
License:          ASL 2.0 or LGPLv2+
Group:            Development/Java
URL:              http://%{base_name}.codehaus.org/

Source0:          http://%{base_name}.codehaus.org/%{version}/%{core_name}-src-%{version}.tar.gz

Patch0:           %{name}-unbundling.patch
Patch1:           %{name}-fsf-address.patch

BuildArch:        noarch

BuildRequires:    felix-osgi-core
BuildRequires:    relaxngDatatype
BuildRequires:    msv-xsdlib
BuildRequires:    msv-msv
BuildRequires:    stax2-api
BuildRequires:    maven
BuildRequires:    jpackage-utils

Requires:         felix-osgi-core
Requires:         relaxngDatatype
Requires:         msv-xsdlib
Requires:         msv-msv
Requires:         stax2-api
Requires:         jpackage-utils
Source44: import.info

%description
Woodstox is a high-performance validating namespace-aware StAX-compliant
(JSR-173) Open Source XML-processor written in Java.
XML processor means that it handles both input (== parsing)
and output (== writing, serialization)), as well as supporting tasks
such as validation.

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{version}

cp src/maven/%{name}-asl.pom pom.xml
cp src/maven/%{name}-lgpl.pom pom-lgpl.xml

%patch0 -p1
%patch1 -p1

sed -i "s/@VERSION@/%{version}/g" pom.xml pom-lgpl.xml
sed -i "s/@REQ_STAX2_VERSION@/%{stax2_ver}/g" pom.xml pom-lgpl.xml

# removing bundled stuff
rm -rf lib
rm -rf src/maven
rm -rf src/resources
rm -rf src/samples
rm -rf src/java/org
rm -rf src/test/org
rm -rf src/test/stax2

# fixing incomplete source directory structure
mkdir src/main
mv -f src/java src/main/
mkdir src/test/java
mv -f src/test/wstxtest src/test/java/

%build
# stax2 missing -> cannot compile tests -> tests skipped
mvn-rpmbuild -Dmaven.test.skip=true \
             install javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{name}-asl-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{name}-asl.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{name}-lgpl.jar

# pom
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-asl.pom
install -Dpm 644 pom-lgpl.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-lgpl.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}-asl.pom %{name}-asl.jar
%add_maven_depmap JPP-%{name}-lgpl.pom %{name}-lgpl.jar

%files
%doc release-notes/asl/ASL2.0 release-notes/lgpl/LGPL2.1 release-notes/asl/NOTICE
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-asl.jar
%{_javadir}/%{name}-lgpl.jar
%{_mavenpomdir}/JPP-%{name}-asl.pom
%{_mavenpomdir}/JPP-%{name}-lgpl.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc release-notes/asl/ASL2.0 release-notes/lgpl/LGPL2.1
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp7
- new version

