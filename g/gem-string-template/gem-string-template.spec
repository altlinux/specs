%define        _unpackaged_files_terminate_build 1
%define        gemname string_template

Name:          gem-string-template
Version:       0.2.1
Release:       alt1
Summary:       A template engine for Rails, focusing on speed, using Ruby's String interpolation syntax
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/amatsuda/string_template
Vcs:           https://github.com/amatsuda/string_template.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(benchmark_driver) >= 0.9.0
BuildRequires: gem(rails) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rails) >= 0
Provides:      gem(string_template) = 0.2.1


%description
string_template is a Rails plugin that adds an Action View handler for .string
template that accepts Ruby's String literal that uses notation for interpolating
dynamic variables


%package       -n gem-string-template-doc
Version:       0.2.1
Release:       alt1
Summary:       A template engine for Rails, focusing on speed, using Ruby's String interpolation syntax documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета string_template
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(string_template) = 0.2.1

%description   -n gem-string-template-doc
A template engine for Rails, focusing on speed, using Ruby's String
interpolation syntax documentation files.

string_template is a Rails plugin that adds an Action View handler for .string
template that accepts Ruby's String literal that uses notation for interpolating
dynamic variables

%description   -n gem-string-template-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета string_template.


%package       -n gem-string-template-devel
Version:       0.2.1
Release:       alt1
Summary:       A template engine for Rails, focusing on speed, using Ruby's String interpolation syntax development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета string_template
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(string_template) = 0.2.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(benchmark_driver) >= 0.9.0

%description   -n gem-string-template-devel
A template engine for Rails, focusing on speed, using Ruby's String
interpolation syntax development package.

string_template is a Rails plugin that adds an Action View handler for .string
template that accepts Ruby's String literal that uses notation for interpolating
dynamic variables

%description   -n gem-string-template-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета string_template.


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

%files         -n gem-string-template-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-string-template-devel
%doc README.md


%changelog
* Fri Apr 14 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
