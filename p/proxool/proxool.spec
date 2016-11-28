Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global git_commit 659fc71

Summary:       Java connection pool library
Name:          proxool
Version:       0.9.1
Release:       alt2_18jpp8
Epoch:         0
License:       ASL 2.0
URL:           http://proxool.sourceforge.net/
# Grabbing a newer version from git due to license change
# https://github.com/proxool/proxool/tarball/master
# (commit 659fc71e617151327779802a5171f0da8205918d)
Source0:       proxool-proxool-%{git_commit}.tar.gz
Source1:       proxool.pom
Patch0:        proxool-no-embedded-cglib.patch

BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: java-devel >= 1.6.0
BuildRequires: javapackages-local
BuildRequires: mvn(avalon-framework:avalon-framework-api)
BuildRequires: mvn(avalon-framework:avalon-framework-impl)
BuildRequires: mvn(avalon-logkit:avalon-logkit)
BuildRequires: mvn(com.puppycrawl.tools:checkstyle)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(hsqldb:hsqldb:1)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.sf.cglib:cglib)

BuildArch: noarch
Source44: import.info

%description
Transparently adds connection pooling to your existing JDBC driver.
Complies with the J2SE API, giving you the confidence to develop to
standards. You can monitor the performance of your database
connections and listen to connection events.
It's easy to configure using the JDBC API, XML, or Java property
files - you decide.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{git_commit}
#find . -name "*.jar" -exec rm {} \;
find . -type f -a -executable -exec chmod -x {} \;
rm -rf lib jarjar

%patch0 -p1 -b .sav0

sed -i.new_checkstyle "s|com.puppycrawl.tools.checkstyle.CheckStyleTask|com.puppycrawl.tools.checkstyle.ant.CheckstyleAntTask|" build.xml

sed -i.doclint "s|public="true"|public="true" additionalparam="-Xdoclint:none"|" build.xml

%mvn_file %{name}:%{name} %{name}

%build
CLASSPATH=$(build-classpath cglib avalon-framework glassfish-servlet-api) ant build-jar javadoc

%install
%mvn_artifact %{SOURCE1} build/%{name}-%{version}.jar
%mvn_install -J build/api

%files -f .mfiles
%doc CHANGES.txt README.txt
%doc LICENCE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENCE.txt

%changelog
* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1-alt2_18jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1-alt2_16jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1-alt2_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1-alt2_8jpp7
- new fc release

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1-alt2_6jpp7
- target 5 build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1-alt1_6jpp7
- fc version

* Wed May 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.8.3-alt4_10jpp5
- repocop bugfixes

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.8.3-alt3_10jpp5
- fixed build with java 5

* Mon Mar 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.8.3-alt2_10jpp1.7
- fixed alternatives intersection

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.8.3-alt1_10jpp1.7
- converted from JPackage by jppimport script

