%define        gemname sass

Name:          gem-sass
Version:       3.7.4
Release:       alt2.1
Summary:       Sass makes CSS fun again
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/sass
Vcs:           https://github.com/sass/ruby-sass.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(sass-listen) >= 4.0.0 gem(sass-listen) < 4.1
BuildRequires: gem(yard) >= 0.8.7.6 gem(yard) < 1
BuildRequires: gem(redcarpet) >= 3.3 gem(redcarpet) < 4
BuildRequires: gem(nokogiri) >= 1.6.0 gem(nokogiri) < 2
BuildRequires: gem(minitest) >= 5 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency nokogiri >= 1.10,nokogiri < 2
%ruby_use_gem_dependency yard >= 0.9,yard < 1
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(sass-listen) >= 4.0.0 gem(sass-listen) < 4.1
Obsoletes:     ruby-sass < %EVR
Provides:      ruby-sass = %EVR
Provides:      gem(sass) = 3.7.4


%description
Sass makes CSS fun again. Sass is an extension of CSS, adding nested rules,
variables, mixins, selector inheritance, and more. It's translated to
well-formatted, standard CSS using the command line tool or a web-framework
plugin.


%package       -n sass
Version:       3.7.4
Release:       alt2.1
Summary:       Sass makes CSS fun again executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sass
Group:         Other
BuildArch:     noarch

Requires:      gem(sass) = 3.7.4

%description   -n sass
Sass makes CSS fun again executable(s).

Sass makes CSS fun again. Sass is an extension of CSS, adding nested rules,
variables, mixins, selector inheritance, and more. It's translated to
well-formatted, standard CSS using the command line tool or a web-framework
plugin.

%description   -n sass -l ru_RU.UTF-8
Исполнямка для самоцвета sass.


%package       -n gem-sass-doc
Version:       3.7.4
Release:       alt2.1
Summary:       Sass makes CSS fun again documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sass) = 3.7.4

%description   -n gem-sass-doc
Sass makes CSS fun again documentation files.

Sass makes CSS fun again. Sass is an extension of CSS, adding nested rules,
variables, mixins, selector inheritance, and more. It's translated to
well-formatted, standard CSS using the command line tool or a web-framework
plugin.

%description   -n gem-sass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sass.


%package       -n gem-sass-devel
Version:       3.7.4
Release:       alt2.1
Summary:       Sass makes CSS fun again development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass) = 3.7.4
Requires:      gem(yard) >= 0.8.7.6 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.3 gem(redcarpet) < 4
Requires:      gem(nokogiri) >= 1.6.0 gem(nokogiri) < 2
Requires:      gem(minitest) >= 5 gem(minitest) < 6

%description   -n gem-sass-devel
Sass makes CSS fun again development package.

Sass makes CSS fun again. Sass is an extension of CSS, adding nested rules,
variables, mixins, selector inheritance, and more. It's translated to
well-formatted, standard CSS using the command line tool or a web-framework
plugin.

%description   -n gem-sass-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sass.


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

%files         -n sass
%doc README.md
%_bindir/sass
%_bindir/sass-convert
%_bindir/scss

%files         -n gem-sass-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sass-devel
%doc README.md


%changelog
* Fri Jul 16 2021 Pavel Skrylev <majioa@altlinux.org> 3.7.4-alt2.1
- ! spec

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.7.4-alt2
- > Ruby Policy 2.0

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.4-alt1
- New version.

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.7-alt1
- New version.

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.6-alt2.1
- Rebuild for new Ruby autorequirements.

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 3.5.6-alt2
- Rebuild as ruby gem for openqa

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.6-alt1
- Initial build for Sisyphus
