Name: python-module-cmemcache
Version: 0.95
Release: alt0.2

Summary: A python module for memcached daemon
Group: System/Servers
License: GPL2+
Url: http://gijsbert.org/cmemcache/index.html
Packager: Alexey Morsov <swi@altlinux.ru>

Source: %name-%version.tar

BuildRequires: python-devel python-modules-encodings libmemcache-devel >= 1.4.0rc2
BuildRequires: rpm-build-python >= 0.21-alt1 

%description
Python extension for libmemcache, the C API to memcached. cmemcache 
API is the same as python-memcache, so it is easy to replace 
python-memcache with cmemcache, and vice versa.

cmemcache is about 1.7 times faster than python-memcache 
with short key names (8 characters), faster with larger key names 
(I get about 2x for 100 character keys). Using get_multi is 
faster still, almost 2x for 2 8-character keys. See cachecmp.py 
for profiling logic.

%prep
%setup -q 

%build
%python_build

%install
python setup.py install --root=%buildroot \
			--optimize=2 \
			--record=INSTALLED_FILES


%files -f INSTALLED_FILES

%changelog
* Tue Dec 20 2011 Alexey Morsov <swi@altlinux.ru> 0.95-alt0.2
- fix build

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.95-alt0.1.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt0.1.1
- Rebuilt with python 2.6

* Thu Sep 05 2008 Alexey Morsov <swi@altlinux.ru> 0.95-alt0.1
- initial build


