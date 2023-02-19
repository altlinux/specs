%define        gemname fuzzyurl

Name:          gem-fuzzyurl
Version:       0.9.0
Release:       alt3.1
Summary:       A Ruby Gem for non-strict parsing, manipulation, and wildcard matching of URLs
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gamache/fuzzyurl.rb
Vcs:           https://github.com/gamache/fuzzyurl.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(minitest) >= 4.7.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Obsoletes:     ruby-fuzzyurl < %EVR
Provides:      ruby-fuzzyurl = %EVR
Provides:      gem(fuzzyurl) = 0.9.0


%description
Fuzzyurl provides two related functions: non-strict parsing of URLs or URL-like
strings into their component pieces (protocol, username, password, hostname,
port, path, query, and fragment), and fuzzy matching of URLs and URL patterns.


%package       -n gem-fuzzyurl-doc
Version:       0.9.0
Release:       alt3.1
Summary:       A Ruby Gem for non-strict parsing, manipulation, and wildcard matching of URLs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fuzzyurl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fuzzyurl) = 0.9.0

%description   -n gem-fuzzyurl-doc
A Ruby Gem for non-strict parsing, manipulation, and wildcard matching of URLs
documentation files.

Fuzzyurl provides two related functions: non-strict parsing of URLs or URL-like
strings into their component pieces (protocol, username, password, hostname,
port, path, query, and fragment), and fuzzy matching of URLs and URL patterns.

%description   -n gem-fuzzyurl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fuzzyurl.


%package       -n gem-fuzzyurl-devel
Version:       0.9.0
Release:       alt3.1
Summary:       A Ruby Gem for non-strict parsing, manipulation, and wildcard matching of URLs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fuzzyurl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fuzzyurl) = 0.9.0
Requires:      gem(rake) >= 10.0
Requires:      gem(minitest) >= 4.7.0
Requires:      gem(mocha) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6

%description   -n gem-fuzzyurl-devel
A Ruby Gem for non-strict parsing, manipulation, and wildcard matching of URLs
development package.

Fuzzyurl provides two related functions: non-strict parsing of URLs or URL-like
strings into their component pieces (protocol, username, password, hostname,
port, path, query, and fragment), and fuzzy matching of URLs and URL patterns.

%description   -n gem-fuzzyurl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fuzzyurl.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-fuzzyurl-doc
%ruby_gemdocdir

%files         -n gem-fuzzyurl-devel


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt3.1
- ! close build deps under check condition

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt3
- ! spec

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt2.1
- Rebuild for new Ruby autorequirements.

* Wed Jul 04 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.9.0-alt2
- Tests disabled because "coveralls" is not available

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
