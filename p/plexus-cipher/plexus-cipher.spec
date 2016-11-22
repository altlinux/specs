Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plexus-cipher
Version:        1.7
Release:        alt3_11jpp8
Summary:        Plexus Cipher: encryption/decryption Component
License:        ASL 2.0
# project moved to GitHub and it looks like there is no official website anymore
URL:            https://github.com/codehaus-plexus/plexus-cipher
BuildArch:      noarch

# git clone https://github.com/sonatype/plexus-cipher.git
# cd plexus-cipher/
# note this is version 1.7 + our patches which were incorporated by upstream maintainer
# git archive --format tar --prefix=plexus-cipher-1.7/ 0cff29e6b2e | gzip -9 > plexus-cipher-1.7.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.sonatype.plugins:sisu-maven-plugin)
BuildRequires:  mvn(org.sonatype.spice:spice-parent:pom:)
Source44: import.info

%description
Plexus Cipher: encryption/decryption Component

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

# replace %{version}-SNAPSHOT with %{version}
%pom_xpath_replace pom:project/pom:version "<version>%{version}</version>"

# fedora moved from sonatype sisu to eclipse sisu. sisu-inject-bean artifact
# doesn't exist in eclipse sisu. this artifact contains nothing but
# bundled classes from atinject, cdi-api, aopalliance and maybe others.
%pom_remove_dep org.sonatype.sisu:sisu-inject-bean
%pom_add_dep javax.inject:javax.inject:1:provided
%pom_add_dep javax.enterprise:cdi-api:1.0:provided

%mvn_file : plexus/%{name}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_11jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_10jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt3_11jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_11jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_11jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_8jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

