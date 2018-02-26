%define tarname tracwysiwygplugin
Name: python-module-trac-wysiwygplugin
%define r_minor r7916
Version: 0.2
Release: alt1.%r_minor.1

Summary: Wysiwyg editor embedded into textarea.wikitext

Group: Development/Python
# FIXME: unknown?
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/tracwysiwygplugin

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
Wysiwyg editor embedded into textarea.wikitext

%prep
%setup -q -n %tarname/0.11

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

chmod -R a+r %buildroot%python_sitelibdir/tracwysiwyg

%files
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.r7916.1
- Rebuild with Python-2.7

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1.r7916
- Build for ALT
