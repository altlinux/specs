%define        gemname markaby

Name:          gem-markaby
Version:       0.9.0.1
Release:       alt0.1
Summary:       markup as ruby
License:       MIT
Group:         Development/Ruby
Url:           http://markaby.github.com/
Vcs:           https://github.com/markaby/markaby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(builder) >= 0
BuildRequires: gem(bundler) >= 2.1.4 gem(bundler) < 3
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version markaby:0.9.0.1
Requires:      gem(builder) >= 0
Provides:      gem(markaby) = 0.9.0.1


%description
Markaby is a very short bit of code for writing HTML pages in pure Ruby. It is
an alternative to ERb which weaves the two languages together. Also a
replacement for templating languages which use primitive languages that blend
with HTML.


%package       -n gem-markaby-doc
Version:       0.9.0.1
Release:       alt0.1
Summary:       markup as ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета markaby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(markaby) = 0.9.0.1

%description   -n gem-markaby-doc
markup as ruby documentation files.

Markaby is a very short bit of code for writing HTML pages in pure Ruby. It is
an alternative to ERb which weaves the two languages together. Also a
replacement for templating languages which use primitive languages that blend
with HTML.

%description   -n gem-markaby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета markaby.


%package       -n gem-markaby-devel
Version:       0.9.0.1
Release:       alt0.1
Summary:       markup as ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета markaby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(markaby) = 0.9.0.1
Requires:      gem(bundler) >= 2.1.4 gem(bundler) < 3
Requires:      gem(rake) >= 0

%description   -n gem-markaby-devel
markup as ruby development package.

Markaby is a very short bit of code for writing HTML pages in pure Ruby. It is
an alternative to ERb which weaves the two languages together. Also a
replacement for templating languages which use primitive languages that blend
with HTML.

%description   -n gem-markaby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета markaby.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-markaby-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-markaby-devel
%doc README.rdoc


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.0.1-alt0.1
- ^ 0.9.0 -> 0.9.0[.1]

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
