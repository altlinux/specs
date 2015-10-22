Name: python-module-pysolr
Version: 3.1.0
Release: alt1
Url: http://github.com/toastdriven/pysolr/
Summary: Lightweight python wrapper for Apache Solr
License: BSD-2-Clause
Group: Development/Python

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python python-dev

%description
pysolr is a lightweight Python wrapper for Apache Solr. It provides an
interface that queries the server and returns results based on the query.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc LICENSE README.rst
%python_sitelibdir/*

%changelog
* Thu Oct 22 2015 Lenar Shakirov <snejok@altlinux.ru> 3.1.0-alt1
- First build for ALT (based on OpenSUSE 3.1.0-2.1.src)
