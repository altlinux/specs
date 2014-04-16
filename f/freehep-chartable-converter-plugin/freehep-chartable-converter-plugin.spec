
Name:           freehep-chartable-converter-plugin
Version:        2.2.1
Release:        alt1
Summary:        Converts 16 bit Unicode text files into lookup tables

Group:          Development/Java
License:        Apache 2.0 and LGPL 2.1
URL:            http://java.freehep.org/freehep-chartableconverter-plugin/
Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-maven-local
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven

BuildArch:	noarch
Requires:       java >= 1.6.0
Requires:       jpackage-utils

%description
Converts 16 bit Unicode text files into lookup tables. These tables are
used by the VectorGraphics package to include and embed fonts in the
output formats.

%package javadoc
Summary:        Javadoc for %name
Group:          Documentation
Requires:       jpackage-utils
BuildArch:      noarch

Requires:       jpackage-utils
Requires:       %name = %version-%release

%description javadoc
Javadoc for %name.

%prep
%setup

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar \
                 %buildroot%_javadir/%{name}.jar

# pom
install -Dpm 644 pom.xml %buildroot%_mavenpomdir/JPP-%name.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %buildroot%_javadocdir/%name
cp -pr target/site/api*/* %buildroot%_javadocdir/%name/

%files
%doc LICENSE.txt
%_javadir/*
%_mavenpomdir/*
%_mavendepmapfragdir/*

%files javadoc
%doc LICENSE.txt
%doc %_javadocdir/%name

%changelog
* Wed Apr 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- Initial build for ALT Linux
