Group: Development/Java
BuildRequires(pre): rpm-macros-java
Name:          c3p0
Epoch:         0
Version:       0.15.1
Release:       alt1
Summary:       JDBC DataSources and Resource Pools
License:       LGPL-2.1-or-later or EPL-1.0
URL:           https://www.mchange.com/projects/c3p0
VCS:           https://github.com/swaldman/c3p0.git
Source0:       %name-%version.tar

BuildRequires: maven-local
BuildRequires: ant ant-junit
BuildRequires: java-17-openjdk-devel
BuildRequires: python3
BuildRequires: mvn(com.mchange:mchange-commons-java)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.typesafe:config)

BuildArch:     noarch

%description
c3p0 augments JDBC drivers with JNDI-bindable DataSources, including
DataSources that implement Connection and Statement Pooling.

%package javadoc
Group: Development/Java
Summary:       API documentation for %name

%description javadoc
This package contains API documentation for %name.

%package manual
Group: Documentation
Summary:       User manual for %name
Requires:      %name-javadoc = %version-%release

%description manual
This package contains the complete upstream HTML manual for %name.

%prep
%setup -q

%mvn_file : %name

%build
# Upstream intentionally uses source7/target7 with newer JDBC APIs.
export JAVA_HOME=%_jvmdir/java-17-openjdk
export PATH=$JAVA_HOME/bin:$PATH
ant -f build.xml -Dversion=%version
%mvn_artifact pom.xml target/%name-%version.jar

%install
%mvn_install
install -dm755 %buildroot%_javadocdir/%name
cp -pr target/apidocs/. %buildroot%_javadocdir/%name/
install -dm755 %buildroot%_docdir/%name-manual-%version/manual
cp -pr target/manual/. %buildroot%_docdir/%name-manual-%version/manual/
ln -s %_javadocdir/%name %buildroot%_docdir/%name-manual-%version/manual/apidocs

%files -f .mfiles
%doc LICENSE LICENSE-LGPL LICENSE-EPL CHANGELOG README.md RELEASE_NOTES-c3p0-0.15.0

%files javadoc
%_javadocdir/%name

%files manual
%_docdir/%name-manual-%version

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 0:0.15.1-alt1
- New version.

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.4-alt1_2jpp8
- new version

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.8.pre8jpp8
- fc update & java 8 build

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.7.pre8jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.6.pre8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.5.pre8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.4.pre8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.3.pre8jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.2.pre8jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2.1-alt1_4jpp7
- new release

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2.1-alt1_2jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt2_0.9.pre1jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt2_0.7.pre1jpp7
- fc version

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt1_0.pre1.1jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt3_2jpp5
- selected java5 compiler explicitly

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt2_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Mon Mar 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt2_2jpp1.7
- fixed alternatives intersection

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

