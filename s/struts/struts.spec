Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global master_version 4
Name:          struts
Version:       1.3.10
Release:       alt4_5jpp7
Summary:       Web application framework
Group:         Development/Java
License:       ASL 2.0
URL:           http://struts.apache.org/
# wget http://www.apache.org/dist/struts/source/struts-1.3.10-src.zip
# remove non free resources
# unzip -qq struts-1.3.10-src.zip
# rm -r struts-1.3.10/src/core/src/main/resources/org/apache/struts/resources/web-app_2_3.dtd
# tar czf struts-1.3.10-clean-src.tar.gz struts-1.3.10
Source0:       %{name}-%{version}-clean-src.tar.gz
# wget -O struts-master-4-pom.xml http://svn.apache.org/repos/asf/struts/maven/tags/STRUTS_MASTER_4/pom.xml
Source1:       %{name}-master-%{master_version}-pom.xml
# add struts-master relativePath
Patch0:        %{name}-%{version}-parent-pom.patch
# add 
#  org.jboss.spec.javax.el jboss-el-api_2.2_spec
#  org.apache.maven.plugins maven-resources-plugin configuration
# change 
#  myfaces myfaces-jsf-api 1.0.9 with org.jboss.spec.javax.faces jboss-jsf-api_2.1_spec
#  jakarta-taglibs-standard with jboss-jstl-1.2-api
#  javax.servlet servlet-api with org.jboss.spec.javax.servlet jboss-servlet-api_3.0_spec
#  javax.servlet jsp-api with org.jboss.spec.javax.servlet.jsp jboss-jsp-api_2.2_spec
# fix
#  bsf gId
#  maven-compiler-plugin build source/target
#  build for junit servlet-3.0-api
Patch1:        %{name}-%{version}-jboss.patch

BuildRequires: jpackage-utils

BuildRequires: antlr
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-chain
BuildRequires: apache-commons-digester
BuildRequires: apache-commons-fileupload
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-validator
BuildRequires: bsf
BuildRequires: jakarta-oro
BuildRequires: jboss-el-2.2-api
BuildRequires: jboss-jsf-2.1-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: jboss-jstl-1.2-api
BuildRequires: jboss-servlet-3.0-api
# not only a test dep
BuildRequires: junit

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      antlr
Requires:      apache-commons-beanutils
Requires:      apache-commons-chain
Requires:      apache-commons-digester
Requires:      apache-commons-fileupload
Requires:      apache-commons-logging
Requires:      apache-commons-validator
Requires:      bsf
Requires:      jakarta-oro
Requires:      jboss-el-2.2-api
Requires:      jboss-jsf-2.1-api
Requires:      jboss-jsp-2.2-api
Requires:      jboss-jstl-1.2-api
Requires:      jboss-servlet-3.0-api
Requires:      junit

Requires:      jpackage-utils
BuildArch:     noarch
Obsoletes:     %{name}-manual < %{version}
Obsoletes:     %{name}-webapps-tomcat5 < %{version}
Source44: import.info

# Provides: struts-core = 0:1.3.8
# Provides: struts-el = 0:1.3.8
# Provides: struts-extras = 0:1.3.8
# Provides: struts-faces = 0:1.3.8
# Provides: struts-mailreader-dao = 0:1.3.8
# Provides: struts-scripting = 0:1.3.8
# Provides: struts-taglib = 0:1.3.8
# Provides: struts-tiles = 0:1.3.8
# Obsoletes: struts-core < 0:1.3.10-alt3_3
# Obsoletes: struts-el < 0:1.3.10-alt3_3
# Obsoletes: struts-extras < 0:1.3.10-alt3_3
# Obsoletes: struts-faces < 0:1.3.10-alt3_3
# Obsoletes: struts-mailreader-dao < 0:1.3.10-alt3_3
# Obsoletes: struts-scripting < 0:1.3.10-alt3_3
# Obsoletes: struts-taglib < 0:1.3.10-alt3_3
# Obsoletes: struts-tiles < 0:1.3.10-alt3_3

%package core
Summary:        Core for %{name}
Group:          Development/Java
#Requires: antlr
#Requires: apache-commons-beanutils
#Requires: apache-commons-chain
#Requires: apache-commons-digester
#Requires: apache-commons-logging
#Requires: apache-commons-validator
#Requires: jakarta-oro
Requires: %{name} = %{epoch}:%{version}-%{release}
#Requires: commons-parent

%description core
%{summary}.

%package el
Summary:        EL extension for %{name}
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
Requires: %{name}-tiles = %{epoch}:%{version}-%{release}
#Requires: jakarta-taglibs-standard

%description el
%{summary}.

%package extras
Summary:        Extras for %{name}
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}

%description extras
%{summary}.

%package faces
Summary:        Integration library for %{name}-faces
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
Requires: %{name}-tiles = %{epoch}:%{version}-%{release}

%description faces
%{summary}.

%package mailreader-dao
Summary:        %{name} mailreader-dao library
Group:          Development/Java
#Requires: apache-commons-digester
#Requires: apache-commons-logging

%description mailreader-dao
%{summary}.

%package scripting
Summary:        %{name} scripting library
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
#Requires: bsf

%description scripting
%{summary}.

%package taglib
Summary:        %{name} taglib library
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}

%description taglib
%{summary}.

%package tiles
Summary:        %{name} tiles library
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}

%description tiles
%{summary}.

%files core
%{_javadir}/%{name}-core.jar
%{_javadir}/%{name}.jar

%files el
%{_javadir}/%{name}-el.jar

%files extras
%{_javadir}/%{name}-extras.jar

%files faces
%{_javadir}/%{name}-faces.jar

%files mailreader-dao
%{_javadir}/%{name}-mailreader-dao.jar

%files scripting
%{_javadir}/%{name}-scripting.jar

%files taglib
%{_javadir}/%{name}-taglib.jar

%files tiles
%{_javadir}/%{name}-tiles.jar


%description
Welcome to the Struts Framework! The goal of this project is to provide
an open source framework useful in building web applications with Java
Servlet and JavaServer Pages (JSP) technology. Struts encourages
application architectures based on the Model-View-Controller (MVC)
design paradigm, colloquially known as Model 2 in discussions on various
servlet and JSP related mailing lists.
Struts includes the following primary areas of functionality:
A controller servlet that dispatches requests to appropriate Action
classes provided by the application developer.
JSP custom tag libraries, and associated support in the controller
servlet, that assists developers in creating interactive form-based
applications.
Utility classes to support XML parsing, automatic population of
JavaBeans properties based on the Java reflection APIs, and
internationalization of prompts and messages.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find -name "*.jar" -delete
find -name "*.class" -delete
%patch0 -p0
%patch1 -p1

sed -i 's/\r//' LICENSE.txt NOTICE.txt

# fix non ASCII chars
for s in src/tiles/src/main/java/org/apache/struts/tiles/ComponentDefinition.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

cp -p %{SOURCE1} pom.xml

%build

cd src
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
  -Dproject.build.sourceEncoding=UTF-8 \
  install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-master.pom
%add_maven_depmap JPP.%{name}-master.pom

install -pm 644 src/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

mkdir -p %{buildroot}%{_javadir}/%{name}
for m in core \
 el \
 extras \
 faces \
 mailreader-dao \
 scripting \
 taglib \
 tiles; do
  install -pm 644 src/${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
  install -pm 644 src/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
  %add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr src/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
rm -rf $RPM_BUILD_ROOT/var/lib/tomcat?/webapps/struts-documentation/download.cgi

for m in core \
 el \
 extras \
 faces \
 mailreader-dao \
 scripting \
 taglib \
 tiles; do
  ln -s %{name}/${m}.jar %{buildroot}%{_javadir}/%{name}-${m}.jar
done

# struts-all compat jar
mkdir tmp-all
pushd tmp-all
for i in %{buildroot}%{_javadir}/%{name}/*.jar; do
jar xf $i;
done
jar cf %{buildroot}%{_javadir}/%{name}.jar *
popd

# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/el/src/main/resources/META-INF/tld/*.tld %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/faces/src/main/resources/META-INF/tld/*.tld %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/taglib/src/main/resources/META-INF/tld/*.tld %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/tiles/src/main/resources/META-INF/tld/*.tld %{buildroot}%{_datadir}/%{name}
#install -p -m 0644 src/target/site/dtds/*.dtd %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/core/src/main/resources/org/apache/struts/validator/vali*.xml %{buildroot}%{_datadir}/%{name}

%files
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt NOTICE.txt
%{_datadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt4_5jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt3_5jpp7
- fc version

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt3_2jpp6
- fixed build using htmlunit1

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt2_2jpp6
- fixed build with java 7

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt1_2jpp6
- new version

* Fri Mar 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.8-alt2_2jpp5
- build with checkstyle4

* Sun Mar 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3.8-alt1_2jpp5
- fixed repocop warnings

* Fri Mar 14 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt4_5jpp1.7
- disabled struts-tomcat4

* Wed Sep 12 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt3_5jpp1.7
- rebuild to remove duplicate struts

* Sat Aug 11 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt2_5jpp1.7
- converted from JPackage by jppimport script

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt1_5jpp1.7
- new version

* Thu Apr 19 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.2.6-alt4
- Built with explicit java-1.5.0

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt3
- Fix build with j2se-1.5

* Wed Apr 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt2
- packaged webapps for tomcats

* Tue Apr 05 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Apr 05 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1
- Initial build for ALT Linux Sisyphus

