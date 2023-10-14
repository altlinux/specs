BuildRequires(pre): rpm-build-python3
%global pypi_name PySimpleSOAP

Name:          python3-module-pysimplesoap
Version:       1.16.2
Release:       alt2
Summary:       Python simple and lightweight SOAP Library
Group:         Development/Python
License:       LGPLv3+
URL:           https://github.com/pysimplesoap/pysimplesoap
Source0:       %name-%version.tar
Source1:       https://raw.githubusercontent.com/pysimplesoap/pysimplesoap/master/license.txt
Patch:         python-pysimplesoap-1.16.2-cStringIO.patch
Patch1:        drop-distutils.patch
BuildArch:     noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-packaging

%description
Python simple and lightweight SOAP library for client and
server web services interfaces, aimed to be as small and easy
as possible, supporting most common functionality.

%prep
%setup -q
%patch -p1
%patch1 -p0

for lib in pysimplesoap/*.py; do
 sed -e '1{\@^#! /usr/bin/env python@d}' -e '1{\@^#!/usr/bin/env python@d}' \
     -e '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
cp -p %{SOURCE1} .

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-pysimplesoap
%doc license.txt
%python3_sitelibdir_noarch/pysimplesoap
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info

%changelog
* Sat Oct 14 2023 Anton Vyatkin <toni@altlinux.org> 1.16.2-alt2
- Dropped dependency on distutils.

* Fri Sep 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.16.2-alt1
- new version

