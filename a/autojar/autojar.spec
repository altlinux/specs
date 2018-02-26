BuildRequires: bcel
BuildRequires: /proc
BuildRequires: jpackage-1.4-compat

Name:           autojar
Version:        1.3.1
Release:        alt2_1jpp1.7
Epoch:          0
Summary:        AutoJar generates self-contained jars starting from a given list of classes.
License:        GPL
Source0:	http://prdownloads.sourceforge.net/autojar/autojar-1.3.1.tar.gz
Source1:	autojar
URL:            http://autojar.sourceforget.net/
Group:          Development/Java
BuildArch:      noarch
Requires: jpackage-utils >= 0:1.5 bcel
BuildRequires: bcel-javadoc ant /bin/bash /usr/bin/perl

%description 
AutoJar generates self-contained jars starting from a given list of classes.
It searches the bytecode recursively for referenced classes, extracts
the corresponding files from wherever they reside, and creates an archive
containing only the classes you really need.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation

%description manual
Manual for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -c -q
cp %{SOURCE1} autojar
mv src/build.xml .
mv src/autojar.mf .
mv doc/* .
perl -p -i -e 's/java -jar autojar.jar/autojar/' index.html 

%build
export CLASSPATH=%(build-classpath bcel)
ant \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  -Dbcel.apiurl=%{_javadocdir}/bcel \
  jar javadoc

%install
rm -fr $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT/usr/bin
install -m 755 autojar $RPM_BUILD_ROOT/usr/bin
install -d -m 755 $RPM_BUILD_ROOT/usr/share/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
#%defattr(0755,root,root,0755)
/usr/bin/*

%files manual
%doc COPYING index.html top.gif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt2_1jpp1.7
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

