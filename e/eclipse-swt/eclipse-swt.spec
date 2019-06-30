Epoch: 1
Name: eclipse-swt
Version: 4.9.0
Summary: SWT Library for GTK+
License: EPL
Url: http://www.eclipse.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: eclipse-swt = 1:4.9.0-2.fc29
Provides: mvn(org.eclipse.swt:org.eclipse.swt) = 3.108.0.v20180912.1831
Provides: mvn(org.eclipse.swt:swt) = 3.108.0.v20180912.1831
Provides: osgi(org.eclipse.swt) = 3.108.0
Requires: libgtk+2
Requires: libgtk+3
Requires: java
Requires: libwebkitgtk2
Requires: libwebkitgtk3

Group: Development/Java
Release: alt0.1jpp

# extract jar&xmvn xml from arch rpm
Source01: extract.sh

Source10: i686.swt.jar
Source11: i686.eclipse-swt.xml
Source20: x86_64.swt.jar
Source21: x86_64.eclipse-swt.xml
Source30: aarch64.swt.jar
Source31: aarch64.eclipse-swt.xml
Source40: armv7hl.swt.jar
Source41: armv7hl.eclipse-swt.xml
Source50: ppc64le.swt.jar
Source51: ppc64le.eclipse-swt.xml

ExclusiveArch: %ix86 x86_64 aarch64 armv7hl ppc64le

%description
SWT Library for GTK+.
bootstrap jar pack.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/maven-metadata
mkdir -p $RPM_BUILD_ROOT/usr/lib/java/
mkdir -p $RPM_BUILD_ROOT%_libdir/eclipse
ln -s ../../lib/java/swt.jar %buildroot%_libdir/eclipse/swt.jar

%ifarch %{ix86}
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT/usr/lib/java/swt.jar
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
%endif
%ifarch x86_64
install -m 644 %{SOURCE20} $RPM_BUILD_ROOT/usr/lib/java/swt.jar
install -m 644 %{SOURCE21} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
%endif
%ifarch aarch64
install -m 644 %{SOURCE30} $RPM_BUILD_ROOT/usr/lib/java/swt.jar
install -m 644 %{SOURCE31} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
%else
%ifarch %arm
install -m 644 %{SOURCE40} $RPM_BUILD_ROOT/usr/lib/java/swt.jar
install -m 644 %{SOURCE41} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
%endif
%endif
%ifarch ppc64le
install -m 644 %{SOURCE50} $RPM_BUILD_ROOT/usr/lib/java/swt.jar
install -m 644 %{SOURCE51} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
%endif

%files
/usr/share/maven-metadata/eclipse-swt.xml
/usr/lib/java/swt.jar
%_libdir/eclipse/swt.jar

%changelog
* Sun Jun 30 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.9.0-alt0.1jpp
- updated to 4.9.0; added armv7hl and ppc64le

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.7.3-alt0.1jpp
- updated to 4.7.3

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt0.2jpp
- added aarch64

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt0.1jpp
- bootstrap pack of jars

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.2jpp
- install to %%_jnidir

* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

