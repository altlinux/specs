
Name:           freehep-io
Version:        2.2.2
Release:        alt1
Summary:        The FreeHEP IO package extends the Java IO package with a number of input and output streams

Group:          Development/Java
License:        Apache 2 and LGPL 2
URL:            http://freehep.github.io/freehep-io/
Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-maven-local
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven
BuildRequires:  maven-shared-artifact-resolver
BuildRequires:  maven-surefire-provider-junit4

BuildArch:	noarch
Requires:       java >= 1.6.0
Requires:       jpackage-utils

%description
The FreeHEP IO package extends the Java IO package with a number of
input and output streams.  The FreeHEP IO streams are in use by the
FreeHEP VectorGraphics package and the PostScript Viewer. Of course all
these classes are usable elsewhere.

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
* Wed Apr 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for ALT Linux
