# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global author      technomancy
%global groupId     lancet
%global artifactId  lancet
%global archivename %{author}-%{artifactId}
%global commit_hash 773e48f

Name:           %{artifactId}
Version:        1.0.1
Release:        alt2_6jpp7
Summary:        A build tool like Ant or Rake

Group:          Development/Java
License:        EPL
URL:            https://github.com/%{author}/%{name}
# This is actually lancet 1.0.1; upstream mistagged it
# No public issue tracker; authors notified in private communication
# wget --content-disposition %%{url}/tarball/%%{version}
Source0:        %{archivename}-%{version}-0-g%{commit_hash}.tar.gz
# Generated using Leiningen 1.7.1
Source1:        lancet-pom.xml

BuildArch:      noarch

BuildRequires:  jpackage-utils >= 1.5


Requires:       jpackage-utils
%if 0%{?rhel}
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
%endif

Requires:       ant >= 1.7.1
Requires:       ant-nodeps >= 1.7.1
Source44: import.info

%description
Lancet is a build tool like Ant or Rake. Lancet makes it
easy to create build targets: any Clojure function can be
a build target. Lancet can call Ant tasks, or shell out
and call other processes.


%prep
%setup -q -n %{archivename}-%{commit_hash}
cp -p %{SOURCE1} pom.xml


%build
jar cf %{name}.jar -C src .


%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom


%if 0%{?add_maven_depmap:1}
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%else
# some systems like RHEL do not have add_maven_depmap defined
# - probably don't need JPP/%%{name} -- do we?
%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP %{name}
%endif

%files
%doc README LICENSE
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}.jar

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_5jpp7
- new version

