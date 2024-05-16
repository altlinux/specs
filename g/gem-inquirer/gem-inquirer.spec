%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname inquirer

Name:          gem-inquirer
Version:       0.2.1
Release:       alt1
Summary:       Interactive user prompts on CLI for ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/arlimus/inquirer.rb
Vcs:           https://github.com/arlimus/inquirer.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(term-ansicolor) >= 1.2.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(term-ansicolor) >= 1.2.2
Provides:      gem(inquirer) = 0.2.1


%description
Interactive user prompts on CLI for ruby.


%if_enabled    doc
%package       -n gem-inquirer-doc
Version:       0.2.1
Release:       alt1
Summary:       Interactive user prompts on CLI for ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inquirer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inquirer) = 0.2.1

%description   -n gem-inquirer-doc
Interactive user prompts on CLI for ruby documentation files.

%description   -n gem-inquirer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inquirer.
%endif


%if_enabled    devel
%package       -n gem-inquirer-devel
Version:       0.2.1
Release:       alt1
Summary:       Interactive user prompts on CLI for ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inquirer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inquirer) = 0.2.1
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0

%description   -n gem-inquirer-devel
Interactive user prompts on CLI for ruby development package.

%description   -n gem-inquirer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inquirer.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-inquirer-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-inquirer-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
