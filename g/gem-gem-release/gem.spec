%define        gemname gem-release

Name:          gem-gem-release
Version:       2.2.2
Release:       alt1
Summary:       Release your ruby gems with ease
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/svenfuchs/gem-release
Vcs:           https://github.com/svenfuchs/gem-release.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names gem-release,release
Provides:      gem(gem-release) = 2.2.2


%description
Release your ruby gems with ease. (What a bold statement for such a tiny plugin
...)


%package       -n gem-gem-release-doc
Version:       2.2.2
Release:       alt1
Summary:       Release your ruby gems with ease documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gem-release
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gem-release) = 2.2.2

%description   -n gem-gem-release-doc
Release your ruby gems with ease documentation files.

Release your ruby gems with ease. (What a bold statement for such a tiny plugin
...)

%description   -n gem-gem-release-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gem-release.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md README.md.erb
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-gem-release-doc
%doc README.md README.md.erb
%ruby_gemdocdir


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt1
- + packaged gem with Ruby Policy 2.0
