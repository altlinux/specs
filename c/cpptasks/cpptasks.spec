Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		cpptasks
Version:	1.0b5
Release:	alt2_9jpp7
Summary:	Compile and link task for ant

Group:		Development/Java

License:	ASL 2.0
URL:		http://ant-contrib.sourceforge.net/
Source0:	http://downloads.sourceforge.net/ant-contrib/cpptasks-1.0b5.tar.gz
Source1:	%{name}-README.fedora

BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	jpackage-utils
BuildRequires:	junit
#BuildRequires:	mave

Requires:	ant
Requires:	jpackage-utils

BuildArch:	noarch
Source44: import.info
	

%description
This ant task can compile various source languages and produce
executables, shared libraries (aka DLL's) and static libraries. Compiler
adaptors are currently available for several C/C++ compilers, FORTRAN,
MIDL and Windows Resource files.

%package        javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	%{name} >= %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description	javadoc
Javadoc documentation for %{summary}.


#The manual for b5 has been moved to xdoc (doxia) format.
# This requires maven, which requires many dependencies which we don't have.
#%package	manual
#Summary:	Docs for %{name}
#Group:		Development/Documentation

#%description	manual
#User manual for %{summary}.

%prep
%setup -q -n %{name}-%{version}

#End of line conversion
%{__sed} -i 's/\r//' NOTICE 

#Check for exisiting jar files
JAR_files=""
for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
	JAR_files="$JAR_files $j"
	fi
done

if [ ! -z "$JAR_files" ] ; then
	echo "These JAR files should be deleted and symlinked to system JAR files: $JAR_files"
	exit 1
fi

cp -p %{SOURCE1} ./README.fedora

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=
ant jars javadocs 

#In lieu of maven built docs, which requires clirr
#a URL is supplied in README.fedora
#mvn-jpp site

%install


# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}/ant/
install -Dpm 644 target/lib/%{name}.jar \
	$RPM_BUILD_ROOT%{_javadir}/ant/%{name}-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}/ant/
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/ant/%{name}.jar
popd

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

cp -pr target/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual - 
#install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

#Place a file into ant's config dir
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/
echo "ant/%{name}" > $RPM_BUILD_ROOT/%{_sysconfdir}/ant.d/%{name}
# jpp compat
ln -s ant/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap ant-contrib %{name} %{namedversion} JPP %{name}

# poms
install -D -m 644 pom.xml $RPM_BUILD_ROOT%_mavenpomdir/JPP-%{name}.pom



%files
%doc LICENSE NOTICE README.fedora
%{_javadir}/ant/*.jar
%{_sysconfdir}/ant.d/%{name}

%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/*
%_mavenpomdir/*


%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

#%files manual
#%defattr(-,root,root,-)
#%doc %{_docdir}/%{name}-%{version}

# -----------------------------------------------------------------------------

%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_9jpp7
- update

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt2_8jpp7
- added jpp compatible symlink

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0b5-alt1_8jpp7
- fc version

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b5.1jpp5
- fixed build

* Tue May 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b5.1jpp5
- new version

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b4.1jpp5
- fixed repocop warnings

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b4.1jpp1.7
- converted from JPackage by jppimport script

