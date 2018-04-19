Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ rpm-build-java swig
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global githash 3fd330c443272699cd8ba5d7da7e56c27a567ec1
Name:          juniversalchardet
Version:       1.0.3
Release:       alt1_10jpp8
Summary:       A Java port of Mozilla's universalchardet
# ALL files are under MPL (v1.1) GPL license
# build.xml and c/* under MPL 1.1/GPL 2.0/LGPL 2.1 license
License:       MPLv1.1 or GPLv2+ or LGPLv2+
URL:           https://github.com/thkoch2001/juniversalchardet
Source0:       https://github.com/thkoch2001/juniversalchardet/archive/%{githash}/%{name}-%{githash}.tar.gz
Source1:       http://repo1.maven.org/maven2/com/googlecode/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# added javadoc task
# fix example build
Patch0:        %{name}-1.0.3-build.patch

BuildRequires: ant
BuildRequires: java-devel
BuildRequires: javapackages-local

BuildArch:     noarch
Source44: import.info

%description
juniversalchardet is a Java port of 'universalchardet',
that is the encoding detector library of Mozilla.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p0

sed -i 's/1.5/1.6/' build.xml

sed -i 's/\r//' readme.txt

%build

%ant dist javadoc example

%install
%mvn_artifact %{SOURCE1} dist/%{name}-%{version}.jar
%mvn_file com.googlecode.%{name}:%{name} %{name}
%mvn_install -J dist/docs

install -pm 644 dist/%{name}-example-%{version}.jar \
 %{buildroot}%{_javadir}/%{name}-example.jar

%files -f .mfiles
%{_javadir}/%{name}-example.jar
%doc readme.txt
%doc --no-dereference MPL-1.1.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference MPL-1.1.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_10jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_9jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_7jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp8
- new version

