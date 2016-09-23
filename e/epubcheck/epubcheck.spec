# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
#
# spec file for package epubcheck
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           epubcheck
Summary:        Validates IDPF EPub Files
License:        BSD-3-Clause
#Vendor:
Group:          Publishing
Version:        3.0
Release:        alt1_5.1
URL:            http://code.google.com/p/epubcheck/
Source0:        %{name}-%{version}.zip
Source1:        %{name}.script
Source2:	%{name}.xml
BuildArchitectures: noarch
BuildRequires:  unzip ant dos2unix
BuildRequires:  java-devel-default
BuildRequires:  saxon jing
BuildRequires:  libzio-devel
BuildRequires:  docbook-style-xsl docbook-dtds
BuildRequires:  libxslt xsltproc
Requires:       saxon jing java
Source44: import.info

%description
EpubCheck is a tool to validate IDPF Epub files. It can
detect many types of errors in Epub. OCF container
structure, OPF and OPS mark-up, and internal reference
consistency are checked. EpubCheck can be run as a
standalone command-line tool, installed as a web application
or used as a library.

Authors
-------
  Peter Sorotokin
  Garth Conboy
  Markus Gylling
  Piotr Kula
  Paul Norton

%define EPUBCHECK_HOME %{_datadir}/%{name}


%prep

%setup -q -n %{name}-%{version} 
# Replace placeholder strings:
cp %{S:1} %{name}
sed -i "s=@HOME@=%{EPUBCHECK_HOME}=" %{name}
cp %{S:2} .

%build
#xsltproc /usr/share/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl %{name}.xml
xsltproc /usr/share/xml/docbook/xsl-stylesheets/manpages/docbook.xsl %{name}.xml
gzip -9 %{name}.1

%install
mkdir -p %{buildroot}%{_mandir}/man1 \
         $RPM_BUILD_ROOT%{_javadir} \
         $RPM_BUILD_ROOT%{_bindir} \
         $RPM_BUILD_ROOT%{EPUBCHECK_HOME}/lib
%{__install} -m 755 %{name}            $RPM_BUILD_ROOT%{_bindir}

cp %{name}.1.gz %{buildroot}%{_mandir}/man1
cp %{name}*.jar $RPM_BUILD_ROOT%{EPUBCHECK_HOME}
cp -a lib/*.jar $RPM_BUILD_ROOT%{EPUBCHECK_HOME}/lib

pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{EPUBCHECK_HOME}/%{name}-%{version}.jar %{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{name}.jar
popd

%files
%doc %{_mandir}/man1/%{name}*
%dir %{EPUBCHECK_HOME}
%{EPUBCHECK_HOME}/*
%{_javadir}/%{name}*.jar
%{_bindir}/%{name}

%changelog
* Fri Sep 23 2016 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_5.1
- converted for ALT Linux by srpmconvert tools

