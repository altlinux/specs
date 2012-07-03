Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define oldname jakarta-commons-validator
# Copyright (c) 2000-2005, JPackage Project
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

%define gcj_support 0

%define with_tests %{?_with_tests:1}%{!?_without_tests:0}

%define base_name  validator
%define short_name commons-%{base_name}

Summary:        Jakarta Commons Validator
Name:           jakarta-commons-validator11
Version:        1.1.4
Release:        alt1_5jpp5
Epoch:          0
License:        Apache Software License
Group:          Development/Java
Source0:        http://www.apache.org/dist/jakarta/commons/validator/source/commons-validator-%{version}-src.tar.gz
Source1:        %{oldname}.catalog
# FIXME DTDs are not in the source tarball anymore (conf directory missing)
# Obtainable from:
# http://svn.apache.org/repos/asf/jakarta/commons/proper/validator/tags/VALIDATOR_1_1_4/conf/
Source2:        commons-validator-%{version}-conf.tar.gz
Patch1:         jakarta-commons-validator-%{version}-build.patch
URL:            http://jakarta.apache.org/commons/validator/
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: ant >= 1.6.2
BuildRequires: jakarta-commons-beanutils >= 0:1.5
BuildRequires: jakarta-commons-collections >= 0:2.1
BuildRequires: jakarta-commons-digester >= 0:1.3
BuildRequires: jakarta-commons-logging >= 0:1.0.2
BuildRequires: oro >= 0:2.0.6
BuildRequires: junit >= 0:3.7
BuildRequires: xml-commons-apis
Requires: jakarta-commons-beanutils >= 0:1.5
Requires: jakarta-commons-collections >= 0:2.1
Requires: jakarta-commons-digester >= 0:1.3
Requires: jakarta-commons-logging >= 0:1.0.2
Requires: oro >= 0:2.0.6
Requires: xml-commons-apis
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Provides:       %{short_name}
Obsoletes:      %{short_name}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
A common issue when receiving data either electronically or from user
input is verifying the integrity of the data. This work is repetitive
and becomes even more complicated when different sets of validation
rules need to be applied to the same set of data based on locale for
example. Error messages may also vary by locale. This package attempts
to address some of these issues and speed development and maintenance
of validation rules.

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation

%description javadoc
Javadoc for %{oldname}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n %{short_name}-%{version}

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

tar xzvf %{SOURCE2}
cp -p %{SOURCE1} conf/share/catalog

%patch1

# -----------------------------------------------------------------------------

%build
export CLASSPATH=$(build-classpath \
xml-commons-apis oro junit jakarta-commons-logging jakarta-commons-digester \
jakarta-commons-beanutils jakarta-commons-collections)

%if %{with_tests}
ant -Dbuild.sysclasspath=first test
%endif

ant -Dbuild.sysclasspath=first dist

# -----------------------------------------------------------------------------

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# dtds and catalog
mkdir -p $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}
cp -p conf/share/{*.dtd,catalog} $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

# -----------------------------------------------------------------------------

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null || :
fi


%postun
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null || :
fi


%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

# -----------------------------------------------------------------------------

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/*
%{_datadir}/sgml/%{name}

%if %{gcj_support}
%{_libdir}/gcj/%{name}
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}

# -----------------------------------------------------------------------------

%changelog
* Thu May 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_5jpp5
- compat version

