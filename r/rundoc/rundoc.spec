Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           rundoc
Version:        0.11
Release:        alt1_16jpp11
Summary:        An Ant task designed to help with the single-sourcing of program documentation

License:        BSD
URL:            http://www.martiansoftware.com/lab/rundoc/
Source0:        http://martiansoftware.com/lab/rundoc/rundoc-0.11-src.zip
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  javapackages-local
#/usr/share/java must be owned: 
Requires:       javapackages-tools
Source44: import.info


%description
An Ant task designed to help with the single-sourcing of program documentation.

%package	javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch
%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -qc -n %{name}-%{version}

rm %{name}-%{version}.jar
rm -rf javadoc/ 

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  jar javadoc


%install
mkdir -p %{buildroot}%{_javadir}
install -pm  0755 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/
mv javadoc/ %{buildroot}%{_javadocdir}/%{name}


%files 
%{_javadir}/%{name}.jar
%doc LICENSE.txt

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 0.11-alt1_16jpp11
- new version

