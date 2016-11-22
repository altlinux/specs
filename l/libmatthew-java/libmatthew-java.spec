# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           libmatthew-java
Version:        0.8
Release:        alt2_14jpp8
Summary:        A few useful Java libraries
Group:          Development/Other
License:        MIT

# actual upstream:
URL: http://matthew.ath.cx/projects/java/
Source0: http://matthew.ath.cx/projects/java/%{name}-%{version}.tar.gz

# OSGi manifests
Source1:        %{name}-hexdump-osgi-MANIFEST.MF
Source2:        %{name}-unix-osgi-MANIFEST.MF

Patch0:         install_doc.patch
Patch1:         native-library-paths.patch
Patch2:         classpath_fix.patch


Source44: import.info

%description
A colleciton of Java libraries:
- Unix Sockets Library
  This is a collection of classes and native code to allow you to read
  and write Unix sockets in Java.

- Debug Library
  This is a comprehensive logging and debugging solution.

- CGI Library
  This is a collection of classes and native code to allow you to write
  CGI applications in Java.

- I/O Library
  This provides a few much needed extensions to the Java I/O subsystem.

- Hexdump
  This class formats byte-arrays in hex and ascii for display.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Other
BuildArch: noarch


%description javadoc
Javadoc for %{name}


%prep
%setup -q
%patch0 -p1

# this patch adds a system dependent path, so we fix it before
# applying the patch
sed -e 's|@JNIPATH@|%{_libdir}/%{name}|' %{PATCH1} | patch -p1 

%patch2 -p1


%build
export JAVA_HOME=%{java_home}
make %{?_smp_mflags} \
    CFLAGS='%{optflags}'\
    GCJFLAGS='%{optflags}' \
    LDFLAGS='%{optflags}' \
    PPFLAGS='%{optflags}' \
    JAVADOC="javadoc -Xdoclint:none" \
    -j1

# Inject OSGi manifests
jar umf %{SOURCE1} hexdump-0.2.jar
jar umf %{SOURCE2} unix-0.5.jar

%install
make install \
    DESTDIR=$RPM_BUILD_ROOT \
    JARDIR=%{_jnidir} \
    LIBDIR=%{_libdir}/%{name} \
    DOCDIR=%{_javadocdir}/%{name} \
    JAVADOC="javadoc -Xdoclint:none"

%files
%{_jnidir}/*.jar
%{_libdir}/%{name}
%doc COPYING INSTALL README

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_14jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_13jpp8
- %%_jnidir set to /usr/lib/java

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_13jpp8
- new version

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_7jpp7
- new release
- added compat symlinks

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_5jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_4jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3jpp7
- fc build

