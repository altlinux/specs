%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname zstd-ruby

Name:          gem-zstd-ruby
Version:       2.0.6
Release:       alt1
Summary:       Ruby binding for zstd(Zstandard - Fast real-time compression algorithm)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/SpringMT/zstd-ruby
Vcs:           https://github.com/springmt/zstd-ruby.git

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(zstd-ruby) = 2.0.6

%description
Ruby binding for zstd(Zstandard - Fast real-time compression algorithm). See
https://github.com/facebook/zstd


%if_enabled    doc
%package       -n gem-zstd-ruby-doc
Version:       2.0.6
Release:       alt1
Summary:       Ruby binding for zstd(Zstandard - Fast real-time compression algorithm) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zstd-ruby
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(zstd-ruby) = 2.0.6

%description   -n gem-zstd-ruby-doc
Ruby binding for zstd(Zstandard - Fast real-time compression algorithm)
documentation files.

Ruby binding for zstd(Zstandard - Fast real-time compression algorithm). See
https://github.com/facebook/zstd

%description   -n gem-zstd-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета zstd-ruby.
%endif


%if_enabled    devel
%package       -n gem-zstd-ruby-devel
Version:       2.0.6
Release:       alt1
Summary:       Ruby binding for zstd(Zstandard - Fast real-time compression algorithm) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zstd-ruby
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(zstd-ruby) = 2.0.6
Requires:      gem(bundler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rspec) >= 4

%description   -n gem-zstd-ruby-devel
Ruby binding for zstd(Zstandard - Fast real-time compression algorithm)
development package.

Ruby binding for zstd(Zstandard - Fast real-time compression algorithm). See
https://github.com/facebook/zstd

%description   -n gem-zstd-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета zstd-ruby.
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
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-zstd-ruby-doc
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-zstd-ruby-devel
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_includedir/*
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 2.0.6-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
