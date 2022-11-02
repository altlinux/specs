%define        gemname options

Name:          gem-options
Version:       2.3.2
Release:       alt1
Summary:       options
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/ahoward/options
Vcs:           https://github.com/ahoward/options.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(options) = 2.3.2


%description
parse options from *args cleanly


%package       -n gem-options-doc
Version:       2.3.2
Release:       alt1
Summary:       options documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета options
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(options) = 2.3.2

%description   -n gem-options-doc
options documentation files.

parse options from *args cleanly

%description   -n gem-options-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета options.


%package       -n gem-options-devel
Version:       2.3.2
Release:       alt1
Summary:       options development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета options
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(options) = 2.3.2

%description   -n gem-options-devel
options development package.

parse options from *args cleanly

%description   -n gem-options-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета options.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README README.erb
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-options-doc
%doc README README.erb
%ruby_gemdocdir

%files         -n gem-options-devel
%doc README README.erb


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 2.3.2-alt1
- + packaged gem with Ruby Policy 2.0
