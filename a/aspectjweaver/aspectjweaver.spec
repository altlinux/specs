Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          aspectjweaver 
Version:       1.8.4
Release:       alt1_4jpp8
Summary:       Java byte-code weaving library
License:       EPL
URL:           http://eclipse.org/aspectj/
Source0:       http://repo1.maven.org/maven2/org/aspectj/%{name}/%{version}/%{name}-%{version}-sources.jar
# This build.xml file was adapted from the Ubuntu package. The src jar has no build scripts.
Source1:       aspectjweaver-build.xml
Source2:       http://repo1.maven.org/maven2/org/aspectj/%{name}/%{version}/%{name}-%{version}.pom
Source3:       epl-v10.txt

BuildRequires: ant
BuildRequires: apache-commons-logging
BuildRequires: javapackages-local
BuildRequires: objectweb-asm
#Requires:      objectweb-asm
BuildArch:     noarch
Source44: import.info

%description
The AspectJ Weaver supports byte-code weaving for aspect-oriented
programming (AOP) in java.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{summary}.

%prep
%setup -q -c
sed -i.objectweb-asm "s|import aj.|import |" \
 org/aspectj/weaver/bcel/asm/StackMapAdder.java

cp %{SOURCE1} build.xml

# JRockit is not open source, so we cannot build against it
rm org/aspectj/weaver/loadtime/JRockitAgent.java

cp %{SOURCE2} pom.xml
%pom_xpath_inject "pom:project" "
  <dependencies>
    <dependency>
      <groupId>org.ow2.asm</groupId>
      <artifactId>asm</artifactId>
      <version>5.0.3</version>
    </dependency>
  </dependencies>"

cp %{SOURCE3} .
  
%build

%mvn_file org.aspectj:%{name} %{name}
%mvn_alias org.aspectj:%{name} "org.aspectj:aspectjrt" "aspectj:aspectjrt"
LANG=en_US.ISO8859-1 CLASSPATH=$( build-classpath objectweb-asm/asm commons-logging ) ant
LANG=en_US.ISO8859-1 CLASSPATH=$( build-classpath objectweb-asm/asm commons-logging ) ant javadoc
%mvn_artifact pom.xml build/%{name}.jar

%install
%mvn_install -J javadoc

%files -f .mfiles
%doc epl-v10.txt

%files javadoc -f .mfiles-javadoc
%doc epl-v10.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.4-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.4-alt1_3jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt4_1jpp6
- applied repocop patches

* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt3_1jpp6
- merged aspectjweaver back

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt1_1jpp6
- new version

* Sat Oct 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.11-alt1_1jpp6
- new version

* Fri Oct 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.5-alt1_1jpp6
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt1_1jpp6
- new version

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt3_1jpp6
- build with saxon6

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt2_1jpp6
- fixed build

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt1_1jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_2jpp5
- fixed build with eclipse 3.5

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_2jpp5
- rebuild with eclipse 3.4

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_2jpp5
- new version

