# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname mechanize

Name:          gem-mechanize
Version:       2.8.5
Release:       alt1
Summary:       WWW::Mechanize, a handy web browsing ruby object
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sparklemotion/mechanize
Vcs:           https://github.com/sparklemotion/mechanize.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.14
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(rubocop) >= 1.12
BuildRequires: gem(addressable) >= 2.8
BuildRequires: gem(domain_name) >= 0.5.20190701
BuildRequires: gem(http-cookie) >= 1.0.3
BuildRequires: gem(mime-types) >= 3.0
BuildRequires: gem(net-http-digest_auth) >= 1.4.1
BuildRequires: gem(net-http-persistent) >= 2.5.2
BuildRequires: gem(nokogiri) >= 1.11.2
BuildRequires: gem(rubyntlm) >= 0.6.3
BuildRequires: gem(webrick) >= 1.7
BuildRequires: gem(webrobots) >= 0.1.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(domain_name) >= 1
BuildConflicts: gem(http-cookie) >= 2
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(net-http-digest_auth) >= 2
BuildConflicts: gem(net-http-persistent) >= 5.0
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rubyntlm) >= 1
BuildConflicts: gem(webrick) >= 2
BuildConflicts: gem(webrobots) >= 0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Requires:      gem(addressable) >= 2.8
Requires:      gem(domain_name) >= 0.5.20190701
Requires:      gem(http-cookie) >= 1.0.3
Requires:      gem(mime-types) >= 3.0
Requires:      gem(net-http-digest_auth) >= 1.4.1
Requires:      gem(net-http-persistent) >= 2.5.2
Requires:      gem(nokogiri) >= 1.11.2
Requires:      gem(rubyntlm) >= 0.6.3
Requires:      gem(webrick) >= 1.7
Requires:      gem(webrobots) >= 0.1.2
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(domain_name) >= 1
Conflicts:     gem(http-cookie) >= 2
Conflicts:     gem(mime-types) >= 4
Conflicts:     gem(net-http-digest_auth) >= 2
Conflicts:     gem(net-http-persistent) >= 5.0
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rubyntlm) >= 1
Conflicts:     gem(webrick) >= 2
Conflicts:     gem(webrobots) >= 0.2
Obsoletes:     ruby-mechanize < %EVR
Provides:      ruby-mechanize = %EVR
Provides:      gem(mechanize) = 2.8.5


%description
The Mechanize library is used for automating interaction with websites.
Mechanize automatically stores and sends cookies, follows redirects, can follow
links, and submit forms. Form fields can be populated and submitted. Mechanize
also keeps track of the sites that you have visited as a history.


%package       -n gem-mechanize-doc
Version:       2.8.5
Release:       alt1
Summary:       WWW::Mechanize, a handy web browsing ruby object documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mechanize
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mechanize) = 2.8.5

%description   -n gem-mechanize-doc
WWW::Mechanize, a handy web browsing ruby object documentation files.

The Mechanize library is used for automating interaction with websites.
Mechanize automatically stores and sends cookies, follows redirects, can follow
links, and submit forms. Form fields can be populated and submitted. Mechanize
also keeps track of the sites that you have visited as a history.

%description   -n gem-mechanize-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mechanize.


%package       -n gem-mechanize-devel
Version:       2.8.5
Release:       alt1
Summary:       WWW::Mechanize, a handy web browsing ruby object development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mechanize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mechanize) = 2.8.5
Requires:      gem(minitest) >= 5.14
Requires:      gem(rake) >= 13.0
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(rubocop) >= 1.12
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(rubocop) >= 2

%description   -n gem-mechanize-devel
WWW::Mechanize, a handy web browsing ruby object development package.

The Mechanize library is used for automating interaction with websites.
Mechanize automatically stores and sends cookies, follows redirects, can follow
links, and submit forms. Form fields can be populated and submitted. Mechanize
also keeps track of the sites that you have visited as a history.

%description   -n gem-mechanize-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mechanize.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-mechanize-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mechanize-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.8.5-alt1
- ^ 2.7.7 -> 2.8.5

* Thu Apr 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.7-alt0.1
- ^ 2.7.6 -> 2.7.7pre
- ! spec tags

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1
- > Ruby Policy 2.0
- ^ 0.9.3 -> 2.7.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1.4
- Rebuild with new Ruby autorequirements.

* Sat Mar 15 2014 Led <led@altlinux.ru> 0.9.3-alt1.3
- fixed encoding without iconv

* Sat Mar 15 2014 Led <led@altlinux.ru> 0.9.3-alt1.2
- don't use iconv for ruby >= 1.9.2

* Fri Dec 07 2012 Led <led@altlinux.ru> 0.9.3-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 11 2009 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt1
- build for Sisyphus
