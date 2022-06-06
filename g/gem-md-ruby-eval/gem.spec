%define        gemname md-ruby-eval

Name:          gem-md-ruby-eval
Version:       0.6.0
Release:       alt1
Summary:       Evaluator of Ruby examples in Markdown files
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/pitr-ch/md-ruby-eval
Vcs:           https://github.com/pitr-ch/md-ruby-eval.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(pry) >= 0.11 gem(pry) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(pry) >= 0.11 gem(pry) < 1
Provides:      gem(md-ruby-eval) = 0.6.0

%description
Evaluator of Ruby examples in Markdown files.


%package       -n md-ruby-eval
Version:       0.6.0
Release:       alt1
Summary:       Evaluator of Ruby examples in Markdown files executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета md-ruby-eval
Group:         Other
BuildArch:     noarch

Requires:      gem(md-ruby-eval) = 0.6.0

%description   -n md-ruby-eval
Evaluator of Ruby examples in Markdown files executable(s).

%description   -n md-ruby-eval -l ru_RU.UTF-8
Исполнямка для самоцвета md-ruby-eval.


%package       -n gem-md-ruby-eval-doc
Version:       0.6.0
Release:       alt1
Summary:       Evaluator of Ruby examples in Markdown files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета md-ruby-eval
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(md-ruby-eval) = 0.6.0

%description   -n gem-md-ruby-eval-doc
Evaluator of Ruby examples in Markdown files documentation files.

%description   -n gem-md-ruby-eval-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета md-ruby-eval.


%package       -n gem-md-ruby-eval-devel
Version:       0.6.0
Release:       alt1
Summary:       Evaluator of Ruby examples in Markdown files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета md-ruby-eval
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(md-ruby-eval) = 0.6.0

%description   -n gem-md-ruby-eval-devel
Evaluator of Ruby examples in Markdown files development package.

%description   -n gem-md-ruby-eval-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета md-ruby-eval.


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

%files         -n md-ruby-eval
%doc README.md
%_bindir/md-ruby-eval

%files         -n gem-md-ruby-eval-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-md-ruby-eval-devel
%doc README.md


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
