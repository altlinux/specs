BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          glassfish-toplink-essentials
Version:       2.0.46
Release:       alt3_12jpp8
Summary:       Glassfish JPA Toplink Essentials
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/javaee5/persistence/
Source0:       http://dlc.sun.com.edgesuite.net/javaee5/promoted/source/glassfish-persistence-v2-b46-src.zip
# wget http://download.java.net/javaee5/v2.1.1_branch/promoted/source/glassfish-v2.1.1-b31g-src.zip
# unzip glassfish-v2.1.1-b31g-src.zip
# mkdir -p glassfish-bootstrap
# mv glassfish/bootstrap/* glassfish-bootstrap
# tar czf glassfish-bootstrap.tar.gz glassfish-bootstrap
Source1:       glassfish-bootstrap.tar.gz
# fix javadoc build
Patch0:        glassfish-entity-persistence-build.patch

Patch1:        glassfish-persistence-2.0.41-jdk7.patch
Patch2:        glassfish-persistence-2.0.41-agent-remove-manifest-classpath.patch
Patch3:        glassfish-persistence-2.0.41-use_system_antlr.patch

BuildRequires: java-devel
BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: antlr-tool
BuildRequires: geronimo-jta
BuildRequires: geronimo-jpa

Requires:      antlr-tool
Requires:      geronimo-jpa
Requires:      geronimo-jta

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Glassfish Persistence Implementation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name} Implementation
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c

tar xzf %{SOURCE1}
mv glassfish-bootstrap glassfish/bootstrap
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3

sed -i -e 's/@VERSION@/%{version}/' glassfish/entity-persistence/toplink-essentials.pom
sed -i -e 's/@VERSION@/%{version}/' glassfish/entity-persistence/toplink-essentials-agent.pom

cd glassfish/bootstrap/legal
for d in CDDLv1.0.txt LICENSE.txt COPYRIGHT 3RD-PARTY-LICENSE.txt ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

%build

pushd glassfish/entity-persistence
  export CLASSPATH=$(build-classpath geronimo-jpa)
  %ant -Djavaee.jar=$(build-classpath geronimo-jta) -Dglassfish.schemas.home=$PWD/../persistence-api/schemas all docs
popd

%install

mkdir -p %{buildroot}%{_javadir}/glassfish
install -m 644 publish/glassfish/lib/toplink-essentials.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 644 publish/glassfish/lib/toplink-essentials-agent.jar %{buildroot}%{_javadir}/%{name}-agent.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 glassfish/entity-persistence/toplink-essentials.pom \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
install -pm 644 glassfish/entity-persistence/toplink-essentials-agent.pom \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}-agent.pom
%add_maven_depmap JPP-%{name}-agent.pom %{name}-agent.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr glassfish/entity-persistence/build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc glassfish/bootstrap/legal/*

%files javadoc
%{_javadocdir}/%{name}
%doc glassfish/bootstrap/legal/3RD-PARTY-LICENSE*.txt
%doc glassfish/bootstrap/legal/CDDL*.txt
%doc glassfish/bootstrap/legal/COPYRIGHT
%doc glassfish/bootstrap/legal/LICENSE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.46-alt3_12jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.46-alt2_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.46-alt2_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.46-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.46-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.46-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.46-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.46-alt1_4jpp7
- new version

