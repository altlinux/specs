Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global upname RSyntaxTextArea

Name:           rsyntaxtextarea
Version:        3.1.3
Release:        alt1_2jpp11
Summary:        A syntax highlighting, code folding text editor for Java Swing applications

License:        BSD
URL:            https://github.com/bobbylight/%{upname}
Source0:        https://github.com/bobbylight/%{upname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        pom.xml

BuildRequires:  maven-local


# Apply workaround until gradle doesn't exists in repos
Provides:       mvn(com.fifesoft:rsyntaxtextarea)
Provides:       osgi(com.fifesoft.rsyntaxtextarea)

BuildArch:      noarch
Source44: import.info

%description
%{upname} is a customizable, syntax highlighting text component for Java
Swing applications. Out of the box, it supports syntax highlighting for 40+
programming languages, code folding, search and replace, and has add-on
libraries for code completion and spell checking. Syntax highlighting for
additional languages can be added via tools such as JFlex.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{upname}

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{upname}-%{version}


# Drop included jars
find . -name "*.jar" -delete

pushd %{upname}
for file in src/main/dist/%{upname}.License.txt src/main/dist/readme.txt; do
    sed "s|\r||g" $file > $file.new && \
    touch -r $file $file.new && \
    mv $file.new $file
done
popd


%build
d=`mktemp -d`
f=`find %{upname}/src/main/java -type f | grep \.java$`
javac  -target 1.8 -source 1.8 -d $d $f
cp -rv %{upname}/src/main/resources/* $d
l=`pwd`
pushd $d
jar -cf $l/%{name}.jar *
popd
%mvn_artifact %{SOURCE1} %{name}.jar

%install
%mvn_install




%files -f .mfiles
%doc --no-dereference %{upname}/src/main/dist/%{upname}.License.txt
%doc %{upname}/src/main/dist/readme.txt
%{_datadir}/java/%{name}/%{name}.jar



%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 3.1.3-alt1_2jpp11
- new version

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 3.1.1-alt2_2jpp11
- built for java8

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 3.1.1-alt1_2jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_6jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_5jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_2jpp8
- new jpp release

