Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global  git_commit d0ec879
%global  cluster jruby

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           bytelist
Version:        1.0.8
Release:        alt3_22jpp11
Summary:        A java library for lists of bytes

License:        CPL or GPLv2+ or LGPLv2+
URL:            http://github.com/%{cluster}/%{name}
Source0:        http://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz

Patch0:         00-set-javac-1.8-source-target.patch

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  jcodings
BuildRequires:  jpackage-utils
BuildRequires:  javapackages-local
BuildRequires:  junit

Requires:       jcodings
Requires:       jpackage-utils
Source44: import.info


%description
A small java library for manipulating lists of bytes.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}
%patch0 -p1

find -name '*.class' -delete
find -name '*.jar' -delete

# install in _javadir
%mvn_file org.jruby.extras:%{name} %{name}

%build
echo "See %{url} for more info about the %{name} project." > README.txt

export CLASSPATH=$(build-classpath junit jcodings)
mkdir -p lib
%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 

%mvn_artifact pom.xml lib/%{name}-1.0.2.jar

%install
%mvn_install

%check
export CLASSPATH=$(build-classpath junit jcodings)
%ant test

%files -f .mfiles
%doc README.txt

%changelog
* Sun Jun 05 2022 Igor Vlasenko <viy@altlinux.org> 1.0.8-alt3_22jpp11
- migrated to %%mvn_artifact

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.0.8-alt2_22jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_19jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_17jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_16jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_15jpp8
- java update

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

