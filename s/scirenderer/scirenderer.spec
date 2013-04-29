Name:           scirenderer
Version:        1.1.0
Release:        alt1
Summary:        A Java rendering library based on JoGL

Group:          Development/Java
License:        CeCILL
URL:            http://forge.scilab.org/index.php/p/scirenderer
Source0:        http://forge.scilab.org/index.php/p/scirenderer/downloads/get/%{name}-%{version}.tar.gz

BuildRequires(pre): rpm-build-java
BuildRequires:  java-devel
BuildRequires:  jpackage-utils

BuildRequires:  ant
BuildRequires:  gluegen2
BuildRequires:  jogl2
BuildRequires:  jlatexmath

Requires:       java
Requires:       jpackage-utils
Requires:       jogl2
Requires:       gluegen2
Requires:       jlatexmath

BuildArch:      noarch

%description
This Java API allows 2-D or 3-D plotting from simple 2-D graph to complex
scenes.
Independent library and used within Scilab software but is
available for other application and developments.

%package javadoc
Summary:        API Documentation for %name
Group:          Documentation
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %name.

%prep
%setup -q

# fix file-not-utf8
iconv -f ISO_8859-15 -t UTF-8 -o COPYING.utf8 COPYING
mv COPYING.utf8 COPYING

%build
ant \
    -Dgluegen2-rt.jar=%_jnidir/gluegen2-rt.jar \
    -Djogl2.jar=%_jnidir/jogl2.jar \
    \
    jar \
    doc

%install
mkdir -p %buildroot%_javadir
cp -pr jar/%name-%version.jar %buildroot%_javadir/%name.jar

mkdir -p %buildroot%_javadocdir/%name
cp -pr docs/* %buildroot%_javadocdir/%name

%files
%doc README COPYING CHANGES
%_javadir/%name.jar

%files javadoc
%doc README COPYING CHANGES
%_javadocdir/%name

%changelog
* Mon Apr 29 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build from Fedora to Sisyphus

