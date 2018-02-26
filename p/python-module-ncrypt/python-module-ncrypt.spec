%define oname ncrypt
Name: python-module-ncrypt
Version: 0.6.4
Release: alt1

Summary: Yet another OpenSSL wrapper for python

License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/ncrypt/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/n/ncrypt/%oname-%version.tar

# can't autobuild correct reqs
BuildPreReq: python-devel python-module-Pyrex libssl-devel

%description
Yet another OpenSSL wrapper for python.

%prep
%setup -n %oname-%version
# __new__ method of extension type will change semantics in a future version of Pyrex. Use __cinit__ instead.
%__subst "s|__new__|__cinit__|g" *.pyx

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%oname/
%python_sitelibdir/_%oname.so
%python_sitelibdir/*egg-info/

%changelog
* Wed Jun 13 2012 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- initial build for ALT Linux Sisyphus

