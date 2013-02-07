# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jgoodies-animation
Version:       1.3.0
Release:       alt1_2jpp7
Summary:       Framework for time-based real-time animations in Java
Group:         Development/Java
License:       BSD
#Alt. URL:     http://java.net/projects/animation
URL:           http://www.jgoodies.com/freeware/animation/index.html

Source0:       http://www.jgoodies.com/download/libraries/animation/%{name}-%(tr "." "_" <<<%{version}).zip
Source1:       %{name}-%{version}.pom

BuildArch:     noarch

BuildRequires: ant
BuildRequires: jpackage-utils
BuildRequires: jgoodies-common

Requires:      jpackage-utils
Requires:      jgoodies-common
Source44: import.info


%description
The JGoodies Animation framework enables you to produce time-based real-time
animations in Java. It uses concepts and notions as described by the W3C
specification for the Synchronized Multimedia Integration Language (SMIL).

This animation framework has been designed for a seemless, flexible
and powerful integration with Java, ease-of-use and a small library size.
Unlike SMIL we use Java to describe the animations a.. not XML.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q

# Delete prebuilt JARs
find -name "*.jar" -delete

# Remove DOS line endings
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed 's|\r||g' $file > $file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done

%build
mkdir -p lib
pushd lib
ln -sf $(build-classpath jgoodies-common) jgoodies-common-1.2.1.jar
popd
%ant jar javadoc

%install
install -Dpm 0644 build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}/
cp -a build/docs/api/* %{buildroot}%{_javadocdir}/%{name}/

install -Dm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE.txt README.html RELEASE-NOTES.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2jpp7
- initial build

