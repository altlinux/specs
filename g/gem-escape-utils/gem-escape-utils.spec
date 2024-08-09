%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname escape_utils

Name:          gem-escape-utils
Version:       1.3.0.6
Release:       alt0.1
Summary:       Faster string escaping routines for your ruby apps
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/brianmario/escape_utils
Vcs:           https://github.com/brianmario/escape_utils.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(actionview) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(haml) >= 0
BuildRequires: gem(fast_xs) >= 0
BuildRequires: gem(actionpack) >= 0
BuildRequires: gem(url_escape) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names escape_utils,escape-utils
Obsoletes:     ruby-escape_utils < %EVR
Provides:      ruby-escape_utils = %EVR
Provides:      gem(escape_utils) = 1.3.0.6

%ruby_use_gem_version escape_utils:1.3.0.6

%description
Being as though we're all html escaping everything these days, why not make it
faster?

For character encoding in 1.9, the output string's encoding is copied from the
input string.

It has monkey-patches for Rack::Utils, CGI, URI, ERB::Util and Haml and
ActionView so you can drop this in and have your app start escaping fast as
balls in no time

It supports HTML, URL, URI and Javascript escaping/unescaping.


%if_enabled    doc
%package       -n gem-escape-utils-doc
Version:       1.3.0.6
Release:       alt0.1
Summary:       Faster string escaping routines for your ruby apps documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета escape_utils
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(escape_utils) = 1.3.0.6

%description   -n gem-escape-utils-doc
Faster string escaping routines for your ruby apps documentation files.

Being as though we're all html escaping everything these days, why not make it
faster?

For character encoding in 1.9, the output string's encoding is copied from the
input string.

It has monkey-patches for Rack::Utils, CGI, URI, ERB::Util and Haml and
ActionView so you can drop this in and have your app start escaping fast as
balls in no time

It supports HTML, URL, URI and Javascript escaping/unescaping.

%description   -n gem-escape-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета escape_utils.
%endif


%if_enabled    devel
%package       -n gem-escape-utils-devel
Version:       1.3.0.6
Release:       alt0.1
Summary:       Faster string escaping routines for your ruby apps development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета escape_utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(escape_utils) = 1.3.0.6
Requires:      gem(rake-compiler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(actionview) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(rack) >= 0
Requires:      gem(haml) >= 0
Requires:      gem(fast_xs) >= 0
Requires:      gem(actionpack) >= 0
Requires:      gem(url_escape) >= 0

%description   -n gem-escape-utils-devel
Faster string escaping routines for your ruby apps development package.

Being as though we're all html escaping everything these days, why not make it
faster?

For character encoding in 1.9, the output string's encoding is copied from the
input string.

It has monkey-patches for Rack::Utils, CGI, URI, ERB::Util and Haml and
ActionView so you can drop this in and have your app start escaping fast as
balls in no time

It supports HTML, URL, URI and Javascript escaping/unescaping.

%description   -n gem-escape-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета escape_utils.
%endif


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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-escape-utils-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-escape-utils-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Thu May 02 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.0.6-alt0.1
- ^ 1.3.0 -> 1.3.0p6

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.2.1 -> 1.3.0

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt3
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt2
- > Ruby Policy 2.0

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.5
- Build for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
