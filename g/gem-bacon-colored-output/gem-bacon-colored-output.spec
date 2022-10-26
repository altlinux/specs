%define        gemname bacon-colored_output

Name:          gem-bacon-colored-output
Version:       1.1.1
Release:       alt1
Summary:       Colored output for Bacon test framework!
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/whitequark/bacon-colored_output
Vcs:           https://github.com/whitequark/bacon-colored_output.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bacon) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(bacon) >= 0
Provides:      gem(bacon-colored_output) = 1.1.1

%description
Colored output for Bacon test framework!


%package       -n gem-bacon-colored-output-doc
Version:       1.1.1
Release:       alt1
Summary:       Colored output for Bacon test framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bacon-colored_output
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bacon-colored_output) = 1.1.1

%description   -n gem-bacon-colored-output-doc
Colored output for Bacon test framework documentation files.

%description   -n gem-bacon-colored-output-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bacon-colored_output.


%package       -n gem-bacon-colored-output-devel
Version:       1.1.1
Release:       alt1
Summary:       Colored output for Bacon test framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bacon-colored_output
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bacon-colored_output) = 1.1.1

%description   -n gem-bacon-colored-output-devel
Colored output for Bacon test framework development package.

%description   -n gem-bacon-colored-output-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bacon-colored_output.


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

%files         -n gem-bacon-colored-output-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bacon-colored-output-devel
%doc README.md


%changelog
* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
