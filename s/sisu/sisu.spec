Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           sisu
Version:        2.2.3
Release:        alt2_6jpp7
Summary:        Sonatype dependency injection framework


Group:          Development/Java
License:        ASL 2.0 and EPL and MIT
URL:            http://github.com/sonatype/sisu

# git clone git://github.com/sonatype/sisu
# git archive --prefix="sisu-2.2.3/" --format=tar sisu-2.1.1 | xz > sisu-2.2.3.tar.xz
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-depmap.xml

BuildArch:      noarch

BuildRequires:  google-guice
BuildRequires:  maven
BuildRequires:  maven-install-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  atinject
BuildRequires:  felix-framework
BuildRequires:  forge-parent
BuildRequires:  maven-surefire-provider-testng
BuildRequires:  maven-surefire-provider-junit4


Requires:       forge-parent
Requires:       google-guice
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q

for module in . sisu-inject/containers/guice-bean/guice-bean-containers; do
    %pom_xpath_remove "pom:dependency[pom:scope[text()='test']]" $module; done

# Fix plexus bundling
sed -i -e '/provide these APIs as a convenience/,+2d' \
    sisu-inject/containers/guice-bean/sisu-inject-bean/pom.xml
%pom_xpath_inject "pom:project/pom:dependencies" "
    <dependency>
      <groupId>javax.inject</groupId>
      <artifactId>javax.inject</artifactId>
      <version>latest</version>
    </dependency>" sisu-inject/containers/guice-plexus/sisu-inject-plexus

# add backward compatible location
cp sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/sonatype/guice/plexus/lifecycles/*java \
   sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/codehaus/plexus/
sed -i 's/org.sonatype.guice.plexus.lifecycles/org.codehaus.plexus/' \
       sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/codehaus/plexus/*java

# TODO enable guice-eclipse
sed -i 's:.*guice-eclipse.*::g' sisu-inject/pom.xml
rm -rf sisu-inject/guice-eclipse
sed -i 's:.*sisu-eclipse-registry.*::g' sisu-inject/registries/pom.xml
rm -rf sisu-inject/registries/sisu-eclipse-registry

%build
mvn-rpmbuild -X \
  -Dmaven.local.depmap.file=%{SOURCE1} \
  -Dmaven.test.skip=true \
  install javadoc:aggregate

%install
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}

pushd sisu-inject
# main pom
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-inject.pom
%add_maven_depmap JPP.%{name}-inject.pom


pushd containers
# main poms
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-containers.pom
%add_maven_depmap JPP.%{name}-containers.pom

for submod in guice-*;do
    pushd $submod
    for module in guice-*;do
        install -pm 644 $module/target/$module-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$module.jar
        install -pm 644 $module/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-$module.pom
        %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar
    done
    # $dir is sisu-inject/XX so we strip the first part
    install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-$submod.pom
    %add_maven_depmap JPP.%{name}-$submod.pom
    popd
done

pushd guice-bean
module="sisu-inject-bean"
install -pm 644 $module/target/$module-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$module.jar
install -pm 644 $module/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-$module.pom
%add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar
popd # guice-bean

pushd guice-plexus
module="sisu-inject-plexus"
install -pm 644 $module/target/$module-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$module.jar
install -pm 644 $module/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-$module.pom
%add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar
popd # guice-plexus

popd # containers

pushd registries
# main poms
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-registries.pom
%add_maven_depmap JPP.%{name}-containers.pom

for module in *registry*;do
    install -pm 644 $module/target/$module-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$module.jar
    install -pm 644 $module/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-$module.pom
    %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar
done
popd # registries

popd # sisu-inject


install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE-ASL.txt LICENSE-EPL.txt
%{_javadir}/%{name}
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%doc LICENSE-ASL.txt LICENSE-EPL.txt
%doc %{_javadocdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt1_6jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

