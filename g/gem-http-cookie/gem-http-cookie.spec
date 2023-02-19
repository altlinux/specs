%define        gemname http-cookie

Name:          gem-http-cookie
Version:       1.0.5
Release:       alt1
Summary:       A Ruby library to handle HTTP cookies in a way both compliant with RFCs
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sparklemotion/http-cookie
Vcs:           https://github.com/sparklemotion/http-cookie.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(sqlite3) >= 1.3
BuildRequires: gem(bundler) >= 1.2.0
BuildRequires: gem(test-unit) >= 2.4.3
BuildRequires: gem(rake) >= 0.9.2.2
BuildRequires: gem(rdoc) > 2.4.2
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(domain_name) >= 0.5
BuildConflicts: gem(sqlite3) >= 2
BuildConflicts: gem(domain_name) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names rails
Requires:      gem(domain_name) >= 0.5
Conflicts:     gem(domain_name) >= 1
Obsoletes:     ruby-http-cookie < %EVR
Provides:      ruby-http-cookie = %EVR
Provides:      gem(http-cookie) = 1.0.5


%description
A Ruby library to handle HTTP cookies in a way both compliant with RFCs and
compatible with today's major browsers


%package       -n gem-http-cookie-doc
Version:       1.0.5
Release:       alt1
Summary:       A Ruby library to handle HTTP cookies in a way both compliant with RFCs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета http-cookie
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(http-cookie) = 1.0.5

%description   -n gem-http-cookie-doc
A Ruby library to handle HTTP cookies in a way both compliant with RFCs
documentation files.

A Ruby library to handle HTTP cookies in a way both compliant with RFCs and
compatible with today's major browsers

%description   -n gem-http-cookie-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета http-cookie.


%package       -n gem-http-cookie-devel
Version:       1.0.5
Release:       alt1
Summary:       A Ruby library to handle HTTP cookies in a way both compliant with RFCs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета http-cookie
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(http-cookie) = 1.0.5
Requires:      gem(sqlite3) >= 1.3
Requires:      gem(bundler) >= 1.2.0
Requires:      gem(test-unit) >= 2.4.3
Requires:      gem(rake) >= 0.9.2.2
Requires:      gem(rdoc) > 2.4.2
Requires:      gem(simplecov) >= 0
Conflicts:     gem(sqlite3) >= 2

%description   -n gem-http-cookie-devel
A Ruby library to handle HTTP cookies in a way both compliant with RFCs
development package.

A Ruby library to handle HTTP cookies in a way both compliant with RFCs and
compatible with today's major browsers

%description   -n gem-http-cookie-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета http-cookie.


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

%files         -n gem-http-cookie-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-http-cookie-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- ^ 1.0.4 -> 1.0.5

* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt0.1
- > Ruby Policy 2.0
- ^ 1.0.3 -> 1.0.4pre
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
