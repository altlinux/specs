Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven2
Version:        2.2.1
Release:        alt6_54jpp8
Summary:        Java project management and project comprehension tool
License:        ASL 2.0 and MIT and BSD
URL:            http://maven.apache.org
BuildArch:      noarch

# export https://svn.apache.org/repos/asf/maven/maven-2/tags/maven-%{version}/ apache-maven-%{version}
# tar czvf %{name}-%{version}.tar.gz apache-maven-%{version}
Source0:        %{name}-%{version}.tar.gz

Patch2:         %{name}-%{version}-update-tests.patch
Patch4:         %{name}-%{version}-unshade.patch
Patch5:         %{name}-%{version}-default-resolver-pool-size.patch
Patch6:         %{name}-%{version}-strip-jackrabbit-dep.patch
Patch8:         %{name}-%{version}-migrate-to-plexus-containers-container-default.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Apache Maven is a software project management and comprehension tool.
Based on the concept of a project object model (POM), Maven can manage
a project's build, reporting and documentation from a central piece of
information.

%package -n maven-artifact
Group: Development/Java
Summary:        Compatibility Maven artifact artifact

%description -n maven-artifact
Maven artifact manager artifact

%package -n maven-artifact-manager
Group: Development/Java
Summary:        Compatibility Maven artifact manager artifact

%description -n maven-artifact-manager
Maven artifact manager artifact

%package -n maven-model
Group: Development/Java
Summary:        Compatibility Maven model artifact

%description -n maven-model
Maven model artifact

%package -n maven-monitor
Group: Development/Java
Summary:        Compatibility Maven monitor artifact

%description -n maven-monitor
Maven monitor artifact

%package -n maven-plugin-registry
Group: Development/Java
Summary:        Compatibility Maven plugin registry artifact

%description -n maven-plugin-registry
Maven plugin registry artifact

%package -n maven-profile
Group: Development/Java
Summary:        Compatibility Maven profile artifact

%description -n maven-profile
Maven profile artifact

%package -n maven-project
Group: Development/Java
Summary:        Compatibility Maven project artifact

%description -n maven-project
Maven project artifact

%package -n maven-settings
Group: Development/Java
Summary:        Compatibility Maven settings artifact

%description -n maven-settings
Maven settings artifact

%package -n maven-toolchain
Group: Development/Java
Summary:        Compatibility Maven toolchain artifact

%description -n maven-toolchain
Maven toolchain artifact

%package -n maven-plugin-descriptor
Group: Development/Java
Summary:        Maven Plugin Description Model

%description -n maven-plugin-descriptor
Maven plugin descriptor artifact

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n apache-maven-2.2.1

%patch2 -b .update-tests

%patch4 -b .unshade

# disable parallel artifact resolution
%patch5 -p1 -b .parallel-artifacts-resolution

# remove unneeded jackrabbit dependency
%patch6 -p1 -b .strip-jackrabbit-dep

%patch8 -p1 -b .plexus-container

for nobuild in apache-maven maven-artifact-test \
               maven-compat maven-core maven-plugin-api \
               maven-plugin-parameter-documenter maven-reporting \
               maven-repository-metadata maven-script \
               maven-error-diagnostics; do
    %pom_disable_module $nobuild
done

# Don't install parent POM
%mvn_package :maven __noinstall

# Install all artifacts in Maven 3 directory.
%mvn_file ":{*}" maven/@1

# these parts are compatibility versions which are available in
# maven-3.x as well. We default to maven-3, but if someone asks for
# 2.x we provide few compat versions
%mvn_compat_version ":maven-{artifact,model,settings}" \
                    2.0.2 2.0.6 2.0.7 2.0.8 2.2.1

# Don't depend on backport-util-concurrent
%pom_remove_dep :backport-util-concurrent
%pom_remove_dep :backport-util-concurrent maven-artifact-manager
sed -i s/edu.emory.mathcs.backport.// `find -name DefaultArtifactResolver.java`

# Tests are skipped, so remove dependencies with scope 'test'.
for pom in $(grep -l ">test<" $(find -name pom.xml | grep -v /test/)); do
    %pom_xpath_remove "pom:dependency[pom:scope[text()='test']]" $pom
done

%build
%mvn_build -f -s -- -P all-models

%install
%mvn_install

%files -n maven-artifact -f .mfiles-maven-artifact
%doc LICENSE.txt NOTICE.txt

%files -n maven-artifact-manager -f .mfiles-maven-artifact-manager
%doc LICENSE.txt NOTICE.txt

%files -n maven-model -f .mfiles-maven-model
%doc LICENSE.txt NOTICE.txt

%files -n maven-monitor -f .mfiles-maven-monitor
%doc LICENSE.txt NOTICE.txt

%files -n maven-plugin-registry -f .mfiles-maven-plugin-registry
%doc LICENSE.txt NOTICE.txt

%files -n maven-profile -f .mfiles-maven-profile
%doc LICENSE.txt NOTICE.txt

%files -n maven-project -f .mfiles-maven-project
%doc LICENSE.txt NOTICE.txt

%files -n maven-settings -f .mfiles-maven-settings
%doc LICENSE.txt NOTICE.txt

%files -n maven-toolchain -f .mfiles-maven-toolchain
%doc LICENSE.txt NOTICE.txt

%files -n maven-plugin-descriptor -f .mfiles-maven-plugin-descriptor
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt6_54jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt6_53jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt6_52jpp8
- java 8 mass update

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt3_32jpp7
- restored maven-model subpackage 

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt2_32jpp7
- fixed verbose post

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt1_32jpp7
- complete build

* Thu Apr 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt19_0jpp
- all plugins replaced with maven3 ones

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt18_0jpp
- more plugins replaced with maven3 ones: ant, antrun, ...

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt17_0jpp
- more plugins replaced with maven3 ones: ear, gpg, ...

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt16_0jpp
- more compat plugins (one,rar,checkstyle,...)

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt15_0jpp
- disabled plugin-remote-resources

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt14_0jpp
- mvn-jpp: added MAVEN_OPTS processing

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt13_0jpp
- added compat mvn-jpp

* Sat Mar 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt12_0jpp
- empty proxy package to use maven3 instead of maven2

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt11_37jpp6
- fixed build w/new xmlrpc

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt10_37jpp6
- new jpp release with ant 1.8 support

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt10_29jpp6
- added missing /etc/mavenrc config

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt9_29jpp6
- new jpp release

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt9_28jpp6
- build with surefire 2.4

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt8_28jpp6
- build with new modello

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt8_27jpp6
- added missing Req: to maven2-plugin-remote-resources

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt7_27jpp6
- patched to build with new plexus-interpolation

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt6_27jpp6
- fixed build

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt6_26jpp6
- build w/o maven-2.0.x-MNG-3948.patch

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt5_26jpp6
- build w/o maven-2.0.x-MNG-3948.patch

* Sun Sep 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt4_26jpp6
- updated bootstrap repository

* Fri Sep 24 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt3_26jpp6
- backported 2.0.11 patch for parent poms lookup

* Fri Sep 24 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt2_26jpp6
- semi-bootstrap build

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_26jpp6
- new version

* Tue Jun 09 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt2_9jpp5
- new jpp release

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt2_8jpp5
- fixed build

* Tue Feb 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt1_8jpp5
- new version

* Tue Nov 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_10jpp1.7
- imported with jppimport script; note: bootstrapped version

