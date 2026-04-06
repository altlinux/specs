Name:           velocity
Epoch:          1
Version:        2.4.1
Release:        alt1

Summary:        Apache Velocity Engine
License:        Apache-2.0
Group:          Development/Java
URL:            http://velocity.apache.org/
VCS:            https://github.com/apache/velocity-engine

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(dom4j:dom4j)

BuildRequires:  mvn(org.hsqldb:hsqldb)

BuildArch:      noarch

%description
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%javadoc_package

%prep
%setup

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.velocity</groupId>"

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :templating-maven-plugin velocity-engine-core
%pom_remove_plugin :maven-clean-plugin velocity-custom-parser-example

sed -i '/<classifier>${test.jdbc.driver.classifier}<\/classifier>/d' velocity-engine-core/pom.xml
rm velocity-engine-core/src/test/java/org/apache/velocity/test/issues/Velocity952TestCase.java

%pom_disable_module spring-velocity-support

cp velocity-engine-core/src/main/java-templates/org/apache/velocity/runtime/VelocityEngineVersion.java \
   velocity-engine-core/src/main/java/org/apache/velocity/runtime/VelocityEngineVersion.java

sed -i 's/$project.version/%version/' \
   velocity-engine-core/src/main/java/org/apache/velocity/runtime/VelocityEngineVersion.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md LICENSE NOTICE

%changelog
* Sun Apr 05 2026 Evgeniy Serov <scala@altlinux.org> 1:2.4.1-alt1
- Udated to 2.4.1.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1:1.7-alt3_36jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:1.7-alt3_34jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:1.7-alt3_32jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_27jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_25jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_22jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_21jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_20jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_19jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_18jpp8
- unbootstrap build

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_7jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_6jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_5jpp7
- new version

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt3_1jpp6
- fixed build

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt2_1jpp6
- added velocity:velocity jppmap

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_1jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt2_4jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_3jpp5
- converted from JPackage by jppimport script

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_2jpp1.7
- pom fixes

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_1jpp1.7
- updated to new jpackage release

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_6jpp1.7
- import from jpackage;set epoch 1; overrides unstable version

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.3
- rebuild with excalibur-avalon-logkit

* Fri Dec 02 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.2
- nightly build 20051125053934 

* Sat May 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.1
- 1.5-dev
- svn snapshot 20050507

* Fri May 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Initial build for ALT Linux Sisyphus

