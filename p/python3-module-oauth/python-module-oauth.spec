%define oname oauth

Name: python3-module-oauth
Version: 1.0.1
Release: alt2

Summary: Library for OAuth version 1.0a
Group: Development/Python3
License: MIT
Url: http://code.google.com/p/oauth/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
%summary

%prep
%setup -q

sed -i 's|import urlparse|import urllib.parse as urlparse|' \
    %oname/oauth.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/oauth*
%doc LICENSE.txt


%changelog
* Thu Jan 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt2
- porting on python3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.1-alt1
- initial build

