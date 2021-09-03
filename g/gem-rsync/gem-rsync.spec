%define        gemname rsync

Name:          gem-rsync
Version:       1.0.9.1
Release:       alt1
Summary:       Ruby/Rsync is a Ruby library that can syncronize files between remote hosts by wrapping a call to the rsync binary
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jbussdieker/ruby-rsync
Vcs:           https://github.com/jbussdieker/ruby-rsync.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_version rsync:1.0.9.1
Provides:      gem(rsync) = 1.0.9.1


%description
Ruby/Rsync is a Ruby library that can syncronize files between remote hosts by
wrapping a call to the rsync binary.


%package       -n gem-rsync-doc
Version:       1.0.9.1
Release:       alt1
Summary:       Ruby/Rsync is a Ruby library that can syncronize files between remote hosts by wrapping a call to the rsync binary documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rsync
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rsync) = 1.0.9.1

%description   -n gem-rsync-doc
Ruby/Rsync is a Ruby library that can syncronize files between remote hosts by
wrapping a call to the rsync binary documentation files.

%description   -n gem-rsync-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rsync.


%package       -n gem-rsync-devel
Version:       1.0.9.1
Release:       alt1
Summary:       Ruby/Rsync is a Ruby library that can syncronize files between remote hosts by wrapping a call to the rsync binary development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rsync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rsync) = 1.0.9.1
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-rsync-devel
Ruby/Rsync is a Ruby library that can syncronize files between remote hosts by
wrapping a call to the rsync binary development package.

%description   -n gem-rsync-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rsync.


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

%files         -n gem-rsync-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rsync-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.9.1-alt1
- ^ 1.0.9 -> 1.0.9[.1]

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.9-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
