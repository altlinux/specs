Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           multiverse
Version:        0.7.0
Release:        alt1_10jpp8
Summary:        A software transactional memory implementation for the JVM

License:        ASL 2.0
URL:            http://multiverse.codehaus.org
Source0:        https://github.com/pveentjer/Multiverse/archive/multiverse-0.7.0.tar.gz
# Only the license header is included in the source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-all)

BuildArch:      noarch
Source44: import.info

%description
A software transactional memory implementation for the JVM. Access (read and
writes) to shared memory is done through transactional references, that can be
compared to the AtomicReferences of Java. Access to these references will be
done under A (atomicity), C (consistency), I (isolation) semantics.

%package javadoc
Group: Development/Java
Summary:        JavaDoc for %{name}
BuildArch: noarch

%description javadoc
JavaDoc for %{name}.


%prep
%setup -q -n Multiverse-%{name}-%{version}

# wagon-webdav
%pom_xpath_remove pom:build/pom:extensions

%pom_remove_plugin :maven-deploy-plugin

cp -p %{SOURCE1} .

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.md
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_10jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_4jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

