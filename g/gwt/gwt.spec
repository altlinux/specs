Name: gwt
Version: 2.5.1
Release: alt3
Summary: Google Web Toolkit
Group: Development/Java
License: ASL 2.0
Url: http://www.gwtproject.org/
# git clone https://gwt.googlesource.com/gwt
# cd gwt
# git archive --format=tar --prefix=gwt-2.5.1/ -o gwt-2.5.1.tar 2.5.1
# xz gwt-2.5.1.tar
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: gwt-%version.tar.xz
# svn checkout http://gwt-tools.googlecode.com/svn/trunk/ gwt-tools
# + Removal of unused files
# + Replacement of some .jar with links to system ones
Source1: gwt-tools.tgz
Source2: gwt-2.5.1.pom
Source3: gwt-codeserver-2.5.1.pom
Source4: gwt-dev-2.5.1.pom
Source5: gwt-servlet-2.5.1.pom
Source6: gwt-user-2.5.1.pom

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: rpm-build-java
BuildRequires: java-devel
BuildRequires: jcommon
BuildRequires: ant
Requires: java

%description
Google Web Toolkit.

%package javadoc
Group: Documentation
Summary: Javadoc for %name

%description javadoc
API documentation for %name.

%prep
%setup -a1

%build
export GWT_TOOLS=$(pwd)/gwt-tools
ant dist

%install
install -d -m 0755 %buildroot%_javadir/%name

# jars
for jar in ant-gwt gwt-api-checker gwt-codeserver gwt-dev gwt-doctool gwt-servlet-deps gwt-servlet gwt-soyc-vis gwt-user; do
	install -m 644 build/lib/$jar.jar %buildroot%_javadir/%name/$jar-%version.jar
	ln -s $jar-%version.jar %buildroot%_javadir/%name/$jar.jar
done

# poms
install -d -m 755 %buildroot%_datadir/maven2/poms/
install %SOURCE2 -m 644 %buildroot%_datadir/maven2/poms/%name.pom
install %SOURCE3 -m 644 %buildroot%_datadir/maven2/poms/%name-codeserver.pom
install %SOURCE4 -m 644 %buildroot%_datadir/maven2/poms/%name-dev.pom
install %SOURCE5 -m 644 %buildroot%_datadir/maven2/poms/%name-servlet.pom
install %SOURCE6 -m 644 %buildroot%_datadir/maven2/poms/%name-user.pom

install -d -m 0755 %buildroot%_datadir/%name
install -m 644 build/lib/gwt-benchmark-viewer.war %buildroot%_datadir/%name/benchmark-viewer-%version.war

# javadoc
install -d -m 0755 %buildroot%_javadocdir/%name-%version
cp -pr build/out/doc/javadoc/* %buildroot%_javadocdir/%name-%version/
ln -s %name-%version %buildroot%_javadocdir/%name

%files
%_datadir/%name/
%dir %_javadir/%name/
%_javadir/%name/*.jar
%_datadir/maven2/poms/*

%files javadoc
%_javadocdir/%name-%version
%_javadocdir/%name

%changelog
* Mon Feb 15 2016 Konstantin Artyushkin <akv@altlinux.org> 2.5.1-alt3
- fix symlink for new destination of jcommon.jar

* Sun Oct 11 2015 Konstantin Artyushkin <akv@altlinux.org> 2.5.1-alt2
- initial build for ALT Linux Sisyphus
- import from ROSA 2014


