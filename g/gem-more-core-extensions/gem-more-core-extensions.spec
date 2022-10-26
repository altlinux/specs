%define        gemname more_core_extensions

Name:          gem-more-core-extensions
Version:       4.4.0
Release:       alt1
Summary:       MoreCoreExtensions are a set of core extensions beyond those provided by ActiveSupport
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/ManageIQ/more_core_extensions
Vcs:           https://github.com/manageiq/more_core_extensions.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(sync) >= 0
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(manageiq-style) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(timecop) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(activesupport) >= 0
Requires:      gem(sync) >= 0
Provides:      gem(more_core_extensions) = 4.4.0

%ruby_alias_names more_core_extensions,more-core-extensions

%description
MoreCoreExtensions are a set of core extensions beyond those provided by
ActiveSupport.


%package       -n gem-more-core-extensions-doc
Version:       4.4.0
Release:       alt1
Summary:       MoreCoreExtensions are a set of core extensions beyond those provided by ActiveSupport documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета more_core_extensions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(more_core_extensions) = 4.4.0

%description   -n gem-more-core-extensions-doc
MoreCoreExtensions are a set of core extensions beyond those provided by
ActiveSupport documentation files.

%description   -n gem-more-core-extensions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета more_core_extensions.


%package       -n gem-more-core-extensions-devel
Version:       4.4.0
Release:       alt1
Summary:       MoreCoreExtensions are a set of core extensions beyond those provided by ActiveSupport development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета more_core_extensions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(more_core_extensions) = 4.4.0
Requires:      gem(bundler) >= 0
Requires:      gem(manageiq-style) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(timecop) >= 0

%description   -n gem-more-core-extensions-devel
MoreCoreExtensions are a set of core extensions beyond those provided by
ActiveSupport development package.

%description   -n gem-more-core-extensions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета more_core_extensions.


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

%files         -n gem-more-core-extensions-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-more-core-extensions-devel
%doc README.md


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 4.4.0-alt1
- + packaged gem with Ruby Policy 2.0
