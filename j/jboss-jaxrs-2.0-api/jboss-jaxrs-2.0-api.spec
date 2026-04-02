%global namedreltag .Final
%global oname jboss-jaxrs-api_2.0_spec

Name:           jboss-jaxrs-2.0-api
Version:        1.0.0
Release:        alt2.1

Summary:        JAX-RS 2.0: The Java API for RESTful Web Services
License:        (CDDL-1.0 or GPLv2 with exceptions) and Apache-2.0
Group:          Development/Java
URL:            https://github.com/jboss/jboss-jaxrs-api_spec
VCS:            https://github.com/jboss/jboss-jaxrs-api_spec

Source0:        %oname-%version%namedreltag.tar.gz

Patch1:         0001-Replace-javax-with-jakarta.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)

BuildArch:      noarch

%description
JSR 339: JAX-RS 2.0: The Java API for RESTful Web Services.

%prep
%setup -n jboss-jaxrs-api_spec-%oname-%version%namedreltag
%autopatch -p1

# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

%pom_add_dep jakarta.xml.bind:jakarta.xml.bind-api

%mvn_file :%oname %name

# remove after upgrading narayana
%mvn_alias ":jboss-jaxrs-api_2.0_spec" "org.jboss.resteasy:jaxrs-api"

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1.0.0-alt2.1
- Cosmetic fixes.

* Tue Jan 20 2026 Evgeniy Serov <scala@altlinux.org> 1.0.0-alt2
- Updated for compatibility with the new jaxb api.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.0.0-alt1_16jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.0.0-alt1_13jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_10jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_8jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_7jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- new version

