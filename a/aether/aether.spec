# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           aether
Version:        1.13.1
Release:        alt5_4jpp7
Summary:        Sonatype library to resolve, install and deploy artifacts the Maven way

Group:          Development/Java
License:        EPL or ASL 2.0
URL:            https://docs.sonatype.org/display/AETHER/Home
# git clone https://github.com/sonatype/sonatype-aether.git
# git archive --prefix="aether-1.11/" --format=tar aether-1.11 | bzip2 > aether-1.11.tar.bz2
Source0:        %{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  plexus-containers-component-metadata >= 1.5.4-4
BuildRequires:  animal-sniffer >= 1.6-5
BuildRequires:  mojo-parent
BuildRequires:  async-http-client >= 1.6.1
BuildRequires:  sonatype-oss-parent

# required by netty really, but we push this dep on level higer
BuildRequires:  jboss-parent
Requires:       jboss-parent

Requires:       async-http-client >= 1.6.1
Source44: import.info


%description
Aether is standalone library to resolve, install and deploy artifacts
the Maven way developed by Sonatype

%package javadoc
Summary:   API documentation for %{name}
Group:     Development/Java
Requires:  jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
# last part will have to change every time
%setup -q

# we'd need org.sonatype.http-testing-harness so let's remove async
# and wagon http tests (leave others enabled)
for module in asynchttpclient wagon; do (
    cd ./aether-connector-$module
    rm -rf src/test
    # Removes all dependencies with test scope
    %pom_xpath_remove "pom:dependency[pom:scope[text()='test']]"
) done

# Remove clirr plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :clirr-maven-plugin aether-api
%pom_remove_plugin :clirr-maven-plugin aether-spi

%build
mvn-rpmbuild -Dmaven.test.skip=true  install javadoc:aggregate


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

for module in aether-api aether-connector-file aether-connector-wagon aether-connector-asynchttpclient\
         aether-impl aether-spi aether-test-util aether-util;do
pushd $module
      jarname=`echo $module | sed s:aether-::`
      install -m 644 target/$module-*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$jarname.jar

      install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-$jarname.pom
      %add_maven_depmap JPP.%{name}-$jarname.pom %{name}/$jarname.jar
popd
done

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

ln -s api.jar $RPM_BUILD_ROOT%{_javadir}/aether/aether-api.jar

%files
%doc README.md
%{_javadir}/%{name}
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*.pom

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt5_4jpp7
- added compat symlink

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt4_4jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

