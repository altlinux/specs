%define        _unpackaged_files_terminate_build 1
%define        gemname semantic_puppet

Name:          gem-semantic-puppet
Version:       1.1.0
Release:       alt1
Summary:       Library of useful tools for working with Semantic Versions and module dependencies
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/semantic_puppet
Vcs:           https://github.com/puppetlabs/semantic_puppet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(cane) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(redcarpet) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names semantic_puppet,semantic-puppet
Obsoletes:     ruby-semantic-puppet < %EVR
Provides:      ruby-semantic-puppet = %EVR
Provides:      gem(semantic_puppet) = 1.1.0


%description
Library of useful tools for working with Semantic Versions and module
dependencies.


%package       -n gem-semantic-puppet-doc
Version:       1.1.0
Release:       alt1
Summary:       Library of useful tools for working with Semantic Versions and module dependencies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета semantic_puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(semantic_puppet) = 1.1.0

%description   -n gem-semantic-puppet-doc
Library of useful tools for working with Semantic Versions and module
dependencies documentation files.

%description   -n gem-semantic-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета semantic_puppet.


%package       -n gem-semantic-puppet-devel
Version:       1.1.0
Release:       alt1
Summary:       Library of useful tools for working with Semantic Versions and module dependencies development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета semantic_puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(semantic_puppet) = 1.1.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(cane) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(redcarpet) >= 0

%description   -n gem-semantic-puppet-devel
Library of useful tools for working with Semantic Versions and module
dependencies development package.

%description   -n gem-semantic-puppet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета semantic_puppet.


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

%files         -n gem-semantic-puppet-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-semantic-puppet-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.0.2 -> 1.1.0

* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt2.1
- ! spec obsolete dep

* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt2
- > Ruby Policy 2.0
- ! spec tags

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
