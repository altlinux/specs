BuildRequires(pre): rpm-build-python3
%global pypi_name PySimpleSOAP

Name:          python3-module-pysimplesoap
Version:       1.16.2
Release:       alt1
Summary:       Python simple and lightweight SOAP Library
Group:         Development/Python
License:       LGPLv3+
URL:           https://github.com/pysimplesoap/pysimplesoap
Source0:       %name-%version.tar
Source1:       https://raw.githubusercontent.com/pysimplesoap/pysimplesoap/master/license.txt
Patch:         python-pysimplesoap-1.16.2-cStringIO.patch
BuildArch:     noarch

BuildRequires: python3-devel python3-module-setuptools


%description
Python simple and lightweight SOAP library for client and
server web services interfaces, aimed to be as small and easy
as possible, supporting most common functionality.

%prep
%setup -q
%patch -p1

for lib in pysimplesoap/*.py; do
 sed -e '1{\@^#! /usr/bin/env python@d}' -e '1{\@^#!/usr/bin/env python@d}' \
     -e '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
cp -p %{SOURCE1} .

%build
%python3_build

%install
%python3_install

%files -n python3-module-pysimplesoap
%doc license.txt
%python3_sitelibdir_noarch/pysimplesoap
%python3_sitelibdir_noarch/%{pypi_name}-%{version}-py%{__python3_version}.egg-info

%changelog
* Fri Sep 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.16.2-alt1
- new version

