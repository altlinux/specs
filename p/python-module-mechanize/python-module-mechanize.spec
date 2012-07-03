%define oname mechanize
Name: python-module-%oname
Version: 0.1.11
Release: alt1.1

Summary: Stateful programmatic web browsing

License: BSD / ZPL
Group: Development/Other
Url: http://wwwsearch.sourceforge.net/mechanize/

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname

Source: http://wwwsearch.sourceforge.net/mechanize/src/%oname-%version.tar.bz2

BuildArch: noarch

BuildPreReq: rpm-build-compat >= 1.2

# manually removed: all
BuildRequires: python-module-setuptools

%description
Stateful programmatic web browsing in Python,
after Andy Lester's Perl module WWW::Mechanize.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc COPYING.txt ChangeLog.txt GeneralFAQ.html README.html doc.html examples/
%python_sitelibdir/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.11-alt1.1
- Rebuild with Python-2.7

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.11-alt1
- new version 0.1.11 (with rpmrb script)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt3
- Rebuilt with python 2.6

* Thu Feb 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt2
- build as noarch

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt1
- new version 0.1.10 (with rpmrb script)

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.7b-alt1
- initial build for ALT Linux Sisyphus

