%define        gemname gems

Name:          gem-gems
Version:       1.2.0
Release:       alt1
Summary:       Ruby wrapper for the RubyGems.org API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubygems/gems
Vcs:           https://github.com/rubygems/gems.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(gems) = 1.2.0


%description
Ruby wrapper for the RubyGems.org API.


%package       -n gem-gems-doc
Version:       1.2.0
Release:       alt1
Summary:       Ruby wrapper for the RubyGems.org API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gems
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gems) = 1.2.0

%description   -n gem-gems-doc
Ruby wrapper for the RubyGems.org API documentation files.

Ruby wrapper for the RubyGems.org API.

%description   -n gem-gems-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gems.


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

%files         -n gem-gems-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
