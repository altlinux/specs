Epoch: 1
Name: eclipse-swt
Version: 4.5.1
Summary: SWT Library for GTK+
License: EPL
Url: http://www.eclipse.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: eclipse-swt = 1:4.5.1-1.fc23
Provides: mvn(org.eclipse.swt:org.eclipse.swt) = 3.104.1.v20151005.1500
Provides: mvn(org.eclipse.swt:swt) = 3.104.1.v20151005.1500
Requires: libgtk+2
Requires: libgtk+3
Requires: java
Requires: libwebkitgtk2
Requires: libwebkitgtk3

Group: Development/Java
Release: alt0.1jpp

Source1: swt.i586.jar
Source2: swt.x86_64.jar
Source3: eclipse-swt.xml.i586
Source4: eclipse-swt.xml.x86_64
ExclusiveArch: %ix86 x86_64

%description
SWT Library for GTK+.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/maven-metadata
mkdir -p $RPM_BUILD_ROOT%_libdir/java
%ifarch x86_64
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
sed -i -e s,/usr/lib/java,%_libdir/java, $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%_libdir/java/swt.jar
%else
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%_libdir/java/swt.jar
%endif


%files
/usr/share/maven-metadata/eclipse-swt.xml
%_libdir/java/swt.jar

%changelog
* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

