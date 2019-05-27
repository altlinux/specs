Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           avalon-logkit
Epoch:          0
Version:        2.1
Release:        alt2_32jpp8
Summary:        Java logging toolkit
License:        ASL 2.0
URL:            http://avalon.apache.org/
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/excalibur/%{name}/source/%{name}-%{version}-src.zip

Patch0001:      0001-Port-build-script-to-Maven-3.patch
Patch0002:      0002-Port-to-Java-7.patch
Patch0003:      0003-Fix-encoding.patch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)

Provides:       deprecated()
Source44: import.info

%description
LogKit is a logging toolkit designed for secure performance orientated
logging in applications. To get started using LogKit, it is recomended
that you read the whitepaper and browse the API docs.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Provides:       deprecated()
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
mv project.xml pom.xml

# LogFactor5 is no longer distributed with log4j
%pom_remove_dep log4j:log4j
rm -rf src/java/org/apache/log/output/lf5

%mvn_file : %{name}
%mvn_alias : logkit:logkit

# Add proper Apache Felix Bundle Plugin instructions
# so that we get a reasonable OSGi manifest.
%pom_xpath_inject pom:project "<packaging>bundle</packaging>"
%pom_xpath_inject pom:build "
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-SymbolicName>avalon-logkit-2.1</Bundle-SymbolicName>
          <_nouses>true</_nouses>
        </instructions>
      </configuration>
    </plugin>
  </plugins>"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_32jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_29jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_28jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_27jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_24jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_22jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_12jpp7
- new release

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_11jpp7
- added avalon:avalon-logkit depmap

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_11jpp7
- new release

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp5
- selected java5 compiler explicitly

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp5
- restored in separate package due to repolib

