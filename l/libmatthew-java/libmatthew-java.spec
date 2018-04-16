Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libmatthew-java
Version:        0.8
Release:        alt2_19jpp8
Summary:        A few useful Java libraries
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

BuildRequires:  javapackages-local

Requires:       javapackages-tools
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
Group: Development/Other
Summary:        Javadoc for %{name}
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
%make_build \
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
%doc INSTALL README
%doc --no-dereference COPYING

%files javadoc
%{_javadocdir}/%{name}
%doc --no-dereference COPYING


%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_19jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_18jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_15jpp8
- new jpp release

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

