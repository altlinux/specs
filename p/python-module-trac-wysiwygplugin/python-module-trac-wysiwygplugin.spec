%define tarname tracwysiwygplugin
Name: python-module-trac-wysiwygplugin
%define r_minor r13457
Version: 0.12.0.5
Release: alt1.%r_minor

Summary: Wysiwyg editor embedded into textarea.wikitext

Group: Development/Python
# FIXME: unknown?
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/tracwysiwygplugin

# http://trac-hacks.org/svn/tracwysiwygplugin/0.12/
Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
Wysiwyg editor embedded into textarea.wikitext

%prep
%setup -n %tarname

%build
%python_build

%install
%python_install

chmod -R a+r %buildroot%python_sitelibdir/tracwysiwyg

%files
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0.5-alt1.r13457
- Version 0.12.0.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.r7916.1
- Rebuild with Python-2.7

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1.r7916
- Build for ALT
