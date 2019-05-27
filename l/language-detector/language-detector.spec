Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          language-detector
Version:       0.5
Release:       alt1_7jpp8
Summary:       Language Detection Library for Java
# Source files without license headers https://github.com/optimaize/language-detector/issues/67
License:       ASL 2.0
URL:           https://github.com/optimaize/language-detector
Source0:       https://github.com/optimaize/language-detector/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.intellij:annotations)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.arnx:jsonic)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.slf4j:slf4j-api)

# This is a fork from https://code.google.com/p/lang-guess/ (forked on 2014-02-27) which itself is a fork
# of the original project https://code.google.com/p/language-detection/ with improvements
# Modified version of com.cybozu.labs:langdetect
# ./src/main/java/be/frma/langguess/GenProfile.java
# ./src/main/java/com/cybozu/labs/langdetect
Provides:      bundled(langdetect) = 1.1-20120112

BuildArch:     noarch
Source44: import.info

%description
A language detector / language guesser library in Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

%pom_change_dep :junit-dep :junit

#rm src/test/java/com/cybozu/labs/langdetect/util/TagExtractorTest.java

%mvn_file com.optimaize.languagedetector:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_7jpp8
- new version

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_5jpp8
- new version

