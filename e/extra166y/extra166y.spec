Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          extra166y
Version:       1.7.0
Release:       alt1_5jpp8
Summary:       Concurrency JSR-166 - Collections supporting parallel operations
License:       Public Domain
URL:           http://gee.cs.oswego.edu/dl/concurrency-interest
# cvs -d :pserver:anonymous@gee.cs.oswego.edu/home/jsr166/jsr166 login
# cvs -d :pserver:anonymous@gee.cs.oswego.edu/home/jsr166/jsr166 export -r release-1_7_0 jsr166
# available in java 7 rt.jar
# rm -r jsr166/src/main/java
# rm -r jsr166/src/jsr166x jsr166/.cvsignore
# rm -r jsr166/src/jsr166y
# rm -r jsr166/src/loops
# rm -r jsr166/src/test/jtreg
# rm -r jsr166/src/test/loops
# rm -r jsr166/src/test/tck
# find jsr166 -type f -name "*.jar" -delete
# find jsr166 -type f -name "*.class" -delete
# tar cJf jsr166-1.7.0.tar.xz jsr166
Source0:       jsr166-%{version}.tar.xz
Source1:       http://repository.codehaus.org/org/codehaus/jsr166-mirror/%{name}/%{version}/%{name}-%{version}.pom
Source2:       extra166y-OSGi.bnd
Patch0:        extra166y-osgi-manifest.patch
BuildRequires: ant
BuildRequires: aqute-bnd
BuildRequires: javapackages-local
BuildRequires: junit
BuildArch:     noarch
Source44: import.info

%description
Implementation of Java collections supporting parallel operations using
Fork-Join concurrent framework provided by JSR-166.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jsr166
%patch0 -p0

# Use JVM jsr166
for s in $(find . -name "*.java");do
  sed -i "s|jsr166y.|java.util.concurrent.|" ${s}
done
sed -i '/configure-compiler, jsr166ycompile/d' build.xml

sed -i '/<compilerarg line="${build.args}"/d' build.xml

cp -p %{SOURCE2} extra166y.bnd
sed -i "s|@VERSION@|%{version}|" extra166y.bnd

%build

%mvn_file org.codehaus.jsr166-mirror:%{name} %{name}
export CLASSPATH=$(build-classpath junit)
ant extra166yjar extra166ydist-docs
%mvn_artifact %{SOURCE1} build/%{name}lib/%{name}.jar

%install
%mvn_install -J dist/%{name}docs

%files -f .mfiles
%doc src/main/intro.html src/main/readme

%files javadoc -f .mfiles-javadoc
%doc src/main/intro.html src/main/readme

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_4jpp8
- new version

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

