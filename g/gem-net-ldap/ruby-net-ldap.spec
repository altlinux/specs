# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname net-ldap

Name:          gem-%pkgname
Epoch:         1
Version:       0.17.0
Release:       alt1
Summary:       Pure Ruby LDAP library
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/ruby-ldap/ruby-net-ldap
Vcs:           https://github.com/ruby-ldap/ruby-net-ldap.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Net::LDAP for Ruby (also called net-ldap) implements client access for
the Lightweight Directory Access Protocol (LDAP), an IETF standard protocol
for accessing distributed directory services. Net::LDAP is written completely
in Ruby with no external dependencies. It supports most LDAP client features
and a subset of server features as well.

Net::LDAP has been tested against modern popular LDAP servers including
OpenLDAP and Active Directory. The current release is mostly compliant with
earlier versions of the IETF LDAP RFCs (2251-2256, 2829-2830, 3377, and 3771).
Our roadmap for Net::LDAP 1.0 is to gain full client compliance with the most
recent LDAP RFCs (4510-4519, plus portions of 4520-4532).


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.17.0-alt1
- > Ruby Policy 2.0
- ^ 0.16.1 -> 0.17.0
- * fixname

* Thu Jul 19 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.16.1-alt1
- New version.
- Disable tests.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 21 2014 Led <led@altlinux.ru> 1.1.0-alt1.2
- fixed tests

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Sep 13 2010 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt1
- Built for Sisyphus

