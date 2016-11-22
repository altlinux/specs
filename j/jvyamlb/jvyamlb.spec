Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global git_commit e0fdedc
%global cluster olabini

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jvyamlb
Version:        0.2.5
Release:        alt1_13jpp8
Summary:        YAML processor for JRuby

License:        MIT
URL:            http://github.com/%{cluster}/%{name}
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{git_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  bytelist
BuildRequires:  jcodings
BuildRequires:  joda-time
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  junit

Requires:       bytelist
Requires:       jcodings
Requires:       joda-time
Source44: import.info


%description
YAML processor extracted from JRuby.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

build-jar-repository -s -p lib joda-time bytelist jcodings


%build
%ant


%install
%__mkdir_p %{buildroot}%{_javadir}

%__cp -p lib/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%check
%ant test


%files
%{_javadir}/*
%doc LICENSE README CREDITS


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_8jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_7jpp7
- new version

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_5jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_4jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.4-alt1_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.4-alt1_2jpp5
- converted from JPackage by jppimport script

