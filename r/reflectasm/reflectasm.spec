Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          reflectasm
Version:       1.07
Release:       alt1_4jpp7
Summary:       High performance Java library that provides reflection by using code generation
License:       BSD
URL:           http://code.google.com/p/reflectasm/
# svn checkout http://reflectasm.googlecode.com/svn/tags/1.07 reflectasm-1.07
# find reflectasm-1.07/ -name '*.jar' -delete
# find reflectasm-1.07/ -name '*.class' -delete
# rm -rf reflectasm-1.07/.svn
# tar cJf reflectasm-1.07-clean.tar.xz reflectasm-1.07
Source0:       %{name}-%{version}-clean.tar.xz
# Upstream update for reflectasm 1.07
Patch0:        %{name}-1.07-update.patch


BuildRequires: mvn(org.ow2.asm:asm)
# test deps
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-surefire-provider-junit4

BuildArch:     noarch
Source44: import.info

%description
ReflectASM is a very small Java library that provides
high performance reflection by using code generation.
An access class is generated to set/get fields,
call methods, or create a new instance. The access class
uses byte-code rather than Java's reflection, so it
is much faster. It can also access primitive fields
via byte-code to avoid boxing.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
sed -i 's/\r//' license.txt

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_4jpp7
- new release

