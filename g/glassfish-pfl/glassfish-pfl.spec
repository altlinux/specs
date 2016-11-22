Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: swig
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name glassfish-pfl
%define version 3.2.0
%global namedreltag -b001
%global namedversion %{version}%{?namedreltag}
Name:          glassfish-pfl
Version:       3.2.0
Release:       alt2_0.10.b001jpp8
Summary:       GlassFish Primitive Function Library
# Few files in src/org/glassfish/pfl/test/ is under ASL 2.0
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:           http://java.net/projects/gmbal/pages/Home
# hg clone -r VERSION-3.2.0-b001 https://hg.java.net/hg/gmbal~pfl glassfish-pfl-3.2.0-b001
# find glassfish-pfl-3.2.0-b001/ -name '*.jar' -delete
# find glassfish-pfl-3.2.0-b001/ -name '*.class' -delete
# find glassfish-pfl-3.2.0-b001/ -name '*.zip' -delete
# rm -rf glassfish-pfl-3.2.0-b001/src/org/glassfish/pfl/objectweb
# tar czf glassfish-pfl-3.2.0-b001-src-hg.tar.gz glassfish-pfl-3.2.0-b001
Source0:       %{name}-%{namedversion}-src-hg.tar.gz
# custom build file
Source1:       %{name}-%{namedversion}-00-build.xml

Source2:       http://repo1.maven.org/maven2/org/glassfish/pfl/pfl-basic/3.2.0-b001/pfl-basic-3.2.0-b001.pom
Source3:       http://repo1.maven.org/maven2/org/glassfish/pfl/pfl-basic-tools/3.2.0-b001/pfl-basic-tools-3.2.0-b001.pom
Source4:       http://repo1.maven.org/maven2/org/glassfish/pfl/pfl-dynamic/3.2.0-b001/pfl-dynamic-3.2.0-b001.pom
# custom pom file
Source5:       pfl-ff-%{namedversion}.pom

Source6:       http://repo1.maven.org/maven2/org/glassfish/pfl/pfl-tf/3.2.0-b001/pfl-tf-3.2.0-b001.pom
Source7:       http://repo1.maven.org/maven2/org/glassfish/pfl/pfl-tf-tools/3.2.0-b001/pfl-tf-tools-3.2.0-b001.pom
Source8:       http://repo1.maven.org/maven2/org/glassfish/pfl/pfl-test/3.2.0-b001/pfl-test-3.2.0-b001.pom

# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-pfl package don't include the license file
Source9:       glassfish-LICENSE.txt

Source10:      http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:        %{name}-%{namedversion}-use-system-asm.patch

BuildRequires: ant
BuildRequires: aqute-bnd
BuildRequires: javapackages-local
BuildRequires: objectweb-asm3

# test deps
BuildRequires: geronimo-ejb
BuildRequires: hamcrest
BuildRequires: junit

BuildArch:     noarch
Source44: import.info

%description
The GlassFish MBean Annotation Library (gmbal, pronounced "Gumball")
is a library for using annotations to create Open MBeans. There is similar
functionality in JSR 255 for JDK 7, but gmbal only requires JDK 5. Gmbal
also supports JSR 77 ObjectNames and the GlassFish Version 3 AMX 
requirements for MBeans. AS a consequence, gmbal-enabled classes
will be fully manageable in GlassFish v3 using the standard GlassFish
v3 admin tools, while still being manageable with generic MBean tools
when not run under GlassFish v3.

This package provides the gmbal Primitive Function Library.
 
%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
cp -p %{SOURCE1} build.xml
%patch0 -p1

cp -p %{SOURCE4} pom-dynamic.xml
%pom_remove_dep org.glassfish.pfl:pfl-asm pom-dynamic.xml
%pom_xpath_inject "pom:project/pom:dependencies" "
    <dependency>
      <groupId>asm</groupId>
      <artifactId>asm</artifactId>
      <version>3</version>
    </dependency>
    <dependency>
      <groupId>asm</groupId>
      <artifactId>asm-util</artifactId>
      <version>3</version>
    </dependency>" pom-dynamic.xml

cp -p %{SOURCE6} pom-tf.xml
%pom_remove_dep org.glassfish.pfl:pfl-asm pom-tf.xml
%pom_xpath_inject "pom:project/pom:dependencies" "
    <dependency>
      <groupId>asm</groupId>
      <artifactId>asm</artifactId>
      <version>3</version>
    </dependency>
    <dependency>
      <groupId>asm</groupId>
      <artifactId>asm-tree</artifactId>
      <version>3</version>
    </dependency>
    <dependency>
      <groupId>asm</groupId>
      <artifactId>asm-util</artifactId>
      <version>3</version>
    </dependency>" pom-tf.xml

cp -p %{SOURCE7} pom-tf-tools.xml
%pom_remove_dep org.glassfish.pfl:pfl-asm pom-tf-tools.xml
%pom_xpath_inject "pom:project/pom:dependencies" "
    <dependency>
      <groupId>asm</groupId>
      <artifactId>asm</artifactId>
      <version>3</version>
    </dependency>
    <dependency>
      <groupId>asm</groupId>
      <artifactId>asm-tree</artifactId>
      <version>3</version>
    </dependency>
    <dependency>
      <groupId>asm</groupId>
      <artifactId>asm-util</artifactId>
      <version>3</version>
    </dependency>" pom-tf-tools.xml

cp -p %{SOURCE9} LICENSE.txt
cp -p %{SOURCE10} .
sed -i 's/\r//' LICENSE.txt LICENSE-2.0.txt

%build

%ant dist javadoc test

%install
%mvn_artifact %{SOURCE2} target/pfl-basic.jar
%mvn_artifact %{SOURCE3} target/pfl-basic-tools.jar
%mvn_artifact pom-dynamic.xml target/pfl-dynamic.jar
%mvn_artifact %{SOURCE5} target/pfl-ff.jar
%mvn_artifact pom-tf.xml target/pfl-tf.jar
%mvn_artifact pom-tf-tools.xml target/pfl-tf-tools.jar
%mvn_artifact %{SOURCE8} target/pfl-test.jar
%mvn_install -J target/apidocs

%files -f .mfiles
%doc LICENSE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt2_0.10.b001jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt2_0.9.b001jpp8
- new version

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt2_0.3.b001jpp7
- new release

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_0.3.b001jpp7
- new release

