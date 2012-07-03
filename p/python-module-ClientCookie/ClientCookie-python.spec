Name: python-module-ClientCookie
Version: 1.0.2
Release: alt0.1.1.1.1.1.1

Summary: Python module for handling HTTP cookies on the client side
Source0: ClientCookie-%version.tar.gz
License: BSD
Group: Development/Python
Requires: python
Packager: Andrey Khavryuchenko <akhavr@altlinux.ru>
Url: http://wwwsearch.sourceforge.net/ClientCookie
BuildRequires: python-devel
Provides: python-ClientCookie
Obsoletes: python-ClientCookie
BuildArch: noarch

%description
ClientCookie is a Python module for handling HTTP cookies on the
client side, useful for accessing web sites that require cookies to be
set and then returned later. It also provides some other (optional)
useful stuff: HTTP-EQUIV and Refresh handling, automatic adding of the
Referer [sic] header and lazily-seek()able responses. These extras are
implemented using an extension that makes it easier to add new
functionality to urllib2. It has developed from a port of Gisle Aas'
Perl module HTTP::Cookies, from the [4]libwww-perl library.

%prep
%setup -n ClientCookie-%version -q

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README.html README.txt doc.html ChangeLog COPYING

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt0.1.1.1.1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt0.1.1.1.1.1
- Rebuilt with python 2.6
- Built as noarch

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.0.2-alt0.1.1.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt0.1.1.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt0.1.1
- Rebuilt with python-2.4.

* Wed Jan 26 2005 Andrey Khavryuchenko <akhavr@altlinux.ru> 1.0.2-alt0.1
- Updated to 1.0.2

* Sat Aug 7 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.19-alt0.1
- Updated to 0.4.19

* Tue Jan 6 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.18-alt0.1
- Updated to 0.4.18

* Tue Dec 30 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.14-alt0.1
- Updated to 0.4.14

* Wed Dec 17 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.11-alt0.1
- Updated to 0.4.11
- Updated to python 2.3

* Sun Dec 7 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.10-alt0.1
- Updated to 0.4.10

* Wed Nov 5 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.9-alt0.1
- Updated to 0.4.9

* Mon Sep 29 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.5a-alt0.1
  Initial build
