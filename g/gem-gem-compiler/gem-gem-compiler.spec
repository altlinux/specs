%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gem-compiler

Name:          gem-gem-compiler
Version:       0.9.0
Release:       alt1
Summary:       A RubyGems plugin that generates binary gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/luislavena/gem-compiler
Vcs:           https://github.com/luislavena/gem-compiler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.14.2
BuildRequires: gem(rake) >= 12.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      ruby >= 2.5.0
Requires:      rubygems >= 2.6.0
Provides:      gem(gem-compiler) = 0.9.0

%description
A RubyGems plugin that helps generates binary gems from already existing ones
without altering the original source code. It compiles Ruby C extensions and
bundles the result into a new gem.


%if_enabled    doc
%package       -n gem-gem-compiler-doc
Version:       0.9.0
Release:       alt1
Summary:       A RubyGems plugin that generates binary gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gem-compiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gem-compiler) = 0.9.0

%description   -n gem-gem-compiler-doc
A RubyGems plugin that generates binary gems documentation files.

A RubyGems plugin that helps generates binary gems from already existing ones
without altering the original source code. It compiles Ruby C extensions and
bundles the result into a new gem.

%description   -n gem-gem-compiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gem-compiler.
%endif


%if_enabled    devel
%package       -n gem-gem-compiler-devel
Version:       0.9.0
Release:       alt1
Summary:       A RubyGems plugin that generates binary gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gem-compiler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gem-compiler) = 0.9.0
Requires:      gem(minitest) >= 5.14.2
Requires:      gem(rake) >= 12.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14

%description   -n gem-gem-compiler-devel
A RubyGems plugin that generates binary gems development package.

A RubyGems plugin that helps generates binary gems from already existing ones
without altering the original source code. It compiles Ruby C extensions and
bundles the result into a new gem.

%description   -n gem-gem-compiler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gem-compiler.
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
%doc CHANGELOG.md README.md LICENSE
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemplugin

%if_enabled    doc
%files         -n gem-gem-compiler-doc
%doc CHANGELOG.md README.md LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gem-compiler-devel
%doc CHANGELOG.md README.md LICENSE
%endif


%changelog
* Thu Apr 24 2025 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
