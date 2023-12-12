%define        _unpackaged_files_terminate_build 1
%define        gemname rubygems-bundler

Name:          gem-rubygems-bundler
Version:       1.4.5
Release:       alt1
Summary:       Stop using bundle exec
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://mpapis.github.com/rubygems-bundler
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(tf) >= 0
BuildRequires: gem(bundler-unload) >= 1.0.2
BuildRequires: gem(executable-hooks) >= 1.5.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(bundler-unload) >= 1.0.2
Requires:      gem(executable-hooks) >= 1.5.0
Provides:      gem(rubygems-bundler) = 1.4.5


%description
Stop using bundle exec. Integrate Rubygems and Bundler. Make rubygems generate
bundler aware executable wrappers.


%package       -n gem-rubygems-bundler-doc
Version:       1.4.5
Release:       alt1
Summary:       Stop using bundle exec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubygems-bundler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubygems-bundler) = 1.4.5

%description   -n gem-rubygems-bundler-doc
Stop using bundle exec documentation files.

Stop using bundle exec. Integrate Rubygems and Bundler. Make rubygems generate
bundler aware executable wrappers.

%description   -n gem-rubygems-bundler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubygems-bundler.


%package       -n gem-rubygems-bundler-devel
Version:       1.4.5
Release:       alt1
Summary:       Stop using bundle exec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubygems-bundler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubygems-bundler) = 1.4.5
Requires:      gem(tf) >= 0

%description   -n gem-rubygems-bundler-devel
Stop using bundle exec development package.

Stop using bundle exec. Integrate Rubygems and Bundler. Make rubygems generate
bundler aware executable wrappers.

%description   -n gem-rubygems-bundler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubygems-bundler.


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

%files         -n gem-rubygems-bundler-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubygems-bundler-devel
%doc README.md


%changelog
* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.5-alt1
- + packaged gem with Ruby Policy 2.0
