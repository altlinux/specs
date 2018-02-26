BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
Name:           jaminid
Version:        0.99
Release:        alt1_1jpp6
Summary:        Java Mini Daemon

Group:          Development/Java
License:        LGPLv2
URL:            http://jaminid.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/Jaminid-%{version}.zip

BuildRequires:  jpackage-utils
Requires:       jpackage-utils
BuildArch:      noarch 
Source44: import.info

%description
Jaminid is a very small HTTP server meant to be embedded in Java applications to
provide an HTTP interface to your Java application. The I/O is purely strings,
and there's no JSP infrastructure, but rather direct printing.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n Jaminid

# Remove DOS line endings
for file in $(find . -name "*.css"); do
  sed 's|\r||g' $file >$file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
pushd src
# Build sources
javac com/prolixtech/jaminid/*.java
javac com/prolixtech/utils/*.java

# Generate JAR
touch MANIFEST.MF
jar cvmf MANIFEST.MF ../%{name}.jar com/prolixtech/jaminid/*.class com/prolixtech/utils/*.class

# Generate Javadoc
javadoc com.prolixtech.jaminid com.prolixtech.utils -d ../javadoc/
popd


%install
install -Dpm 0644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/
cp -a javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%files
%doc README.TXT doc/{doc.html,jaminid.css,jaminid.gif} src/com/prolixtech/jaminid_examples/
%{_javadir}/*.jar


%files javadoc
%{_javadocdir}/%{name}/


%changelog
* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_1jpp6
- new version

