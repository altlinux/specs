Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name glassfish-annotation-api
%define version 1.2
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global oname javax.annotation-api
Name:          glassfish-annotation-api
Version:       1.2
Release:       alt1_10jpp8
Summary:       Common Annotations API Specification (JSR 250)
License:       CDDL or GPLv2 with exceptions
# http://jcp.org/en/jsr/detail?id=250
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/javax.annotation-api-1.2/ glassfish-annotation-api-1.2
# tar czf glassfish-annotation-api-1.2-src-svn.tar.gz glassfish-annotation-api-1.2
Source0:       %{name}-%{namedversion}-src-svn.tar.gz

BuildRequires: jvnet-parent
BuildRequires: glassfish-legal

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: spec-version-maven-plugin

BuildArch:     noarch
Source44: import.info

%description
Common Annotations APIs for the Java Platform (JSR 250).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%mvn_file :%{oname} %{name}

%build

%mvn_build

sed -i 's/\r//' target/classes/META-INF/LICENSE.txt
cp -p target/classes/META-INF/LICENSE.txt .

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9jpp8
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_5jpp7
- new release

