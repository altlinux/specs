%define        gemname sass-globbing

Name:          gem-sass-globbing
Version:       1.1.5.1
Release:       alt0.1
Summary:       Allows use of globs in Sass @import directives
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chriseppstein/sass-globbing
Vcs:           https://github.com/chriseppstein/sass-globbing.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sass) >= 3.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(sass) >= 3.1
Provides:      gem(sass-globbing) = 1.1.5.1

%ruby_use_gem_version sass-globbing:1.1.5.1

%description
Allows use of globs in Sass @import directives.


%package       -n gem-sass-globbing-doc
Version:       1.1.5.1
Release:       alt0.1
Summary:       Allows use of globs in Sass @import directives documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sass-globbing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sass-globbing) = 1.1.5.1

%description   -n gem-sass-globbing-doc
Allows use of globs in Sass @import directives documentation files.

%description   -n gem-sass-globbing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sass-globbing.


%package       -n gem-sass-globbing-devel
Version:       1.1.5.1
Release:       alt0.1
Summary:       Allows use of globs in Sass @import directives development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sass-globbing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass-globbing) = 1.1.5.1
Requires:      gem(rake) >= 0

%description   -n gem-sass-globbing-devel
Allows use of globs in Sass @import directives development package.

%description   -n gem-sass-globbing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sass-globbing.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-sass-globbing-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-sass-globbing-devel
%doc README.markdown


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.5.1-alt0.1
- ^ 1.1.5 -> 1.1.5p1

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.5-alt1
- + packaged gem with Ruby Policy 2.0
