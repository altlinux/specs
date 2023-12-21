%define        _unpackaged_files_terminate_build 1
%define        gemname puppet-syntax

Name:          gem-puppet-syntax
Version:       3.3.0
Release:       alt1
Summary:       Syntax checks for Puppet manifests, templates, and Hiera YAML
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/voxpupuli/puppet-syntax
Vcs:           https://github.com/voxpupuli/puppet-syntax.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(github_changelog_generator) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(puppet) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Requires:      gem(puppet) >= 5
Provides:      gem(puppet-syntax) = 3.3.0


%description
Syntax checks for Puppet manifests and templates


%package       -n gem-puppet-syntax-doc
Version:       3.3.0
Release:       alt1
Summary:       Syntax checks for Puppet manifests, templates, and Hiera YAML documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet-syntax
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppet-syntax) = 3.3.0

%description   -n gem-puppet-syntax-doc
Syntax checks for Puppet manifests, templates, and Hiera YAML documentation
files.

Syntax checks for Puppet manifests and templates

%description   -n gem-puppet-syntax-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppet-syntax.


%package       -n gem-puppet-syntax-devel
Version:       3.3.0
Release:       alt1
Summary:       Syntax checks for Puppet manifests, templates, and Hiera YAML development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppet-syntax
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppet-syntax) = 3.3.0
Requires:      gem(pry) >= 0
Requires:      gem(rb-readline) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(github_changelog_generator) >= 0

%description   -n gem-puppet-syntax-devel
Syntax checks for Puppet manifests, templates, and Hiera YAML development
package.

Syntax checks for Puppet manifests and templates

%description   -n gem-puppet-syntax-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppet-syntax.


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

%files         -n gem-puppet-syntax-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-puppet-syntax-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- + packaged gem with Ruby Policy 2.0
