Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           aopalliance
Epoch:          0
Version:        1.0
Release:        alt6_19jpp8
Summary:        Java/J2EE AOP standards
License:        Public Domain
URL:            http://aopalliance.sourceforge.net/
BuildArch:      noarch

# cvs -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance login
# password empty
# cvs -z3 -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance export -r HEAD aopalliance
Source0:        aopalliance-src.tar.gz
Source1:        http://repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
Source2:        %{name}-MANIFEST.MF

BuildRequires:  ant
BuildRequires:  javapackages-local
Source44: import.info

%description
Aspect-Oriented Programming (AOP) offers a better solution to many
problems than do existing technologies, such as EJB.  AOP Alliance
intends to facilitate and standardize the use of AOP to enhance
existing middleware environments (such as J2EE), or development
environements (e.g. Eclipse).  The AOP Alliance also aims to ensure
interoperability between Java/J2EE AOP implementations to build a
larger AOP community.

%{?javadoc_package}

%prep
%setup -q -n %{name}

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dbuild.sysclasspath=only jar javadoc

# Inject OSGi manifest required by Eclipse.
jar umf %{SOURCE2} build/%{name}.jar

%install
%mvn_file : %{name}
%mvn_artifact %{SOURCE1} build/%{name}.jar

%mvn_install -J build/javadoc

%files -f .mfiles

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_19jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_15jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_12jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_11jpp8
- added osgi provides

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_11jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_7jpp6
- new jpp relase

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp6
- new jpp release

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_6jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp5
- converted from JPackage by jppimport script

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

