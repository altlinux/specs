%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname html2slim

Name:          gem-html2slim
Version:       0.2.0.13
Release:       alt1
Summary:       HTML to Slim converter
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/slim-template/html2slim
Vcs:           https://github.com/slim-template/html2slim.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(slim) >= 1.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(nokogiri) >= 0
Provides:      gem(html2slim) = 0.2.0.13

%ruby_use_gem_version html2slim:0.2.0.13

%description
Convert HTML to Slim templates. Because HTML sux and Slim rules. That's why.


%package       -n html2slim
Version:       0.2.0.13
Release:       alt1
Summary:       HTML to Slim converter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета html2slim
Group:         Other
BuildArch:     noarch

Requires:      gem(html2slim) = 0.2.0.13

%description   -n html2slim
HTML to Slim converter executable(s).

Convert HTML to Slim templates. Because HTML sux and Slim rules. That's why.

%description   -n html2slim -l ru_RU.UTF-8
Исполнямка для самоцвета html2slim.


%if_enabled    doc
%package       -n gem-html2slim-doc
Version:       0.2.0.13
Release:       alt1
Summary:       HTML to Slim converter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета html2slim
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(html2slim) = 0.2.0.13

%description   -n gem-html2slim-doc
HTML to Slim converter documentation files.

Convert HTML to Slim templates. Because HTML sux and Slim rules. That's why.

%description   -n gem-html2slim-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета html2slim.
%endif


%if_enabled    devel
%package       -n gem-html2slim-devel
Version:       0.2.0.13
Release:       alt1
Summary:       HTML to Slim converter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета html2slim
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(html2slim) = 0.2.0.13
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(slim) >= 1.0.0

%description   -n gem-html2slim-devel
HTML to Slim converter development package.

Convert HTML to Slim templates. Because HTML sux and Slim rules. That's why.

%description   -n gem-html2slim-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета html2slim.
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

%files         -n html2slim
%doc README.md
%_bindir/erb2slim
%_bindir/html2slim

%if_enabled    doc
%files         -n gem-html2slim-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-html2slim-devel
%doc README.md
%endif


%changelog
* Thu Oct 30 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.0.13-alt1
- + packaged gem with Ruby Policy 2.0 for v 0.2.0p13
- * define explicit dependencies
