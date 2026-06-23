%define base_name plexus-build-api

Name:           plexus-build-api0
Epoch:          0
Version:        0.0.7
Release:        alt5

Summary:        Plexus Build API
License:        ASL 2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-build-api/
VCS:            https://github.com/codehaus-plexus/plexus-build-api

Source0:        %base_name-%version.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         %base_name-migration-to-component-metadata.patch
Patch1:         0000-Port-to-plexus-utils-3.3.0.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)

BuildArch:      noarch

%description
This API allows IDEs to integrate with Maven deeper than it would be possible
by just using regular Maven/Mojo API.

%javadoc_package

%prep
%setup -n %base_name-%base_name-%version
%autopatch -p1

cp -p %SOURCE1 .

%pom_remove_parent

%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/*" 1.8

%mvn_file : plexus/%name

# Install plexus-build-api-tests as well
%mvn_package :

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Tue Jun 23 2026 Evgeniy Serov <scala@altlinux.org> 0:0.0.7-alt5
- Renamed package to plexus-build-api0.

* Mon Mar 30 2026 Evgeniy Serov <scala@altlinux.org> 0:0.0.7-alt4
- Fix build with new sisu and plexus-containers.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:0.0.7-alt3_36jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:0.0.7-alt3_33jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:0.0.7-alt3_30jpp11
- update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:0.0.7-alt3_27jpp8
- fc update

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_23jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_22jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_18jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_17jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_16jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_15jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt1_8jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt1_4jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt1_3jpp7
- fc version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.4-alt2_2jpp6
- added maven2-plugin-resources dep

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.4-alt1_2jpp6
- new jpp release

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.4-alt0.1jpp
- bootstrap

