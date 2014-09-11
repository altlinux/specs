Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.osgi.service.obr

Name:           felix-osgi-obr
Version:        1.0.2
Release:        alt2_11jpp7
Summary:        Felix OSGi OBR Service API

License:        ASL 2.0
URL:            http://felix.apache.org/site/apache-felix-osgi-bundle-repository.html
Source0:        http://www.apache.org/dist/felix/org.osgi.service.obr-%{version}-project.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:felix)
BuildRequires:  mvn(org.apache.felix:org.osgi.core)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.mockito:mockito-all)
Source44: import.info


%description
OSGi OBR Service API.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file ":{*}" felix/@1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/felix
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_9jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_6jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_6jpp7
- new release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_5jpp7
- fc package

