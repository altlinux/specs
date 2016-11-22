Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name log4j12
%define version 1.2.17
%global archiversion %(echo %{version} | tr . _ )

Name:          log4j12
Version:       1.2.17
Release:       alt1_12jpp8
Summary:       Java logging package
License:       ASL 2.0
URL:           http://logging.apache.org/log4j/1.2/
Source0:       https://github.com/apache/log4j/archive/v%{archiversion}.tar.gz

Source1:       log4j.catalog

Patch0:        0001-logfactor5-changed-userdir.patch
Patch1:        0009-Fix-tests.patch
Patch2:        0010-Fix-javadoc-link.patch

BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(javax.mail:mail)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(oro:oro)
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
Obsoletes:     log4j <= 0:1.2.17-14
BuildArch:     noarch
Source44: import.info

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n log4j-%{archiversion}
# Cleanup
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete
find . -name "*.dll" -print -delete
rm -rf docs/api

%patch0 -p1 -b .logfactor-home
%patch1 -p1 -b .fix-tests
%patch2 -p1 -b .xlink-javadoc

# Remove unavailable plugin
%pom_remove_plugin :clirr-maven-plugin
# Remove unwanted plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :rat-maven-plugin
# Disable javadoc jar
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

# Remove openejb from dependencies
%pom_remove_dep org.apache.openejb:javaee-api

# Fix ant gId
sed -i.ant "s|groupId>ant<|groupId>org.apache.ant<|g" pom.xml

sed -i.javac "s|1.4|1.5|g" pom.xml build.xml
sed -i.javac "s|1.4|1.5|g" pom.xml build.xml
sed -i.javac "s|1.1|1.5|g" tests/build.xml
sed -i.javac "s|1.1|1.5|g" tests/build.xml

# Fix OSGi manifest
sed -i.javax.jmdns "s|javax.jmdns.*;resolution:=optional,|!javax.jmdns.*,|g" pom.xml
# Add proper bundle symbolicname
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:configuration/pom:instructions" "
  <Bundle-SymbolicName>org.apache.log4j</Bundle-SymbolicName>
  <_nouses>true</_nouses>"

# Disable build unwanted dll library 
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-antrun-plugin']/pom:executions/pom:execution[pom:phase = 'process-classes' ]"

sed -i 's/\r//g' LICENSE NOTICE src/site/resources/css/*.css

# fix encoding of mailbox files
for i in contribs/JimMoore/mail*;do
    iconv --from=ISO-8859-1 --to=UTF-8 "$i" > new
    mv new "$i"
done

# Needed by tests
mkdir -p tests/lib/
(cd tests/lib/
  ln -s `build-classpath jakarta-oro`
  ln -s `build-classpath javamail/mail`
  ln -s `build-classpath junit`
)

%mvn_compat_version log4j:log4j 1.2.17 1.2.12 12
# Remove Microsoft Windows platform specific files
rm -r src/main/java/org/apache/log4j/nt/NTEventLogAppender.java \
 tests/src/java/org/apache/log4j/nt/NTEventLogAppenderTest.java

%mvn_file log4j:log4j log4j %{name}

%build

%mvn_build

%install
%mvn_install -X

# log4j-1 symlink for use with build-classpath et al.
ln -s log4j-%{version}.jar %{buildroot}%{_javadir}/log4j-1.jar

# DTD and the SGML catalog (XML catalog handled in scriptlets)
install -pD -T -m 644 src/main/javadoc/org/apache/log4j/xml/doc-files/log4j.dtd \
  %{buildroot}%{_datadir}/sgml/log4j/log4j.dtd
install -pD -T -m 644 %{SOURCE1} \
  %{buildroot}%{_datadir}/sgml/log4j/catalog

%post
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/log4j-%{version}-%{release}.cat \
    %{_datadir}/sgml/log4j/catalog > /dev/null || :
fi
if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --add public "-//APACHE//DTD LOG4J 1.2//EN" \
    file://%{_datadir}/sgml/log4j/log4j.dtd %{_sysconfdir}/xml/catalog \
    > /dev/null
  %{_bindir}/xmlcatalog --noout --add system log4j.dtd \
    file://%{_datadir}/sgml/log4j/log4j.dtd %{_sysconfdir}/xml/catalog \
    > /dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
  if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
    %{_bindir}/xmlcatalog --noout --del \
      file://%{_datadir}/sgml/log4j/log4j.dtd \
      %{_sysconfdir}/xml/catalog > /dev/null || :
  fi
fi

%postun
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/log4j-%{version}-%{release}.cat \
    %{_datadir}/sgml/log4j/catalog > /dev/null || :
fi

%files -f .mfiles
%{_javadir}/log4j-1.jar
%{_datadir}/sgml/log4j
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.17-alt1_12jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.17-alt1_10jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

