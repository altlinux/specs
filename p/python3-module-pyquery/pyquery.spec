Name: python3-module-pyquery
Version: 1.4.1.0.5.49eb
Release: alt1
Summary: A jQuery-like library for python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.io/project/pyquery/
Packager: ALT python <python@packages.altlinux.org>

# git://git.altlinux.org/gears/p/python3-module-pyquery.git
Source: %name-%version-%release.tar
BuildArch: noarch

# Automatically added by buildreq on Sun Aug 16 2020 (-bi)
# optimized out: python3 python3-base python3-dev python3-module-BeautifulSoup4 python3-module-chardet python3-module-cssselect python3-module-html5lib python3-module-idna python3-module-lxml python3-module-pkg_resources python3-module-six python3-module-urllib3 python3-module-waitress python3-module-webencodings python3-module-webob rpm-build-python3
BuildRequires: python3-module-nose python3-module-requests python3-module-setuptools python3-module-webtest

%description
%name allows you to make jQuery queries on XML documents.  The API is as much
as possible the similar to jQuery.  %name uses lxml for fast XML and HTML
manipulation.

%prep
%setup -n %name-%version-%release

%build
%python3_build

%install
%python3_install

%check
nosetests-3 -v

%files
%python3_sitelibdir/pyquery*
%doc *.rst

%changelog
* Sun Aug 16 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.1.0.5.49eb-alt1
- Packaged pyquery-1.4.1-5-g49ebccf.
