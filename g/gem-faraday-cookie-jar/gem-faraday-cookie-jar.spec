%define        gemname faraday-cookie_jar

Name:          gem-faraday-cookie-jar
Version:       0.0.7
Release:       alt1.1
Summary:       Cookie jar middleware for Faraday
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/miyagawa/faraday-cookie_jar
Vcs:           https://github.com/miyagawa/faraday-cookie_jar.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(sham_rack) >= 0
BuildRequires: gem(faraday) >= 0.8.0
BuildRequires: gem(http-cookie) >= 1.0.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(http-cookie) >= 1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_alias_names faraday-cookie_jar,faraday-cookie-jar
Requires:      gem(faraday) >= 0.8.0
Requires:      gem(http-cookie) >= 1.0.0
Conflicts:     gem(http-cookie) >= 1.1
Provides:      gem(faraday-cookie_jar) = 0.0.7


%description
This gem is a piece of Faraday middleware that adds client-side Cookies
management, using http-cookie gem.


%package       -n gem-faraday-cookie-jar-doc
Version:       0.0.7
Release:       alt1.1
Summary:       Cookie jar middleware for Faraday documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-cookie_jar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-cookie_jar) = 0.0.7

%description   -n gem-faraday-cookie-jar-doc
Cookie jar middleware for Faraday documentation files.

This gem is a piece of Faraday middleware that adds client-side Cookies
management, using http-cookie gem.

%description   -n gem-faraday-cookie-jar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-cookie_jar.


%package       -n gem-faraday-cookie-jar-devel
Version:       0.0.7
Release:       alt1.1
Summary:       Cookie jar middleware for Faraday development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-cookie_jar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-cookie_jar) = 0.0.7
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.2
Requires:      gem(sinatra) >= 0
Requires:      gem(sham_rack) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-faraday-cookie-jar-devel
Cookie jar middleware for Faraday development package.

This gem is a piece of Faraday middleware that adds client-side Cookies
management, using http-cookie gem.

%description   -n gem-faraday-cookie-jar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-cookie_jar.


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

%files         -n gem-faraday-cookie-jar-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-cookie-jar-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.7-alt1.1
- ! closes build deps under check condition

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.7-alt1
- ^ 0.0.6 -> 0.0.7

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.6-alt1.1
- ! spec according to changelog rules

* Tue Aug 13 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.6-alt1
- + packaged gem with usage Ruby Policy 2.0
