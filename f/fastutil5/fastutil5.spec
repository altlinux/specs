Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:           fastutil5
Version:        5.1.5
Release:        alt3_1jpp5
Epoch:          0
Summary:        Fast & compact type-specific Java utility classes
Group:          Development/Java
License:        LGPL
Source0:        http://fastutil.dsi.unimi.it/fastutil-%{version}-src.tar.gz
URL:            http://fastutil.dsi.unimi.it/
BuildArch:      noarch
BuildRequires: ant make gcc jpackage-utils >= 0:1.6 /bin/bash
BuildRequires: java-javadoc

%description
fastutil extends the Java Collections Framework by providing type-specific
maps, sets, lists and priority queues with a small memory footprint and
fast access and insertion; it also includes a fast I/O API for binary and
text files. The classes implement their standard counterpart interface
(e.g., Map for maps) and can be plugged into existing code. Moreover, they
provide additional features (such as bidirectional iterators) that are not
available in the standard classes.

From version 5, fastutil runs only on Java 5+.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n fastutil-%{version}

%build
make -s sources
export CLASSPATH=
ant \
  -Dj2se.apiurl=%{_javadocdir}/java \
  jar javadoc
mv fastutil-%{version}.jar %{name}-%{version}.jar

%install
# jars
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink


%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}
 

%files
%doc README CHANGES COPYING.LIB
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.1.5-alt3_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.1.5-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.1.5-alt1_1jpp5
- converted from JPackage by jppimport script

