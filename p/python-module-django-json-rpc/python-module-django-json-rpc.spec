%define module_name django-json-rpc

%define git_commit 699856
Name: python-module-%module_name
Version: 0.6.2
Release: alt1.git%git_commit.1

Summary: Simple Reference JSON-RPC Implementation for Django

License: MIT
Group: Development/Python
Url: http://github.com/samuraisam/django-json-rpc
Packager: Denis Klimov <zver@altlinux.org>

# https://github.com/samuraisam/django-json-rpc.git
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name


%description
Simple Reference JSON-RPC Implementation for Django

%prep
%setup
find . -name \*.py -print0|xargs -0 sed -i -e 's/from jsonrpc/from django_jsonrpc/'
sed -i -e 's/from jsonrpc/from django_jsonrpc/' README.mdown
sed -i -e "s/packages=\['jsonrpc'\]/packages=['django_jsonrpc']/" setup.py
sed -i -e "s/package_data={'jsonrpc'/package_data={'django_jsonrpc'/" setup.py
mv jsonrpc django_jsonrpc

%build
%python_build

%install
%python_install

%files
%doc README.ALT
%python_sitelibdir/django_jsonrpc*
%python_sitelibdir/django_json_rpc*


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.git699856.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git699856
- Version 0.6.2

* Tue Feb 23 2010 Denis Klimov <zver@altlinux.org> 0.5.1-alt3.git3052f3
- fix gears inheritance check

* Tue Feb 23 2010 Denis Klimov <zver@altlinux.org> 0.5.1-alt2.git3052f3
- modify files section

* Mon Feb 22 2010 Denis Klimov <zver@altlinux.org> 0.5.1-alt1.git3052f3
- new version
- jsonrpc module renamed to django_jsonrpc

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3.gita815e3.1
- Rebuilt with python 2.6

* Thu Nov 19 2009 Denis Klimov <zver@altlinux.org> 0.2-alt3.gita815e3
- new version
- use build and install python macros

* Tue Nov 10 2009 Denis Klimov <zver@altlinux.org> 0.2-alt2.git30fad1
- new version

* Sun Nov 08 2009 Denis Klimov <zver@altlinux.org> 0.2-alt1.gite9c07b
- Initial build for ALT Linux

