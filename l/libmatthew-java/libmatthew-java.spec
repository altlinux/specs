BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           libmatthew-java
Version:        0.8
Release:        alt1_3jpp7
Summary:        A few useful Java libraries
Group:          Development/Java
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

BuildRequires:  jpackage-utils

Requires:       jpackage-utils
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
Group:          Development/Java
Requires:       jpackage-utils
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
    -j1

# Inject OSGi manifests
jar umf %{SOURCE1} hexdump-0.2.jar
jar umf %{SOURCE2} unix-0.5.jar

%install
make install \
    DESTDIR=$RPM_BUILD_ROOT \
    JARDIR=%{_libdir}/%{name} \
    LIBDIR=%{_libdir}/%{name} \
    DOCDIR=%{_javadocdir}/%{name}

%files
%{_libdir}/%{name}
%doc COPYING INSTALL README

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING


%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3jpp7
- fc build

