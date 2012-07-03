Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           sinjdoc
Version:        0.5
Release:        alt1_8jpp5
Summary:        Documentation generator for Java source code

Group:          Development/Java
# No version given.
License:        GPL+
URL:            http://cscott.net/Projects/GJ/sinjdoc-latest/
Source0:        http://cscott.net/Projects/GJ/sinjdoc-latest/sinjdoc-0.5.tar.gz
Patch0:         sinjdoc-annotations.patch
Patch1:         sinjdoc-autotools-changes.patch

BuildRequires: autoconf
BuildRequires: automake_1.6
BuildRequires: eclipse-ecj >= 3.2.1
BuildRequires: gcc-java >= 4.0.2
BuildRequires: java-gcj-compat-devel >= 1.0.70
BuildRequires: java-cup >= 0.10

Requires: java-cup >= 0.10
Requires: libgcj >= 4.1.2
Requires(post): java-gcj-compat >= 1.0.70
Requires(postun): java-gcj-compat >= 1.0.70

#Obsoletes: gjdoc <= 0.7.7-14.fc7 <= 0.7.7-14.fc7

%description
This package contains Sinjdoc a tool for generating Javadoc-style
documentation from Java source code

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
automake-1.6
autoconf
%configure
make %{?_smp_mflags}

%install
cat > sinjdoc << EOF
#!/bin/sh
%{_bindir}/gij -classpath \
  %{_javadir}/java_cup-runtime.jar:%{_javadir}/sinjdoc.jar \
  net.cscott.sinjdoc.Main "\$@"
EOF
install -d 755 $RPM_BUILD_ROOT%{_bindir}
install -m 655 sinjdoc $RPM_BUILD_ROOT%{_bindir}/sinjdoc
install -d 755 $RPM_BUILD_ROOT%{_javadir}
install -D -m 644 sinjdoc.jar $RPM_BUILD_ROOT%{_javadir}/sinjdoc.jar
aot-compile-rpm

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/sinjdoc
%{_javadir}/sinjdoc.jar
%{_libdir}/gcj/%{name}

%changelog
* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_8jpp5
- first build

