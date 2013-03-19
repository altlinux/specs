# vim: set ft=spec: -*- rpm-spec -*-

%define modulename dnspython

# Testing requires network access
%def_without check

Name: python-module-%modulename
Version: 1.10.0
Release: alt1

%setup_python_module %modulename

Summary: DNS toolkit for Python
License: %bsdstyle
Group: Development/Python

Url: http://www.dnspython.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

# git://github.com/rthalley/dnspython.git
Source: %name-%version.tar

BuildPreReq: rpm-build-licenses
BuildPreReq: python-module-distribute
BuildPreReq: python-module-epydoc

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic updates.
It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high level
classes perform queries for data of a given name, type, and class,
and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%prep
%setup

%build
%python_build
%make_build doc

%install
%python_install

%if_with check
%check
pushd tests
%make PYTHONPATH="../:$PYTHONPATH" check
popd
%endif

%files
%doc ChangeLog LICENSE README examples/ html/
%python_sitelibdir/*

%changelog
* Tue Mar 19 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.0-alt1
- Initial build for ALT Linux Sisyphus
