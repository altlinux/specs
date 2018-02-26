Name: python-module-krbV
Version: 1.0.13
Release: alt1.1.1
Summary: Python extension module for Kerberos 5

Group: System/Libraries
License: LGPLv2

URL: http://people.redhat.com/mikeb/python-krbV
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
Source: python-module-krbV-%version.tar.bz2

BuildRequires: python-devel
BuildRequires: libkrb5-devel >= 1.2.2
BuildRequires: /bin/awk

%description
python-krbV allows python programs to use Kerberos 5 authentication/security.

%prep
%setup -q

%build
export LIBNAME="%_lib"
export CFLAGS="%optflags -Wextra"
%configure
make %{?_smp_mflags}

%install
%makeinstall
rm -f %buildroot/%python_sitelibdir/*.la

%files
%doc README COPYING krbV-code-snippets.py
%python_sitelibdir/krbVmodule.so

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.13-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.13-alt1.1
- Rebuilt with python 2.6

* Thu May 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 1.0.13-alt1
- Build for Sisyphus

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.13-8
- Rebuild for Python 2.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.13-7
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Mike Bonnet <mikeb@redhat.com> - 1.0.13-6
- rebuild for F8

* Mon Dec 11 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-5
- rebuild for python 2.5
- remove obsolete python-abi Requires:

* Wed Sep 13 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-4
- support building against krb5-1.5, where the headers have been moved to /usr/include/krb5

* Mon Sep 11 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-3
- rebuild for FC6

* Sun May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-2
- spec file cleanup

* Wed May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-1
- AuthContext.addrs can now be set manually, rather than calling genaddrs()

* Sun May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-3
- use macros consistently

* Thu Apr 27 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-2
- configure.in: parse version number out of spec file
- add URL tag
- add LGPL text
- remove Requires: krb5-libs, let rpm pick up library dependencies
- bump revision

* Mon Apr 24 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-1
- bump version number due to API changes

* Fri Mar 24 2006 Mike Bonnet <mikeb@redhat.com>
- fix typo in error definition
- change the return value of recvauth() from ac to (ac, princ), where princ is the principal sent by sendauth()
- rename the package and reorganize the BuildRequires, to be more Extras-friendly

* Tue Sep 25 2001 Elliot Lee <sopwith@redhat.com>
- Initial version
