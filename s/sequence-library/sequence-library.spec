Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           sequence-library
Version:        1.0.2
Release:        alt1_9jpp8
Summary:        Textual diff and merge library

License:        Sequence     
URL:            http://svn.svnkit.com/repos/3rdparty/de.regnis.q.sequence/

# generated with:
#        svn checkout http://svn.svnkit.com/repos/3rdparty/de.regnis.q.sequence/tags/1.0.2/
Source0:        %{name}-%{version}.tar.gz
#Source1:        http://search.maven.org/remotecontent?filepath=de/regnis/q/sequence/%{name}/%{version}/%{name}-%{version}.pom
Source1:        %{name}-%{version}.pom
Source2:        %{name}-build.xml
BuildArch:      noarch

BuildRequires:  junit
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
A textual diff and merge library.

%package        javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch
%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

# removing gradle build stuff
rm -rf gradle gradlew gradlew.bat

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

cp %{SOURCE2} build.xml

cat > sequence-library.build.properties <<EOF
version=%{versionr}
build.number=${versionr}
EOF

cat > manifest.mf <<EOF
Build-Version: %{versionr}
EOF


%build
ant all


%install

install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/libs/%{name}-%{versionr}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -Dpm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp docs/api/ %{buildroot}%{_javadocdir}/%{name}


%files -f .mfiles
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/*
%doc LICENSE.txt


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp7
- new release

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- replaced by fc package

