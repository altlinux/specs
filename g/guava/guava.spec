# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          guava
Version:       13.0
Release:       alt1_3jpp7
Summary:       Google Core Libraries for Java

Group:         Development/Java
License:       ASL 2.0 
URL:           http://code.google.com/p/guava-libraries
# git clone https://code.google.com/p/guava-libraries/
# (cd ./guava-libraries && git archive --format=tar --prefix=guava-%{version}/ v%{version}) | xz >guava-%{version}.tar.xz
Source0:       %{name}-%{version}.tar.xz

BuildRequires: jpackage-utils
BuildRequires: sonatype-oss-parent

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin

BuildRequires: jsr-305 >= 0-0.6.20090319svn
BuildRequires: ant-nodeps

Requires:      jsr-305

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Guava is a suite of core and expanded libraries that include 
utility classes, Google's collections, io classes, and much 
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
find . -name '*.jar' -delete

%pom_disable_module guava-gwt
%pom_disable_module guava-testlib
%pom_disable_module guava-tests
%pom_remove_plugin :animal-sniffer-maven-plugin guava

%build

mvn-rpmbuild install javadoc:aggregate

%install

# jars
mkdir -p %{buildroot}%{_javadir}
install -pm 644 %{name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-parent.pom
install -pm 644 %{name}/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "com.google.collections:google-collections"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%files
%doc AUTHORS CONTRIBUTORS COPYING README*
%{_javadir}/%{name}*.jar
%{_mavenpomdir}/JPP-%{name}*.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_3jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_1jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

