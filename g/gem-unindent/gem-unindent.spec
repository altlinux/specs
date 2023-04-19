%define        _unpackaged_files_terminate_build 1
%define        gemname unindent

Name:          gem-unindent
Version:       1.0
Release:       alt1
Summary:       Ruby method to unindent strings
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/mynyml/unindent
Vcs:           https://github.com/mynyml/unindent.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(nanotest) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(unindent) = 1.0


%description
Ruby method to unindent strings. Useful for multiline strings embeded in already
indented code.


%package       -n gem-unindent-doc
Version:       1.0
Release:       alt1
Summary:       Ruby method to unindent strings documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unindent
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unindent) = 1.0

%description   -n gem-unindent-doc
Ruby method to unindent strings documentation files.

Ruby method to unindent strings. Useful for multiline strings embeded in already
indented code.

%description   -n gem-unindent-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unindent.


%package       -n gem-unindent-devel
Version:       1.0
Release:       alt1
Summary:       Ruby method to unindent strings development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unindent
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unindent) = 1.0
Requires:      gem(nanotest) >= 0

%description   -n gem-unindent-devel
Ruby method to unindent strings development package.

Ruby method to unindent strings. Useful for multiline strings embeded in already
indented code.

%description   -n gem-unindent-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета unindent.


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

%files         -n gem-unindent-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-unindent-devel
%doc README.md


%changelog
* Fri Apr 14 2023 Pavel Skrylev <majioa@altlinux.org> 1.0-alt1
- + packaged gem with Ruby Policy 2.0
