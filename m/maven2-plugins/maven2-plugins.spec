# hack until 2.0.7 will be built
# Requires: jakarta-commons-cli10
# Requires(post): jakarta-commons-cli10
# another hack to be resolved
# Requires: excalibur-avalon-framework
# 2.0.4; gone in 2.0.7
#Requires: maven2-plugin-antlr
#Requires: maven2-plugin-jxr
Requires: maven2-plugin-release
#Requires: maven2-plugin-surefire
#Requires: maven2-plugin-surefire-report
Requires: maven2
Requires: maven2-plugin-ant
Requires: maven2-plugin-antrun
Requires: maven2-plugin-assembly
#Requires: maven2-plugin-checkstyle
Requires: maven2-plugin-clean
Requires: maven2-plugin-compiler
Requires: maven2-plugin-dependency
Requires: maven2-plugin-deploy
Requires: maven2-plugin-ear
Requires: maven2-plugin-eclipse
Requires: maven2-plugin-ejb
Requires: maven2-plugin-help
Requires: maven2-plugin-idea
Requires: maven2-plugin-install
Requires: maven2-plugin-jar
Requires: maven2-plugin-javadoc
Requires: maven2-plugin-one
# gone in 2.0.8-28
#Requires: maven2-plugin-plugin
Requires: maven2-plugin-pmd
Requires: maven2-plugin-project-info-reports
Requires: maven2-plugin-rar
Requires: maven2-plugin-repository
Requires: maven2-plugin-resources
Requires: maven2-plugin-site
Requires: maven2-plugin-source
Requires: maven2-plugin-verifier
Requires: maven2-plugin-war

Requires: saxon-scripts
Requires: maven-scm

Name:           maven2-plugins
Version:        2.0.7
Release:        alt6
Summary:        convenience package for all maven2 plugins

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://maven.apache.org/

BuildArch:      noarch

%description
convenience package for all maven2 plugins

%prep

%build

%install

install -dm 755 $RPM_BUILD_ROOT%{_bindir}

#%post
#[ -e /usr/share/java/commons-cli.jar ] && [ -e /usr/share/java/commons-cli10.jar ] && ln -sf commons-cli10.jar /usr/share/java/commons-cli.jar
#:

%files

%changelog
* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt6
- removed maven2-plugin-plugin

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt5
- added maven-release to requires

* Sat Jan 31 2009 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt4
- to be used together with maven2 2.0.7

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt3
- provides maven-release

* Tue Sep 23 2008 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2
- requires jakarta-commons-cli10

* Sat Sep 13 2008 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1
- maven 2.0.7 support 

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt2
- added maven-scm

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1
- first build
