BuildRequires: javapackages-local
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global  git_commit d0ec879
%global  cluster jruby

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           bytelist
Version:        1.0.8
Release:        alt2_12jpp8
Summary:        A java library for lists of bytes

Group:          Development/Other
License:        CPL or GPLv2+ or LGPLv2+
URL:            http://github.com/%{cluster}/%{name}
Source0:        http://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel
BuildRequires:  jcodings
BuildRequires:  jpackage-utils
BuildRequires:  junit

Requires:       jcodings
Requires:       jpackage-utils
Source44: import.info


%description
A small java library for manipulating lists of bytes.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}

find -name '*.class' -delete
find -name '*.jar' -delete


%build
echo "See %{url} for more info about the %{name} project." > README.txt

export CLASSPATH=$(build-classpath junit jcodings)
mkdir -p lib
%ant


%install
mkdir -p %{buildroot}%{_javadir}

cp -p lib/%{name}-1.0.2.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%check
export CLASSPATH=$(build-classpath junit jcodings)
%ant test

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml
%doc README.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_12jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_5jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_3jpp7
- new release

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_1jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp5
- new version

