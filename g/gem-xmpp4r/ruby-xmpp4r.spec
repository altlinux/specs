%define        gemname xmpp4r

Name:          gem-xmpp4r
Version:       0.5.6
Release:       alt2.1
Summary:       XMPP/Jabber library for Ruby
License:       GPLv2
Group:         Development/Ruby
Url:           http://xmpp4r.github.io/
Vcs:           https://github.com/xmpp4r/xmpp4r.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     xmpp4r
Obsoletes:     ruby-xmpp4r < %EVR
Provides:      ruby-xmpp4r = %EVR
Provides:      gem(xmpp4r) = 0.5.6


%description
XMPP4R is an XMPP/Jabber library for Ruby. Its goal is to provide a complete
framework to develop Jabber-related applications or scripts in Ruby.

* Fully object-oriented * Aims at being XMPP compliant * Threaded, events-based
* Well unit-tested and documented code * Uses well-known and well-tested
software like REXML, instead of reinventing the wheel * Very easy to extend


%package       -n gem-xmpp4r-doc
Version:       0.5.6
Release:       alt2.1
Summary:       XMPP/Jabber library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета xmpp4r
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(xmpp4r) = 0.5.6

%description   -n gem-xmpp4r-doc
XMPP/Jabber library for Ruby documentation files.

XMPP4R is an XMPP/Jabber library for Ruby. Its goal is to provide a complete
framework to develop Jabber-related applications or scripts in Ruby.

* Fully object-oriented * Aims at being XMPP compliant * Threaded,
events-based
* Well unit-tested and documented code * Uses well-known and well-tested
software like REXML, instead of reinventing the wheel * Very easy to extend

%description   -n gem-xmpp4r-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета xmpp4r.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-xmpp4r-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.6-alt2.1
- ! spec
- * policify names

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.6-alt2
- Use Ruby Policy 2.0

* Thu Jul 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.6-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5-alt2.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.5-alt2.2
- Rebuild with Ruby 2.4.1
- Disable tests

* Fri Nov 30 2012 Led <led@altlinux.ru> 0.5-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Jun 11 2011 Michael Shigorin <mike@altlinux.org> 0.5-alt2
- fixed build by dropping failing tests
- spec tags rearranged a bit (see ALT Packaging HOWTO)

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5-alt1
- [0.5]

* Mon Sep 01 2008 Sir Raorn <raorn@altlinux.ru> 0.4-alt1
- 0.4

* Thu Jul 20 2006 Sir Raorn <raorn@altlinux.ru> 0.3-alt1
- [0.3]

* Wed Jul 12 2006 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Built for Sisyphus
