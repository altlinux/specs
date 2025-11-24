%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname socksify

Name:          gem-socksify
Version:       1.8.1
Release:       alt1
Summary:       Redirect all TCPSockets through a SOCKS5 proxy
License:       Ruby or GPL-3.0-only
Group:         Development/Ruby
Url:           https://github.com/astro/socksify-ruby
Vcs:           https://github.com/astro/socksify-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.25
BuildRequires: gem(rake) >= 13.3
BuildRequires: gem(rubocop) >= 1.78
BuildRequires: gem(rubocop-minitest) >= 0.38
BuildRequires: gem(rubocop-performance) >= 1.25
BuildRequires: gem(rubocop-rake) >= 0.7
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7
Provides:      gem(socksify) = 1.8.1

%description
Redirect all TCPSockets through a SOCKS5 proxy


%package       -n socksify-ruby
Version:       1.8.1
Release:       alt1
Summary:       Redirect all TCPSockets through a SOCKS5 proxy executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета socksify
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(socksify) = 1.8.1

%description   -n socksify-ruby
Redirect all TCPSockets through a SOCKS5 proxy executable(s).

%description   -n socksify-ruby -l ru_RU.UTF-8
Исполнямка для самоцвета socksify.


%if_enabled    doc
%package       -n gem-socksify-doc
Version:       1.8.1
Release:       alt1
Summary:       Redirect all TCPSockets through a SOCKS5 proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета socksify
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(socksify) = 1.8.1

%description   -n gem-socksify-doc
Redirect all TCPSockets through a SOCKS5 proxy documentation files.

%description   -n gem-socksify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета socksify.
%endif


%if_enabled    devel
%package       -n gem-socksify-devel
Version:       1.8.1
Release:       alt1
Summary:       Redirect all TCPSockets through a SOCKS5 proxy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета socksify
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(socksify) = 1.8.1
Requires:      gem(minitest) >= 5.25
Requires:      gem(rake) >= 13.3
Requires:      gem(rubocop) >= 1.78
Requires:      gem(rubocop-minitest) >= 0.38
Requires:      gem(rubocop-performance) >= 1.25
Requires:      gem(rubocop-rake) >= 0.7
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1

%description   -n gem-socksify-devel
Redirect all TCPSockets through a SOCKS5 proxy development package.

%description   -n gem-socksify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета socksify.
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
%doc COPYING ChangeLog LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n socksify-ruby
%doc COPYING ChangeLog LICENSE README.md
%_bindir/socksify_ruby

%if_enabled    doc
%files         -n gem-socksify-doc
%doc COPYING ChangeLog LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-socksify-devel
%doc COPYING ChangeLog LICENSE README.md
%endif


%changelog
* Sun Nov 23 2025 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
