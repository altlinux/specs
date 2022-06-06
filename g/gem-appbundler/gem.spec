%define        gemname appbundler

Name:          gem-appbundler
Version:       0.13.5
Release:       alt1
Summary:       Extracts a dependency solution from bundler's Gemfile.lock to speed gem activation
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/appbundler
Vcs:           https://github.com/chef/appbundler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
BuildRequires: gem(mixlib-cli) >= 1.4 gem(mixlib-cli) < 3.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
Requires:      gem(mixlib-cli) >= 1.4 gem(mixlib-cli) < 3.0
Provides:      gem(appbundler) = 0.13.5


%description
Extracts a dependency solution from bundler's Gemfile.lock to speed gem
activation.


%package       -n appbundler
Version:       0.13.5
Release:       alt1
Summary:       Extracts a dependency solution from bundler's Gemfile.lock to speed gem activation executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета appbundler
Group:         Other
BuildArch:     noarch

Requires:      gem(appbundler) = 0.13.5

%description   -n appbundler
Extracts a dependency solution from bundler's Gemfile.lock to speed gem
activation executable(s).

%description   -n appbundler -l ru_RU.UTF-8
Исполнямка для самоцвета appbundler.


%package       -n gem-appbundler-doc
Version:       0.13.5
Release:       alt1
Summary:       Extracts a dependency solution from bundler's Gemfile.lock to speed gem activation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета appbundler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(appbundler) = 0.13.5

%description   -n gem-appbundler-doc
Extracts a dependency solution from bundler's Gemfile.lock to speed gem
activation documentation files.

%description   -n gem-appbundler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета appbundler.


%package       -n gem-appbundler-devel
Version:       0.13.5
Release:       alt1
Summary:       Extracts a dependency solution from bundler's Gemfile.lock to speed gem activation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета appbundler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(appbundler) = 0.13.5

%description   -n gem-appbundler-devel
Extracts a dependency solution from bundler's Gemfile.lock to speed gem
activation development package.

%description   -n gem-appbundler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета appbundler.


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

%files         -n appbundler
%doc README.md
%_bindir/appbundler

%files         -n gem-appbundler-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-appbundler-devel
%doc README.md


%changelog
* Fri Apr 22 2022 Pavel Skrylev <majioa@altlinux.org> 0.13.5-alt1
- + packaged gem with Ruby Policy 2.0
