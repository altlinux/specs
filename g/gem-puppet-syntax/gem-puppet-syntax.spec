%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname puppet-syntax

Name:          gem-puppet-syntax
Version:       7.2.0
Release:       alt1
Summary:       Syntax checks for Puppet manifests, templates, and Hiera YAML
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/voxpupuli/puppet-syntax
Vcs:           https://github.com/voxpupuli/puppet-syntax.git
Packager:      Baltix Maintainers Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(openvox) >= 8
BuildRequires: gem(rake) >= 13.1
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(voxpupuli-rubocop) >= 5.2.0
BuildConflicts: gem(openvox) >= 9
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(voxpupuli-rubocop) >= 5.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Requires:      gem(openvox) >= 8
Requires:      gem(rake) >= 13.1
Conflicts:     gem(openvox) >= 9
Conflicts:     gem(rake) >= 14
Provides:      puppet-syntax = %EVR
Provides:      gem(puppet-syntax) = 7.2.0

%description
Syntax checks for Puppet manifests and templates


%if_enabled    doc
%package       -n gem-puppet-syntax-doc
Version:       7.2.0
Release:       alt1
Summary:       Syntax checks for Puppet manifests, templates, and Hiera YAML documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet-syntax
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(puppet-syntax) = 7.2.0

%description   -n gem-puppet-syntax-doc
Syntax checks for Puppet manifests, templates, and Hiera YAML documentation
files.

Syntax checks for Puppet manifests and templates

%description   -n gem-puppet-syntax-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppet-syntax.
%endif


%if_enabled    devel
%package       -n gem-puppet-syntax-devel
Version:       7.2.0
Release:       alt1
Summary:       Syntax checks for Puppet manifests, templates, and Hiera YAML development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppet-syntax
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(puppet-syntax) = 7.2.0
Requires:      gem(openvox) >= 8
Requires:      gem(rake) >= 13.1
Requires:      gem(rspec) >= 0
Requires:      gem(voxpupuli-rubocop) >= 5.2.0
Conflicts:     gem(openvox) >= 9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(voxpupuli-rubocop) >= 5.3

%description   -n gem-puppet-syntax-devel
Syntax checks for Puppet manifests, templates, and Hiera YAML development
package.

Syntax checks for Puppet manifests and templates

%description   -n gem-puppet-syntax-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppet-syntax.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md HISTORY.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-puppet-syntax-doc
%doc CHANGELOG.md HISTORY.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-puppet-syntax-devel
%doc CHANGELOG.md HISTORY.md LICENSE.txt README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 7.2.0-alt1
- ^ 3.3.0 -> 7.2.0

* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- + packaged gem with Ruby Policy 2.0
