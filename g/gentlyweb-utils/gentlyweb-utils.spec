# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          gentlyweb-utils
# there are no differences in the debian source taraball
# http://ftp.de.debian.org/debian/pool/main/g/gentlyweb-utils/gentlyweb-utils_1.5.orig.tar.gz
# the version is changed only in the activemq package see activemq-5.6.0/pom.xml
Version:       1.5
Release:       alt1_3jpp7
Summary:       Java utility library used by JoSQL for I/O
Group:         Development/Java
License:       ASL 2.0
Url:           http://josql.sourceforge.net/
#Sour ce0:       http://gentlyweb-utils.sourcearchive.com/downloads/1.5-1/gentlyweb-utils_1.5.orig.tar.gz
Source0:       http://sourceforge.net/projects/josql/files/josql/stable-2.2/gentlyWEB-src-utils-1.1.tar.gz
Source1:       http://repo.fusesource.com/nexus/content/groups/public/net/sf/josql/%{name}/%{version}/gentlyweb-utils-%{version}.pom
# use system libraries
# fix javac target/source 1.5, encoding
# fix version
# add javadoc task
Patch0:        %{name}-%{version}-build.patch


BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: jdom

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Simple java utility library used mainly by JoSQL for I/O.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n gentlyWEB-src-utils-1.1
%patch0 -p0

%build

%ant -f build-utils.xml createUtilsJar javadoc

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 gentlyWEB-utils-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/gentlyWEB-utils.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %SOURCE1 %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/gentlyWEB-utils.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_2jpp7
- new version

