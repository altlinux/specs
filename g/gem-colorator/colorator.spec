%define        gemname colorator

Name:          gem-colorator
Version:       1.1.0
Release:       alt1.1
Summary:       Colorize your text in the terminal
License:       MIT
Group:         Development/Ruby
Url:           http://octopress.org/colorator/
Vcs:           https://github.com/octopress/colorator.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.1 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(colorator) = 1.1.0


%description
Colorize your text in the terminal.


%package       -n gem-colorator-doc
Version:       1.1.0
Release:       alt1.1
Summary:       Colorize your text in the terminal documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета colorator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(colorator) = 1.1.0

%description   -n gem-colorator-doc
Colorize your text in the terminal documentation files.

%description   -n gem-colorator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета colorator.


%package       -n gem-colorator-devel
Version:       1.1.0
Release:       alt1.1
Summary:       Colorize your text in the terminal development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета colorator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(colorator) = 1.1.0
Requires:      gem(rspec) >= 3.1 gem(rspec) < 4

%description   -n gem-colorator-devel
Colorize your text in the terminal development package.

%description   -n gem-colorator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета colorator.


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

%files         -n gem-colorator-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-colorator-devel
%doc README.markdown


%changelog
* Mon Sep 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1.1
- ! spec

* Wed Mar 17 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 1.1.0-alt1
- initial build
