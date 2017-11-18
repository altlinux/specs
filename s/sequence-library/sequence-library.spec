BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           sequence-library
Version:        1.0.2
Release:        alt2_10jpp8
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

BuildRequires:  java-devel
BuildRequires:  junit
BuildRequires:  jpackage-utils
BuildRequires:  ant
Requires:  jpackage-utils
Source44: import.info

%description
A textual diff and merge library.

%package        javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
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
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_10jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_10jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp7
- new release

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- replaced by fc package

