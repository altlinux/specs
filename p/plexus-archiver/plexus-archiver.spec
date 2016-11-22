Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global commit dc873a4d3eb1ae1e55d661dff8ed85ec3d8eb936
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           plexus-archiver
Version:        3.0.1
Release:        alt1_0.3.gitdc873a4jpp8
Epoch:          0
Summary:        Plexus Archiver Component
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-archiver
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/plexus-archiver/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# This prevents "Too many open files" when building Eclipse documentation
# bundles inside a slow VM/mock environment
# This problem is reported upstream: https://github.com/codehaus-plexus/plexus-archiver/issues/6
Patch0:         0001-Avoid-using-ParallelScatterZipCreator.patch

BuildRequires:  maven-local
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-io
BuildRequires:  plexus-utils
BuildRequires:  apache-commons-compress
BuildRequires:  snappy-java
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{name}-%{commit}
%pom_remove_plugin :maven-shade-plugin
%mvn_file :%{name} plexus/archiver

%patch0 -p1

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_0.3.gitdc873a4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_0.2.gitdc873a4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt1_3jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

