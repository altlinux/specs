Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global master_version 3
Name:          tiles
Version:       2.2.2
Release:       alt3_9jpp7
Summary:       Java templating framework for web application user interfaces
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
BuildRequires: velocity-tools

# test deps
%if 0
BuildRequires: mvn(org.easymock:easymockclassextension) >= 2.4
BuildRequires: mvn(org.apache.shale:shale-test) >= 1.0.5
%endif
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin

# requires by remote-resources-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)

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

%patch3 -p0
%patch4 -p0

# require org.springframework spring-webmvc-portlet 2.5.6
%pom_disable_module tiles-portlet-wildcard src/pom.xml
# org.springframework spring-web 2.5.6
%pom_disable_module tiles-servlet-wildcard src/pom.xml
# depends on previous artifacts
%pom_disable_module tiles-extras src/pom.xml
%pom_disable_module assembly src/pom.xml

sed -i "s|<artifactId>jasper-el|<artifactId>tomcat-jasper-el|" src/tiles-el/pom.xml

cp -p %{SOURCE1} pom.xml

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
%mvn_build -f -- -Dmaven.local.depmap.file="%{SOURCE2}"

%install

(
cd src
%mvn_install
)

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-master.pom
%add_maven_depmap JPP.%{name}-master.pom

%files -f src/.mfiles
%dir %{_javadir}/%{name}
%{_mavenpomdir}/JPP.%{name}-master.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files javadoc -f src/.mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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

