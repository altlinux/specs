Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:       saxpath
Version:    1.0
Release:    alt4_4.7jpp7
Summary:    Simple API for XPath

Group:      Development/Java
License:    Saxpath
URL:        http://sourceforge.net/projects/saxpath/
Source0:    http://downloads.sourceforge.net/saxpath/saxpath-1.0.tar.gz
Source1:    %{name}-%{version}.pom

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  ant-trax
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
The SAXPath project is a Simple API for XPath. SAXPath is analogous to SAX
in that the API abstracts away the details of parsing and provides a simple
event based callback interface.

%package javadoc
Summary:    Javadoc for saxpath
Group:      Development/Java
Requires:   jpackage-utils
BuildArch: noarch

%description javadoc
Java API documentation for saxpath.

%prep
%setup -q -n %{name}-%{version}-FCS

find -type f -name "*.jar" -exec rm -f '{}' \;

%build
mkdir src/conf
touch src/conf/MANIFEST.MF

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 

# fix rpmlint warings: saxpath-javadoc.noarch: W: wrong-file-end-of-line-encoding /usr/share/javadoc/saxpath/**/*.css
for file in `find build/doc -type f | grep .css`; do
    %{__sed} -i 's/\r//g' $file
done

%install

# install jar
install -dm 755 $RPM_BUILD_ROOT/%{_javadir}
cp -p build/saxpath.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar

#install pom
install -dm 755 $RPM_BUILD_ROOT/%{_mavenpomdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-saxpath.pom

#depmap entry
%add_to_maven_depmap saxpath saxpath %{version}-FCS JPP saxpath

# install javadoc
install -dm 755 $RPM_BUILD_ROOT/%{_javadocdir}/%{name}
cp -a build/doc/* $RPM_BUILD_ROOT/%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}

%files javadoc
%{_javadocdir}/*


%changelog
* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_4.7jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4.7jpp7
- fc update

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp6
- new jpp release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp5
- converted from JPackage by jppimport script

