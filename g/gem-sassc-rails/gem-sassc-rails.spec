# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname sassc-rails

Name:          gem-sassc-rails
Version:       2.1.2.1
Release:       alt1.1
Summary:       Integrate SassC-Ruby with Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/sassc-rails
Vcs:           https://github.com/sass/sassc-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pry) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(sassc) >= 2.0
BuildRequires: gem(tilt) >= 0
BuildRequires: gem(railties) >= 4.0.0
BuildRequires: gem(sprockets) > 3.0
BuildRequires: gem(sprockets-rails) >= 0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(sassc) >= 2.0
Requires:      gem(tilt) >= 0
Requires:      gem(railties) >= 4.0.0
Requires:      gem(sprockets) > 3.0
Requires:      gem(sprockets-rails) >= 0
Provides:      gem(sassc-rails) = 2.1.2.1

%ruby_use_gem_version sassc-rails:2.1.2.1

%description
Integrate SassC-Ruby with Rails.

We all love working with Sass, but compilation can take quite a long time for
larger codebases. This gem integrates the C implementation of Sass, LibSass,
into the asset pipeline.

In one larger project, this made compilation 4x faster than sass-rails


%package       -n gem-sassc-rails-doc
Version:       2.1.2.1
Release:       alt1.1
Summary:       Integrate SassC-Ruby with Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sassc-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sassc-rails) = 2.1.2.1

%description   -n gem-sassc-rails-doc
Integrate SassC-Ruby with Rails documentation files.

%description   -n gem-sassc-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sassc-rails.


%package       -n gem-sassc-rails-devel
Version:       2.1.2.1
Release:       alt1.1
Summary:       Integrate SassC-Ruby with Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sassc-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sassc-rails) = 2.1.2.1
Requires:      gem(pry) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 10.0
Requires:      gem(mocha) >= 0
Conflicts:     gem(rake) >= 14

%description   -n gem-sassc-rails-devel
Integrate SassC-Ruby with Rails development package.

%description   -n gem-sassc-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sassc-rails.


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

%files         -n gem-sassc-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sassc-rails-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 2.1.2.1-alt1.1
- ! spec

* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.2.1-alt1
- ^ 2.1.2 -> 2.1.2[1]

* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1
- + packaged gem with usage Ruby Policy 2.0
