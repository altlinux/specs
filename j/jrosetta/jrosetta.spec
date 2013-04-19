Name: jrosetta
Version: 1.0.4
Release: alt1
Summary: A common base to build a graphical console

Group:   Development/Java
License: GPLv2
Url:     http://dev.artenum.com/projects/JRosetta/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: maven
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

%description
JRosetta provides a common base for graphical component that could be
used to build a graphical console in Swing with the latest requirements,
such as command history, completion and so on for instance for scripting
language or command line.

%prep
%setup -q 
#wrong-file-end-of-line-encoding
subst 's/\r//' CHANGE.txt COPYRIGHT.txt

%build
mvn-rpmbuild -e install javadoc:aggregate

%install
mkdir -p %buildroot%_javadir
cp -p modules/%name-api/target/%name-api-%version.jar \
    %buildroot%_javadir/%name-API-%version.jar
ln -s %name-API-%version.jar %buildroot%_javadir/%name-API.jar
cp -p modules/%name-engine/target/%name-engine-%version.jar \
    %buildroot%_javadir/%name-engine-%version.jar
ln -s %name-engine-%version.jar %buildroot%_javadir/%name-engine.jar

mkdir -p %buildroot%_javadocdir/%name
cp -rp target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 %buildroot%_mavenpomdir
install -pm 644 pom.xml  \
        %buildroot%_mavenpomdir/JPP-%name.pom
install -pm 644 modules/%name-api/pom.xml  \
        %buildroot%_mavenpomdir/JPP-%name-API.pom
install -pm 644 modules/%name-engine/pom.xml  \
        %buildroot%_mavenpomdir/JPP-%name-engine.pom


%files
%doc CHANGE.txt COPYRIGHT.txt LICENSE.txt
%_mavenpomdir/JPP-%name.pom
%_mavenpomdir/JPP-%name-*.pom
%_javadir/%name-*.jar
%_javadocdir/%name

%changelog
* Fri Apr 19 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version (ALT #28870)
- Build by maven

* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2
- Fix BuildRequires (ALT #21518)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1
- initial from Fedora

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 kwizart < kwizart at gmail.com > - 1.0.2-1
- Fix License (GPLv2 only)
- Fix Summary
- Update to 1.0.2 - previous patch merged upstream

* Mon Oct 27 2008 kwizart < kwizart at gmail.com > - 1.0.1-1
- Initial Package

