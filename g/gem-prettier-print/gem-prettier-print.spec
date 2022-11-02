%define        gemname prettier_print

Name:          gem-prettier-print
Version:       1.0.2
Release:       alt1
Summary:       A drop-in replacement for the prettyprint gem with more functionality
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-syntax-tree/prettier_print
Vcs:           https://github.com/ruby-syntax-tree/prettier_print.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(prettier_print) = 1.0.2


%description
A drop-in replacement for the prettyprint gem with more functionality.


%package       -n gem-prettier-print-doc
Version:       1.0.2
Release:       alt1
Summary:       A drop-in replacement for the prettyprint gem with more functionality documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prettier_print
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prettier_print) = 1.0.2

%description   -n gem-prettier-print-doc
A drop-in replacement for the prettyprint gem with more functionality
documentation files.

%description   -n gem-prettier-print-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prettier_print.


%package       -n gem-prettier-print-devel
Version:       1.0.2
Release:       alt1
Summary:       A drop-in replacement for the prettyprint gem with more functionality development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prettier_print
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prettier_print) = 1.0.2
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-prettier-print-devel
A drop-in replacement for the prettyprint gem with more functionality
development package.

%description   -n gem-prettier-print-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prettier_print.


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

%files         -n gem-prettier-print-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-prettier-print-devel
%doc README.md


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
