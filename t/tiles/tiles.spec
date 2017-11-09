Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global master_version 3
Name:          tiles
Version:       2.2.2
Release:       alt3_17jpp8
Summary:       Java templating framework for web application user interfaces
License:       ASL 2.0
Url:           http://tiles.apache.org/
Source0:       http://www.apache.org/dist/%{name}/v%{version}/%{name}-%{version}-src.tar.gz

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
# build fix fot tomcat 8.x apis
Patch3:        %{name}-%{version}-servlet3.1.patch

BuildRequires: mvn(commons-digester:commons-digester)
BuildRequires: mvn(javax.portlet:portlet-api)
BuildRequires: mvn(org.apache.commons:commons-ognl)
BuildRequires: mvn(org.apache.tomcat:tomcat-el-api)
BuildRequires: mvn(org.apache.tomcat:tomcat-jasper-el)
BuildRequires: mvn(org.apache.tomcat:tomcat-jsp-api)
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: mvn(org.apache.velocity:velocity-tools)
BuildRequires: mvn(org.freemarker:freemarker)
BuildRequires: mvn(org.mvel:mvel2)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)
BuildRequires: slf4j
BuildRequires: tomcat-lib

# test deps
%if 0
BuildRequires: mvn(org.easymock:easymockclassextension) >= 2.4
BuildRequires: mvn(org.apache.shale:shale-test) >= 1.0.5
%endif
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin

# requires by remote-resources-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

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
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1


# require org.springframework spring-webmvc-portlet 2.5.6
%pom_disable_module tiles-portlet-wildcard src/pom.xml
# org.springframework spring-web 2.5.6
%pom_disable_module tiles-servlet-wildcard src/pom.xml
# depends on previous artifacts
%pom_disable_module tiles-extras src/pom.xml
%pom_disable_module assembly src/pom.xml

sed -i "s|<artifactId>jasper-el|<artifactId>tomcat-jasper-el|" src/tiles-el/pom.xml

sed -i "s|<groupId>javax.servlet</groupId>|<groupId>org.apache.tomcat</groupId>|" src/tiles-core/pom.xml \
 src/tiles-api/pom.xml \
 src/tiles-velocity/pom.xml \
 src/tiles-servlet/pom.xml \
 src/tiles-compat/pom.xml \
 src/tiles-portlet/pom.xml \
 src/tiles-jsp/pom.xml \
 src/tiles-extras/pom.xml \
 src/tiles-freemarker/pom.xml \
 src/tiles-el/pom.xml \
 src/tiles-servlet-wildcard/pom.xml

sed -i "s|<artifactId>servlet-api</artifactId>|<artifactId>tomcat-servlet-api</artifactId>|" src/tiles-core/pom.xml \
 src/tiles-api/pom.xml \
 src/tiles-velocity/pom.xml \
 src/tiles-servlet/pom.xml \
 src/tiles-compat/pom.xml \
 src/tiles-portlet/pom.xml \
 src/tiles-jsp/pom.xml \
 src/tiles-extras/pom.xml \
 src/tiles-freemarker/pom.xml \
 src/tiles-el/pom.xml \
 src/tiles-servlet-wildcard/pom.xml


%pom_remove_parent src
#cp -p %%{SOURCE1} pom.xml

%build

cd src
# TODO
# extras
# portlet-wildcard
# servlet-wildcard
%mvn_file :%{name}-api %{name}/api
%mvn_file :%{name}-compat %{name}/compat
%mvn_file :%{name}-core %{name}/core
%mvn_file :%{name}-el %{name}/el
%mvn_file :%{name}-freemarker %{name}/freemarker
%mvn_file :%{name}-jsp %{name}/jsp
%mvn_file :%{name}-mvel %{name}/mvel
%mvn_file :%{name}-ognl %{name}/ognl
%mvn_file :%{name}-portlet %{name}/portlet
%mvn_file :%{name}-servlet %{name}/servlet
%mvn_file :%{name}-template %{name}/template
%mvn_file :%{name}-velocity %{name}/velocity

# test skip for unavailable deps
%mvn_build -f

%install

(
cd src
%mvn_install
)

%files -f src/.mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files javadoc -f src/.mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt3_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt3_16jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt3_15jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt3_14jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt3_9jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt3_6jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt2_6jpp7
- new release

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

