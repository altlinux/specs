Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cobertura
Version:        1.9.4.1
Release:        alt2_9jpp7
Summary:        Java tool that calculates the percentage of code accessed by tests

# ASL 2.0: src/net/sourceforge/cobertura/webapp/web.xml
# GPL+: src/net/sourceforge/cobertura/reporting/html/files/sortabletable.js
#       src/net/sourceforge/cobertura/reporting/html/files/stringbuilder.js
# MPL 1.1, GPLv2+, LGPLv2+: some files in src/net/sourceforge/cobertura/javancss/ccl/
# rest is mix of GPLv2+ and ASL 1.1
License:        ASL 1.1 and GPLv2+ and MPL and ASL 2.0 and GPL+
URL:            http://cobertura.sourceforge.net/

# ./create-tarball.sh %%{version}
Source0:        %{name}-%{version}-clean.tar.gz
# POMs based from those available from the Maven repository
Source1:        http://repo1.maven.org/maven2/net/sourceforge/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source2:        http://repo1.maven.org/maven2/net/sourceforge/%{name}/%{name}-runtime/%{version}/%{name}-runtime-%{version}.pom
Source3:        http://www.apache.org/licenses/LICENSE-1.1.txt
Source4:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source5:        create-tarball.sh

Patch0:         %{name}-unmappable-characters.patch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  antlr
BuildRequires:  apache-commons-cli
BuildRequires:  groovy
BuildRequires:  jakarta-oro
BuildRequires:  jaxen
BuildRequires:  jdom
BuildRequires:  junit4
BuildRequires:  log4j
BuildRequires:  objectweb-asm
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis

Requires:       ant
Requires:       jakarta-oro
Requires:       junit4
Requires:       log4j
Requires:       objectweb-asm

BuildArch:      noarch
Source44: import.info

%description
Cobertura is a free Java tool that calculates the percentage of code
accessed by tests. It can be used to identify which parts of your
Java program are lacking test coverage.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

cp %{SOURCE3} LICENSE-ASL-1.1
cp %{SOURCE4} LICENSE-ASL-2.0

sed -i 's/\r//' ChangeLog COPYING COPYRIGHT README

%build
export LANG=en_US.ISO8859-1
pushd lib
  ln -s $(build-classpath jaxen) .
  ln -s $(build-classpath jdom) .
  ln -s $(build-classpath junit4) .
  ln -s $(build-classpath log4j) .
  ln -s $(build-classpath objectweb-asm/asm-all) .
  ln -s $(build-classpath oro) .
  ln -s $(build-classpath xalan-j2) .
  ln -s $(build-classpath tomcat-servlet-3.0-api) servlet-api.jar
  ln -s $(build-classpath apache-commons-cli) commons-cli.jar
  pushd xerces
    ln -s $(build-classpath xalan-j2) .
    ln -s $(build-classpath xml-commons-jaxp-1.3-apis) .
  popd
popd

pushd antLibrary/common
  ln -s $(build-classpath groovy) .
popd

export CLASSPATH=$(build-classpath objectweb-asm/asm-all commons-cli antlr junit4)
%ant -Djetty.dir=. -Dlib.dir=. compile test jar javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar
(cd %{buildroot}%{_javadir} && ln -s %{name}.jar %{name}-runtime.jar)

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -p -m 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{name}-runtime.pom

# depmap
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{name}:%{name}"
%add_maven_depmap JPP-%{name}-runtime.pom %{name}-runtime.jar -a "%{name}:%{name}-runtime"

# ant config
install -d -m 755  %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
ant cobertura junit4 log4j oro xerces-j2
EOF

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/cobertura-check.conf`
touch $RPM_BUILD_ROOT/etc/cobertura-check.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/cobertura-instrument.conf`
touch $RPM_BUILD_ROOT/etc/cobertura-instrument.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/cobertura-merge.conf`
touch $RPM_BUILD_ROOT/etc/cobertura-merge.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/cobertura-report.conf`
touch $RPM_BUILD_ROOT/etc/cobertura-report.conf

%files
%doc ChangeLog COPYING COPYRIGHT README LICENSE-ASL-1.1 LICENSE-ASL-2.0
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-runtime.jar
%config %{_sysconfdir}/ant.d/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-runtime.pom
%{_mavendepmapfragdir}/*
%config(noreplace,missingok) /etc/cobertura-check.conf
%config(noreplace,missingok) /etc/cobertura-instrument.conf
%config(noreplace,missingok) /etc/cobertura-merge.conf
%config(noreplace,missingok) /etc/cobertura-report.conf

%files javadoc
%doc COPYING COPYRIGHT LICENSE-ASL-1.1 LICENSE-ASL-2.0
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4.1-alt2_9jpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4.1-alt2_3jpp7
- fc update

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4.1-alt2_2jpp7
- fixed build of maven-plugin -- set asm version to 3.3.1 in pom

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4.1-alt1_2jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt3_6jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt3_3jpp7
- applied repocop patches

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt2_3jpp7
- dropped obsoletes on mojo-maven2-plugin-cobertura

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_3jpp7
- new version

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_2jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_11jpp5
- new jpp release

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_10jpp5
- new version

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_2jpp1.7
- converted from JPackage by jppimport script

