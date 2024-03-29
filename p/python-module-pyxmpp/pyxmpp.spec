Version: 1.1.2
Release: alt1.3
%setup_python_module pyxmpp
Name: %packagename
Summary: XMPP-IM-compliant library for jabber instant messenging
Source0: http://pyxmpp.jajcus.net/downloads/snapshots/%modulename-%version.tar.gz
License: LGPL
Group: Development/Python
Prefix: %prefix
#BuildArchitectures: noarch
Url: http://pyxmpp.jajcus.net
Packager: Fr. Br. George <george@altlinux.ru>

%add_python_req_skip kerberos

BuildRequires(pre): rpm-macros-make

# Automatically added by buildreq on Sat Jul 29 2006
BuildRequires: libxml2-devel python-module-dns python-modules-libxml2

Requires: python-module-dns python-modules-libxml2

%description
PyXMPP is a Python XMPP (RFC 3920,3921) and Jabber implementation. It is
based on libxml2 -- fast and fully-featured XML parser.

PyXMPP provides most core features of the XMPP protocol and several
JSF-defined extensions. PyXMPP provides building blocks for creating
Jabber clients and components. Developer uses them to setup XMPP
streams, handle incoming events and create outgoing stanzas (XMPP
"packets").

%prep
%setup -n %modulename-%version

# Set correct python2 executable in shebang and scripts
subst 's|#!.*python$|#!%__python|' $(grep -Rl '#!.*python$' *) \
        $(find ./ -name '*.py')
subst 's|#!.*python -u|#!%__python -u|' $(grep -Rl '#!.*python -u' *) \
        $(find ./ -name '*.py')
subst 's|python |%__python |' $(find ./ -name 'Makefile')


%build
%make_ext build

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT/

%check
%make test

%files
%python_sitelibdir/%modulename
%python_sitelibdir/*.egg-info

%changelog
* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1.3
- Fixed BuildRequires.

* Thu Aug 13 2020 Pavel Vasenkov <pav@altlinux.org> 1.1.2-alt1.2
- NMU: set correct python2 executable in shebang and script

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1.1
- Rebuild with Python-2.7

* Fri May 20 2011 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.1
- Rebuilt for debuginfo

* Mon Jul 05 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Version up
- Add examples to documentatiln

* Sun Apr 11 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Version up

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6
- Rebuilt with python 2.6

* Mon Nov 03 2008 Fr. Br. George <george@altlinux.ru> 1.0.0-alt5
- Kerberos req removed

* Sat Nov 01 2008 Fr. Br. George <george@altlinux.ru> 1.0.0-alt4
- Version up to 1.0.0.s20080822

* Sat May 17 2008 Fr. Br. George <george@altlinux.ru> 1.0.0-alt3
- Version up to 1.0.0.s20080507

* Wed Dec 27 2006 Fr. Br. George <george@altlinux.ru> 1.0.0-alt2
- x86_64 fix: %python_sitelibdir is used

* Sat Jul 29 2006 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial ALT build

