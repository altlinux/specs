
Name:           freehep-vectorgraphics
Version:        2.3
Release:        alt1
Summary:        Java library for export to a variety of vector and bitmap image formats

Group:          Development/Java
License:        Apache 2 and LGPL 2
URL:            http://freehep.github.io/freehep-vectorgraphics/
Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-maven-local
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven
BuildRequires:  maven-plugin-exec
BuildRequires:  maven-shared-artifact-resolver
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-shade-plugin

BuildRequires:  freehep-io
BuildRequires:  freehep-chartable-converter-plugin

BuildArch:	noarch
Requires:       java >= 1.6.0
Requires:       jpackage-utils
Requires:	freehep-io
Requires:	freehep-chartable-converter-plugin

Provides:	freehep-graphicsio = %version-%release
Provides:	freehep-graphics2d = %version-%release

%description
The Vector Graphics package of the FreeHEP Java Library enables any Java
program to export to a variety of vector graphics formats as well as
bitmap image formats. Among the vector formats are Encapsulated
PostScript (EPS), Portable Document Format (PDF), Enhanced Meta Format
(EMF), Scalable Vector Graphics (SVg), and Flash (SWF), while the image
formats include GIF, PNG, JPG and PPM.

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
# Remove obsoleted modules
rm -rf  freehep-graphics3d \
	freehep-graphicsio-cgm \
	freehep-graphicsio-latex

%build
mvn-rpmbuild install javadoc:aggregate

%install
# install submodules
for m in freehep-graphics*; do
	install -Dpm 644 $m/pom.xml %buildroot%_mavenpomdir/JPP-$m.pom
	install -Dpm 644 $m/target/$m-%{version}.jar %buildroot%_javadir/$m.jar
	%add_maven_depmap JPP-$m.pom $m.jar
done
 
# javadoc
install -d -m 755 %buildroot%_javadocdir/%name
cp -pr target/site/api*/* %buildroot%_javadocdir/%name/
 
%files
%doc README.txt LICENSE.txt
%_javadir/*
%_mavenpomdir/*
%_mavendepmapfragdir/*
 
%files javadoc
%doc LICENSE.txt
%doc %_javadocdir/%name
 
%changelog
* Wed Apr 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- Initial build for ALT Linux
