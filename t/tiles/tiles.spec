Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global master_version 3
Name:          tiles
Version:       2.2.2
Release:       alt2_3jpp7
Summary:       Java templating framework for web application user interfaces
Group:         Development/Java
License:       ASL 2.0
Url:           http://tiles.apache.org/
Source0:       http://www.apache.org/dist/%{name}/v%{version}/%{name}-%{version}-src.tar.gz
# wget -O tiles-master-3-pom.xml http://svn.apache.org/repos/asf/tiles/maven/tags/tiles-master-3/pom.xml
Source1:       %{name}-master-%{master_version}-pom.xml
# force tomcat 7.x apis use
Source2:       %{name}-%{version}-2-depmap
# remove shale-test and maven-taglib-plugin
# change 
#  org.codehaus.mojo rat-maven-plugin in org.apache.rat apache-rat-plugin
#  org.codehaus.mojo jxr-maven-plugin in org.apache.maven.plugins maven-jxr-plugin
# use tomcat 7.x apis
Patch0:        %{name}-%{version}-fix-build.patch
# replace ognl ognl 2.7.3 with apache-commons-ognl
Patch1:        %{name}-%{version}-commons-ognl.patch
# add tiles-master relativePath
Patch2:        %{name}-%{version}-parent-pom.patch
# build fix fot tomcat 7.x apis
Patch3:        %{name}-%{version}-servlet-servlet30.patch
Patch4:        %{name}-%{version}-jsp-servlet30.patch

BuildRequires: jpackage-utils

BuildRequires: apache-commons-digester
BuildRequires: apache-commons-ognl
BuildRequires: freemarker
BuildRequires: mvel
BuildRequires: portlet-2.0-api
BuildRequires: slf4j
BuildRequires: tomcat-lib
BuildRequires: tomcat-el-2.2-api
BuildRequires: tomcat-jsp-2.2-api
BuildRequires: tomcat-servlet-3.0-api

# test deps
# org.easymock easymockclassextension 2.4
# org.apache.shale shale-test 1.0.5
BuildRequires: easymock2
BuildRequires: junit4

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin

Requires:      apache-commons-digester
Requires:      apache-commons-ognl
Requires:      freemarker
Requires:      mvel
Requires:      portlet-2.0-api
Requires:      slf4j
Requires:      tomcat-lib
Requires:      tomcat-el-2.2-api
Requires:      tomcat-jsp-2.2-api
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Apache Tiles is a templating framework built to simplify the
development of web application user interfaces. Tiles allows
authors to define page fragments which can be assembled into
a complete page at runtime. These fragments, or tiles, can
be used as simple includes in order to reduce the duplication
of common page elements or embedded within other tiles to
develop a series of reusable templates. These templates
streamline the development of a consistent look and feel
across an entire application. Tiles grew in popularity as a
component of the popular Struts framework. It has since been
extracted from Struts and is now integrated with various
frameworks, such as Struts 2 and Shale.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0

%patch3 -p0
%patch4 -p0

# require org.springframework spring-webmvc-portlet 2.5.6
sed -i "s|<module>tiles-portlet-wildcard</module>|<!--module>tiles-portlet-wildcard</module-->|" src/pom.xml
# org.springframework spring-web 2.5.6
sed -i "s|<module>tiles-servlet-wildcard</module>|<!--module>tiles-servlet-wildcard</module-->|" src/pom.xml
# require org.apache.velocity velocity-tools 2.0
sed -i "s|<module>tiles-velocity</module>|<!--module>tiles-velocity</module-->|" src/pom.xml
# depends on previous artifacts
sed -i "s|<module>tiles-extras</module>|<!--module>tiles-extras</module-->|" src/pom.xml

sed -i "s|<module>assembly</module>|<!--module>assembly</module-->|" src/pom.xml

cp -p %{SOURCE1} pom.xml

%build

cd src
# test skip for unavailable deps:
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  -Dmaven.local.depmap.file="%{SOURCE2}" \
  install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-master.pom
%add_maven_depmap JPP.%{name}-master.pom

install -pm 644 src/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

# TODO
# extras
# portlet-wildcard
# servlet-wildcard
# velocity
mkdir -p %{buildroot}%{_javadir}/%{name}
for m in api \
 compat \
 core \
 el \
 freemarker \
 jsp \
 mvel \
 ognl \
 portlet \
 servlet \
 template; do
  install -pm 644 src/%{name}-${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
  install -pm 644 src/%{name}-${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
  %add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr src/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt1_3jpp7
- new version

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt2_1jpp6
- fixed build

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt1_1jpp6
- new jpp relase

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt4_1jpp5
- fixed build

* Wed Sep 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt3_1jpp5
- fixed build with new maven 2.0.8

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt2_1jpp5
- fixes for java6 support

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_1jpp5
- new version

