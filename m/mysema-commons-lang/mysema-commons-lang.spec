Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          mysema-commons-lang
Version:       0.2.4
Release:       alt1_4jpp8
Summary:       Mysema Commons Lang
License:       ASL 2.0
URL:           http://www.mysema.com/
# often is offline https://github.com/querydsl/querydsl/issues/1080
# svn export https://source.mysema.com/svn/mysema/projects/commons/lang/tags/lang-0.2.4/ mysema-commons-lang-0.2.4
# tar cJf mysema-commons-lang-0.2.4.tar.xz mysema-commons-lang-0.2.4
Source0:       http://repo1.maven.org/maven2/com/mysema/commons/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:       http://repo1.maven.org/maven2/com/mysema/commons/%{name}/%{version}/%{name}-%{version}.pom
# mysema-commons-lang package don't include the license file
Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)

BuildArch:     noarch
Source44: import.info

%description
Mysema Commons Lang provides:

* General assertion utilities
* Empty implementation of the CloseableIterator interface
* Adapter implementation for Iterator and CloseableIterator instances
* Typed pair of values
* URIResolver provides URI resolving functionality
* URLEncoder provides URL encoding functionality

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -T -q -c

mkdir -p src/main/{java,resources}
(
  cd src/main/java
  %jar -xf %{SOURCE0}
  rm -rf META-INF
)

# clone source directory structure
find src/main/java/ -type d | while read dirname ; do
  newdirname=`echo $dirname | sed "s:src/main/java:src/main/resources:g"`
  mkdir -p $newdirname
done

# copy everything except *.java sources
find src/main/java/ -type f | grep -v "\.java" | while read cpfrom ; do
  cpto=`echo $cpfrom | sed "s:src/main/java:src/main/resources:g"`
  cp $cpfrom $cpto
done


cp -p %{SOURCE1} pom.xml

%pom_remove_parent
%pom_remove_plugin com.springsource.bundlor:com.springsource.bundlor.maven
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<configuration>
 <instructions>
  <Bundle-Name>Commons Lang</Bundle-Name>
  <Bundle-SymbolicName>com.mysema.commons.lang</Bundle-SymbolicName>
  <Bundle-Vendor>Mysema</Bundle-Vendor>
  <Export-Package>com.mysema.commons.lang*;version="${project.version}"</Export-Package>
 </instructions>
</configuration>
<executions>
 <execution>
  <id>bundle-manifest</id>
  <phase>process-classes</phase>
  <goals>
    <goal>manifest</goal>
  </goals>
 </execution>
</executions>'

%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:useDefaultManifestFile"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration" '
<archive>
 <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
</archive>'

cp -p %{SOURCE2} LICENSE
sed -i 's/\r//' LICENSE

%mvn_file com.mysema.commons:%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_4jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_2jpp8
- java 8 mass update

