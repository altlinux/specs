Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name      commons-email

Name:             apache-%{short_name}
Version:          1.3.1
Release:          alt1_5jpp8
Summary:          Apache Commons Email Package
Group:            Development/Other
License:          ASL 2.0
URL:              http://commons.apache.org/proper/%{short_name}/
Source0:          http://archive.apache.org/dist/commons/email/source/%{short_name}-%{version}-src.tar.gz

BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
BuildRequires:    javamail
Source44: import.info

%description
Commons-Email aims to provide an API for sending email. It is built on top of 
the JavaMail API, which it aims to simplify.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src

# Activation is now provided by the JRE
%pom_remove_dep "javax.activation:activation"

# Some test deps are not in fedora
%pom_remove_dep "org.subethamail:subethasmtp"
%pom_remove_dep "org.powermock:"

# Compatibility links
%mvn_alias "org.apache.commons:commons-email" "commons-email:commons-email"
%mvn_file :commons-email %{short_name} %{name}

%build
# Skip tests due to some missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt RELEASE-NOTES.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp7
- new version

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_4jpp6
- fixed build (added jansi BR:)

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp6
- fixed symlinks

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp6
- added osgi manifest

