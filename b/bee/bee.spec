BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with bootstrap
%bcond_with bootstrap


Name:           bee
Version:        1.1.0
Release:        alt2_4jpp6
Epoch:          0
Summary:        Java-based build tool
License:        Public Domain
URL:            http://7bee.j2ee.us/bee/index-bee.html
Group:          Development/Java
Source0:        %{name}-%{version}.zip
Source1:        %{name}-script
Source2:        %{name}.catalog
Patch0:         %{name}-build.patch
%if %without bootstrap
BuildRequires: bee = %{epoch}:%{version}
%endif
BuildRequires: unzip
BuildRequires: zip
BuildArch:      noarch
Source44: import.info

%description
7Bee is a Java-based build tool. 7Bee inherited some principles of Make.

Why another build tool when there are make, gnumake, nmake, ant, maven, jam,
and many others? Because all those tools have limitations that 7Bee's
original author couldn't live with when developing software across multiple
platforms using different products. Actually, the author had two objections
before starting this project:

   1. Usage of Make requires to install a set of GNU tools
   2. Ant didn't meet to requirements of creation sophisticated build
      procedures, and had too big footprint 

Why 7, because 7 is a number of base classes giving 7Bee implementation.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -c
%patch0 -p0 -b .build
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{_bindir}/find deploy/examples -type f | %{_bindir}/xargs -t %{__perl} -pi -e 's/\r$//g'
%{__perl} -pi -e 's/\r$//g' deploy/index.html deploy/readme

sed -i -e s,"http://7bee.j2ee.us/xml/DTD/bee.dtd,"`pwd`/deploy/doc/bee.dtd,g `find . -name '*.xml'`

%build
pushd deploy
%{_bindir}/unzip -d tmp -qq dependency.zip
%{__rm} dependency.zip
pushd tmp
%{_bindir}/find -type f -name "*.class" | %{_bindir}/xargs -t %{__rm}
%{__rm} DependencyVisitor.java
%{javac} -d lib `%{_bindir}/find -type f -name "*.java"`
%{_bindir}/zip -q -9 -r ../dependency.zip *
popd
%{__rm} -r tmp/
popd

pushd deploy
%if %with bootstrap
%{_bindir}/unzip -qq dependency.zip 'src/jdepend/*'
%else
%{_bindir}/unzip -qq dependency.zip 'lib/jdepend/*'
%endif
popd

export CLASSPATH=
pushd deploy
%if %with bootstrap
pushd src
%{javac} -d ../lib `%{_bindir}/find -type f -name "*.java"`
popd
%{jar} cfm lib/bee.jar manifest.mf -C lib org -C lib jdepend -C doc bee.properties
%else
%{_bindir}/bee
%endif
popd
pushd deploy/src
%{javadoc} -d ../javadoc `%{_bindir}/find org -type f -name "*.java"`
popd

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p deploy/lib/bee.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr deploy/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# data
%{__mkdir_p} %{buildroot}%{_datadir}/sgml/%{name}
%{__cp} -p deploy/doc/bee.dtd %{buildroot}%{_datadir}/sgml/%{name}/%{name}.dtd
%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/sgml/%{name}/catalog

%{__mkdir_p} %{buildroot}%{_sysconfdir}/sgml
/bin/touch %{buildroot}%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat

# bin
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# doc
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -pr deploy/examples deploy/index.html deploy/readme %{buildroot}%{_docdir}/%{name}-%{version}

%post
/bin/touch %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat 2>/dev/null
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null 2>&1 || :
fi
if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --add system %{name}.dtd \
    file://%{_datadir}/sgml/%{name}/%{name}.dtd %{_sysconfdir}/xml/catalog \
    > /dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ]; then
  if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
    %{_bindir}/xmlcatalog --noout --del %{name}.dtd \
      %{_sysconfdir}/xml/catalog > /dev/null 2>&1 || :
  fi
fi

%postun
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null 2>&1 || :
fi

%files
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/sgml
%dir %{_datadir}/sgml/%{name}
%{_datadir}/sgml/%{name}/catalog
%{_datadir}/sgml/%{name}/%{name}.dtd
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%dir %{_sysconfdir}/sgml
#%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_4jpp6
- fixed build

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_4jpp6
- full build

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt0.1jpp
- bootstrap

