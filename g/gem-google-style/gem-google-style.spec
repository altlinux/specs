%define        gemname google-style

Name:          gem-google-style
Version:       1.26.1
Release:       alt1
Summary:       Collection of rubocop rules
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/ruby-style
Vcs:           https://github.com/googleapis/ruby-style.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Provides:      gem(google-style) = 1.26.1


%description
Shared style guide for Google's ruby projects


%package       -n gem-google-style-doc
Version:       1.26.1
Release:       alt1
Summary:       Collection of rubocop rules documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-style
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-style) = 1.26.1

%description   -n gem-google-style-doc
Collection of rubocop rules documentation files.

Shared style guide for Google's ruby projects

%description   -n gem-google-style-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-style.


%package       -n gem-google-style-devel
Version:       1.26.1
Release:       alt1
Summary:       Collection of rubocop rules development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-style
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-style) = 1.26.1

%description   -n gem-google-style-devel
Collection of rubocop rules development package.

Shared style guide for Google's ruby projects

%description   -n gem-google-style-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-style.


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

%files         -n gem-google-style-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-google-style-devel
%doc README.md


%changelog
* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.26.1-alt1
- ^ 1.25.1 -> 1.26.1

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.25.1-alt1
- + packaged gem with Ruby Policy 2.0
