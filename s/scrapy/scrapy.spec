Name: scrapy
Version: 2.11.1
Release: alt1

Summary: Scrapy, a fast high-level web crawling & scraping framework for Python.
License: BSD3
Group: Development/Python
Url: https://scrapy.org/

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel zlib-devel libxml2-devel libxslt-devel libssl-devel libffi-devel

%description
Scrapy is a BSD-licensed fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

%package -n python3-module-%name
Group:  Development/Python
Summary: Python3 module for scrapy
%description -n python3-module-%name
module for developing web crawlers used by scrapy

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/scrapy

%files -n python3-module-%name
%python3_sitelibdir/scrapy
%python3_sitelibdir/Scrapy-%version.dist-info

%changelog
* Mon Mar 04 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.11.1-alt1
- update version

* Fri Nov 24 2023 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.11.0-alt1
- Initial build for ALT Linux
