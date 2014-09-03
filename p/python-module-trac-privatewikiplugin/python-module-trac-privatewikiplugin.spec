%define tarname privatewikiplugin
Name: python-module-trac-privatewikiplugin
%define r_minor r13400
Version: 1.0.0
Release: alt1.%r_minor

Summary: Allows you to protect wiki pages against access.

Group: Development/Python
License: BSD
Url: http://trac-hacks.org/wiki/privatewikiplugin

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
Allows you to protect wiki pages against access

%prep
%setup -n %tarname

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.r13400
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.r7916.1
- Rebuild with Python-2.7

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1.r7916
- Build for ALT
