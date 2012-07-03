BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jwordsplitter
Version:        3.0
Release:        alt1_1jpp6
Summary:        Splits compound words into their parts

Group:          System/Libraries
License:        ASL 2.0
URL:            http://sourceforge.net/projects/jwordsplitter/
Source0:        import-%{name}.sh
Source1:        %{name}-%{version}.tar.bz2
#
# add a javadoc target into ant.
#
Patch0:         %{name}-%{version}-javadoc.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  junit
BuildRequires:  ant-junit

Requires:       jpackage-utils
Source44: import.info

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description 
jWordSplitter a a small Java library that splits compound words into their
parts. This is especially useful for languages like German where an
infinite number of new words can be formed by just appending nouns
("DonaudampfschifffahrtskapitA.n"). 

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -T -b 1
%patch0 -p1
sed "s/\r//" license.txt > license.txt.back
touch license.txt.back -r license.txt
mv license.txt.back license.txt

%build
CLASSPATH="$(build-classpath junit)"
export CLASSPATH
ant -v javadoc build

%install
pushd build

#isntall jar
pushd jWordSplitter
mv jWordSplitter.jar %{name}.jar
install -m 0644 -D %{name}.jar %{buildroot}/%{_javadir}/%{name}.jar
ln -s %{_javadir}/%{name}.jar %{buildroot}/%{_javadir}/jWordSplitter.jar

#install javadoc
popd
mkdir -p %{buildroot}%{_javadocdir}/
cp -rp javadoc %{buildroot}%{_javadocdir}/%{name}

#%check
#CLASSPATH="$(build-classpath junit)"
#export CLASSPATH
#ant test

%files
%doc build/jWordSplitter/README.txt
%doc build/jWordSplitter/license.txt
%doc build/jWordSplitter/CHANGES.txt
%{_javadir}/%{name}.jar
%{_javadir}/jWordSplitter.jar

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_1jpp6
- new version

