%define        gemname memoist

Name:          gem-memoist
Version:       0.16.2
Release:       alt1
Summary:       ActiveSupport::Memoizable with a few enhancements
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/matthewrudy/memoist
Vcs:           https://github.com/matthewrudy/memoist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.10 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-memoist < %EVR
Provides:      ruby-memoist = %EVR
Provides:      gem(memoist) = 0.16.2


%description
Memoist is an extraction of ActiveSupport::Memoizable.

Since June 2011 ActiveSupport::Memoizable has been deprecated. But I love it,
and so I plan to keep it alive.


%package       -n gem-memoist-doc
Version:       0.16.2
Release:       alt1
Summary:       ActiveSupport::Memoizable with a few enhancements documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета memoist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(memoist) = 0.16.2

%description   -n gem-memoist-doc
ActiveSupport::Memoizable with a few enhancements documentation files.

Memoist is an extraction of ActiveSupport::Memoizable.

Since June 2011 ActiveSupport::Memoizable has been deprecated. But I love it,
and so I plan to keep it alive.

%description   -n gem-memoist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета memoist.


%package       -n gem-memoist-devel
Version:       0.16.2
Release:       alt1
Summary:       ActiveSupport::Memoizable with a few enhancements development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета memoist
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(memoist) = 0.16.2
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(minitest) >= 5.10 gem(minitest) < 6

%description   -n gem-memoist-devel
ActiveSupport::Memoizable with a few enhancements development package.

Memoist is an extraction of ActiveSupport::Memoizable.

Since June 2011 ActiveSupport::Memoizable has been deprecated. But I love it,
and so I plan to keep it alive.

%description   -n gem-memoist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета memoist.


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

%files         -n gem-memoist-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-memoist-devel
%doc README.md


%changelog
* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.16.2-alt1
- ^ 0.16.0 -> 0.16.2

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus
