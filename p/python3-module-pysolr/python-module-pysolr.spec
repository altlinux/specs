%define oname pysolr

Name: python3-module-%oname
Version: 3.8.1
Release: alt1

Summary: Lightweight python wrapper for Apache Solr
License: BSD-2-Clause
Group: Development/Python3
Url: http://github.com/toastdriven/pysolr/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm


%description
pysolr is a lightweight Python wrapper for Apache Solr. It provides an
interface that queries the server and returns results based on the query.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/*


%changelog
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.8.1-alt1
- Version updated to 3.8.1
- porting on python3.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1.qa1
- NMU: applied repocop patch

* Thu Oct 22 2015 Lenar Shakirov <snejok@altlinux.ru> 3.1.0-alt1
- First build for ALT (based on OpenSUSE 3.1.0-2.1.src)
