Name: python-module-jcl
Version: 0.1
Release: alt1.1.1

%setup_python_module jcl

Summary: Jabber component library
License: LGPL
Group: Development/Python
Url: http://people.happycoders.org/dax/projects/jcl
Packager: Sergey Bolshakov <sbolshakov@altlinux.ru>

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

Requires: python-module-SQLObject >= 0.8

%description
JCL aims to create a common base for Jabber server components.
It handle account registration and propose different component behaviors to inherit from.

%prep
%setup

%build
%__python setup.py build

%install
%__python setup.py install \
    --root=%buildroot \
    --optimize=2 \
    --record=INSTALLED_FILES

# we have rpm for that, btw
sed -i '/egg-info/d' INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with python 2.6

* Thu Jul 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
