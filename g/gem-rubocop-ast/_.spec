%define        gemname rubocop-ast

Name:          gem-rubocop-ast
Version:       1.7.0
Release:       alt1
Summary:       RuboCop's Node and NodePattern classes
License:       MIT
Group:         Development/Ruby
Url:           https://rubocop.org/
Vcs:           https://github.com/rubocop-hq/rubocop-ast.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(parser) >= 3.0.1.1
BuildRequires: gem(bundler) >= 1.15.0 gem(bundler) < 3.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(parser) >= 3.0.1.1
Provides:      gem(rubocop-ast) = 1.7.0


%description
RuboCop is a Ruby code style checking and code formatting tool. It aims to
enforce the community-driven Ruby Style Guide.


%package       -n gem-rubocop-ast-doc
Version:       1.7.0
Release:       alt1
Summary:       RuboCop's Node and NodePattern classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-ast
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-ast) = 1.7.0

%description   -n gem-rubocop-ast-doc
RuboCop's Node and NodePattern classes documentation files.

RuboCop is a Ruby code style checking and code formatting tool. It aims to
enforce the community-driven Ruby Style Guide.

%description   -n gem-rubocop-ast-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-ast.


%package       -n gem-rubocop-ast-devel
Version:       1.7.0
Release:       alt1
Summary:       RuboCop's Node and NodePattern classes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-ast
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-ast) = 1.7.0
Requires:      gem(bundler) >= 1.15.0 gem(bundler) < 3.0

%description   -n gem-rubocop-ast-devel
RuboCop's Node and NodePattern classes development package.

RuboCop is a Ruby code style checking and code formatting tool. It aims to
enforce the community-driven Ruby Style Guide.

%description   -n gem-rubocop-ast-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-ast.


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

%files         -n gem-rubocop-ast-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-ast-devel
%doc README.md


%changelog
* Sun May 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- ^ 0.1.0 -> 1.7.0

* Mon Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
