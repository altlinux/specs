# vim: set ft=spec: -*- rpm-spec -*-

Name: ruby-ldap
Version: 0.9.11
Release: alt2

Summary: Ruby LDAP library
Group: Development/Ruby
License: BSD
Url: http://ruby-ldap.sourceforge.net/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

# Automatically added by buildreq on Thu Aug 14 2008 (-bi)
BuildRequires: libldap-devel libruby-devel libssl-devel libsasl2-devel

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
Ruby/LDAP is an extension library for Ruby. It provides the interface
to some LDAP libraries (e.g. OpenLDAP, UMich LDAP, Netscape SDK,
ActiveDirectory). The common API for application development is
described in RFC1823 and is supported by Ruby/LDAP.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup
%patch -p1

%build
%ruby_configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%rdoc *.c lib/

%files
%doc NOTES README FAQ TODO COPYING
%ruby_sitearchdir/*
%ruby_sitelibdir/ldap*

%files doc
%ruby_ri_sitedir/LDAP*

%changelog
* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 0.9.11-alt2
- Repair build

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.9.11-alt1
- [0.9.11]

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 0.9.9-alt1.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Wed Jul 08 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.9-alt1
- [0.9.9]
- Ruby 1.9 compatibility (closes: #20714)

* Wed May 13 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.8-alt1
- [0.9.8]

* Thu Aug 14 2008 Sir Raorn <raorn@altlinux.ru> 0.9.7-alt2
- Rebuilt with rpm-build-ruby

* Mon Dec 03 2007 Sir Raorn <raorn@altlinux.ru> 0.9.7-alt1
- [0.9.7] (closes: #9768)
- Fixed license (SourceForge says "BSD License")
- Added RI documentation
- Updated buildrequires
- Updated requires

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.2-alt1.1.1
- Rebuilt with libldap-2.3.so.0.

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.2-alt1.1
- Rebuilt with openldap-2.2.18-alt3.

* Tue Aug 17 2004 Serge A. Volkov <vserge@altlinux.ru> 0.8.2-alt1
- Update to new version 0.8.2

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.2-alt2.1
- Rebuilt with openssl-0.9.7d.

* Sun Jul 06 2003 Alexander Bokovoy <ab@altlinux.ru> 0.7.2-alt2
- Rebuild against Ruby 1.8.0-alt3

* Tue Nov 19 2002 Serge A. Volkov <vserge@altlinux.ru> 0.7.2-alt1
- Initial packaging for ALT Linux Team

