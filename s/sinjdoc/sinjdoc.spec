# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: /usr/bin/fastjar java-devel-default
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           sinjdoc
Version:        0.5
Release:        alt2_15jpp6
Summary:        Documentation generator for Java source code

Group:          Development/Java
# No version given.
License:        GPL+
URL:            http://cscott.net/Projects/GJ/sinjdoc-latest/
Source0:        http://cscott.net/Projects/GJ/sinjdoc-latest/sinjdoc-0.5.tar.gz
Patch0:         sinjdoc-annotations.patch
Patch1:         sinjdoc-autotools-changes.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: ecj 
BuildRequires: gcc-java >= 4.0.2
BuildRequires: java-gcj-compat-devel >= 1.0.70
BuildRequires: java_cup >= 0.10

Requires:         java_cup >= 0.10
Requires:         libgcj >= 4.1.2
Requires(post):   java-gcj-compat >= 1.0.70
Requires(postun): java-gcj-compat >= 1.0.70

#Obsoletes: gjdoc <= 0.7.7-14.fc7 <= 0.7.7-14.fc7
Source44: import.info

%description
This package contains Sinjdoc a tool for generating Javadoc-style
documentation from Java source code

%prep
%setup -q
%patch0 -p0
%patch1 -p0
# Use packaged jar, not bundled jar.
rm -f lib/cup.jar
ln -s %{_javadir}/java_cup.jar lib/cup.jar
# This is given in classpath in various makefiles, but no classes
# from this jar are actually imported.
rm -f lib/jutil.jar

%build
aclocal
automake
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
* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_15jpp6
- fixed build

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_15jpp7
- new release

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5-alt1_8jpp5.qa1
- NMU: rebuilt for debuginfo.

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_8jpp5
- first build

