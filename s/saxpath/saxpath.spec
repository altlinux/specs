Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:       saxpath
Version:    1.0
Release:    alt4_11jpp8
Summary:    Simple API for XPath
License:    Saxpath
URL:        http://sourceforge.net/projects/saxpath/
Source0:    http://downloads.sourceforge.net/saxpath/saxpath-1.0.tar.gz
Source1:    %{name}-%{version}.pom
Source2:    LICENSE
BuildArch:  noarch

BuildRequires:  ant
BuildRequires:  ant-junit
Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
The SAXPath project is a Simple API for XPath. SAXPath is analogous to SAX
in that the API abstracts away the details of parsing and provides a simple
event based callback interface.

%package javadoc
Group: Development/Java
Summary:    API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{version}-FCS

find -name \*.jar -delete

cp %{SOURCE2} .

%build
mkdir src/conf
touch src/conf/MANIFEST.MF

ant

# fix rpmlint warings: saxpath-javadoc.noarch: W: wrong-file-end-of-line-encoding /usr/share/javadoc/saxpath/**/*.css
for file in `find build/doc -type f | grep .css`; do
    sed -i 's/\r//g' $file
done

%install
install -d -m 755 %{buildroot}/%{_javadir}
install -d -m 755 %{buildroot}/%{_mavenpomdir}
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}

install -p -m 644 build/%{name}.jar %{buildroot}/%{_javadir}/
install -p -m 644 %{SOURCE1} %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap
cp -a build/doc/* %{buildroot}/%{_javadocdir}/%{name}/

%check
ant test

%files -f .mfiles
%doc LICENSE

%files javadoc
%doc LICENSE
%{_javadocdir}/*


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_5.8jpp7
- new release

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

