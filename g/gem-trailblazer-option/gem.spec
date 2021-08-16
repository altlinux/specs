%define        gemname trailblazer-option

Name:          gem-trailblazer-option
Version:       0.1.1
Release:       alt1
Summary:       Callable patterns for options in Trailblazer
License:       MIT
Group:         Development/Ruby
Url:           https://trailblazer.to/
Vcs:           https://github.com/trailblazer/trailblazer-option.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(trailblazer-option) = 0.1.1


%description
Wrap an option at compile-time and `call` it at runtime, which allows to have
the common `-> ()`, `:method` or `Callable` pattern used for most options.


%package       -n gem-trailblazer-option-doc
Version:       0.1.1
Release:       alt1
Summary:       Callable patterns for options in Trailblazer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета trailblazer-option
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(trailblazer-option) = 0.1.1

%description   -n gem-trailblazer-option-doc
Callable patterns for options in Trailblazer documentation files.

Wrap an option at compile-time and `call` it at runtime, which allows to have
the common `-> ()`, `:method` or `Callable` pattern used for most options.

%description   -n gem-trailblazer-option-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета trailblazer-option.


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

%files         -n gem-trailblazer-option-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
