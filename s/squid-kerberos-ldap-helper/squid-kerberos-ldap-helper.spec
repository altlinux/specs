Summary: Squid proxy server plugin for the SASL/GSSAPI authentication to an ldap server
Name: squid-kerberos-ldap-helper
Version: 1.2.2
Release: alt1.1
License: GPLv2
Group: System/Servers
URL: http://squidkerbauth.sourceforge.net/
Packager: Paul Wolneykien <manowar@altlinux.ru>

Source0: %{name}-%{version}.tar.gz
#Patch0: support_resolv.format.patch
Patch1: fix-kerb-nolib-rpath.patch
Patch2: squid-kerberos-ldap-helper-1.2.2-alt-DSO.patch

# Automatically added by buildreq on Tue Apr 28 2009
BuildRequires: libkrb5-devel libldap-devel rpm-macros-alterator rpm-macros-fillup

%description
Squid-Kerberos-LDAP helper is a reference implementation that supports
SASL/GSSAPI authentication to an ldap server. It is mainly intended
to connect to Active Directory or Openldap based ldap servers.

%prep
%setup -q
#%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
autoreconf -fi
%configure CPPFLAGS=-I%_includedir/krb5
%make_build CPPFLAGS=-I%_includedir/krb5

%install
%make_install install \
	prefix=%buildroot%_prefix \
	bindir=%buildroot%_libdir/squid

install -D -m 644 README %buildroot%_docdir/%name-%version/README

%files
%_libdir/squid/*
%_docdir/%name-%version/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/squid-kerberos-ldap-helper-%version 

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.1
- Fixed build

* Sat Jan 07 2012 Paul Wolneykien <manowar@altlinux.ru> 1.2.2-alt1
- New upstream version 1.2.2.
- Fix "no/lib" library path for Kerberos libs.
- Disable the support-resolve patch (fixed in upstream).

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.2-alt4.1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for squid-kerberos-ldap-helper
  * postclean-05-filetriggers for spec file

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 1.1.2-alt4.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Tue Jan 28 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1.2-alt4
- Initial release for ALT Linux.
