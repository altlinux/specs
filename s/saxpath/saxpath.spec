Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       saxpath
Version:    1.0
Release:    alt5_20jpp11
Summary:    Simple API for XPath
License:    Saxpath
URL:        http://sourceforge.net/projects/saxpath/
Source0:    http://downloads.sourceforge.net/saxpath/saxpath-1.0.tar.gz
Source1:    %{name}-%{version}.pom
Source2:    LICENSE
BuildArch:  noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  javapackages-local
Requires:       jpackage-utils
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

# install in _javadir
%mvn_file %{name}:%{name} %{name}

%build
mkdir src/conf
touch src/conf/MANIFEST.MF

ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 

# fix rpmlint warings: saxpath-javadoc.noarch: W: wrong-file-end-of-line-encoding /usr/share/javadoc/saxpath/**/*.css
for file in `find build/doc -type f | grep .css`; do
    sed -i 's/\r//g' $file
done

%mvn_artifact %{SOURCE1} build/%{name}.jar

%install
%mvn_install -J build/doc

%check
ant test

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:1.0-alt5_20jpp11
- java11 build

* Mon Jun 06 2022 Igor Vlasenko <viy@altlinux.org> 0:1.0-alt5_20jpp8
- migrated to %%mvn_artifact

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_20jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_18jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_15jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_14jpp8
- new jpp release

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

