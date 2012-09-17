# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           xml-writer
Version:        0.2
Release:        alt1_5jpp7
Summary:        Java filter class designed to work with SAX2
Group:          Development/Java
License:        Public Domain
URL:            http://www.megginson.com/
Source0:        http://www.megginson.com/downloads/xml-writer-0.2.zip
# The filtering attribute is not supported by javac (IcedTea 1.6, at least). Remove it.
Patch0:         xml-writer.patch
BuildArch:      noarch

BuildRequires:     ant
BuildRequires:     jpackage-utils
Requires:          jpackage-utils
Source44: import.info

%description
With this filter one can use it to take a snapshot of
any point in a SAX2 filter chain, as well as serializing the final
result to XML (this may be important for auditing as well).


%package javadoc
Summary:           Javadocs for xml-writer
Group:             Development/Java
Requires:          %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
xml-writer development documentation.


%prep
%setup -q
%patch0

rm -f xml-writer.jar

%build
ant clean jar javadoc

%install

# jar
install -d $RPM_BUILD_ROOT%{_javadir}
install -m644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rp docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc COPYING README ChangeLog BUGS
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}/
%{_javadocdir}/%{name}


%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_5jpp7
- new version

