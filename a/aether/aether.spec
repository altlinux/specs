Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           aether
Version:        1.13.1
Release:        alt6_7jpp7
Summary:        Sonatype library to resolve, install and deploy artifacts the Maven way

License:        EPL or ASL 2.0
URL:            https://docs.sonatype.org/display/AETHER/Home
# git clone https://github.com/sonatype/sonatype-aether.git
# git archive --prefix="aether-1.11/" --format=tar aether-1.11 | bzip2 > aether-1.11.tar.bz2
Source0:        %{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  plexus-containers-component-metadata >= 1.5.4-4
BuildRequires:  forge-parent
BuildRequires:  async-http-client >= 1.6.1
Source44: import.info


%description
Aether is standalone library to resolve, install and deploy artifacts
the Maven way developed by Sonatype

%package javadoc
Group: Development/Java
Summary:   API documentation for %{name}
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

for module in . aether-connector-wagon aether-util aether-api   \
              aether-impl aether-connector-asynchttpclient      \
              aether-connector-file aether-demo aether-test-util; do
    %pom_remove_plugin :animal-sniffer-maven-plugin $module
done

# Tests would fail without cglib dependency
%pom_xpath_inject pom:project "<dependencies/>"
%pom_add_dep cglib:cglib:2.2:test

%build
%mvn_file ":%{name}-{*}" %{name}/@1
%mvn_build

%install
%mvn_install
for i in api connector-wagon impl spi util; do
ln -s $i.jar $RPM_BUILD_ROOT%{_javadir}/aether/aether-$i.jar
done


%files -f .mfiles
%doc README.md
%dir %{_javadir}/%{name}
%{_javadir}/aether/aether-*.jar

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt6_7jpp7
- xmvn build

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt6_4jpp7
- more compat symlinks added

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

